from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import SingleDiscriminatorClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from corehttp.runtime import AsyncPipelineClient

    from .._serialization import Deserializer, Serializer


class SingleDiscriminatorClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: SingleDiscriminatorClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
