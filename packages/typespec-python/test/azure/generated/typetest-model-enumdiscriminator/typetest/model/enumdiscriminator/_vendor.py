from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import EnumDiscriminatorClientConfiguration

if TYPE_CHECKING:
    from azure.core import PipelineClient

    from ._serialization import Deserializer, Serializer


class EnumDiscriminatorClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: EnumDiscriminatorClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
