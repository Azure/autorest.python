#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from pathlib import Path
from helpers import is_pipeline_build, call
import argparse
import shutil
import json

pipeline_build = is_pipeline_build()
root_dir = Path.resolve(Path(__file__) / "../../..")

def main(package_name: str, version_suffix: str, output_dir: str, package_versions: dict):
    if package_name == "autorest.python":
        versionVariableName = "generatorVersion"
        tarball_prefix = "autorest-python"
    elif package_name == "typespec-python":
        versionVariableName = "emitterVersion"
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

    package_versions[package_name] = newVersion

    if pipeline_build:
        # Update version variable
        print(
            f"##vso[task.setvariable variable={versionVariableName};isOutput=true]{newVersion}"
        )

    # Build project
    call("pnpm run build")

    # Check version mismatch
    call("pnpm check-version-mismatch")

    call(f'pnpm pack --pack-destination "{output_dir}"', cwd=package_dir)

    tarball_path = output_dir / f"{tarball_prefix}-{newVersion}.tgz"

    call(f'pnpm install "{ tarball_path }" -w --verbose')

    call(f"git restore .")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run emitter build commands.")

    parser.add_argument(
        "--output-dir",
        help="Output directory",
        type=str,
    )

    parser.add_argument(
        "--package",
        dest="package_name",
        help="The package to build",
        choices=["autorest.python", "typespec-python", ""],
        type=str,
    )

    parser.add_argument(
        "--publish-internal",
        help="Produce overrides targeting the internal feed",
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "--version-suffix",
        help="A suffix to append to the version number of the package",
        type=str,
    )

    args = parser.parse_args()

    # Clean output directory
    output_dir = Path(args.output_dir or root_dir / "artifacts").resolve()
    shutil.rmtree(output_dir, ignore_errors=True)

    packages_dir = output_dir / "packages"
    packages_dir.mkdir(parents=True, exist_ok=True)
    package_versions = {}

    if args.package_name:
        main(
            args.package_name,
            args.version_suffix,
            packages_dir,
            package_versions,
        )
    else:
        main(
            "autorest.python",
            args.version_suffix,
            packages_dir,
            package_versions,
        )

        main(
            "typespec-python",
            args.version_suffix,
            packages_dir,
            package_versions,
        )

    feedUrl = "https://pkgs.dev.azure.com/azure-sdk/public/_packaging/azure-sdk-for-js-test-autorest@local/npm/registry"
    overrides = {}

    if "autorest.python" in package_versions:
        version = package_versions["autorest.python"]
        if args.publish_internal:
            overrides["@autorest/python"] = f'{feedUrl}/@autorest/python/-/python-{version}.tgz'

    if "typespec-python" in package_versions:
        version = package_versions["typespec-python"]
        if args.publish_internal:
            overrides["@azure-tools/typespec-python"] = f'{feedUrl}/@azure-tools/typespec-python/-/typespec-python-{version}.tgz'
    
    with open(output_dir / "overrides.json", "w") as fp:
        json.dump(overrides, fp, indent=2) 

    with open(output_dir / "package-versions.json", "w") as fp:
        json.dump(package_versions, fp, indent=2)
