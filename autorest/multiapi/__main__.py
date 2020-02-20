# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import argparse
import logging
import sys
from . import MultiApiScriptPlugin
from ..jsonrpc.localapi import LocalAutorestAPI


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

input_package_name: str = args.package_name
python_sdks_folder: str = args.python_sdks_folder
default_api: str = args.default_api

autorest_api = LocalAutorestAPI(output_folder=python_sdks_folder)
autorest_api.values = {
    "python-sdks-folder": python_sdks_folder,
    "package-name": input_package_name,
    "default-api": default_api
}


generator = MultiApiScriptPlugin(autorest_api)
if not generator.process():
    sys.exit(1)
