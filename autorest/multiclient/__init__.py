# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from pathlib import Path
from jinja2 import Environment, PackageLoader
from .. import Plugin

_LOGGER = logging.getLogger(__name__)


class MultiClientPlugin(Plugin):
    def process(self) -> bool:
        package_version: str = (
            self._autorestapi.get_value("package-version") or "1.0.0b1"
        )
        _LOGGER.info("Generating files for multi client")

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
            Path("_version.py"), template.render(package_version=package_version)
        )

        # py.typed
        self._autorestapi.write_file(Path("py.typed"), "# Marker file for PEP 561.")

        _LOGGER.info("Generating Done for multi client!")
        return True
