#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""Sync shared files from the typespec repo (http-client-python) into this repo.

The typespec repo is the source of truth for:
  1. regenerate-common.ts — shared regeneration logic
  2. requirements — test dependency files (tests/requirements/)
  3. Test files — mock API tests under tests/mock_api/{shared,azure,unbranded}

Usage:
    python sync_from_typespec.py <local-typespec-repo-path>
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Set

# --- Path configuration (relative to each repo root) ---

TYPESPEC_COMMON_TS = Path("packages/http-client-python/eng/scripts/ci/regenerate-common.ts")
AUTOREST_COMMON_TS = Path("packages/typespec-python/eng/scripts/regenerate-common.ts")

TYPESPEC_TEST_DIR = Path("packages/http-client-python/tests")
AUTOREST_TEST_DIR = Path("packages/typespec-python/tests")

TYPESPEC_DEV_REQUIREMENTS = Path("packages/http-client-python/eng/scripts/ci/dev_requirements.txt")
AUTOREST_DEV_REQUIREMENTS = Path("packages/typespec-python/dev_requirements.txt")

# Marker indicating where repo-specific content begins in dev_requirements.txt.
# Everything from this line onward in the autorest file is preserved; everything
# above is replaced with the upstream content (prefixed by a header comment).
_DEV_REQUIREMENTS_HEADER = "# shall keep aligned with dev_requirements.txt of @typespec/http-client-python"
_DEV_REQUIREMENTS_TAIL_MARKER = "# additional dependency needed for development"

# --- Marker patterns for requirements sync ---
#
# Convention in requirements files (e.g. azure.txt, unbranded.txt):
#   # === common azure dependencies across repos ===
#   azure-core>=1.37.0
#   ...
#   # === end common azure dependencies across repos ===

_MARKER_PATTERN = re.compile(r"^# === (common .+ across repos) ===$")
_END_MARKER_PATTERN = re.compile(r"^# === end (common .+ across repos) ===$")

_REQUIREMENTS_FILES = ["azure.txt", "base.txt", "docs.txt", "lint.txt", "typecheck.txt", "unbranded.txt"]


# ---------------------------------------------------------------------------
# Test file sync
# ---------------------------------------------------------------------------

_SKIP_DIRS: Set[str] = {"__pycache__", "generated", ".venv", "node_modules", ".tox"}

_TEST_SUBDIRS = [
    os.path.join("mock_api", "shared"),
    os.path.join("mock_api", "azure"),
    os.path.join("mock_api", "unbranded"),
]

# Files that remain repo-specific (e.g. conftest.py differs between repos)
_SKIP_FILES: Set[str] = {
    os.path.join("mock_api", "shared", "conftest.py"),
    os.path.join("mock_api", "azure", "conftest.py"),
    os.path.join("mock_api", "unbranded", "conftest.py"),
}

_SKIP_EXTENSIONS: Set[str] = {".pyc"}
_SKIP_FILENAMES: Set[str] = {"tox.ini", "requirements.txt", "dev_requirements.txt"}


# ---------------------------------------------------------------------------
# Requirements sync
# ---------------------------------------------------------------------------


def _extract_marker_sections(filepath: Path) -> Dict[str, List[str]]:
    """Extract content between marker comment pairs from a file.

    Returns a dict mapping marker name to the lines between begin/end markers
    (inclusive of both marker lines).
    """
    sections: Dict[str, List[str]] = {}
    lines = filepath.read_text(encoding="utf-8").splitlines()

    current_marker = None
    current_lines: List[str] = []
    for line in lines:
        begin_match = _MARKER_PATTERN.match(line.strip())
        end_match = _END_MARKER_PATTERN.match(line.strip())
        if begin_match and current_marker is None:
            current_marker = begin_match.group(1)
            current_lines = [line]
        elif end_match and current_marker is not None:
            current_lines.append(line)
            sections[current_marker] = current_lines
            current_marker = None
            current_lines = []
        elif current_marker is not None:
            current_lines.append(line)

    return sections


def _replace_marker_sections(filepath: Path, source_sections: Dict[str, List[str]]) -> None:
    """Replace marker sections in a file with content from source_sections."""
    lines = filepath.read_text(encoding="utf-8").splitlines()

    result: List[str] = []
    current_marker = None
    for line in lines:
        begin_match = _MARKER_PATTERN.match(line.strip())
        end_match = _END_MARKER_PATTERN.match(line.strip())
        if begin_match and current_marker is None:
            current_marker = begin_match.group(1)
            if current_marker in source_sections:
                result.extend(source_sections[current_marker])
            else:
                result.append(line)
        elif end_match and current_marker is not None:
            if current_marker not in source_sections:
                result.append(line)
            current_marker = None
        elif current_marker is None:
            result.append(line)

    filepath.write_text("\n".join(result) + "\n", encoding="utf-8", newline="\n")


def sync_requirements(source_dir: Path, target_dir: Path) -> None:
    """Copy requirements files from typespec to autorest.

    If marker sections are present, only the marker-delimited sections are
    replaced in the target (preserving repo-specific dependencies outside
    markers). Otherwise the file is copied directly.
    """
    for filename in _REQUIREMENTS_FILES:
        src = source_dir / filename
        dst = target_dir / filename
        if not src.is_file():
            print(f"  WARNING: {src} not found, skipping")
            continue

        source_sections = _extract_marker_sections(src)
        if source_sections and dst.is_file():
            _replace_marker_sections(dst, source_sections)
            print(f"  Synced markers: requirements/{filename}")
        else:
            if dst.is_file() and src.read_bytes() == dst.read_bytes():
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            print(f"  Copied: requirements/{filename}")


# ---------------------------------------------------------------------------
# dev_requirements.txt sync
# ---------------------------------------------------------------------------


def sync_dev_requirements(source_file: Path, target_file: Path) -> None:
    """Sync upstream dev_requirements.txt, preserving repo-specific tail.

    The target file layout is:
        <header>
        <upstream content>

        # additional dependency needed for development
        <repo-specific deps>     <-- preserved from existing target

    Content from the tail marker onward in the existing target is kept;
    everything above is replaced with header + upstream.
    """
    if not source_file.is_file():
        print(f"  WARNING: {source_file} not found, skipping")
        return

    upstream = source_file.read_text(encoding="utf-8").strip()

    tail = ""
    if target_file.is_file():
        existing = target_file.read_text(encoding="utf-8")
        idx = existing.find(_DEV_REQUIREMENTS_TAIL_MARKER)
        if idx >= 0:
            tail = existing[idx:].strip()

    content = f"{_DEV_REQUIREMENTS_HEADER}\n{upstream}\n"
    if tail:
        content += f"\n{tail}\n"

    target_file.parent.mkdir(parents=True, exist_ok=True)
    target_file.write_text(content, encoding="utf-8", newline="\n")
    print(f"  Synced: {target_file.name}")


# ---------------------------------------------------------------------------
# Test file sync
# ---------------------------------------------------------------------------


def _should_skip_file(rel_path: str, filename: str) -> bool:
    """Return True if a file should not be synced."""
    if filename in _SKIP_FILENAMES:
        return True
    if os.path.splitext(filename)[1] in _SKIP_EXTENSIONS:
        return True
    return rel_path in _SKIP_FILES


def sync_test_files(source_root: Path, target_root: Path) -> None:
    """Copy test files from typespec to autorest, skipping repo-specific files.

    Only overwrites files that actually differ. Never deletes target-only files.
    """
    copied = 0
    skipped = 0

    for subdir in _TEST_SUBDIRS:
        src_dir = source_root / subdir
        if not src_dir.is_dir():
            print(f"  WARNING: {src_dir} not found, skipping")
            continue

        for dirpath, dirnames, filenames in os.walk(src_dir):
            dirnames[:] = [d for d in dirnames if d not in _SKIP_DIRS]

            for filename in filenames:
                src_file = Path(dirpath) / filename
                rel_from_root = src_file.relative_to(source_root).as_posix()
                rel_native = str(src_file.relative_to(source_root))

                if _should_skip_file(rel_native, filename):
                    skipped += 1
                    continue

                dst_file = target_root / rel_from_root
                dst_file.parent.mkdir(parents=True, exist_ok=True)

                if dst_file.is_file() and src_file.read_bytes() == dst_file.read_bytes():
                    continue

                shutil.copy2(src_file, dst_file)
                copied += 1
                print(f"  Copied: {rel_from_root}")

    print(f"  Test files: {copied} copied, {skipped} skipped")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync shared files from the typespec repo (http-client-python) into autorest.python.",
    )
    parser.add_argument(
        "typespec_repo",
        type=Path,
        help="Path to the local typespec repo root (e.g. C:/dev/typespec)",
    )
    args = parser.parse_args()

    typespec_repo: Path = args.typespec_repo.resolve()
    autorest_repo: Path = Path(__file__).resolve().parents[2]  # eng/scripts/.. -> repo root

    if not typespec_repo.is_dir():
        print(f"ERROR: typespec repo not found: {typespec_repo}", file=sys.stderr)
        return 1

    # 1. Sync regenerate-common.ts
    src_ts = typespec_repo / TYPESPEC_COMMON_TS
    dst_ts = autorest_repo / AUTOREST_COMMON_TS
    if not src_ts.is_file():
        print(f"ERROR: {src_ts} not found", file=sys.stderr)
        return 1
    shutil.copy2(src_ts, dst_ts)
    print(f"Synced regenerate-common.ts")

    # 2. Sync requirements files
    print("Syncing requirements...")
    sync_requirements(
        typespec_repo / TYPESPEC_TEST_DIR / "requirements",
        autorest_repo / AUTOREST_TEST_DIR / "requirements",
    )

    # 3. Sync dev_requirements.txt
    print("Syncing dev_requirements.txt...")
    sync_dev_requirements(
        typespec_repo / TYPESPEC_DEV_REQUIREMENTS,
        autorest_repo / AUTOREST_DEV_REQUIREMENTS,
    )

    # 4. Sync test files
    print("Syncing test files...")
    sync_test_files(
        typespec_repo / TYPESPEC_TEST_DIR,
        autorest_repo / AUTOREST_TEST_DIR,
    )

    # 5. Format TypeScript files
    ts_python_dir = autorest_repo / "packages" / "typespec-python"
    print("Running pnpm format...")
    result = subprocess.run(
        ["pnpm", "format"],
        cwd=ts_python_dir,
        capture_output=True,
        text=True,
        shell=(os.name == "nt"),
    )
    if result.returncode != 0:
        print(f"WARNING: pnpm format failed:\n{result.stderr}", file=sys.stderr)
    else:
        print("pnpm format succeeded.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
