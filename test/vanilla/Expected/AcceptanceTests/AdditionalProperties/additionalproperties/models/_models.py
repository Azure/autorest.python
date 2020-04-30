# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class PetAPTrue(msrest.serialization.Model):
    """PetAPTrue.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param name:
    :type name: str
    :param id: Required.
    :type id: int
    :ivar status:
    :vartype status: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'status': {'key': 'status', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PetAPTrue, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.name = kwargs.get('name', None)
        self.id = kwargs['id']
        self.status = None


class CatAPTrue(PetAPTrue):
    """CatAPTrue.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param name:
    :type name: str
    :param id: Required.
    :type id: int
    :ivar status:
    :vartype status: bool
    :param friendly:
    :type friendly: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'status': {'key': 'status', 'type': 'bool'},
        'friendly': {'key': 'friendly', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CatAPTrue, self).__init__(**kwargs)
        self.friendly = kwargs.get('friendly', None)


class Error(msrest.serialization.Model):
    """Error.

    :param message:
    :type message: str
    :param status:
    :type status: int
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'status': {'key': 'status', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.message = kwargs.get('message', None)
        self.status = kwargs.get('status', None)


class PetAPInProperties(msrest.serialization.Model):
    """PetAPInProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name:
    :type name: str
    :param additional_properties: Dictionary of :code:`<number>`.
    :type additional_properties: dict[str, float]
    :param id: Required.
    :type id: int
    :ivar status:
    :vartype status: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'additional_properties': {'key': 'additionalProperties', 'type': '{float}'},
        'id': {'key': 'id', 'type': 'int'},
        'status': {'key': 'status', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PetAPInProperties, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.id = kwargs['id']
        self.status = None


class PetAPInPropertiesWithAPString(msrest.serialization.Model):
    """PetAPInPropertiesWithAPString.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, str]
    :param name:
    :type name: str
    :param odata_location: Required.
    :type odata_location: str
    :param additional_properties1: Dictionary of :code:`<number>`.
    :type additional_properties1: dict[str, float]
    :param id: Required.
    :type id: int
    :ivar status:
    :vartype status: bool
    """

    _validation = {
        'odata_location': {'required': True},
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'odata_location': {'key': '@odata\\.location', 'type': 'str'},
        'additional_properties1': {'key': 'additionalProperties', 'type': '{float}'},
        'id': {'key': 'id', 'type': 'int'},
        'status': {'key': 'status', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PetAPInPropertiesWithAPString, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.name = kwargs.get('name', None)
        self.odata_location = kwargs['odata_location']
        self.additional_properties1 = kwargs.get('additional_properties1', None)
        self.id = kwargs['id']
        self.status = None


class PetAPObject(msrest.serialization.Model):
    """PetAPObject.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, object]
    :param name:
    :type name: str
    :param id: Required.
    :type id: int
    :ivar status:
    :vartype status: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'status': {'key': 'status', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PetAPObject, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.name = kwargs.get('name', None)
        self.id = kwargs['id']
        self.status = None


class PetAPString(msrest.serialization.Model):
    """PetAPString.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, str]
    :param name:
    :type name: str
    :param id: Required.
    :type id: int
    :ivar status:
    :vartype status: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'status': {'key': 'status', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PetAPString, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.name = kwargs.get('name', None)
        self.id = kwargs['id']
        self.status = None
