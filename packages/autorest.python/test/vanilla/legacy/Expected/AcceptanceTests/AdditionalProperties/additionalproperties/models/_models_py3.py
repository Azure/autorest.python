# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Dict, Optional

from .. import _serialization


class PetAPTrue(_serialization.Model):
    """PetAPTrue.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, any]
    :ivar id: Required.
    :vartype id: int
    :ivar name:
    :vartype name: str
    :ivar status:
    :vartype status: bool
    """

    _validation = {
        "id": {"required": True},
        "status": {"readonly": True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{object}"},
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "status": {"key": "status", "type": "bool"},
    }

    def __init__(
        self,
        *,
        id: int,  # pylint: disable=redefined-builtin
        additional_properties: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, any]
        :keyword id: Required.
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        """
        super().__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status: Optional[bool] = None


class CatAPTrue(PetAPTrue):
    """CatAPTrue.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, any]
    :ivar id: Required.
    :vartype id: int
    :ivar name:
    :vartype name: str
    :ivar status:
    :vartype status: bool
    :ivar friendly:
    :vartype friendly: bool
    """

    _validation = {
        "id": {"required": True},
        "status": {"readonly": True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{object}"},
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "status": {"key": "status", "type": "bool"},
        "friendly": {"key": "friendly", "type": "bool"},
    }

    def __init__(
        self,
        *,
        id: int,  # pylint: disable=redefined-builtin
        additional_properties: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        friendly: Optional[bool] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, any]
        :keyword id: Required.
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        :keyword friendly:
        :paramtype friendly: bool
        """
        super().__init__(additional_properties=additional_properties, id=id, name=name, **kwargs)
        self.friendly = friendly


class Error(_serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.status = status
        self.message = message


class PetAPInProperties(_serialization.Model):
    """PetAPInProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Required.
    :vartype id: int
    :ivar name:
    :vartype name: str
    :ivar status:
    :vartype status: bool
    :ivar additional_properties: Dictionary of :code:`<number>`.
    :vartype additional_properties: dict[str, float]
    """

    _validation = {
        "id": {"required": True},
        "status": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "status": {"key": "status", "type": "bool"},
        "additional_properties": {"key": "additionalProperties", "type": "{float}"},
    }

    def __init__(
        self,
        *,
        id: int,  # pylint: disable=redefined-builtin
        name: Optional[str] = None,
        additional_properties: Optional[Dict[str, float]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword id: Required.
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        :keyword additional_properties: Dictionary of :code:`<number>`.
        :paramtype additional_properties: dict[str, float]
        """
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.status: Optional[bool] = None
        self.additional_properties = additional_properties


class PetAPInPropertiesWithAPString(_serialization.Model):
    """PetAPInPropertiesWithAPString.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, str]
    :ivar id: Required.
    :vartype id: int
    :ivar name:
    :vartype name: str
    :ivar status:
    :vartype status: bool
    :ivar odata_location: Required.
    :vartype odata_location: str
    :ivar additional_properties1: Dictionary of :code:`<number>`.
    :vartype additional_properties1: dict[str, float]
    """

    _validation = {
        "id": {"required": True},
        "status": {"readonly": True},
        "odata_location": {"required": True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{str}"},
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "status": {"key": "status", "type": "bool"},
        "odata_location": {"key": "@odata\\.location", "type": "str"},
        "additional_properties1": {"key": "additionalProperties", "type": "{float}"},
    }

    def __init__(
        self,
        *,
        id: int,  # pylint: disable=redefined-builtin
        odata_location: str,
        additional_properties: Optional[Dict[str, str]] = None,
        name: Optional[str] = None,
        additional_properties1: Optional[Dict[str, float]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, str]
        :keyword id: Required.
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        :keyword odata_location: Required.
        :paramtype odata_location: str
        :keyword additional_properties1: Dictionary of :code:`<number>`.
        :paramtype additional_properties1: dict[str, float]
        """
        super().__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status: Optional[bool] = None
        self.odata_location = odata_location
        self.additional_properties1 = additional_properties1


class PetAPObject(_serialization.Model):
    """PetAPObject.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, any]
    :ivar id: Required.
    :vartype id: int
    :ivar name:
    :vartype name: str
    :ivar status:
    :vartype status: bool
    """

    _validation = {
        "id": {"required": True},
        "status": {"readonly": True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{object}"},
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "status": {"key": "status", "type": "bool"},
    }

    def __init__(
        self,
        *,
        id: int,  # pylint: disable=redefined-builtin
        additional_properties: Optional[Dict[str, Any]] = None,
        name: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, any]
        :keyword id: Required.
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        """
        super().__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status: Optional[bool] = None


class PetAPString(_serialization.Model):
    """PetAPString.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, str]
    :ivar id: Required.
    :vartype id: int
    :ivar name:
    :vartype name: str
    :ivar status:
    :vartype status: bool
    """

    _validation = {
        "id": {"required": True},
        "status": {"readonly": True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{str}"},
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "status": {"key": "status", "type": "bool"},
    }

    def __init__(
        self,
        *,
        id: int,  # pylint: disable=redefined-builtin
        additional_properties: Optional[Dict[str, str]] = None,
        name: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, str]
        :keyword id: Required.
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        """
        super().__init__(**kwargs)
        self.additional_properties = additional_properties
        self.id = id
        self.name = name
        self.status: Optional[bool] = None
