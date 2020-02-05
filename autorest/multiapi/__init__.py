# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from .. import Plugin
import importlib
import pkgutil
import sys
import argparse
import logging
import azure

from pathlib import Path
from typing import Any, List, Tuple, Optional

try:
    import msrestazure
except:  # Install msrestazure. Would be best to mock it, since we don't need it, but all scenarios I know are fine with a pip install for now
    import subprocess

    subprocess.call(
        sys.executable + " -m pip install msrestazure", shell=True
    )  # Use shell to use venv if available

try:
    from jinja2 import Template, FileSystemLoader, Environment
except:
    import subprocess

    subprocess.call(
        sys.executable + " -m pip install jinja2", shell=True
    )  # Use shell to use venv if available
    from jinja2 import Template, FileSystemLoader, Environment

import pkg_resources
pkg_resources.declare_namespace("azure")

_LOGGER = logging.getLogger(__name__)

class MultiAPI:
    def __init__(self, input_str: str, default_api: Optional[str] = None):
        self.input_str = input_str
        self.default_api = default_api

    @staticmethod
    def _parse_input(input_parameter: str):
        """From a syntax like package_name#submodule, build a package name
        and complete module name.
        """
        split_package_name = input_parameter.split("#")
        package_name = split_package_name[0]
        module_name = package_name.replace("-", ".")
        if len(split_package_name) >= 2:
            module_name = ".".join([module_name, split_package_name[1]])
        return package_name, module_name

    @staticmethod
    def _resolve_package_directory(package_name: str, sdk_root: Path):
        """Returns the appropriate relative diff between the sdk_root and the actual package_directory
        """
        packages = [
            p.parent
            for p in (
                list(sdk_root.glob(f"{package_name}/setup.py")) +
                list(sdk_root.glob(f"sdk/*/{package_name}/setup.py"))
            )
        ]

        if len(packages) > 1:
            print(
                f"There should only be a single package matched in either repository structure. The following were found: {packages}"
            )
            sys.exit(1)
        return str(packages[0].relative_to(sdk_root))

    @staticmethod
    def _get_versioned_modules(package_name: str, module_name: str, sdk_root: Optional[Path] = None):
        """Get (label, submodule) where label starts with "v20" and submodule is the corresponding imported module.
        """
        if not sdk_root:
            sdk_root = Path(__file__).parents[3] / "azure-sdk-for-python"

        path_to_package = MultiAPI._resolve_package_directory(package_name, sdk_root)

        azure.__path__.append(str((sdk_root / path_to_package / "azure").resolve()))
        module_to_generate = importlib.import_module(module_name)
        raise ValueError(module_to_generate)
        return {
            label: importlib.import_module("." + label, module_to_generate.__name__)
            for (_, label, ispkg) in pkgutil.iter_modules(module_to_generate.__path__)
            if label.startswith("v20") and ispkg
        }

    def process(self) -> bool:
        # If True, means the auto-profile will consider preview versions.
        # If not, if it exists a stable API version for a global or RT, will always be used
        preview_mode = self.default_api and "preview" in self.default_api

        # The only known multi-client package right now is azure-mgmt-resource
        is_multi_client_package = "#" in self.input_str

        package_name, module_name = MultiAPI._parse_input(self.input_str)
        versioned_modules = MultiAPI._get_versioned_modules(package_name, module_name)
        raise ValueError(versioned_modules)

        return True


if __name__ == "__main__":
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

    args = parser.parse_args()

    main_logger = logging.getLogger()
    logging.basicConfig()
    main_logger.setLevel(logging.DEBUG if args.debug else logging.INFO)

    MultiAPI(args.package_name, args.default_api).process()
