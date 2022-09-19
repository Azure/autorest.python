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
from ..utils import parse_args

logging.getLogger("blib2to3").setLevel(logging.ERROR)

_BLACK_MODE = black.Mode()
_BLACK_MODE.line_length = 120


class BlackScriptPlugin(Plugin):  # pylint: disable=abstract-method
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        output_folder = self.options.get("output_folder", str(self.output_folder))
        if output_folder.startswith("file:"):
            output_folder = output_folder[5:]
        if os.name == "nt" and output_folder.startswith("///"):
            output_folder = output_folder[3:]
        self.output_folder = Path(output_folder)

    def process(self) -> bool:
        # apply format_file on every file in the output folder
        list(map(self.format_file, [Path(f) for f in self.list_file()]))
        return True

    def format_file(self, file: Path) -> None:
        file_content = self.read_file(file)
        if not file.suffix == ".py":
            self.write_file(file, file_content)
            return
        try:
            file_content = black.format_file_contents(
                file_content, fast=True, mode=_BLACK_MODE
            )
        except black.NothingChanged:
            pass
        self.write_file(file, file_content)


if __name__ == "__main__":
    # CADL pipeline will call this
    args = parse_args(need_cadl_file=False)
    BlackScriptPlugin(output_folder=args.output_folder).process()
