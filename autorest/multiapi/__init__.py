# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import sys
import logging
import json
import shutil

from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple, Optional, cast, Any
from .multiapi_serializer import MultiAPISerializer
from ..jsonrpc import AutorestAPI

from .. import Plugin

_LOGGER = logging.getLogger(__name__)


class MultiApiScriptPlugin(Plugin):
    def process(self) -> bool:
        input_package_name: str = self._autorestapi.get_value("package-name")
        output_folder: str = self._autorestapi.get_value("output-folder")
        default_api: str = self._autorestapi.get_value("default-api")
        no_async = self._autorestapi.get_boolean_value("no-async")
        generator = MultiAPI(
            input_package_name,
            output_folder,
            self._autorestapi,
            no_async,
            default_api
        )
        return generator.process()


def _get_floating_latest(api_versions_list: List[str], preview_mode: bool) -> str:
    """Get the floating latest, from a random list of API versions.
    """
    api_versions_list = list(api_versions_list)
    absolute_latest = sorted(api_versions_list)[-1]
    trimmed_preview = [
        version for version in api_versions_list if "preview" not in version
    ]

    # If there is no preview, easy: the absolute latest is the only latest
    if not trimmed_preview:
        return absolute_latest

    # If preview mode, let's use the absolute latest, I don't care preview or stable
    if preview_mode:
        return absolute_latest

    # If not preview mode, and there is preview, take the latest known stable
    return sorted(trimmed_preview)[-1]

def _build_last_rt_list(
    versioned_operations_dict: Dict[str, List[Tuple[str, str]]],
    mixin_operations: Dict[str, Dict[str, Dict[str, Any]]],
    last_api_version: str,
    preview_mode: bool,
    async_mode: bool
) -> Dict[str, str]:
    """Build the a mapping RT => API version if RT doesn't exist in latest detected API version.

    Example:
    last_rt_list = {
    'check_dns_name_availability': '2018-05-01'
    }

    There is one subtle scenario if PREVIEW mode is disabled:
    - RT1 available on 2019-05-01 and 2019-06-01-preview
    - RT2 available on 2019-06-01-preview
    - RT3 available on 2019-07-01-preview

    Then, if I put "RT2: 2019-06-01-preview" in the list, this means I have to make
    "2019-06-01-preview" the default for models loading (otherwise "RT2: 2019-06-01-preview" won't work).
    But this likely breaks RT1 default operations at "2019-05-01", with default models at "2019-06-01-preview"
    since "models" are shared for the entire set of operations groups (I wished models would be split by
    operation groups, but meh, that's not the case)

    So, until we have a smarter Autorest to deal with that, only preview RTs which do not share models with
    a stable RT can be added to this map. In this case, RT2 is out, RT3 is in.
    """

    def there_is_a_rt_that_contains_api_version(rt_dict, api_version):
        "Test in the given api_version is is one of those RT."
        for rt_api_version in rt_dict.values():
            if api_version in rt_api_version:
                return True
        return False

    last_rt_list = {}

    sync_or_async = "async" if async_mode else "sync"

    # Operation groups
    versioned_dict = {
        operation_group_name: [meta[0] for meta in operation_metadata]
        for operation_group_name, operation_metadata in versioned_operations_dict.items()
    }
    # Operations at client level
    versioned_dict.update(
        {
            operation_metadata[sync_or_async]["operation_name"]: operation_metadata[sync_or_async]["available_apis"]
            for operation_metadata in mixin_operations.values()
        }
    )
    for operation, api_versions_list in versioned_dict.items():
        local_last_api_version = _get_floating_latest(api_versions_list, preview_mode)
        if local_last_api_version == last_api_version:
            continue
        # If some others RT contains "local_last_api_version", and
        # if it's greater than the future default, danger, don't profile it
        if (
            there_is_a_rt_that_contains_api_version(
                versioned_dict, local_last_api_version
            )
            and local_last_api_version > last_api_version
        ):
            continue
        last_rt_list[operation] = local_last_api_version
    return last_rt_list

class MultiAPI:
    def __init__(
        self,
        input_package_name: str,
        output_folder: str,
        autorestapi: AutorestAPI,
        no_async: Optional[bool] = False,
        default_api: Optional[str] = None
    ) -> None:
        if input_package_name is None:
            raise ValueError("package-name is required, either provide it as args or check your readme configuration")
        self.input_package_name = input_package_name
        _LOGGER.debug("Received package name %s", input_package_name)

        self.output_folder = Path(output_folder).resolve()
        _LOGGER.debug("Received output-folder %s", output_folder)
        self.output_package_name: str = ""
        self.no_async = no_async
        self._autorestapi = autorestapi
        self.default_api = default_api

    def _get_paths_to_versions(self) -> List[Path]:
        paths_to_versions = []
        for child in [x for x in self.output_folder.iterdir() if x.is_dir()]:
            child_dir = (self.output_folder / child).resolve()
            if Path(child_dir / '_metadata.json') in child_dir.iterdir():
                paths_to_versions.append(Path(child.stem))
        return paths_to_versions

    def _build_operation_mixin_meta(self, paths_to_versions: List[Path]) -> Dict[str, Dict[str, Dict[str, Any]]]:
        """Introspect the client:

        version_dict => {
            'check_dns_name_availability': {
                'doc': 'docstring',
                'signature': '(self, p1, p2, **operation_config),
                'call': 'p1, p2',
                'available_apis': [
                    'v2018_05_01'
                ]
            }
        }
        """
        mixin_operations: Dict[str, Dict[str, Dict[str, Any]]] = {}
        for version_path in paths_to_versions:
            metadata_json = json.loads(self._autorestapi.read_file(version_path / "_metadata.json"))
            if not metadata_json.get('operation_mixins'):
                continue
            for func_name, func in metadata_json['operation_mixins'].items():
                if func_name.startswith("_"):
                    continue

                mixin_operations.setdefault(func_name, {}).setdefault('sync', {})
                mixin_operations.setdefault(func_name, {}).setdefault('async', {})
                mixin_operations[func_name]['sync'].update({
                    "signature": func['sync']['signature'],
                    "operation_name": func['sync']['operation_name'],
                    "doc": func['doc'],
                    "call": func['call']
                })
                mixin_operations[func_name]['async'].update({
                    "signature": func['async']['signature'],
                    "operation_name": func['async']['operation_name'],
                    "coroutine": func['async']['coroutine'],
                    "doc": func['doc'],
                    "call": func['call']
                })
                mixin_operations[func_name]['sync'].setdefault(
                    "available_apis", []
                ).append(version_path.name)
                mixin_operations[func_name]['async'].setdefault(
                    "available_apis", []
                ).append(version_path.name)


        return mixin_operations

    def _build_operation_meta(
        self, paths_to_versions: List[Path]
    ) -> Tuple[Dict[str, List[Tuple[str, str]]], Dict[str, str]]:
        """Introspect the client:

        version_dict => {
            'application_gateways': [
                ('v2018_05_01', 'ApplicationGatewaysOperations')
            ]
        }
        mod_to_api_version => {'v2018_05_01': '2018-05-01'}
        """
        mod_to_api_version: Dict[str, str] = defaultdict(str)
        versioned_operations_dict: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
        for version_path in paths_to_versions:
            metadata_json = json.loads(self._autorestapi.read_file(version_path / "_metadata.json"))
            operation_groups = metadata_json['operation_groups']
            version = metadata_json['chosen_version']
            total_api_version_list = metadata_json['total_api_version_list']
            if not version:
                if total_api_version_list:
                    sys.exit(
                        f"Unable to match {total_api_version_list} to label {version_path.stem}"
                    )
                else:
                    sys.exit(
                        f"Unable to extract api version of {version_path.stem}"
                    )
            mod_to_api_version[version_path.name] = version
            for operation_group, operation_group_class_name in operation_groups.items():
                versioned_operations_dict[operation_group].append((version_path.name, operation_group_class_name))
        return versioned_operations_dict, mod_to_api_version

    def _parse_package_name_input(self) -> str:
        """From a syntax like package_name#submodule, build a package name
        and complete module name.
        """
        split_package_name = self.input_package_name.split("#")
        package_name = split_package_name[0]
        module_name = package_name.replace("-", ".")
        if len(split_package_name) >= 2:
            module_name = ".".join([module_name, split_package_name[1]])
            self.output_package_name = package_name
        else:
            self.output_package_name = self.input_package_name
        return module_name

    def process(self) -> bool:
        _LOGGER.info("Generating multiapi client")
        # If True, means the auto-profile will consider preview versions.
        # If not, if it exists a stable API version for a global or RT, will always be used
        preview_mode = cast(bool, self.default_api and "preview" in self.default_api)

        module_name = self._parse_package_name_input()
        paths_to_versions = self._get_paths_to_versions()
        versioned_operations_dict, mod_to_api_version = self._build_operation_meta(
            paths_to_versions
        )

        last_api_version = _get_floating_latest(list(mod_to_api_version.keys()), preview_mode)

        # I need default_api to be v2019_06_07_preview shaped if it exists, let's be smart
        # and change it automatically so I can take both syntax as input
        if self.default_api and not self.default_api.startswith("v"):
            last_api_version = [
                mod_api
                for mod_api, real_api in mod_to_api_version.items()
                if real_api == self.default_api
            ][0]
            _LOGGER.info("Default API version will be: %s", last_api_version)

        # I need default_api to be v2019_06_07_preview shaped if it exists, let's be smart
        # and change it automatically so I can take both syntax as input
        if self.default_api and not self.default_api.startswith("v"):
            last_api_version = [
                mod_api
                for mod_api, real_api in mod_to_api_version.items()
                if real_api == self.default_api
            ][0]
            _LOGGER.info("Default API version will be: %s", last_api_version)

        # In case we are transitioning from a single api generation, clean old folders
        shutil.rmtree(str(self.output_folder / "operations"), ignore_errors=True)
        shutil.rmtree(str(self.output_folder / "models"), ignore_errors=True)

        # Detect if this client is using an operation mixin (Network)
        # Operation mixins are available since Autorest.Python 4.x
        mixin_operations = self._build_operation_mixin_meta(paths_to_versions)

        # get client name from default api version
        path_to_default_version = Path()
        for path_to_version in paths_to_versions:
            if last_api_version.replace("-", "_") == path_to_version.stem:
                path_to_default_version = path_to_version
                break
        metadata_json = json.loads(self._autorestapi.read_file(path_to_default_version / "_metadata.json"))

        # versioned_operations_dict => {
        #     'application_gateways': [
        #         ('v2018-05-01', 'ApplicationGatewaysOperations')
        #     ]
        # }
        # mod_to_api_version => {'v2018-05-01': '2018-05-01'}
        # mixin_operations => {
        #     'check_dns_name_availability': {
        #         'doc': 'docstring',
        #         'signature': '(self, p1, p2, **operation_config),
        #         'call': 'p1, p2',
        #         'available_apis': [
        #             'v2018_05_01'
        #         ]
        #     }
        # }
        # last_rt_list = {
        #    'check_dns_name_availability': '2018-05-01'
        # }

        last_rt_list_sync = _build_last_rt_list(
            versioned_operations_dict, mixin_operations, last_api_version, preview_mode, async_mode=False
        )
        last_rt_list_async = _build_last_rt_list(
            versioned_operations_dict, mixin_operations, last_api_version, preview_mode, async_mode=True
        )

        conf = {
            "client_name": metadata_json["client"]["name"],
            "package_name": self.output_package_name,
            "module_name": module_name,
            "operations": versioned_operations_dict,
            "mixin_operations": mixin_operations,
            "mod_to_api_version": mod_to_api_version,
            "last_api_version": mod_to_api_version[last_api_version],
            "client_doc": metadata_json["client"]["description"],
            "last_rt_list_sync": last_rt_list_sync,
            "last_rt_list_async": last_rt_list_async,
            "default_models": sorted(
                {last_api_version} | {versions for _, versions in last_rt_list_sync.items()}
            ),
            "config": metadata_json["config"],
            "global_parameters": metadata_json["global_parameters"],
            "sync_imports": metadata_json["sync_imports"],
            "async_imports": metadata_json["async_imports"]
        }

        multiapi_serializer = MultiAPISerializer(
            conf=conf,
            async_mode=False,
            autorestapi=self._autorestapi,
            service_client_filename=metadata_json["client"]["filename"]
        )
        multiapi_serializer.serialize()

        if not self.no_async:
            async_multiapi_serializer = MultiAPISerializer(
                conf=conf,
                async_mode=True,
                autorestapi=self._autorestapi,
                service_client_filename=metadata_json["client"]["filename"]
            )
            async_multiapi_serializer.serialize()


        # don't erase patch file
        if self._autorestapi.read_file("_patch.py"):
            self._autorestapi.write_file(
                "_patch.py",
                self._autorestapi.read_file("_patch.py")
            )

        _LOGGER.info("Done!")
        return True
