# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List
from pathlib import Path
import os

from .. import Plugin

class CustomizePlugin(Plugin):

    def __init__(self, autorestapi):
        super().__init__(autorestapi)
        output_folder_uri = self._autorestapi.get_value("outputFolderUri")
        if output_folder_uri.startswith("file:"):
            output_folder_uri = output_folder_uri[5:]
        if os.name == 'nt' and output_folder_uri.startswith("///"):
            output_folder_uri = output_folder_uri[3:]
        self.output_folder = Path(output_folder_uri)

        self.namespace_path = (
            Path(".")
            if self._autorestapi.get_value("no_namespace_folders")
            else Path(*(self._autorestapi.get_value("namespace").split(".")))
        )

    def process(self) -> bool:
        folders = [f for f in self.output_folder.glob('**/*') if f.is_dir()]

        # if there's a models folder, fix imports for customized models
        try:
            models_folder = next(f for f in folders if f.stem == "models")
            self.fix_imports_in_init(models_folder)
        except StopIteration:
            pass

    def fix_imports_in_init(self, folder_path: Path) -> None:
        customized_objects = self.get_customized_objects(folder_path)

    def get_customized_objects(self, folder_path: Path) -> List[str]:
        """Get the list of customized models from the patch file"""
        a = "b"
