# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from __future__ import annotations
from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import ObjectTypeClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from msrest import Deserializer, Serializer

    from azure.core import AsyncPipelineClient


class MixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: AsyncPipelineClient
    _config: ObjectTypeClientConfiguration
    _serialize: Serializer
    _deserialize: Deserializer
