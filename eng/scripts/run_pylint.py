#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# This script is used to execute pylint within a tox environment. Depending on which package is being executed against,
# a failure may be suppressed.

from subprocess import check_call, CalledProcessError
import os
import logging
import sys
from pathlib import Path
import argparse
from multiprocessing import Pool
logging.getLogger().setLevel(logging.INFO)

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", ".."))
rfc_file_location = os.path.join(root_dir, "pylintrc")
lint_plugin_path = os.path.join(root_dir, "scripts/pylint_custom_plugin")

def _single_dir_pylint(mod):
    inner_class = next(d for d in mod.iterdir() if d.is_dir() and not str(d).endswith("egg-info"))
    try:
        check_call(
            [
                sys.executable,
                "-m",
                "pylint",
                "--rcfile={}".format(rfc_file_location),
                "--output-format=parseable",
                str(inner_class.absolute()),
            ]
        )
    except CalledProcessError as e:
        logging.error(
            "{} exited with linting error {}".format(inner_class.stem, e.returncode)
        )
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run pylint against target folder. Add a local custom plugin to the path prior to execution. "
    )
    parser.add_argument(
        "-t",
        "--test-folder",
        dest="test_folder",
        help="The test folder we're in. Can be 'azure', 'llc', 'multiapi', or 'vanilla'",
        required=True,
    )
    parser.add_argument(
        "-g",
        "--generator",
        dest="generator",
        help="The generator we're using. Can be 'legacy', 'version-tolerant', or 'low-level'.",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--file-name",
        dest="file_name",
        help="The specific file name if you only want to run one file. Optional.",
        required=False,
    )

    args = parser.parse_args()

    pkg_dir = Path(root_dir) / Path("test") / Path(args.test_folder) / Path(args.generator) / Path("Expected") / Path("AcceptanceTests")
    dirs = [d for d in pkg_dir.iterdir() if d.is_dir()]
    if args.file_name:
        dirs = [d for d in dirs if d.stem.lower() == args.file_name.lower()]
    with Pool() as pool:
        result = pool.map(_single_dir_pylint, dirs)
