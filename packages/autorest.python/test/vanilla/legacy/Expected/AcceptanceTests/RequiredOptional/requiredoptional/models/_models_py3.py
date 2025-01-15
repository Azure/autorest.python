# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Optional, TYPE_CHECKING

import msrest.serialization

if TYPE_CHECKING:
    from .. import models as _models


class ArrayOptionalWrapper(msrest.serialization.Model):
    """ArrayOptionalWrapper.

    :ivar value:
    :vartype value: list[str]
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[str]"},
    }

    def __init__(self, *, value: Optional[List[str]] = None, **kwargs: Any) -> None:
        """
        :keyword value:
        :paramtype value: list[str]
        """
        super().__init__(**kwargs)
        self.value: Optional[List[str]] = value


class ArrayWrapper(msrest.serialization.Model):
    """ArrayWrapper.

    All required parameters must be populated in order to send to server.

    :ivar value: Required.
    :vartype value: list[str]
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[str]"},
    }

    def __init__(self, *, value: List[str], **kwargs: Any) -> None:
        """
        :keyword value: Required.
        :paramtype value: list[str]
        """
        super().__init__(**kwargs)
        self.value: List[str] = value


class ClassOptionalWrapper(msrest.serialization.Model):
    """ClassOptionalWrapper.

    :ivar value:
    :vartype value: ~requiredoptional.models.Product
    """

    _attribute_map = {
        "value": {"key": "value", "type": "Product"},
    }

    def __init__(self, *, value: Optional["_models.Product"] = None, **kwargs: Any) -> None:
        """
        :keyword value:
        :paramtype value: ~requiredoptional.models.Product
        """
        super().__init__(**kwargs)
        self.value: Optional["_models.Product"] = value


class ClassWrapper(msrest.serialization.Model):
    """ClassWrapper.

    All required parameters must be populated in order to send to server.

    :ivar value: Required.
    :vartype value: ~requiredoptional.models.Product
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "Product"},
    }

    def __init__(self, *, value: "_models.Product", **kwargs: Any) -> None:
        """
        :keyword value: Required.
        :paramtype value: ~requiredoptional.models.Product
        """
        super().__init__(**kwargs)
        self.value: "_models.Product" = value


class Error(msrest.serialization.Model):
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
        self.status: Optional[int] = status
        self.message: Optional[str] = message


class IntOptionalWrapper(msrest.serialization.Model):
    """IntOptionalWrapper.

    :ivar value:
    :vartype value: int
    """

    _attribute_map = {
        "value": {"key": "value", "type": "int"},
    }

    def __init__(self, *, value: Optional[int] = None, **kwargs: Any) -> None:
        """
        :keyword value:
        :paramtype value: int
        """
        super().__init__(**kwargs)
        self.value: Optional[int] = value


class IntWrapper(msrest.serialization.Model):
    """IntWrapper.

    All required parameters must be populated in order to send to server.

    :ivar value: Required.
    :vartype value: int
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "int"},
    }

    def __init__(self, *, value: int, **kwargs: Any) -> None:
        """
        :keyword value: Required.
        :paramtype value: int
        """
        super().__init__(**kwargs)
        self.value: int = value


class Product(msrest.serialization.Model):
    """Product.

    All required parameters must be populated in order to send to server.

    :ivar id: Required.
    :vartype id: int
    :ivar name:
    :vartype name: str
    """

    _validation = {
        "id": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
    }

    def __init__(
        self, *, id: int, name: Optional[str] = None, **kwargs: Any  # pylint: disable=redefined-builtin
    ) -> None:
        """
        :keyword id: Required.
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        """
        super().__init__(**kwargs)
        self.id: int = id
        self.name: Optional[str] = name


class StringOptionalWrapper(msrest.serialization.Model):
    """StringOptionalWrapper.

    :ivar value:
    :vartype value: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "str"},
    }

    def __init__(self, *, value: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword value:
        :paramtype value: str
        """
        super().__init__(**kwargs)
        self.value: Optional[str] = value


class StringWrapper(msrest.serialization.Model):
    """StringWrapper.

    All required parameters must be populated in order to send to server.

    :ivar value: Required.
    :vartype value: str
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "str"},
    }

    def __init__(self, *, value: str, **kwargs: Any) -> None:
        """
        :keyword value: Required.
        :paramtype value: str
        """
        super().__init__(**kwargs)
        self.value: str = value
