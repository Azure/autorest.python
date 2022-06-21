# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from pathlib import Path
import os
import black

from .. import Plugin

_LOGGER = logging.getLogger(__name__)

_BLACK_MODE = black.Mode()
_BLACK_MODE.line_length = 120


class BlackScriptPlugin(Plugin):
    def __init__(self, autorestapi):
        super().__init__(autorestapi)
        output_folder_uri = self._autorestapi.get_value("outputFolderUri")
        if output_folder_uri.startswith("file:"):
            output_folder_uri = output_folder_uri[5:]
        if os.name == "nt" and output_folder_uri.startswith("///"):
            output_folder_uri = output_folder_uri[3:]
        self.output_folder = Path(output_folder_uri)

    def proc_files(self, folder: Path, pattern: str):
        list(
            map(
                self.format_file,
                [f for f in folder.glob(pattern) if f.is_file()],
            )
        )

    def process(self) -> bool:
        # apply format_file on every file in the output folder
        self.proc_files(folder=self.output_folder, pattern="**/*")

        # format files that may be outside output folder(setup.py, etc)
        if self._autorestapi.get_boolean_value("no-namespace-folders", False):
            if self._autorestapi.get_boolean_value("generate-sample", False):
                namespace = self._autorestapi.get_value("namespace") or ""
                depth = namespace.count(".") + 1
                self.proc_files(
                    folder=self.output_folder / Path("../" * depth),
                    pattern="generated_samples/**/*",
                )
        return True

    def format_file(self, full_path) -> None:
        file = full_path.relative_to(self.output_folder)
        file_content = self._autorestapi.read_file(file)
        if not file.suffix == ".py":
            self._autorestapi.write_file(file, file_content)
            return
        try:
            file_content = black.format_file_contents(
                file_content, fast=True, mode=_BLACK_MODE
            )
        except black.NothingChanged:
            pass
        self._autorestapi.write_file(file, file_content)
