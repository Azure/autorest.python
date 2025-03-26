None

from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import MultipleClientConfiguration

if TYPE_CHECKING:
    from azure.core import PipelineClient

    from ._serialization import Deserializer, Serializer


class MultipleClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: MultipleClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
