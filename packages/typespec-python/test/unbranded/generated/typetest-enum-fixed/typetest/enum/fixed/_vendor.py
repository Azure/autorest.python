from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import FixedClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from corehttp.runtime import PipelineClient

    from ._serialization import Deserializer, Serializer


class FixedClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: FixedClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
