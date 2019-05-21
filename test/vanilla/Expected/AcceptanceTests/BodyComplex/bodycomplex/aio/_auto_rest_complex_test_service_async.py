# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.async_client import SDKClientAsync
from msrest import Serializer, Deserializer

from .._configuration import AutoRestComplexTestServiceConfiguration
from msrest.exceptions import HttpOperationError
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


class AutoRestComplexTestService(SDKClientAsync):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestComplexTestServiceConfiguration

    :ivar basic: Basic operations
    :vartype basic: bodycomplex.aio.operations_async.BasicOperations
    :ivar primitive: Primitive operations
    :vartype primitive: bodycomplex.aio.operations_async.PrimitiveOperations
    :ivar array: Array operations
    :vartype array: bodycomplex.aio.operations_async.ArrayOperations
    :ivar dictionary: Dictionary operations
    :vartype dictionary: bodycomplex.aio.operations_async.DictionaryOperations
    :ivar inheritance: Inheritance operations
    :vartype inheritance: bodycomplex.aio.operations_async.InheritanceOperations
    :ivar polymorphism: Polymorphism operations
    :vartype polymorphism: bodycomplex.aio.operations_async.PolymorphismOperations
    :ivar polymorphicrecursive: Polymorphicrecursive operations
    :vartype polymorphicrecursive: bodycomplex.aio.operations_async.PolymorphicrecursiveOperations
    :ivar readonlyproperty: Readonlyproperty operations
    :vartype readonlyproperty: bodycomplex.aio.operations_async.ReadonlypropertyOperations
    :ivar flattencomplex: Flattencomplex operations
    :vartype flattencomplex: bodycomplex.aio.operations_async.FlattencomplexOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = AutoRestComplexTestServiceConfiguration(base_url)
        super(AutoRestComplexTestService, self).__init__(self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-02-29'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.basic = BasicOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.primitive = PrimitiveOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.array = ArrayOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.dictionary = DictionaryOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.inheritance = InheritanceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.polymorphism = PolymorphismOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.polymorphicrecursive = PolymorphicrecursiveOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.readonlyproperty = ReadonlypropertyOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.flattencomplex = FlattencomplexOperations(
            self._client, self.config, self._serialize, self._deserialize)
