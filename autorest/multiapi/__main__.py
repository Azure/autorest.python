# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import argparse
import logging
from . import MultiAPI


parser = argparse.ArgumentParser(
    description="Multi-API client generation for Azure SDK for Python"
)
parser.add_argument(
    "--debug", dest="debug", action="store_true", help="Verbosity in DEBUG mode"
)
parser.add_argument(
    "--default-api-version",
    dest="default_api",
    default=None,
    help="Force default API version, do not detect it. [default: %(default)s]",
)
parser.add_argument("package_name", help="The package name.")
parser.add_argument(
    "--python-sdks-folder",
    dest="python_sdks_folder",
    help="The root of your python sdk repo."
)

args = parser.parse_args()

main_logger = logging.getLogger()
logging.basicConfig()
main_logger.setLevel(logging.DEBUG if args.debug else logging.INFO)

MultiAPI(args).process()
