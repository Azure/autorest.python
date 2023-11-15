#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# This script is used to execute mypy within a tox environment. Depending on which package is being executed against,
# a failure may be suppressed.

import os
from pathlib import Path
from helpers import call, str2bool
import argparse
import shutil

root_dir = Path.resolve(Path(__file__) / "../../..")


def copy(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dest)


def main(update_to_latest_typespec: bool, build_artifacts_path: Path) -> None:
    # Install global dependencies
    call("npm install -g pnpm@8.3.1")
    call("npm install -g autorest@3.6.3")
    call("npm install -g @typespec/compiler@0.49.0")

    if build_artifacts_path:
        # copy package.json and pnpm-lock.yaml from build artifacts
        lock_files_dir = Path(build_artifacts_path) / "lock-files"
        if lock_files_dir.exists():
            print(f"Copying package.json and pnmp-lock.yaml from {lock_files_dir}")
            copy(lock_files_dir / "package.json", root_dir)
            copy(lock_files_dir / "pnpm-lock.yaml", root_dir)
            copy(
                lock_files_dir / "emitter/package.json",
                root_dir / "packages/typespec-python",
            )

        # Pnpm install
        call("pnpm install --frozen-lockfile")
    else:
        if update_to_latest_typespec:
            # Update typespec packages to latest dev version
            call(
                "npx -y @azure-tools/typespec-bump-deps@0.4.0 --use-peer-ranges package.json packages/typespec-python/package.json"
            )

            # Pnpm install
            call("pnpm install --no-frozen-lockfile")
        else:
            # No updates to package.json or lock files, just use what's in the repository
            call("pnpm install --frozen-lockfile")

        artifact_staging_dir = os.environ.get("BUILD_ARTIFACTSTAGINGDIRECTORY")
        if artifact_staging_dir:
            lock_files_dir = Path(artifact_staging_dir)

            # copy package.json and pnpm-lock.yaml to build artifacts
            copy(root_dir / "package.json", lock_files_dir)
            copy(root_dir / "pnpm-lock.yaml", lock_files_dir)
            copy(
                root_dir / "packages/typespec-python/package.json",
                lock_files_dir / "emitter",
            )

    # Pnpm list
    call("pnpm list -r")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run emitter build commands.")

    parser.add_argument(
        "--use-typespec-next",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        help="Update package.json files to use latest dev typespec version. Optional.",
        required=False,
    )

    parser.add_argument(
        "--build-artifacts-path",
        type=Path,
        help="Path to the artifacts generated in the build stage, used for package lock file synchronization. Optional.",
        required=False,
    )

    args = parser.parse_args()

    main(args.use_typespec_next, args.build_artifacts_path)
