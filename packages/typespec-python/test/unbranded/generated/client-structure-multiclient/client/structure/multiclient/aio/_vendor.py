from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import ClientAClientConfiguration, ClientBClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from corehttp.runtime import AsyncPipelineClient

    from .._serialization import Deserializer, Serializer


class ClientAClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: ClientAClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"


class ClientBClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: ClientBClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
