# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List
import importlib.util
import sys
from pathlib import Path
import os

from .. import Plugin

class PostProcessPlugin(Plugin):

    def __init__(self, autorestapi):
        super().__init__(autorestapi)
        output_folder_uri = self._autorestapi.get_value("outputFolderUri")
        if output_folder_uri.startswith("file:"):
            output_folder_uri = output_folder_uri[5:]
        if os.name == 'nt' and output_folder_uri.startswith("///"):
            output_folder_uri = output_folder_uri[3:]
        self.output_folder = Path(output_folder_uri)

    def process(self) -> bool:
        folders = [f for f in self.output_folder.glob('**/*') if f.is_dir()]
        # # if there's a models folder, fix imports for customized models
        # spec = importlib.util.spec_from_file_location("generated", '/Users/isabellacai/Desktop/github_repos/autorest.python/test/dpg/version-tolerant/Expected/AcceptanceTests/DPGTestPostProcessPluginVersionTolerant/dpgtestpostprocesspluginversiontolerant/models/_models_py3.py')
        # my_mod = importlib.util.module_from_spec(spec)
        # spec.loader.exec_module(my_mod)

        # spec = importlib.util.spec_from_file_location("patch", '/Users/isabellacai/Desktop/github_repos/autorest.python/test/dpg/version-tolerant/Expected/AcceptanceTests/DPGTestPostProcessPluginVersionTolerant/dpgtestpostprocesspluginversiontolerant/models/_patch.py')
        # my_mod = importlib.util.module_from_spec(spec)
        # spec.loader.exec_module(my_mod)

        # will always have the root
        self.fix_imports_in_init("_dpg_client", folders[0])
        try:
            aio_folder = next(f for f in folders if f.stem == "aio")
            self.fix_imports_in_init("_dpg_client", aio_folder)
        except StopIteration:
            pass

        try:
            models_folder = next(f for f in folders if f.stem == "models")
            self.fix_imports_in_init("_models_py3", models_folder)
        except StopIteration:
            pass
        operations_folders = [f for f in folders if f.stem in ["operations", "_operations"]]
        for operations_folder in operations_folders:
            self.fix_imports_in_init("_operations", operations_folder)
        return True

    def fix_imports_in_init(self, generated_file_name: str, folder_path: Path) -> None:
        file = (folder_path / "__init__.py").relative_to(self.output_folder)
        file_content = self._autorestapi.read_file(file)
        for obj in self.get_customized_objects(folder_path):
            file_content = file_content.replace(f"from .{generated_file_name} import {obj}\n", f"from ._patch import {obj}\n")
        self._autorestapi.write_file(file, file_content)

    def get_customized_objects(self, folder_path: Path) -> List[str]:
        """Get the list of customized models from the patch file"""
        return ["Product", "AddedModel", "DPGClientOperationsMixin", "DPGClient"]
        # imported_folder = self.import_module_from_folder()
        # return imported_folder.__all__

    def import_module_from_folder(self, folder_path: Path):
        pass
