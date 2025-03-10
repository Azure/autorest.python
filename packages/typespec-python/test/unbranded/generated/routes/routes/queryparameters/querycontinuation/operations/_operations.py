# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from corehttp.runtime import PipelineClient

from ...._configuration import RoutesClientConfiguration
from ...._serialization import Deserializer, Serializer
from ..explode.operations._operations import QueryParametersQueryContinuationExplodeOperations
from ..standard.operations._operations import QueryParametersQueryContinuationStandardOperations


class QueryParametersQueryContinuationOperations:  # pylint: disable=name-too-long
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~routes.RoutesClient`'s
        :attr:`query_continuation` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client: PipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: RoutesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

        self.standard = QueryParametersQueryContinuationStandardOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.explode = QueryParametersQueryContinuationExplodeOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
