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
from util import run_check, ROOT_FOLDER

logging.getLogger().setLevel(logging.INFO)

def get_rfc_file_location():
    rfc_file_location = os.path.join(os.getcwd(), "../../scripts/eng/pylintrc")
    if os.path.exists(rfc_file_location):
        return rfc_file_location
    else:
        return os.path.join(os.getcwd(), "../../../scripts/eng/pylintrc")


def _single_dir_pylint(mod):
    inner_class = next(d for d in mod.iterdir() if d.is_dir() and not str(d).endswith("egg-info"))
    try:
        check_call(
            [
                sys.executable,
                "-m",
                "pylint",
                "--rcfile={}".format(get_rfc_file_location()),
                "--load-plugins=pylint_guidelines_checker",
                "--output-format=parseable",
                str(inner_class.absolute()),
            ]
        )
        return True
    except CalledProcessError as e:
        logging.error("{} exited with linting error {}".format(inner_class.stem, e.returncode))
        return False


if __name__ == "__main__":
    run_check("pylint", _single_dir_pylint, "Pylint")
