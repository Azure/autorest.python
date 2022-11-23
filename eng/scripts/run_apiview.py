#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# This script is used to execute apiview generation within a tox environment. Depending on which package is being executed against,
# a failure may be suppressed.

from subprocess import check_call, CalledProcessError
import os
import logging
from pathlib import Path
import argparse
from multiprocessing import Pool
logging.getLogger().setLevel(logging.INFO)

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", ".."))

def _single_dir_apiview(mod):
    # inner_dirs = next(d for d in mod.iterdir() if d.is_dir() and not str(d).endswith("egg-info"))
    try:
        check_call(
            [
                "apistubgen",
                "--pkg-path",
                str(mod.absolute()),
            ]
        )
        return True
        #   $_.FullName
    except CalledProcessError as e:
        logging.error(
            "{} exited with apiview generation error {}".format(mod.stem, e.returncode)
        )
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run apiview generation against target folder. Add a local custom plugin to the path prior to execution. "
    )
    parser.add_argument(
        "-t",
        "--test-folder",
        dest="test_folder",
        help="The test folder we're in. Can be 'azure', 'multiapi', or 'vanilla'",
        required=True,
    )
    parser.add_argument(
        "-g",
        "--generator",
        dest="generator",
        help="The generator we're using. Can be 'legacy', 'version-tolerant'.",
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

    pkg_dir = Path(root_dir) / Path("packages/autorest.python") / Path("test") / Path(args.test_folder) / Path(args.generator) / Path("Expected") / Path("AcceptanceTests")
    dirs = [d for d in pkg_dir.iterdir() if d.is_dir()]
    if args.file_name:
        dirs = [d for d in dirs if d.stem.lower() == args.file_name.lower()]
    if len(dirs) > 1:
        with Pool() as pool:
            result = pool.map(_single_dir_apiview, dirs)
        response = all(result)
    else:
        response = _single_dir_apiview(dirs[0])
    if not response:
        logging.error(
            "Linting fails"
        )
        exit(1)
