from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import RepeatabilityClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from corehttp.runtime import PipelineClient

    from ._serialization import Deserializer, Serializer


class RepeatabilityClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: RepeatabilityClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
