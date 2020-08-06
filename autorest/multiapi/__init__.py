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
from .serializers import MultiAPISerializer, FileImportSerializer
from .models import CodeModel, FileImport
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


def _extract_version(metadata_json: Dict[str, Any], version_path: Path) -> str:
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
    return version

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

    def _build_last_rt_list(
        self,
        versioned_operations_dict: Dict[str, List[Tuple[str, str]]],
        mixin_operations: Dict[str, Dict[str, Dict[str, Any]]],
        default_api_version: str,
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
                operation_name: operation_metadata[sync_or_async]["available_apis"]
                for operation_name, operation_metadata in mixin_operations.items()
            }
        )
        for operation, api_versions_list in versioned_dict.items():
            local_default_api_version = self._get_default_api_version(api_versions_list, preview_mode)
            if local_default_api_version == default_api_version:
                continue
            # If some others RT contains "local_default_api_version", and
            # if it's greater than the future default, danger, don't profile it
            if (
                there_is_a_rt_that_contains_api_version(
                    versioned_dict, local_default_api_version
                )
                and local_default_api_version > default_api_version
            ):
                continue
            last_rt_list[operation] = local_default_api_version
        return last_rt_list

    def _get_default_api_version(
        self,
        api_versions_list: List[str],
        preview_mode: bool,
        mod_to_api_version: Optional[Dict[str, str]] = None,
    ) -> str:
        """Get the floating latest, from a random list of API versions.
        """

        # I need default_api to be v2019_06_07_preview shaped if it exists, let's be smart
        # and change it automatically so I can take both syntax as input
        if mod_to_api_version and self.default_api and not self.default_api.startswith("v"):
            default_api_version = [
                mod_api
                for mod_api, real_api in mod_to_api_version.items()
                if real_api == self.default_api
            ][0]
            _LOGGER.info("Default API version will be: %s", default_api_version)
            return default_api_version

        absolute_latest = sorted(api_versions_list)[-1]
        not_preview_versions = [
            version for version in api_versions_list if "preview" not in version
        ]

        # If there is no preview, easy: the absolute latest is the only latest
        if not not_preview_versions:
            return absolute_latest

        # If preview mode, let's use the absolute latest, I don't care preview or stable
        if preview_mode:
            return absolute_latest

        # If not preview mode, and there is preview, take the latest known stable
        return sorted(not_preview_versions)[-1]

    def _get_mod_to_api_version(self, paths_to_versions: List[Path]) -> Dict[str, str]:
        mod_to_api_version: Dict[str, str] = defaultdict(str)
        for version_path in paths_to_versions:
            metadata_json = json.loads(self._autorestapi.read_file(version_path / "_metadata.json"))
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
        return mod_to_api_version


    def _get_paths_to_versions(self) -> List[Path]:
        paths_to_versions = []
        directory = [x for x in self.output_folder.iterdir() if x.is_dir()]
        directory.sort()
        for child in directory:
            child_dir = (self.output_folder / child).resolve()
            if Path(child_dir / '_metadata.json') in child_dir.iterdir():
                paths_to_versions.append(Path(child.stem))
        return paths_to_versions

    def _make_signature_of_mixin_based_on_default_api_version(
        self,
        mixin_operations: Dict[str, Dict[str, Dict[str, Any]]],
        default_api_version_path: Path
    ) -> Dict[str, Dict[str, Dict[str, Any]]]:
        metadata_json = json.loads(self._autorestapi.read_file(default_api_version_path / "_metadata.json"))
        if not metadata_json.get('operation_mixins'):
            return mixin_operations
        for func_name, func in metadata_json['operation_mixins'].items():
            if func_name.startswith("_"):
                continue

            mixin_operations.setdefault(func_name, {}).setdefault('sync', {})
            mixin_operations.setdefault(func_name, {}).setdefault('async', {})
            mixin_operations[func_name]['sync'].update({
                "signature": func['sync']['signature'],
                "doc": func['sync']['doc'],
                "call": func['call']
            })
            mixin_operations[func_name]['async'].update({
                "signature": func['async']['signature'],
                "coroutine": func['async']['coroutine'],
                "doc": func['async']['doc'],
                "call": func['call']
            })
        return mixin_operations

    def _build_operation_mixin_meta(
        self, paths_to_versions: List[Path], default_api_version: str
    ) -> Dict[str, Dict[str, Dict[str, Any]]]:
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
                    "doc": func['sync']['doc'],
                    "call": func['call']
                })
                mixin_operations[func_name]['async'].update({
                    "signature": func['async']['signature'],
                    "coroutine": func['async']['coroutine'],
                    "doc": func['async']['doc'],
                    "call": func['call']
                })
                mixin_operations[func_name]['sync'].setdefault(
                    "available_apis", []
                ).append(version_path.name)
                mixin_operations[func_name]['async'].setdefault(
                    "available_apis", []
                ).append(version_path.name)

        # make sure that the signature, doc, call, and coroutine is based off of the default api version,
        # if the default api version has a definition for it.
        # will hopefully get this removed once we deal with mixin operations with different signatures
        # for different api versions
        default_api_version_path = [
            version_path for version_path in paths_to_versions if version_path.name == default_api_version
        ][0]
        return self._make_signature_of_mixin_based_on_default_api_version(mixin_operations, default_api_version_path)

    def _build_custom_base_url_to_api_version(
        self, paths_to_versions: List[Path]
    ) -> Dict[str, List[str]]:
        custom_base_url_to_api_version: Dict[str, List[str]] = {}
        for version_path in paths_to_versions:
            metadata_json = json.loads(self._autorestapi.read_file(version_path / "_metadata.json"))
            custom_base_url = metadata_json["client"]["custom_base_url"]
            version = _extract_version(metadata_json, version_path)
            custom_base_url_to_api_version.setdefault(custom_base_url, []).append(version)
        return custom_base_url_to_api_version

    def _get_versioned_operations_dict(
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
        versioned_operations_dict: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
        for version_path in paths_to_versions:
            metadata_json = json.loads(self._autorestapi.read_file(version_path / "_metadata.json"))
            operation_groups = metadata_json['operation_groups']
            version = _extract_version(metadata_json, version_path)
            for operation_group, operation_group_class_name in operation_groups.items():
                versioned_operations_dict[operation_group].append((version_path.name, operation_group_class_name))
        return versioned_operations_dict

    def _get_module_name(self) -> str:
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

    def _get_default_version_metadata(
        self, default_api_version: str, paths_to_versions: List[Path]
    ) -> Dict[str, Any]:
        # get client name from default api version
        path_to_default_version = Path()
        for path_to_version in paths_to_versions:
            if default_api_version.replace("-", "_") == path_to_version.stem:
                path_to_default_version = path_to_version
                break
        return json.loads(self._autorestapi.read_file(path_to_default_version / "_metadata.json"))

    def _merge_mixin_imports_across_versions(
        self, paths_to_versions: List[Path], async_mode: bool
    ) -> FileImport:
        imports = FileImport()
        imports_to_load = "async_imports" if async_mode else "sync_imports"
        for version_path in paths_to_versions:
            metadata_json = json.loads(self._autorestapi.read_file(version_path / "_metadata.json"))
            if not metadata_json.get('operation_mixins'):
                continue
            current_version_imports = FileImport(json.loads(metadata_json[imports_to_load]))
            imports.merge(current_version_imports)

        return imports

    def _has_lro_operations(
        self, paths_to_versions: List[Path]
    ) -> bool:
        has_lro_operations = False
        for version_path in paths_to_versions:
            metadata_json = json.loads(self._autorestapi.read_file(version_path / "_metadata.json"))
            current_client_has_lro_operations = metadata_json["client"]["has_lro_operations"]
            if current_client_has_lro_operations:
                has_lro_operations = True
        return has_lro_operations

    def process(self) -> bool:
        _LOGGER.info("Generating multiapi client")
        # If True, means the auto-profile will consider preview versions.
        # If not, if it exists a stable API version for a global or RT, will always be used
        preview_mode = cast(bool, self.default_api and "preview" in self.default_api)

        module_name = self._get_module_name()
        paths_to_versions = self._get_paths_to_versions()
        mod_to_api_version = self._get_mod_to_api_version(paths_to_versions)

        default_api_version = self._get_default_api_version(
            [p.name for p in paths_to_versions],
            preview_mode,
            mod_to_api_version,
        )

        default_version_metadata = self._get_default_version_metadata(default_api_version, paths_to_versions)

        code_model = CodeModel(
            module_name=module_name,
            default_api_version=default_api_version,
            default_version_metadata=default_version_metadata,
            mod_to_api_version=mod_to_api_version
        )

        versioned_operations_dict = self._get_versioned_operations_dict(paths_to_versions)

        # In case we are transitioning from a single api generation, clean old folders
        shutil.rmtree(str(self.output_folder / "operations"), ignore_errors=True)
        shutil.rmtree(str(self.output_folder / "models"), ignore_errors=True)

        # Detect if this client is using an operation mixin (Network)
        # Operation mixins are available since Autorest.Python 4.x
        mixin_operations = self._build_operation_mixin_meta(paths_to_versions, default_api_version)


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

        last_rt_list_sync = self._build_last_rt_list(
            versioned_operations_dict, mixin_operations, default_api_version, preview_mode, async_mode=False
        )
        last_rt_list_async = self._build_last_rt_list(
            versioned_operations_dict, mixin_operations, default_api_version, preview_mode, async_mode=True
        )

        sync_imports = self._merge_mixin_imports_across_versions(
            paths_to_versions, async_mode=False
        )

        async_imports = self._merge_mixin_imports_across_versions(
            paths_to_versions, async_mode=True
        )

        conf = {
            "client_name": default_version_metadata["client"]["name"],
            "package_name": self.output_package_name,
            "module_name": code_model.module_name,
            "operations": versioned_operations_dict,
            "mixin_operations": mixin_operations,
            "mod_to_api_version": mod_to_api_version,
            "default_api_version": mod_to_api_version[default_api_version],
            "client_doc": default_version_metadata["client"]["description"],
            "last_rt_list_sync": last_rt_list_sync,
            "last_rt_list_async": last_rt_list_async,
            "default_models": sorted(
                {default_api_version} | {versions for _, versions in last_rt_list_sync.items()}
            ),
            "config": default_version_metadata["config"],
            "global_parameters": default_version_metadata["global_parameters"],
            "sync_imports": str(FileImportSerializer(sync_imports, is_python_3_file=False)),
            "async_imports": str(FileImportSerializer(async_imports, is_python_3_file=True)),
            "base_url": default_version_metadata["client"]["base_url"],
            "custom_base_url_to_api_version": self._build_custom_base_url_to_api_version(paths_to_versions),
            "azure_arm": default_version_metadata["client"]["azure_arm"],
            "has_lro_operations": self._has_lro_operations(paths_to_versions)
        }

        multiapi_serializer = MultiAPISerializer(
            conf=conf,
            async_mode=False,
            autorestapi=self._autorestapi,
            service_client_filename=default_version_metadata["client"]["filename"]
        )
        multiapi_serializer.serialize()

        if not self.no_async:
            async_multiapi_serializer = MultiAPISerializer(
                conf=conf,
                async_mode=True,
                autorestapi=self._autorestapi,
                service_client_filename=default_version_metadata["client"]["filename"]
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
