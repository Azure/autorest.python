# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Animal(msrest.serialization.Model):
    """Animal.

    :param ani_type:
    :type ani_type: str
    """

    _attribute_map = {
        'ani_type': {'key': 'aniType', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        ani_type: Optional[str] = None,
        **kwargs
    ):
        super(Animal, self).__init__(**kwargs)
        self.ani_type = ani_type


class BaseError(msrest.serialization.Model):
    """BaseError.

    :param some_base_prop:
    :type some_base_prop: str
    """

    _attribute_map = {
        'some_base_prop': {'key': 'someBaseProp', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        some_base_prop: Optional[str] = None,
        **kwargs
    ):
        super(BaseError, self).__init__(**kwargs)
        self.some_base_prop = some_base_prop


class NotFoundErrorBaseException(HttpResponseError):
    """Server responded with exception of type: 'NotFoundErrorBase'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(NotFoundErrorBaseException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'NotFoundErrorBase'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class NotFoundErrorBase(BaseError):
    """NotFoundErrorBase.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: AnimalNotFound, LinkNotFound.

    All required parameters must be populated in order to send to Azure.

    :param some_base_prop:
    :type some_base_prop: str
    :param reason:
    :type reason: str
    :param what_not_found: Required. Constant filled by server.
    :type what_not_found: str
    """
    _EXCEPTION_TYPE = NotFoundErrorBaseException

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

    def __init__(
        self,
        *,
        some_base_prop: Optional[str] = None,
        reason: Optional[str] = None,
        **kwargs
    ):
        super(NotFoundErrorBase, self).__init__(some_base_prop=some_base_prop, **kwargs)
        self.reason = reason
        self.what_not_found = 'NotFoundErrorBase'


class AnimalNotFoundException(NotFoundErrorBaseException):
    """Server responded with exception of type: 'AnimalNotFound'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(AnimalNotFoundException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'AnimalNotFound'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


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
    _EXCEPTION_TYPE = AnimalNotFoundException

    _validation = {
        'what_not_found': {'required': True},
    }

    _attribute_map = {
        'some_base_prop': {'key': 'someBaseProp', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'what_not_found': {'key': 'whatNotFound', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        some_base_prop: Optional[str] = None,
        reason: Optional[str] = None,
        name: Optional[str] = None,
        **kwargs
    ):
        super(AnimalNotFound, self).__init__(some_base_prop=some_base_prop, reason=reason, **kwargs)
        self.what_not_found = 'AnimalNotFound'
        self.name = name


class LinkNotFoundException(NotFoundErrorBaseException):
    """Server responded with exception of type: 'LinkNotFound'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(LinkNotFoundException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'LinkNotFound'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


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
    _EXCEPTION_TYPE = LinkNotFoundException

    _validation = {
        'what_not_found': {'required': True},
    }

    _attribute_map = {
        'some_base_prop': {'key': 'someBaseProp', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'what_not_found': {'key': 'whatNotFound', 'type': 'str'},
        'what_sub_address': {'key': 'whatSubAddress', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        some_base_prop: Optional[str] = None,
        reason: Optional[str] = None,
        what_sub_address: Optional[str] = None,
        **kwargs
    ):
        super(LinkNotFound, self).__init__(some_base_prop=some_base_prop, reason=reason, **kwargs)
        self.what_not_found = 'InvalidResourceLink'
        self.what_sub_address = what_sub_address


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

    def __init__(
        self,
        *,
        ani_type: Optional[str] = None,
        **kwargs
    ):
        super(Pet, self).__init__(ani_type=ani_type, **kwargs)
        self.name = None


class PetAction(msrest.serialization.Model):
    """PetAction.

    :param action_response: action feedback.
    :type action_response: str
    """

    _attribute_map = {
        'action_response': {'key': 'actionResponse', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        action_response: Optional[str] = None,
        **kwargs
    ):
        super(PetAction, self).__init__(**kwargs)
        self.action_response = action_response


class PetActionErrorException(HttpResponseError):
    """Server responded with exception of type: 'PetActionError'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(PetActionErrorException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'PetActionError'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class PetActionError(msrest.serialization.Model):
    """PetActionError.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: PetSadError.

    All required parameters must be populated in order to send to Azure.

    :param error_type: Required. Constant filled by server.
    :type error_type: str
    :param error_message: the error message.
    :type error_message: str
    """
    _EXCEPTION_TYPE = PetActionErrorException

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

    def __init__(
        self,
        *,
        error_message: Optional[str] = None,
        **kwargs
    ):
        super(PetActionError, self).__init__(**kwargs)
        self.error_type = 'None'
        self.error_message = error_message


class PetSadErrorException(PetActionErrorException):
    """Server responded with exception of type: 'PetSadError'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(PetSadErrorException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'PetSadError'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class PetSadError(PetActionError):
    """PetSadError.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: PetHungryOrThirstyError.

    All required parameters must be populated in order to send to Azure.

    :param error_type: Required. Constant filled by server.
    :type error_type: str
    :param error_message: the error message.
    :type error_message: str
    :param reason: why is the pet sad.
    :type reason: str
    """
    _EXCEPTION_TYPE = PetSadErrorException

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

    def __init__(
        self,
        *,
        error_message: Optional[str] = None,
        reason: Optional[str] = None,
        **kwargs
    ):
        super(PetSadError, self).__init__(error_message=error_message, **kwargs)
        self.error_type = 'PetSadError'
        self.reason = reason


class PetHungryOrThirstyErrorException(PetSadErrorException):
    """Server responded with exception of type: 'PetHungryOrThirstyError'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(PetHungryOrThirstyErrorException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'PetHungryOrThirstyError'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


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
    _EXCEPTION_TYPE = PetHungryOrThirstyErrorException

    _validation = {
        'error_type': {'required': True},
    }

    _attribute_map = {
        'error_type': {'key': 'errorType', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
        'hungry_or_thirsty': {'key': 'hungryOrThirsty', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        error_message: Optional[str] = None,
        reason: Optional[str] = None,
        hungry_or_thirsty: Optional[str] = None,
        **kwargs
    ):
        super(PetHungryOrThirstyError, self).__init__(error_message=error_message, reason=reason, **kwargs)
        self.error_type = 'PetHungryOrThirstyError'
        self.hungry_or_thirsty = hungry_or_thirsty
