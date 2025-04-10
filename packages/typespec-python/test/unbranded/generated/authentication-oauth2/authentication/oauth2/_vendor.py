from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import OAuth2ClientConfiguration

if TYPE_CHECKING:
    from corehttp.runtime import PipelineClient

    from ._serialization import Deserializer, Serializer


class OAuth2ClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: OAuth2ClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
