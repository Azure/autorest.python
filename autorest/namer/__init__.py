# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""The namer autorest plugin.
"""
import logging
from typing import Dict, Any

from .. import YamlUpdatePlugin
from .name_converter import NameConverter


_LOGGER = logging.getLogger(__name__)


class Namer(YamlUpdatePlugin):
    """Add Python naming information."""

    def update_yaml(self, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert in place the YAML str."""
        return yaml_data
        # NameConverter.convert_yaml_names(yaml_data)
        # return yaml_data
