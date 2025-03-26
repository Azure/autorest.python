None

from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import ClientNamespaceFirstClientConfiguration

if TYPE_CHECKING:
    from azure.core import AsyncPipelineClient

    from .._serialization import Deserializer, Serializer


class ClientNamespaceFirstClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: ClientNamespaceFirstClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
