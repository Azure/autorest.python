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
from .utils import _extract_version, _sync_or_async, _get_default_api_version_from_list
from ..jsonrpc import AutorestAPI

from .. import Plugin

_LOGGER = logging.getLogger(__name__)


class MultiApiScriptPlugin(Plugin):
    def process(self) -> bool:
        input_package_name: str = self._autorestapi.get_value("package-name")
        output_folder: str = self._autorestapi.get_value("output-folder")
        user_specified_default_api: str = self._autorestapi.get_value("default-api")
        no_async = self._autorestapi.get_boolean_value("no-async")
        generator = MultiAPI(
            input_package_name,
            output_folder,
            self._autorestapi,
            no_async,
            user_specified_default_api
        )
        return generator.process()


class MultiAPI:
    def __init__(
        self,
        input_package_name: str,
        output_folder: str,
        autorestapi: AutorestAPI,
        no_async: Optional[bool] = False,
        user_specified_default_api: Optional[str] = None
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
        self.user_specified_default_api = user_specified_default_api

    def _merge_mixin_imports_across_versions(self, async_mode: bool) -> FileImport:
        imports = FileImport()
        imports_to_load = "async_imports" if async_mode else "sync_imports"
        for version_path in self.paths_to_versions:
            metadata_json = json.loads(self._autorestapi.read_file(version_path / "_metadata.json"))
            if not metadata_json.get('operation_mixins'):
                continue
            current_version_imports = FileImport(json.loads(metadata_json[imports_to_load]))
            imports.merge(current_version_imports)

        return imports

    @property
    def default_api_version(self) -> str:
        return _get_default_api_version_from_list(
            self.mod_to_api_version,
            [p.name for p in self.paths_to_versions],
            self.preview_mode,
            self.user_specified_default_api
        )

    @property
    def default_version_metadata(self) -> Dict[str, Any]:
        # get client name from default api version
        path_to_default_version = Path()
        for path_to_version in self.paths_to_versions:
            if self.default_api_version.replace("-", "_") == path_to_version.stem:
                path_to_default_version = path_to_version
                break
        return json.loads(self._autorestapi.read_file(path_to_default_version / "_metadata.json"))

    @property
    def module_name(self) -> str:
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

    @property
    def preview_mode(self) -> bool:
        # If True, means the auto-profile will consider preview versions.
        # If not, if it exists a stable API version for a global or RT, will always be used
        return cast(bool, self.user_specified_default_api and "preview" in self.user_specified_default_api)

    @property
    def paths_to_versions(self) -> List[Path]:
        paths_to_versions = []
        directory = [x for x in self.output_folder.iterdir() if x.is_dir()]
        directory.sort()
        for child in directory:
            child_dir = (self.output_folder / child).resolve()
            if Path(child_dir / '_metadata.json') in child_dir.iterdir():
                paths_to_versions.append(Path(child.stem))
        return paths_to_versions

    @property
    def version_path_to_metadata(self) -> Dict[Path, Dict[str, Any]]:
        return {
            version_path: json.loads(self._autorestapi.read_file(version_path / "_metadata.json"))
            for version_path in self.paths_to_versions
        }

    @property
    def mod_to_api_version(self) -> Dict[str, str]:
        mod_to_api_version: Dict[str, str] = defaultdict(str)
        for version_path in self.paths_to_versions:
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

    def process(self) -> bool:
        _LOGGER.info("Generating multiapi client")

        code_model = CodeModel(
            module_name=self.module_name,
            default_api_version=self.default_api_version,
            preview_mode=self.preview_mode,
            default_version_metadata=self.default_version_metadata,
            mod_to_api_version=self.mod_to_api_version,
            version_path_to_metadata=self.version_path_to_metadata,
            user_specified_default_api=self.user_specified_default_api
        )

        # In case we are transitioning from a single api generation, clean old folders
        shutil.rmtree(str(self.output_folder / "operations"), ignore_errors=True)
        shutil.rmtree(str(self.output_folder / "models"), ignore_errors=True)

        sync_imports = code_model.mixin_operation_group.imports(async_mode=False)

        async_imports = code_model.mixin_operation_group.imports(async_mode=True)

        conf = {
            "client_name": code_model.service_client.name,
            "package_name": self.output_package_name,
            "module_name": code_model.module_name,
            "operation_groups": code_model.operation_groups,
            "operation_mixin_group": code_model.mixin_operation_group,
            "mod_to_api_version": self.mod_to_api_version,
            "default_api_version": self.mod_to_api_version[self.default_api_version],
            "client_description": code_model.service_client.description,
            "last_rt_list": code_model.last_rt_list,
            "default_models": sorted(
                {self.default_api_version} | {versions for _, versions in code_model.last_rt_list.items()}
            ),
            "config": code_model.config,
            "global_parameters": code_model.global_parameters,
            "sync_imports": str(FileImportSerializer(sync_imports, is_python_3_file=False)),
            "async_imports": str(FileImportSerializer(async_imports, is_python_3_file=True)),
            "base_url": self.default_version_metadata["client"]["base_url"],
            "custom_base_url_to_api_version": code_model.service_client.custom_base_url_to_api_version,
            "azure_arm": code_model.azure_arm,
            "has_lro_operations": code_model.service_client.has_lro_operations
        }

        multiapi_serializer = MultiAPISerializer(
            conf=conf,
            async_mode=False,
            autorestapi=self._autorestapi,
            service_client_filename=self.default_version_metadata["client"]["filename"]
        )
        multiapi_serializer.serialize()

        if not self.no_async:
            async_multiapi_serializer = MultiAPISerializer(
                conf=conf,
                async_mode=True,
                autorestapi=self._autorestapi,
                service_client_filename=self.default_version_metadata["client"]["filename"]
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
