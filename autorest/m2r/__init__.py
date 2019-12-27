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

from .. import Plugin


_LOGGER = logging.getLogger(__name__)


class M2R(Plugin):
    """A plugin to convert any description and summary from MD to RST.
    """

    def process(self) -> bool:
        # List the input file, should be only one
        inputs = self._autorestapi.list_inputs()
        _LOGGER.debug("Possible Inputs: %s", inputs)
        if "code-model-v4-no-tags.yaml" not in inputs:
            raise ValueError("code-model-v4-no-tags.yaml must be a possible input")

        file_content = self._autorestapi.read_file("code-model-v4-no-tags.yaml")
        yaml_code_model = yaml.safe_load(file_content)

        self.convert_docstring(yaml_code_model)

        yaml_string = yaml.safe_dump(yaml_code_model)

        self._autorestapi.write_file("code-model-v4-no-tags.yaml", yaml_string)
        return True

    def convert_docstring(self, yaml_code_model) -> None:
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
        return m2r.convert(string_to_convert).strip()
