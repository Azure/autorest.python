#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from typing import Dict, List
from pathlib import Path
from datetime import datetime
from subprocess import check_call, check_output
import argparse
import logging
import json


def update_emitter_package(sdk_root: str, typespec_python_root: str):
    # find the typespec-python.tgz
    typespec_python_tgz = None
    for item in (Path(typespec_python_root) / "packages/typespec-python").iterdir():
        if "typespec-python" in item.name and item.name.endswith(".tgz"):
            typespec_python_tgz = item
            break
    if not typespec_python_tgz:
        logging.error("can not find .tgz for typespec-python")
        raise FileNotFoundError("can not find .tgz for typespec-python")

    # update the emitter-package.json
    emitter_package_folder = Path(sdk_root) / "eng/emitter-package.json"
    with open(emitter_package_folder, "r") as f:
        emitter_package = json.load(f)
    emitter_package["dependencies"]["@azure-tools/typespec-python"] = typespec_python_tgz.absolute().as_posix()
    with open(emitter_package_folder, "w") as f:
        json.dump(emitter_package, f, indent=2)

    # update the emitter-package-lock.json
    try:
        check_call("tsp-client --generate-lock-file", shell=True)
    except Exception as e:
        logging.error("failed to update emitter-package-lock.json")
        logging.error(e)
        raise e


def regenerate_sdk() -> Dict[str, List[str]]:
    result = {"succeed_to_regenerate": [], "fail_to_regenerate": [], "time_to_regenerate": str(datetime.now())}
    # get all tsp-location.yaml
    for item in Path(".").rglob("tsp-location.yaml"):
        package_folder = item.parent
        try:
            check_call("tsp-client update", shell=True, cwd=str(package_folder))
        except Exception as e:
            logging.error(f"failed to regenerate {package_folder.name}")
            logging.error(e)
            result["fail_to_regenerate"].append(package_folder.name)
        else:
            result["succeed_to_regenerate"].append(package_folder.name)
        break
    return result


def checkout_branch(branch: str):
    try:
        check_call(f"git fetch azure-sdk {branch}", shell=True)
        check_call(f"git checkout {branch}", shell=True)
    except Exception:
        check_call(f"git checkout -b {branch}", shell=True)


def prepare_branch(typespec_python_branch: str):
    check_call("git remote add azure-sdk https://github.com/azure-sdk/azure-sdk-for-python.git", shell=True)
    checkout_branch("typespec-python-main")

    if typespec_python_branch != "main":
        checkout_branch(f"typespec-python-{typespec_python_branch}")


def git_add():
    check_call("git add .", shell=True)


def main(sdk_root: str, typespec_python_root: str, typespec_python_branch: str):
    prepare_branch(typespec_python_branch)
    update_emitter_package(sdk_root, typespec_python_root)
    result = regenerate_sdk()
    with open("aaaa-regenerate-sdk-result.json", "w") as f:
        json.dump(result, f, indent=2)
    git_add()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SDK regeneration")

    parser.add_argument(
        "--sdk-root",
        help="SDK repo root folder",
        type=str,
    )

    parser.add_argument(
        "--typespec-python-root",
        help="typespec-python repo root folder",
        type=str,
    )

    parser.add_argument(
        "--typespec-python-branch",
        help="branch of typespec-python repo",
        type=str,
    )

    args = parser.parse_args()

    main(args.sdk_root, args.typespec_python_root, args.typespec_python_branch)
