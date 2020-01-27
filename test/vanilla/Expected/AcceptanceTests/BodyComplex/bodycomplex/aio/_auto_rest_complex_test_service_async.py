# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import AutoRestComplexTestServiceConfiguration
from .operations_async import BasicOperations
from .operations_async import PrimitiveOperations
from .operations_async import ArrayOperations
from .operations_async import DictionaryOperations
from .operations_async import InheritanceOperations
from .operations_async import PolymorphismOperations
from .operations_async import PolymorphicrecursiveOperations
from .operations_async import ReadonlypropertyOperations
from .operations_async import FlattencomplexOperations
from .. import models


class AutoRestComplexTestService(object):
    """Test Infrastructure for AutoRest

    :ivar basic: BasicOperations operations
    :vartype basic: bodycomplex.aio.operations_async.BasicOperations
    :ivar primitive: PrimitiveOperations operations
    :vartype primitive: bodycomplex.aio.operations_async.PrimitiveOperations
    :ivar array: ArrayOperations operations
    :vartype array: bodycomplex.aio.operations_async.ArrayOperations
    :ivar dictionary: DictionaryOperations operations
    :vartype dictionary: bodycomplex.aio.operations_async.DictionaryOperations
    :ivar inheritance: InheritanceOperations operations
    :vartype inheritance: bodycomplex.aio.operations_async.InheritanceOperations
    :ivar polymorphism: PolymorphismOperations operations
    :vartype polymorphism: bodycomplex.aio.operations_async.PolymorphismOperations
    :ivar polymorphicrecursive: PolymorphicrecursiveOperations operations
    :vartype polymorphicrecursive: bodycomplex.aio.operations_async.PolymorphicrecursiveOperations
    :ivar readonlyproperty: ReadonlypropertyOperations operations
    :vartype readonlyproperty: bodycomplex.aio.operations_async.ReadonlypropertyOperations
    :ivar flattencomplex: FlattencomplexOperations operations
    :vartype flattencomplex: bodycomplex.aio.operations_async.FlattencomplexOperations
    :param str base_url: Service URL
    """

    def __init__(self[], base_url: Optional[str] = None, **kwargs) -> None:
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = AutoRestComplexTestServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.basic = BasicOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.primitive = PrimitiveOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.array = ArrayOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.dictionary = DictionaryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.inheritance = InheritanceOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.polymorphism = PolymorphismOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.polymorphicrecursive = PolymorphicrecursiveOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.readonlyproperty = ReadonlypropertyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.flattencomplex = FlattencomplexOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "AutoRestComplexTestService":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
