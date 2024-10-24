#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import argparse
from pathlib import Path
import logging
import json

from subprocess import check_call, CalledProcessError
from msrest.authentication import BasicAuthentication
from azure.devops.v7_1.build import BuildClient

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def log_call(command: str):
    logger.info(f"== {command} ==")
    check_call(command, shell=True)


def main(branch: str, build_id: str, package_path: str, token: str):
    new_branch = f"auto-{branch}"
    # checkout branch
    try:
        log_call(f"git checkout {new_branch}")
    except CalledProcessError:
        logger.info(f"Branch {new_branch} does not exist. Creating a new branch.")
        log_call(f"git checkout -b {new_branch}")

    # get download url of http-client-python
    client = BuildClient(base_url="https://dev.azure.com/azure-sdk", creds=BasicAuthentication(token, ""))
    artifact = client.get_artifact(
        project="internal",
        build_id=build_id,
        artifact_name="http-client-python",
    )
    resource_url = artifact.resource.download_url
    package_name = Path(package_path).name
    url = resource_url.replace("=zip", f"=file&subPath=%2F{package_name}")
    logger.info(f"Download url of {package_name}: {url}")

    # update package.json for autorest.python and typespec-python
    # for package in ["autorest.python", "typespec-python"]:
    for package in ["typespec-python"]:
        package_path = Path(f"packages/{package}")
        package_json = package_path / "package.json"
        with open(package_json, "r") as f:
            package_data = json.load(f)
        package_data["dependencies"]["@typespec/http-client-python"] = url
        with open(package_json, "w") as f:
            json.dump(package_data, f, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--branch",
        help="Branch name of microsoft/typespec",
        type=str,
    )

    parser.add_argument(
        "--build-id",
        help="build id of pipeline",
        type=str,
    )

    parser.add_argument(
        "--package-path",
        help="package path of http-client-python",
        type=str,
    )

    parser.add_argument(
        "--token",
        help="pipeline token",
        type=str,
    )

    args = parser.parse_args()

    main(args.branch, args.build_id, args.package_path, args.token)
