# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from .. import _serialization


class Animal(_serialization.Model):
    """Animal.

    :ivar ani_type:
    :vartype ani_type: str
    """

    _attribute_map = {
        "ani_type": {"key": "aniType", "type": "str"},
    }

    def __init__(self, *, ani_type: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword ani_type:
        :paramtype ani_type: str
        """
        super().__init__(**kwargs)
        self.ani_type = ani_type


class BaseError(_serialization.Model):
    """BaseError.

    :ivar some_base_prop:
    :vartype some_base_prop: str
    """

    _attribute_map = {
        "some_base_prop": {"key": "someBaseProp", "type": "str"},
    }

    def __init__(self, *, some_base_prop: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword some_base_prop:
        :paramtype some_base_prop: str
        """
        super().__init__(**kwargs)
        self.some_base_prop = some_base_prop


class NotFoundErrorBase(BaseError):
    """NotFoundErrorBase.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    AnimalNotFound, LinkNotFound

    All required parameters must be populated in order to send to server.

    :ivar some_base_prop:
    :vartype some_base_prop: str
    :ivar reason:
    :vartype reason: str
    :ivar what_not_found: Required.
    :vartype what_not_found: str
    """

    _validation = {
        "what_not_found": {"required": True},
    }

    _attribute_map = {
        "some_base_prop": {"key": "someBaseProp", "type": "str"},
        "reason": {"key": "reason", "type": "str"},
        "what_not_found": {"key": "whatNotFound", "type": "str"},
    }

    _subtype_map = {"what_not_found": {"AnimalNotFound": "AnimalNotFound", "InvalidResourceLink": "LinkNotFound"}}

    def __init__(self, *, some_base_prop: Optional[str] = None, reason: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword some_base_prop:
        :paramtype some_base_prop: str
        :keyword reason:
        :paramtype reason: str
        """
        super().__init__(some_base_prop=some_base_prop, **kwargs)
        self.reason = reason
        self.what_not_found: Optional[str] = None


class AnimalNotFound(NotFoundErrorBase):
    """AnimalNotFound.

    All required parameters must be populated in order to send to server.

    :ivar some_base_prop:
    :vartype some_base_prop: str
    :ivar reason:
    :vartype reason: str
    :ivar what_not_found: Required.
    :vartype what_not_found: str
    :ivar name:
    :vartype name: str
    """

    _validation = {
        "what_not_found": {"required": True},
    }

    _attribute_map = {
        "some_base_prop": {"key": "someBaseProp", "type": "str"},
        "reason": {"key": "reason", "type": "str"},
        "what_not_found": {"key": "whatNotFound", "type": "str"},
        "name": {"key": "name", "type": "str"},
    }

    def __init__(
        self,
        *,
        some_base_prop: Optional[str] = None,
        reason: Optional[str] = None,
        name: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword some_base_prop:
        :paramtype some_base_prop: str
        :keyword reason:
        :paramtype reason: str
        :keyword name:
        :paramtype name: str
        """
        super().__init__(some_base_prop=some_base_prop, reason=reason, **kwargs)
        self.what_not_found: str = "AnimalNotFound"
        self.name = name


class LinkNotFound(NotFoundErrorBase):
    """LinkNotFound.

    All required parameters must be populated in order to send to server.

    :ivar some_base_prop:
    :vartype some_base_prop: str
    :ivar reason:
    :vartype reason: str
    :ivar what_not_found: Required.
    :vartype what_not_found: str
    :ivar what_sub_address:
    :vartype what_sub_address: str
    """

    _validation = {
        "what_not_found": {"required": True},
    }

    _attribute_map = {
        "some_base_prop": {"key": "someBaseProp", "type": "str"},
        "reason": {"key": "reason", "type": "str"},
        "what_not_found": {"key": "whatNotFound", "type": "str"},
        "what_sub_address": {"key": "whatSubAddress", "type": "str"},
    }

    def __init__(
        self,
        *,
        some_base_prop: Optional[str] = None,
        reason: Optional[str] = None,
        what_sub_address: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword some_base_prop:
        :paramtype some_base_prop: str
        :keyword reason:
        :paramtype reason: str
        :keyword what_sub_address:
        :paramtype what_sub_address: str
        """
        super().__init__(some_base_prop=some_base_prop, reason=reason, **kwargs)
        self.what_not_found: str = "InvalidResourceLink"
        self.what_sub_address = what_sub_address


class Pet(Animal):
    """Pet.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar ani_type:
    :vartype ani_type: str
    :ivar name: Gets the Pet by id.
    :vartype name: str
    """

    _validation = {
        "name": {"readonly": True},
    }

    _attribute_map = {
        "ani_type": {"key": "aniType", "type": "str"},
        "name": {"key": "name", "type": "str"},
    }

    def __init__(self, *, ani_type: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword ani_type:
        :paramtype ani_type: str
        """
        super().__init__(ani_type=ani_type, **kwargs)
        self.name = None


class PetAction(_serialization.Model):
    """PetAction.

    :ivar action_response: action feedback.
    :vartype action_response: str
    """

    _attribute_map = {
        "action_response": {"key": "actionResponse", "type": "str"},
    }

    def __init__(self, *, action_response: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword action_response: action feedback.
        :paramtype action_response: str
        """
        super().__init__(**kwargs)
        self.action_response = action_response


class PetActionError(PetAction):
    """PetActionError.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    PetSadError

    All required parameters must be populated in order to send to server.

    :ivar action_response: action feedback.
    :vartype action_response: str
    :ivar error_type: Required.
    :vartype error_type: str
    :ivar error_message: the error message.
    :vartype error_message: str
    """

    _validation = {
        "error_type": {"required": True},
    }

    _attribute_map = {
        "action_response": {"key": "actionResponse", "type": "str"},
        "error_type": {"key": "errorType", "type": "str"},
        "error_message": {"key": "errorMessage", "type": "str"},
    }

    _subtype_map = {"error_type": {"PetSadError": "PetSadError"}}

    def __init__(
        self, *, action_response: Optional[str] = None, error_message: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword action_response: action feedback.
        :paramtype action_response: str
        :keyword error_message: the error message.
        :paramtype error_message: str
        """
        super().__init__(action_response=action_response, **kwargs)
        self.error_type: Optional[str] = None
        self.error_message = error_message


class PetSadError(PetActionError):
    """PetSadError.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    PetHungryOrThirstyError

    All required parameters must be populated in order to send to server.

    :ivar action_response: action feedback.
    :vartype action_response: str
    :ivar error_type: Required.
    :vartype error_type: str
    :ivar error_message: the error message.
    :vartype error_message: str
    :ivar reason: why is the pet sad.
    :vartype reason: str
    """

    _validation = {
        "error_type": {"required": True},
    }

    _attribute_map = {
        "action_response": {"key": "actionResponse", "type": "str"},
        "error_type": {"key": "errorType", "type": "str"},
        "error_message": {"key": "errorMessage", "type": "str"},
        "reason": {"key": "reason", "type": "str"},
    }

    _subtype_map = {"error_type": {"PetHungryOrThirstyError": "PetHungryOrThirstyError"}}

    def __init__(
        self,
        *,
        action_response: Optional[str] = None,
        error_message: Optional[str] = None,
        reason: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword action_response: action feedback.
        :paramtype action_response: str
        :keyword error_message: the error message.
        :paramtype error_message: str
        :keyword reason: why is the pet sad.
        :paramtype reason: str
        """
        super().__init__(action_response=action_response, error_message=error_message, **kwargs)
        self.error_type: str = "PetSadError"
        self.reason = reason


class PetHungryOrThirstyError(PetSadError):
    """PetHungryOrThirstyError.

    All required parameters must be populated in order to send to server.

    :ivar action_response: action feedback.
    :vartype action_response: str
    :ivar error_type: Required.
    :vartype error_type: str
    :ivar error_message: the error message.
    :vartype error_message: str
    :ivar reason: why is the pet sad.
    :vartype reason: str
    :ivar hungry_or_thirsty: is the pet hungry or thirsty or both.
    :vartype hungry_or_thirsty: str
    """

    _validation = {
        "error_type": {"required": True},
    }

    _attribute_map = {
        "action_response": {"key": "actionResponse", "type": "str"},
        "error_type": {"key": "errorType", "type": "str"},
        "error_message": {"key": "errorMessage", "type": "str"},
        "reason": {"key": "reason", "type": "str"},
        "hungry_or_thirsty": {"key": "hungryOrThirsty", "type": "str"},
    }

    def __init__(
        self,
        *,
        action_response: Optional[str] = None,
        error_message: Optional[str] = None,
        reason: Optional[str] = None,
        hungry_or_thirsty: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword action_response: action feedback.
        :paramtype action_response: str
        :keyword error_message: the error message.
        :paramtype error_message: str
        :keyword reason: why is the pet sad.
        :paramtype reason: str
        :keyword hungry_or_thirsty: is the pet hungry or thirsty or both.
        :paramtype hungry_or_thirsty: str
        """
        super().__init__(action_response=action_response, error_message=error_message, reason=reason, **kwargs)
        self.error_type: str = "PetHungryOrThirstyError"
        self.hungry_or_thirsty = hungry_or_thirsty
