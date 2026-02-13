#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""Sync shared files from the typespec repo (http-client-python) into this repo.

The typespec repo is the source of truth for:
  1. regenerate-common.ts — shared regeneration logic
  2. requirements.txt — common test dependencies (delimited by marker comments)
  3. Test files — mock API tests and test data

Marker convention in requirements.txt:
  # === common azure dependencies across repos ===
  ...
  # === end common azure dependencies across repos ===
  # === common test dependencies across repos ===
  ...
  # === end common test dependencies across repos ===

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
AUTOREST_COMMON_TS = Path("packages/typespec-python/scripts/eng/regenerate-common.ts")

TYPESPEC_TEST_DIR = Path("packages/http-client-python/generator/test")
AUTOREST_TEST_DIR = Path("packages/typespec-python/test")

# --- Marker patterns for requirements.txt sync ---

_MARKER_PATTERN = re.compile(r"^# === (common .+ across repos) ===$")
_END_MARKER_PATTERN = re.compile(r"^# === end (common .+ across repos) ===$")

# --- Test file sync configuration ---

_SKIP_DIRS: Set[str] = {"__pycache__", "generated", ".venv", "node_modules", ".tox"}

_TEST_SUBDIRS = [
    "generic_mock_api_tests",
    os.path.join("azure", "mock_api_tests"),
    os.path.join("unbranded", "mock_api_tests"),
]

# Files that remain repo-specific (different relative paths between repo layouts)
_SKIP_FILES: Set[str] = {
    os.path.join("generic_mock_api_tests", "conftest.py"),
    os.path.join("azure", "mock_api_tests", "conftest.py"),
    os.path.join("unbranded", "mock_api_tests", "conftest.py"),
}

_SKIP_EXTENSIONS: Set[str] = {".pyc"}
_SKIP_FILENAMES: Set[str] = {"tox.ini", "requirements.txt", "dev_requirements.txt"}


# ---------------------------------------------------------------------------
# Requirements.txt marker-based sync
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


def sync_requirements(source: Path, target: Path) -> None:
    """Sync common marker sections from source to target requirements.txt."""
    source_sections = _extract_marker_sections(source)
    if not source_sections:
        print(f"  WARNING: no marker sections found in {source}, skipping")
        return
    _replace_marker_sections(target, source_sections)
    print(f"  Synced requirements: {source.name} ({source.parent.name}/)")


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

    # 2. Sync requirements.txt marker sections
    for flavor in ("azure", "unbranded"):
        src_req = typespec_repo / TYPESPEC_TEST_DIR / flavor / "requirements.txt"
        dst_req = autorest_repo / AUTOREST_TEST_DIR / flavor / "requirements.txt"
        if src_req.is_file() and dst_req.is_file():
            sync_requirements(src_req, dst_req)
        else:
            print(f"  WARNING: requirements.txt not found for {flavor}, skipping")

    # 3. Sync test files
    print("Syncing test files...")
    sync_test_files(
        typespec_repo / TYPESPEC_TEST_DIR,
        autorest_repo / AUTOREST_TEST_DIR,
    )

    # 4. Format TypeScript files
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
