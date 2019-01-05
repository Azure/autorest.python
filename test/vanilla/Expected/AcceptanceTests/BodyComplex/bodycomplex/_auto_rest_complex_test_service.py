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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import AutoRestComplexTestServiceConfiguration
from msrest.exceptions import HttpOperationError
from .operations import BasicOperations
from .operations import PrimitiveOperations
from .operations import ArrayOperations
from .operations import DictionaryOperations
from .operations import InheritanceOperations
from .operations import PolymorphismOperations
from .operations import PolymorphicrecursiveOperations
from .operations import ReadonlypropertyOperations
from .operations import FlattencomplexOperations
from . import models


class AutoRestComplexTestService(SDKClient):
    """Test Infrastructure for AutoRest

    :ivar config: Configuration for client.
    :vartype config: AutoRestComplexTestServiceConfiguration

    :ivar basic: Basic operations
    :vartype basic: bodycomplex.operations.BasicOperations
    :ivar primitive: Primitive operations
    :vartype primitive: bodycomplex.operations.PrimitiveOperations
    :ivar array: Array operations
    :vartype array: bodycomplex.operations.ArrayOperations
    :ivar dictionary: Dictionary operations
    :vartype dictionary: bodycomplex.operations.DictionaryOperations
    :ivar inheritance: Inheritance operations
    :vartype inheritance: bodycomplex.operations.InheritanceOperations
    :ivar polymorphism: Polymorphism operations
    :vartype polymorphism: bodycomplex.operations.PolymorphismOperations
    :ivar polymorphicrecursive: Polymorphicrecursive operations
    :vartype polymorphicrecursive: bodycomplex.operations.PolymorphicrecursiveOperations
    :ivar readonlyproperty: Readonlyproperty operations
    :vartype readonlyproperty: bodycomplex.operations.ReadonlypropertyOperations
    :ivar flattencomplex: Flattencomplex operations
    :vartype flattencomplex: bodycomplex.operations.FlattencomplexOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = AutoRestComplexTestServiceConfiguration(base_url)
        super(AutoRestComplexTestService, self).__init__(None, self.config)

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
