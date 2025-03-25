from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import RemovedClientConfiguration

if TYPE_CHECKING:
    from azure.core import AsyncPipelineClient

    from .._serialization import Deserializer, Serializer


class RemovedClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: RemovedClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
