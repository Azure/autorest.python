from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import XmsClientRequestIdClientConfiguration

if TYPE_CHECKING:
    from azure.core import AsyncPipelineClient

    from .._serialization import Deserializer, Serializer


class XmsClientRequestIdClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: XmsClientRequestIdClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
