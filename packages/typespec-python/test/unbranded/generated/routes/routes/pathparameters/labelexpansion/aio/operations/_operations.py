# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from corehttp.runtime import AsyncPipelineClient

from ....._serialization import Deserializer, Serializer
from .....aio._configuration import RoutesClientConfiguration
from ...explode.aio.operations._operations import PathParametersLabelExpansionExplodeOperations
from ...standard.aio.operations._operations import PathParametersLabelExpansionStandardOperations


class PathParametersLabelExpansionOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~routes.aio.RoutesClient`'s
        :attr:`label_expansion` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client: AsyncPipelineClient = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config: RoutesClientConfiguration = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize: Serializer = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize: Deserializer = input_args.pop(0) if input_args else kwargs.pop("deserializer")

        self.standard = PathParametersLabelExpansionStandardOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.explode = PathParametersLabelExpansionExplodeOperations(
            self._client, self._config, self._serialize, self._deserialize
        )