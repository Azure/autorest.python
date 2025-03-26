# coding=utf-8
from corehttp.runtime import AsyncPipelineClient

from ....._serialization import Deserializer, Serializer
from .....aio._configuration import RoutesClientConfiguration
from ...explode.aio.operations._operations import QueryParametersQueryExpansionExplodeOperations
from ...standard.aio.operations._operations import QueryParametersQueryExpansionStandardOperations


class QueryParametersQueryExpansionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~routes.aio.RoutesClient`'s
        :attr:`query_expansion` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: RoutesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

        self.standard = QueryParametersQueryExpansionStandardOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.explode = QueryParametersQueryExpansionExplodeOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
