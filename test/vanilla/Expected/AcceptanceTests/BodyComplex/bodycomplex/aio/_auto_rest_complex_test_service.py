# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import AsyncPipelineClient
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest
from msrest import Deserializer, Serializer

from .. import models
from ._configuration import AutoRestComplexTestServiceConfiguration
from .operations import (
    ArrayOperations,
    BasicOperations,
    DictionaryOperations,
    FlattencomplexOperations,
    InheritanceOperations,
    PolymorphicrecursiveOperations,
    PolymorphismOperations,
    PrimitiveOperations,
    ReadonlypropertyOperations,
)


class AutoRestComplexTestService(object):
    """Test Infrastructure for AutoRest.

    :ivar basic: BasicOperations operations
    :vartype basic: bodycomplex.aio.operations.BasicOperations
    :ivar primitive: PrimitiveOperations operations
    :vartype primitive: bodycomplex.aio.operations.PrimitiveOperations
    :ivar array: ArrayOperations operations
    :vartype array: bodycomplex.aio.operations.ArrayOperations
    :ivar dictionary: DictionaryOperations operations
    :vartype dictionary: bodycomplex.aio.operations.DictionaryOperations
    :ivar inheritance: InheritanceOperations operations
    :vartype inheritance: bodycomplex.aio.operations.InheritanceOperations
    :ivar polymorphism: PolymorphismOperations operations
    :vartype polymorphism: bodycomplex.aio.operations.PolymorphismOperations
    :ivar polymorphicrecursive: PolymorphicrecursiveOperations operations
    :vartype polymorphicrecursive: bodycomplex.aio.operations.PolymorphicrecursiveOperations
    :ivar readonlyproperty: ReadonlypropertyOperations operations
    :vartype readonlyproperty: bodycomplex.aio.operations.ReadonlypropertyOperations
    :ivar flattencomplex: FlattencomplexOperations operations
    :vartype flattencomplex: bodycomplex.aio.operations.FlattencomplexOperations
    :param str base_url: Service URL
    """

    def __init__(self, base_url: Optional[str] = None, **kwargs: Any) -> None:
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestComplexTestServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.basic = BasicOperations(self._client, self._config, self._serialize, self._deserialize)
        self.primitive = PrimitiveOperations(self._client, self._config, self._serialize, self._deserialize)
        self.array = ArrayOperations(self._client, self._config, self._serialize, self._deserialize)
        self.dictionary = DictionaryOperations(self._client, self._config, self._serialize, self._deserialize)
        self.inheritance = InheritanceOperations(self._client, self._config, self._serialize, self._deserialize)
        self.polymorphism = PolymorphismOperations(self._client, self._config, self._serialize, self._deserialize)
        self.polymorphicrecursive = PolymorphicrecursiveOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.readonlyproperty = ReadonlypropertyOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.flattencomplex = FlattencomplexOperations(self._client, self._config, self._serialize, self._deserialize)

    async def invoke(self, request: HttpRequest, **kwargs: Any) -> PipelineResponse:
        return await self._client._pipeline.run(request, stream=False, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestComplexTestService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
