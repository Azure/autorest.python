# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""An autorest MD to RST plugin.
"""
import logging

import yaml
import m2r

from .. import YamlUpdatePlugin


_LOGGER = logging.getLogger(__name__)


class AutorestRender(m2r.RestRenderer):
    """Redefine the concept of inline HTML in the renderer, we don't want to define a new format
    in the description/summary.
    """
    def inline_html(self, html):
        """Do not render inline HTML with a role definition."""
        return f":code:`{html}`"


class M2R(YamlUpdatePlugin):
    """A plugin to convert any description and summary from MD to RST.
    """
    def update_yaml(self, yaml_code_model) -> None:
        """Convert in place the YAML str.
        """
        self._convert_docstring_no_cycles(yaml_code_model, set())

    def _convert_docstring_no_cycles(self, yaml_code_model, node_list) -> None:
        """Walk the YAML tree to convert MD to RST.
        """
        if id(yaml_code_model) in node_list:
            return
        node_list.add(id(yaml_code_model))

        if isinstance(yaml_code_model, list):
            for elt in yaml_code_model:
                self._convert_docstring_no_cycles(elt, node_list)
        elif isinstance(yaml_code_model, dict):
            for key, value in yaml_code_model.items():
                if key in ["description", "summary"]:
                    yaml_code_model[key] = self.convert_to_rst(value)
                    continue
                self._convert_docstring_no_cycles(value, node_list)

    @staticmethod
    def convert_to_rst(string_to_convert: str) -> str:
        """Convert that string from MD to RST.
        """
        return m2r.convert(string_to_convert, renderer=AutorestRender()).strip()
