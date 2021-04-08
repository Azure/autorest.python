#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import argparse
import logging
import os
from subprocess import check_call, CalledProcessError


SWAGGER_FOLDER = "swagger"


def run_check_call(
    command_array,
    working_directory,
    acceptable_return_codes=[],
    run_as_shell=False,
    always_exit=True,
):
    try:
        if run_as_shell:
            logging.info(
                "Command Array: {0}, Target Working Directory: {1}".format(
                    " ".join(command_array), working_directory
                )
            )
            check_call(" ".join(command_array), cwd=working_directory, shell=True)
        else:
            logging.info(
                "Command Array: {0}, Target Working Directory: {1}".format(
                    command_array, working_directory
                )
            )
            check_call(command_array, cwd=working_directory)
    except CalledProcessError as err:
        if err.returncode not in acceptable_return_codes:
            logging.error(err)  # , file = sys.stderr
            if always_exit:
                exit(1)
            else:
                return err


def find_swagger_folders(directory):
    logging.info("Searching for swagger files in: {}".format(directory))

    ret = []
    for root, subdirs, files in os.walk(directory):
        for d in subdirs:
            if d == SWAGGER_FOLDER:
                if os.path.exists(os.path.join(root, d, "README.md")):
                    ret.append(os.path.join(root, d))

    logging.info("Found swagger files at: {}".format(ret))
    return ret


def run_autorest(service_dir):

    swagger_folders = find_swagger_folders(service_dir)

    for working_dir in swagger_folders:
        # os.chdir(working_dir)
        f = os.path.join(working_dir, "README.md")
        print(f)
        if os.path.exists(f):
            reset_command = ["autorest", "--reset"]
            print(reset_command, os.path.abspath("."))
            run_check_call(reset_command, os.path.abspath("."), run_as_shell=True)

            command = ["autorest", "--python", os.path.abspath(f), "--verbose"]
            logging.info("Command: {}\nLocation: {}\n".format(command, working_dir))
            print(command, working_dir)
            run_check_call(command, working_dir, run_as_shell=True)
    # return swagger_folders


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Update generated code"
    )

    parser.add_argument(
        "-s",
        "--sdk-repo-root",
        dest="repo_root",
        help="Home location of azure-sdk-for-python",
        required=True,
    )

    args = parser.parse_args()

    root = os.path.abspath(args.repo_root)
    service_dir = os.path.join(root, "sdk")

    logging.info("Starting autorest generation")

    run_autorest(service_dir)