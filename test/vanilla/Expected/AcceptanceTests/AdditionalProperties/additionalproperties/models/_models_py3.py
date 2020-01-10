# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict

from azure.core.exceptions import HttpResponseError
from msrest.serialization import Model

class PetAPTrue(Model):
    """PetAPTrue.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this collection.
	:type additional_properties: dict[str, object]
    :param id: Required. 
	:type id: int
    :param name:
	:type name: str
    :ivar status:
	:vartype status: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
    }

    def __init__(self, *, id: int, additional_properties: Dict[str, object]=None, name: str=None, **kwargs) -> None:
        super(PetAPTrue, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status = None

class CatAPTrue(PetAPTrue):
    """CatAPTrue.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this collection.
	:type additional_properties: dict[str, object]
    :param id: Required. 
	:type id: int
    :param name:
	:type name: str
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
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
        'friendly': {'key': 'friendly', 'type': 'bool'},
    }

    def __init__(self, *, id: int, additional_properties: Dict[str, object]=None, name: str=None, friendly: bool=None, **kwargs) -> None:
        super(CatAPTrue, self).__init__(additional_properties=additional_properties, id=id, name=name, **kwargs)
        self.friendly = friendly

class ErrorException(HttpResponseError):
    """Server responded with exception of type: 'Error'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(ErrorException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'Error'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class Error(Model):
    """Error.

    :param status:
	:type status: int
    :param message:
	:type message: str
    """
    _EXCEPTION_TYPE = ErrorException

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, status: int=None, message: str=None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message

class PetAPInProperties(Model):
    """PetAPInProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. 
	:type id: int
    :param name:
	:type name: str
    :ivar status:
	:vartype status: bool
    :param additional_properties: Dictionary of <components·schemas·petapinproperties·properties·additionalproperties·additionalproperties>.
	:type additional_properties: dict[str, float]
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
        'additional_properties': {'key': 'additionalProperties', 'type': '{float}'},
    }

    def __init__(self, *, id: int, name: str=None, additional_properties: Dict[str, float]=None, **kwargs) -> None:
        super(PetAPInProperties, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.status = None
        self.additional_properties = additional_properties

class PetAPInPropertiesWithAPString(Model):
    """PetAPInPropertiesWithAPString.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this collection.
	:type additional_properties: dict[str, str]
    :param id: Required. 
	:type id: int
    :param name:
	:type name: str
    :ivar status:
	:vartype status: bool
    :param odatalocation: Required. 
	:type odatalocation: str
    :param additional_properties1: Dictionary of <components·schemas·petapinproperties·properties·additionalproperties·additionalproperties>.
	:type additional_properties1: dict[str, float]
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
        'odatalocation': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
        'odatalocation': {'key': '@odata\\.location', 'type': 'str'},
        'additional_properties1': {'key': 'additionalProperties', 'type': '{float}'},
    }

    def __init__(self, *, id: int, odatalocation: str, additional_properties: Dict[str, str]=None, name: str=None, additional_properties1: Dict[str, float]=None, **kwargs) -> None:
        super(PetAPInPropertiesWithAPString, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status = None
        self.odatalocation = odatalocation
        self.additional_properties1 = additional_properties1

class PetAPObject(Model):
    """PetAPObject.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this collection.
	:type additional_properties: dict[str, object]
    :param id: Required. 
	:type id: int
    :param name:
	:type name: str
    :ivar status:
	:vartype status: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
    }

    def __init__(self, *, id: int, additional_properties: Dict[str, object]=None, name: str=None, **kwargs) -> None:
        super(PetAPObject, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status = None

class PetAPString(Model):
    """PetAPString.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are deserialized to this collection.
	:type additional_properties: dict[str, str]
    :param id: Required. 
	:type id: int
    :param name:
	:type name: str
    :ivar status:
	:vartype status: bool
    """

    _validation = {
        'id': {'required': True},
        'status': {'readonly': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'bool'},
    }

    def __init__(self, *, id: int, additional_properties: Dict[str, str]=None, name: str=None, **kwargs) -> None:
        super(PetAPString, self).__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status = None

