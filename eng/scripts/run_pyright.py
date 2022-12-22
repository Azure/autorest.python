#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# This script is used to execute pyright within a tox environment. Depending on which package is being executed against,
# a failure may be suppressed.

from subprocess import check_output, CalledProcessError
import os
import logging
import sys
import time
from pathlib import Path
import argparse
from multiprocessing import Pool
logging.getLogger().setLevel(logging.INFO)

root_dir = os.path.abspath(os.path.join(
    os.path.abspath(__file__), "..", "..", ".."))
config_file_dir = Path(root_dir) / Path("packages/autorest.python")

def _single_dir_pyright(mod):
    inner_class = next(d for d in mod.iterdir() if d.is_dir()
                       and not str(d).endswith("egg-info"))
    retries = 3
    while retries:
        try:
            check_output(
                [
                    sys.executable,
                    "-m",
                    "pyright",
                    "-p",
                    str(config_file_dir),
                    str(inner_class.absolute()),
                ]
            )
            return True
        except CalledProcessError as e:
            logging.exception(
                "{} exited with pyright error {}".format(
                    inner_class.stem, e.returncode)
            )
            logging.error(f"PyRight stdout:\n{e.stdout}\n===========")
            logging.error(f"PyRight stderr:\n{e.stderr}\n===========")
            # PyRight has shown to randomly failed with a 217, retry the same folder 3 times should help
            retries -= 1
            time.sleep(5)

    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run pyright against target folder. Add a local custom plugin to the path prior to execution. "
    )
    parser.add_argument(
        "-p",
        "--package",
        dest="package",
        help="The specific which package to verify, autorest.python or cadl-python. Optional.",
        required=False,
        default="autorest.python",
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
        required=False,
    )
    parser.add_argument(
        "-f",
        "--file-name",
        dest="file_name",
        help="The specific file name if you only want to run one file. Optional.",
        required=False,
    )
    parser.add_argument(
        "-s",
        "--subfolder",
        dest="subfolder",
        help="The specific sub folder to validate, default to Expected/AcceptanceTests. Optional.",
        required=False,
        default="Expected/AcceptanceTests",
    )

    args = parser.parse_args()

    pkg_dir = Path(
        root_dir) / Path(f"packages/{args.package}") / Path("test") / Path(args.test_folder)
    if args.generator:
        pkg_dir /= Path(args.generator)
    if args.subfolder:
        pkg_dir /= Path(args.subfolder)
    dirs = [d for d in pkg_dir.iterdir() if d.is_dir()]
    if args.file_name:
        dirs = [d for d in dirs if d.stem.lower() == args.file_name.lower()]
    if len(dirs) > 1:
        with Pool() as pool:
            result = pool.map(_single_dir_pyright, dirs)
        response = all(result)
    else:
        response = _single_dir_pyright(dirs[0])
    if not response:
        logging.error(
            "Linting fails"
        )
        exit(1)
