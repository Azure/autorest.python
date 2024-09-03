# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import MediaTypesClientConfiguration

if TYPE_CHECKING:
    from azure.core import PipelineClient

    from ._serialization import Deserializer, Serializer


class MediaTypesClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: MediaTypesClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


def raise_if_not_implemented(cls, abstract_methods):
    not_implemented = [f for f in abstract_methods if not callable(getattr(cls, f, None))]
    if not_implemented:
        raise NotImplementedError(
            "The following methods on operation group '{}' are not implemented: '{}'."
            " Please refer to https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize.".format(
                cls.__name__, "', '".join(not_implemented)
            )
        )
