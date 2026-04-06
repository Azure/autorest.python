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
from util import run_check

logging.getLogger().setLevel(logging.INFO)


def get_rfc_file_location():
    # When running from tests/ directory via tox
    rfc_file_location = os.path.join(os.getcwd(), "../eng/scripts/ci/config/pylintrc")
    if os.path.exists(rfc_file_location):
        return rfc_file_location
    # Fallback for running from different directories
    return os.path.join(os.path.dirname(__file__), "config/pylintrc")


def _has_python_files(directory):
    """Check if a directory contains any .py files recursively."""
    return any(directory.rglob("*.py"))


def _single_dir_pylint(mod):
    inner_class = next(
        (d for d in mod.iterdir() if d.is_dir() and d.name != "build" and not str(d).endswith("egg-info") and _has_python_files(d)),
        None
    )
    if inner_class is None:
        logging.warning("No valid source directory found in %s, skipping", mod)
        return True
    try:
        check_call(
            [
                sys.executable,
                "-m",
                "pylint",
                "--rcfile={}".format(get_rfc_file_location()),
                "--evaluation=(max(0, 0 if fatal else 10.0 - ((float(5 * error + warning + refactor + convention + info)/ statement) * 10)))",
                "--load-plugins=pylint_guidelines_checker",
                "--output-format=parseable",
                "--recursive=y",
                "--ignore=build",
                "--py-version=3.9",
                str(inner_class.absolute()),
            ]
        )
        return True
    except CalledProcessError as e:
        logging.error("{} exited with linting error {}".format(str(inner_class.absolute()), e.returncode))
        return False


if __name__ == "__main__":
    if os.name == "nt":
        # Before https://github.com/microsoft/typespec/issues/4759 fixed, skip running Pylint for now on Windows
        logging.info("Skip running Pylint on Windows for now")
        sys.exit(0)
    run_check("pylint", _single_dir_pylint, "Pylint")
