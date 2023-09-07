#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from pathlib import Path
from helpers import is_pipeline_build, call, str2bool
import argparse
import shutil

pipeline_build = is_pipeline_build()
root_dir = Path.resolve(Path(__file__) / "../../..")
packages_dir = root_dir / "artifacts/packages"


def main(package_name: str, regenerate: bool, check_change: bool, code_checks: bool, version_suffix: str, output_dir: str):
    if package_name == "autorest.python":
        folder_name = "autorest"
        versionVariableName = "autorestVersion"
        tarball_prefix = "autorest-python"
    elif package_name == "typespec-python":
        folder_name = ""
        versionVariableName = "typespecVersion"
        tarball_prefix = "azure-tools-typespec-python"
    else:
        print(f"Invalid package name: {package_name}")
        exit(1)

    package_dir = root_dir / Path("packages") / package_name

    currentVersion = call(
        "node -pe \"require('./package.json').version\"", capture_output=True, cwd=package_dir
    ).strip()

    if version_suffix:
        newVersion = f"{currentVersion}{version_suffix}"

        # Update version
        call(f'npm version "{newVersion}" --no-workspaces-update', cwd=package_dir)
        call("git add package.json", cwd=package_dir)
    else:
        newVersion = currentVersion

    print(f"Building version {newVersion}")

    if pipeline_build:
        # Update version variable
        print(
            f"##vso[task.setvariable variable={versionVariableName};isOutput=true]{newVersion}"
        )

    # Build project
    call("pnpm run build")

    # Check version mismatch
    call("pnpm check-version-mismatch")

    # Lint project
    call("pnpm lint")

    # Check formatting
    call("pnpm check-format")

    # Pip install dev requirements
    call("pip install -r dev_requirements.txt", cwd=package_dir)

    if code_checks:
        # Pylint
        call(f"pylint {folder_name}", cwd=package_dir)
        # Mypy
        call(f"mypy {folder_name}", cwd=package_dir)
        # Pyright
        call(f"pyright {folder_name}", cwd=package_dir)
        # Black
        call(f"black {folder_name}", cwd=package_dir)
        # Fail on black autorest diff
        call("node ./eng/scripts/check-for-changed-files.js")
        # Unit tests
        call("tox run -e ci", cwd=package_dir / Path("test/unittests"))

    if regenerate:
        # "Regenerate Code"
        call("inv regenerate", cwd=package_dir)

        if check_change:
            # Fail on regeneration diff in Typespec
            call(
                "node ../../../eng/scripts/check-for-changed-files.js",
                cwd=package_dir / Path("test"),
            )

    call(f'pnpm pack --pack-destination "{packages_dir}"', cwd=package_dir)

    tarball_path = packages_dir / f"{tarball_prefix}-{newVersion}.tgz"

    call(f'pnpm install "{ tarball_path }" -w --verbose')

    call(f"git restore .")

    shutil.rmtree(artifacts_dir, ignore_errors=True)
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(root_dir / "package.json", artifacts_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run emitter build commands.")

    parser.add_argument(
        "--output-dir",
        help="Output directory",
        type=str,
    )

    parser.add_argument(
        "--regenerate",
        help="Regenrate code",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
    )

    parser.add_argument(
        "--check-change",
        help="Check for changes in regenerated code",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
    )

    parser.add_argument(
        "--code-checks",
        help="Check code quality",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
    )

    parser.add_argument(
        "--package",
        dest="package_name",
        help="The package to build",
        choices=["autorest.python", "typespec-python", ""],
        type=str,
    )

    parser.add_argument(
        "--version-suffix",
        help="A suffix to append to the version number of the package",
        type=str,
    )

    args = parser.parse_args()

    # Clean packages directory
    shutil.rmtree(packages_dir, ignore_errors=True)
    packages_dir.mkdir(parents=True, exist_ok=True)

    if args.package_name:
        main(
            package_name=args.package_name,
            regenerate=args.regenerate,
            check_change=args.check_change,
            code_checks=args.code_checks,
            version_suffix=args.version_suffix,
            output_dir=args.output_dir,
        )
    else:
        main(
            package_name="autorest.python",
            regenerate=args.regenerate,
            check_change=args.check_change,
            code_checks=args.code_checks,
            version_suffix=args.version_suffix,
            output_dir=args.output_dir,
        )

        main(
            package_name="typespec-python",
            regenerate=args.regenerate,
            check_change=args.check_change,
            code_checks=args.code_checks,
            version_suffix=args.version_suffix,
            output_dir=args.output_dir,
        )
