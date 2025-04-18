from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import AddedClientConfiguration

if TYPE_CHECKING:
    from corehttp.runtime import AsyncPipelineClient

    from .._serialization import Deserializer, Serializer


class AddedClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: AddedClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
