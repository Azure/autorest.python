from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import NotDiscriminatedClientConfiguration

if TYPE_CHECKING:
    from corehttp.runtime import PipelineClient

    from ._serialization import Deserializer, Serializer


class NotDiscriminatedClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: NotDiscriminatedClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
