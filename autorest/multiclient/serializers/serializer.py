# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from pathlib import Path
from jinja2 import Environment, PackageLoader
from ..models import CodeModel
from ...jsonrpc import AutorestAPI


class MultiClientSerializer:
    def __init__(self, autorestapi: AutorestAPI, code_model: CodeModel):
        self._autorestapi = autorestapi
        self.code_model = code_model

    def serialize(self):
        env = Environment(
            loader=PackageLoader("autorest.multiclient", "templates"),
            keep_trailing_newline=True,
            line_statement_prefix="##",
            line_comment_prefix="###",
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # _version.py
        template = env.get_template("version.py.jinja2")
        self._autorestapi.write_file(
            Path("_version.py"), template.render(code_model=self.code_model)
        )

        # py.typed
        self._autorestapi.write_file(Path("py.typed"), "# Marker file for PEP 561.")
