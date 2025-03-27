from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import FlattenPropertyClientConfiguration

if TYPE_CHECKING:
    from azure.core import AsyncPipelineClient

    from .._serialization import Deserializer, Serializer


class FlattenPropertyClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: FlattenPropertyClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
