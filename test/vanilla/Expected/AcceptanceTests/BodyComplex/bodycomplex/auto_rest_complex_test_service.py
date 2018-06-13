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
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.exceptions import HttpOperationError
from .operations.basic_operations import BasicOperations
from .operations.primitive_operations import PrimitiveOperations
from .operations.array_operations import ArrayOperations
from .operations.dictionary_operations import DictionaryOperations
from .operations.inheritance_operations import InheritanceOperations
from .operations.polymorphism_operations import PolymorphismOperations
from .operations.polymorphicrecursive_operations import PolymorphicrecursiveOperations
from .operations.readonlyproperty_operations import ReadonlypropertyOperations
from .operations.flattencomplex_operations import FlattencomplexOperations
from . import models


class AutoRestComplexTestServiceConfiguration(Configuration):
    """Configuration for AutoRestComplexTestService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        if not base_url:
            base_url = 'http://localhost:3000'

        super(AutoRestComplexTestServiceConfiguration, self).__init__(base_url)

        self.add_user_agent('autorestcomplextestservice/{}'.format(VERSION))


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
