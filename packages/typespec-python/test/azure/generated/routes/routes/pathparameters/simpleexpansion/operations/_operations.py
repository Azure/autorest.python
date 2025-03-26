# coding=utf-8
None
from azure.core import PipelineClient

from ...._configuration import RoutesClientConfiguration
from ...._serialization import Deserializer, Serializer
from ..explode.operations._operations import PathParametersSimpleExpansionExplodeOperations
from ..standard.operations._operations import PathParametersSimpleExpansionStandardOperations


class PathParametersSimpleExpansionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~routes.RoutesClient`'s
        :attr:`simple_expansion` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: RoutesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

        self.standard = PathParametersSimpleExpansionStandardOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.explode = PathParametersSimpleExpansionExplodeOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
