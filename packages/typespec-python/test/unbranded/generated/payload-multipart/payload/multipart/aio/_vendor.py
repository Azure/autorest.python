# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import MultiPartClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from corehttp.runtime import AsyncPipelineClient

    from .._serialization import Deserializer, Serializer


class MultiPartClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: MultiPartClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"