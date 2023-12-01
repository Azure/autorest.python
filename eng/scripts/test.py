#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from pathlib import Path
from helpers import is_pipeline_build, call, str2bool
import argparse

pipeline_build = is_pipeline_build()
root_dir = Path.resolve(Path(__file__) / "../../..")


def main(
    package_name: str, regenerate: bool, check_change: bool, check_code: bool = False
):
    if package_name == "autorest.python":
        folder_name = "autorest"
    elif package_name == "typespec-python":
        folder_name = ""
    else:
        print(f"Invalid package name: {package_name}")
        exit(1)

    package_dir = root_dir / Path("packages") / package_name

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

    if check_code:
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

    call(f"git restore .")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run emitter build commands.")

    parser.add_argument(
        "--regenerate",
        help="Regenerate code",
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
        "--check-code",
        help="Check code quality",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
    )

    parser.add_argument(
        "--package",
        help="The package to test",
        type=str,
        required=False,
        choices=["autorest", "typespec"],
    )

    args = parser.parse_args()

    package = args.package
    if package == "autorest":
        main(
            "autorest.python",
            args.regenerate,
            args.check_change,
            args.check_code,
        )
    elif package == "typespec":
        main(
            "typespec-python",
            args.regenerate,
            args.check_change,
        )
    else:
        main(
            "autorest.python",
            args.regenerate,
            args.check_change,
            args.check_code,
        )
        main(
            "typespec-python",
            args.regenerate,
            args.check_change,
        )
