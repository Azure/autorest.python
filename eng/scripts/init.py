#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# This script is used to execute mypy within a tox environment. Depending on which package is being executed against,
# a failure may be suppressed.

from pathlib import Path
from helpers import call, str2bool
import shutil
import argparse

root_dir = Path.resolve(Path(__file__) / Path("../../.."))
package_artifacts_dir = root_dir / Path("artifacts/package-json")
autorest_package_dir = root_dir / Path("packages/autorest.python")
typespec_package_dir = root_dir / Path("packages/typespec-python")


def main(package_json_artifacts: Path, update_to_latest_typespec: bool, install_autorest: bool, install_typeSpec: bool, install_cadl_ranch: bool):
    if package_json_artifacts:
        shutil.copy(package_json_artifacts / "pnpm-lock.yaml", root_dir)
        shutil.copy(package_json_artifacts / "package.json", root_dir)
        shutil.copy(
            package_json_artifacts / "typespec-python_package.json",
            root_dir / "packages/typespec-python/package.json",
        )

    # Install pnpm 8.3.1
    call("npm install -g pnpm@8.3.1")

    if install_autorest:
        # Install autorest
        call("npm install -g autorest")

    if install_typeSpec:
        # Install TypeSpec
        typespecVersionSuffix = "@next" if update_to_latest_typespec else ""
        call(f"npm install -g @typespec/compiler{typespecVersionSuffix}")

    if install_cadl_ranch:
        # Install Cadl Ranch
        call("npm install -g @azure-tools/cadl-ranch")

    if update_to_latest_typespec:
        # Update typespec packages to latest dev version
        call(
            "npx -y @azure-tools/typespec-bump-deps@0.3.0 --use-peer-ranges package.json packages/typespec-python/package.json"
        )
        # Pnpm install
        call("pnpm install --no-frozen-lockfile")
    else:
        # Pnpm install
        call("pnpm install")

    # Pnpm list
    call("pnpm list -r")

    call("git add pnpm-lock.yaml package.json packages/typespec-python/package.json")

    # Clean or create artifacts directory
    shutil.rmtree(package_artifacts_dir, ignore_errors=True)
    package_artifacts_dir.mkdir(parents=True, exist_ok=True)

    # Copy package.json related files to artifacts directory
    shutil.copy(root_dir / "pnpm-lock.yaml", package_artifacts_dir)
    shutil.copy(root_dir / "package.json", package_artifacts_dir)
    shutil.copy(
        root_dir / "packages/typespec-python/package.json",
        package_artifacts_dir / "typespec-python_package.json",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run emitter build commands.")

    parser.add_argument(
        "--package-json-artifacts",
        type=Path,
        help="A folder containing package.json related files for synchronized CI builds. Optional.",
        required=False,
    )

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
        "--install-autorest",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        help="Install the autorest global npm module. Optional.",
        required=False,
    )

    parser.add_argument(
        "--install-typeSpec",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        help="Install the @typespec/compiler global npm module. Optional.",
        required=False,
    )

    parser.add_argument(
        "--install-cadl-ranch",
        type=str2bool,
        nargs="?",
        const=True,
        default=False,
        help="Install the @azure-tools/cadl-ranch global npm module. Optional.",
        required=False,
    )

    args = parser.parse_args()

    main(args.package_json_artifacts, args.use_typespec_next, args.install_autorest, args.install_typespec, args.install_cadl_ranch)
