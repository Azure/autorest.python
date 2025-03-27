from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import NotDefinedClientConfiguration

if TYPE_CHECKING:
    from corehttp.runtime import AsyncPipelineClient

    from .._serialization import Deserializer, Serializer


class NotDefinedClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: NotDefinedClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
