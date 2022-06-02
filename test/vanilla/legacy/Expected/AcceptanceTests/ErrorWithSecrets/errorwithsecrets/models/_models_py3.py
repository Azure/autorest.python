# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

import msrest.serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Error(msrest.serialization.Model):
    """The error object.

    All required parameters must be populated in order to send to Azure.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, any]
    :ivar code: One of a server-defined set of error codes. Required. Known values are:
     "BadParameter" and "Unauthorized".
    :vartype code: str or ~errorwithsecrets.models.ErrorCode
    :ivar message: A human-readable representation of the error. Required.
    :vartype message: str
    :ivar target: The target of the error.
    :vartype target: str
    :ivar details: An array of details about specific errors that led to this reported error.
    :vartype details: list[~errorwithsecrets.models.Error]
    :ivar innererror: An object containing more specific information than the current object about
     the error.
    :vartype innererror: ~errorwithsecrets.models.InnerError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{object}"},
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[Error]"},
        "innererror": {"key": "innererror", "type": "InnerError"},
    }

    def __init__(
        self,
        *,
        code: Union[str, "_models.ErrorCode"],
        message: str,
        additional_properties: Optional[Dict[str, Any]] = None,
        target: Optional[str] = None,
        details: Optional[List["_models.Error"]] = None,
        innererror: Optional["_models.InnerError"] = None,
        **kwargs
    ):
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, any]
        :keyword code: One of a server-defined set of error codes. Required. Known values are:
         "BadParameter" and "Unauthorized".
        :paramtype code: str or ~errorwithsecrets.models.ErrorCode
        :keyword message: A human-readable representation of the error. Required.
        :paramtype message: str
        :keyword target: The target of the error.
        :paramtype target: str
        :keyword details: An array of details about specific errors that led to this reported error.
        :paramtype details: list[~errorwithsecrets.models.Error]
        :keyword innererror: An object containing more specific information than the current object
         about the error.
        :paramtype innererror: ~errorwithsecrets.models.InnerError
        """
        super().__init__(**kwargs)
        self.additional_properties = additional_properties
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    All required parameters must be populated in order to send to Azure.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, any]
    :ivar error: The error object. Required.
    :vartype error: ~errorwithsecrets.models.Error
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{object}"},
        "error": {"key": "error", "type": "Error"},
    }

    def __init__(
        self,
        *,
        error: "_models.Error",
        additional_properties: Optional[Dict[str, Any]] = None,
        **kwargs
    ):
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, any]
        :keyword error: The error object. Required.
        :paramtype error: ~errorwithsecrets.models.Error
        """
        super().__init__(**kwargs)
        self.additional_properties = additional_properties
        self.error = error


class InnerError(msrest.serialization.Model):
    """An object containing more specific information about the error. As per Microsoft One API guidelines - https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    All required parameters must be populated in order to send to Azure.

    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, any]
    :ivar code: One of a server-defined set of error codes. Required. Known values are:
     "MissingSharedKey" and "UnauthorizedSharedKey".
    :vartype code: str or ~errorwithsecrets.models.InnerErrorCode
    :ivar message: Error message. Required.
    :vartype message: str
    :ivar innererror: An object containing more specific information than the current object about
     the error.
    :vartype innererror: ~errorwithsecrets.models.InnerError
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        "additional_properties": {"key": "", "type": "{object}"},
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "innererror": {"key": "innererror", "type": "InnerError"},
    }

    def __init__(
        self,
        *,
        code: Union[str, "_models.InnerErrorCode"],
        message: str,
        additional_properties: Optional[Dict[str, Any]] = None,
        innererror: Optional["_models.InnerError"] = None,
        **kwargs
    ):
        """
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, any]
        :keyword code: One of a server-defined set of error codes. Required. Known values are:
         "MissingSharedKey" and "UnauthorizedSharedKey".
        :paramtype code: str or ~errorwithsecrets.models.InnerErrorCode
        :keyword message: Error message. Required.
        :paramtype message: str
        :keyword innererror: An object containing more specific information than the current object
         about the error.
        :paramtype innererror: ~errorwithsecrets.models.InnerError
        """
        super().__init__(**kwargs)
        self.additional_properties = additional_properties
        self.code = code
        self.message = message
        self.innererror = innererror


class SecretResponse(msrest.serialization.Model):
    """A secret.

    All required parameters must be populated in order to send to Azure.

    :ivar key: The secret key. Required.
    :vartype key: str
    :ivar value: The secret value. Required.
    :vartype value: str
    """

    _validation = {
        'key': {'required': True},
        'value': {'required': True},
    }

    _attribute_map = {
        "key": {"key": "key", "type": "str"},
        "value": {"key": "value", "type": "str"},
    }

    def __init__(
        self,
        *,
        key: str,
        value: str,
        **kwargs
    ):
        """
        :keyword key: The secret key. Required.
        :paramtype key: str
        :keyword value: The secret value. Required.
        :paramtype value: str
        """
        super().__init__(**kwargs)
        self.key = key
        self.value = value
