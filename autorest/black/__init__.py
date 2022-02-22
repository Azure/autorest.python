# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from pathlib import Path
import black
import os

from .. import Plugin

_LOGGER = logging.getLogger(__name__)

_BLACK_MODE = black.Mode()
_BLACK_MODE.line_length = 120

class BlackScriptPlugin(Plugin):

    def __init__(self, autorestapi):
        super(BlackScriptPlugin, self).__init__(autorestapi)
        output_folder_uri = self._autorestapi.get_value("outputFolderUri")
        if output_folder_uri.startswith("file:"):
            output_folder_uri = output_folder_uri[5:]
        if os.name == 'nt' and output_folder_uri.startswith("///"):
            output_folder_uri = output_folder_uri[3:]
        self.output_folder = Path(output_folder_uri)

    def process(self) -> bool:
        # apply format_file on every file in the output folder
        list(map(self.format_file, [f for f in self.output_folder.glob('**/*') if f.is_file()]))
        return True

    def format_file(self, full_path) -> None:
        file = full_path.relative_to(self.output_folder)
        file_content = self._autorestapi.read_file(file)
        if not file.suffix == ".py":
            self._autorestapi.write_file(file, file_content)
            return
        try:
            file_content = black.format_file_contents(file_content, fast=True, mode=_BLACK_MODE)
        except black.NothingChanged:
            pass
        self._autorestapi.write_file(file, file_content)
