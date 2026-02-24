# coding=utf-8
from corehttp.runtime import PipelineClient

from ...._configuration import RoutesClientConfiguration
from ...._utils.serialization import Deserializer, Serializer
from ..explode.operations._operations import RoutesClientPathParametersPathExpansionExplodeOperations
from ..standard.operations._operations import RoutesClientPathParametersPathExpansionStandardOperations


class RoutesClientPathParametersPathExpansionOperations:  # pylint: disable=name-too-long
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~routes.RoutesClient`'s
        :attr:`routes_client_path_parameters_path_expansion` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: RoutesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

        self.routes_client_path_parameters_path_expansion_standard = (
            RoutesClientPathParametersPathExpansionStandardOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
        self.routes_client_path_parameters_path_expansion_explode = (
            RoutesClientPathParametersPathExpansionExplodeOperations(
                self._client, self._config, self._serialize, self._deserialize
            )
        )
