# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
from msrest.serialization import Model

class Animal(Model):
    """Animal.

    :param ani_type:
	:type ani_type: str
    """

    _attribute_map = {
        'ani_type': {'key': 'aniType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Animal, self).__init__(**kwargs)
        self.ani_type = kwargs.get('ani_type', None)


class BaseError(Model):
    """BaseError.

    :param some_base_prop:
	:type some_base_prop: str
    """

    _attribute_map = {
        'some_base_prop': {'key': 'someBaseProp', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BaseError, self).__init__(**kwargs)
        self.some_base_prop = kwargs.get('some_base_prop', None)


class NotFoundErrorBase(BaseError):
    """NotFoundErrorBase.

	You probably want to use the sub-classes and not this class directly. Known sub-classes are: AnimalNotFound, LinkNotFound.


	All required parameters must be populated in order to send to Azure.

    :param some_base_prop:
	:type some_base_prop: str
    :param reason:
	:type reason: str
    :param what_not_found: Required. Constant filled by server. 
	:type what_not_found: str
    """

    _validation = {
        'what_not_found': {'required': True},
    }

    _attribute_map = {
        'some_base_prop': {'key': 'someBaseProp', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'what_not_found': {'key': 'whatNotFound', 'type': 'str'},
    }

    _subtype_map = {
        'what_not_found': {'AnimalNotFound': 'AnimalNotFound', 'InvalidResourceLink': 'LinkNotFound'}
    }

    def __init__(self, **kwargs):
        super(NotFoundErrorBase, self).__init__(**kwargs)
        self.reason = kwargs.get('reason', None)
        self.what_not_found = 'NotFoundErrorBase'


class NotFoundErrorBaseException(HttpResponseError):
    """Server responded with exception of type: 'NotFoundErrorBase'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, response, deserialize, *args):

        model_name = 'NotFoundErrorBase'
        self.error = deserialize(model_name, response)
        if self.error is None:
            self.error = deserialize.dependencies[model_name]()
        super(NotFoundErrorBaseException, self).__init__(response=response)


class AnimalNotFound(NotFoundErrorBase):
    """AnimalNotFound.

	All required parameters must be populated in order to send to Azure.

    :param some_base_prop:
	:type some_base_prop: str
    :param reason:
	:type reason: str
    :param what_not_found: Required. Constant filled by server. 
	:type what_not_found: str
    :param name:
	:type name: str
    """

    _validation = {
        'what_not_found': {'required': True},
    }

    _attribute_map = {
        'some_base_prop': {'key': 'someBaseProp', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'what_not_found': {'key': 'whatNotFound', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AnimalNotFound, self).__init__(**kwargs)
        self.what_not_found = 'AnimalNotFound'
        self.name = kwargs.get('name', None)


class AnimalNotFoundException(HttpResponseError):
    """Server responded with exception of type: 'AnimalNotFound'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, response, deserialize, *args):

        model_name = 'AnimalNotFound'
        self.error = deserialize(model_name, response)
        if self.error is None:
            self.error = deserialize.dependencies[model_name]()
        super(AnimalNotFoundException, self).__init__(response=response)


class LinkNotFound(NotFoundErrorBase):
    """LinkNotFound.

	All required parameters must be populated in order to send to Azure.

    :param some_base_prop:
	:type some_base_prop: str
    :param reason:
	:type reason: str
    :param what_not_found: Required. Constant filled by server. 
	:type what_not_found: str
    :param what_sub_address:
	:type what_sub_address: str
    """

    _validation = {
        'what_not_found': {'required': True},
    }

    _attribute_map = {
        'some_base_prop': {'key': 'someBaseProp', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'what_not_found': {'key': 'whatNotFound', 'type': 'str'},
        'what_sub_address': {'key': 'whatSubAddress', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LinkNotFound, self).__init__(**kwargs)
        self.what_not_found = 'InvalidResourceLink'
        self.what_sub_address = kwargs.get('what_sub_address', None)


class LinkNotFoundException(HttpResponseError):
    """Server responded with exception of type: 'LinkNotFound'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, response, deserialize, *args):

        model_name = 'LinkNotFound'
        self.error = deserialize(model_name, response)
        if self.error is None:
            self.error = deserialize.dependencies[model_name]()
        super(LinkNotFoundException, self).__init__(response=response)


class Pet(Animal):
    """Pet.

	Variables are only populated by the server, and will be ignored when sending a request.

    :param ani_type:
	:type ani_type: str
    :ivar name: Gets the Pet by id.
	:vartype name: str
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'ani_type': {'key': 'aniType', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Pet, self).__init__(**kwargs)
        self.name = None


class PetAction(Model):
    """PetAction.

    :param action_response: action feedback.
	:type action_response: str
    """

    _attribute_map = {
        'action_response': {'key': 'actionResponse', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PetAction, self).__init__(**kwargs)
        self.action_response = kwargs.get('action_response', None)


class PetActionError(Model):
    """PetActionError.

	You probably want to use the sub-classes and not this class directly. Known sub-classes are: PetSadError.


	All required parameters must be populated in order to send to Azure.

    :param error_type: Required. Constant filled by server. 
	:type error_type: str
    :param error_message: the error message.
	:type error_message: str
    """

    _validation = {
        'error_type': {'required': True},
    }

    _attribute_map = {
        'error_type': {'key': 'errorType', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    _subtype_map = {
        'error_type': {'PetSadError': 'PetSadError'}
    }

    def __init__(self, **kwargs):
        super(PetActionError, self).__init__(**kwargs)
        self.error_type = None
        self.error_message = kwargs.get('error_message', None)


class PetActionErrorException(HttpResponseError):
    """Server responded with exception of type: 'PetActionError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, response, deserialize, *args):

        model_name = 'PetActionError'
        self.error = deserialize(model_name, response)
        if self.error is None:
            self.error = deserialize.dependencies[model_name]()
        super(PetActionErrorException, self).__init__(response=response)


class PetSadError(PetActionError):
    """PetSadError.

	You probably want to use the sub-classes and not this class directly. Known sub-classes are: PetHungryOrThirstyError.


	All required parameters must be populated in order to send to Azure.

    :param error_type: Required. Constant filled by server. 
	:type error_type: str
    :param error_message: the error message.
	:type error_message: str
    :param reason: why is the pet sad.
	:type reason: str
    """

    _validation = {
        'error_type': {'required': True},
    }

    _attribute_map = {
        'error_type': {'key': 'errorType', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    _subtype_map = {
        'error_type': {'PetHungryOrThirstyError': 'PetHungryOrThirstyError'}
    }

    def __init__(self, **kwargs):
        super(PetSadError, self).__init__(**kwargs)
        self.error_type = 'PetSadError'
        self.reason = kwargs.get('reason', None)


class PetSadErrorException(HttpResponseError):
    """Server responded with exception of type: 'PetSadError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, response, deserialize, *args):

        model_name = 'PetSadError'
        self.error = deserialize(model_name, response)
        if self.error is None:
            self.error = deserialize.dependencies[model_name]()
        super(PetSadErrorException, self).__init__(response=response)


class PetHungryOrThirstyError(PetSadError):
    """PetHungryOrThirstyError.

	All required parameters must be populated in order to send to Azure.

    :param error_type: Required. Constant filled by server. 
	:type error_type: str
    :param error_message: the error message.
	:type error_message: str
    :param reason: why is the pet sad.
	:type reason: str
    :param hungry_or_thirsty: is the pet hungry or thirsty or both.
	:type hungry_or_thirsty: str
    """

    _validation = {
        'error_type': {'required': True},
    }

    _attribute_map = {
        'error_type': {'key': 'errorType', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'hungry_or_thirsty': {'key': 'hungryOrThirsty', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PetHungryOrThirstyError, self).__init__(**kwargs)
        self.error_type = 'PetHungryOrThirstyError'
        self.hungry_or_thirsty = kwargs.get('hungry_or_thirsty', None)


class PetHungryOrThirstyErrorException(HttpResponseError):
    """Server responded with exception of type: 'PetHungryOrThirstyError'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, response, deserialize, *args):

        model_name = 'PetHungryOrThirstyError'
        self.error = deserialize(model_name, response)
        if self.error is None:
            self.error = deserialize.dependencies[model_name]()
        super(PetHungryOrThirstyErrorException, self).__init__(response=response)


