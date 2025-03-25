from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import ApiKeyClientConfiguration

if TYPE_CHECKING:
    from corehttp.runtime import PipelineClient

    from ._serialization import Deserializer, Serializer


class ApiKeyClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: ApiKeyClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
