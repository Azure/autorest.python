from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import ProjectedNameClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from corehttp.runtime import PipelineClient

    from ._serialization import Deserializer, Serializer


class ProjectedNameClientMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "PipelineClient"
    _config: ProjectedNameClientConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
