# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Optional, TYPE_CHECKING, Union

from .. import _serialization

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Paths14Hl8BdFormsdataurlencodedPetAddPetidPostRequestbodyContentApplicationXWwwFormUrlencodedSchema(
    _serialization.Model
):
    """Paths14Hl8BdFormsdataurlencodedPetAddPetidPostRequestbodyContentApplicationXWwwFormUrlencodedSchema.

    All required parameters must be populated in order to send to Azure.

    :ivar pet_type: Can take a value of dog, or cat, or fish. Required. Known values are: "dog",
     "cat", and "fish".
    :vartype pet_type: str or ~bodyformurlencodeddata.models.PetType
    :ivar pet_food: Can take a value of meat, or fish, or plant. Required. Known values are:
     "meat", "fish", and "plant".
    :vartype pet_food: str or ~bodyformurlencodeddata.models.PetFood
    :ivar pet_age: How many years is it old?. Required.
    :vartype pet_age: int
    :ivar name: Updated name of the pet.
    :vartype name: str
    :ivar status: Updated status of the pet.
    :vartype status: str
    """

    _validation = {
        "pet_type": {"required": True},
        "pet_food": {"required": True},
        "pet_age": {"required": True},
    }

    _attribute_map = {
        "pet_type": {"key": "pet_type", "type": "str"},
        "pet_food": {"key": "pet_food", "type": "str"},
        "pet_age": {"key": "pet_age", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "status": {"key": "status", "type": "str"},
    }

    def __init__(
        self,
        *,
        pet_type: Union[str, "_models.PetType"],
        pet_food: Union[str, "_models.PetFood"],
        pet_age: int,
        name: Optional[str] = None,
        status: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword pet_type: Can take a value of dog, or cat, or fish. Required. Known values are: "dog",
         "cat", and "fish".
        :paramtype pet_type: str or ~bodyformurlencodeddata.models.PetType
        :keyword pet_food: Can take a value of meat, or fish, or plant. Required. Known values are:
         "meat", "fish", and "plant".
        :paramtype pet_food: str or ~bodyformurlencodeddata.models.PetFood
        :keyword pet_age: How many years is it old?. Required.
        :paramtype pet_age: int
        :keyword name: Updated name of the pet.
        :paramtype name: str
        :keyword status: Updated status of the pet.
        :paramtype status: str
        """
        super().__init__(**kwargs)
        self.pet_type = pet_type
        self.pet_food = pet_food
        self.pet_age = pet_age
        self.name = name
        self.status = status


class PathsPvivzlFormsdataurlencodedPartialconstantbodyPostRequestbodyContentApplicationXWwwFormUrlencodedSchema(
    _serialization.Model
):
    """PathsPvivzlFormsdataurlencodedPartialconstantbodyPostRequestbodyContentApplicationXWwwFormUrlencodedSchema.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar grant_type: Constant part of a formdata body. Required. Default value is "access_token".
    :vartype grant_type: str
    :ivar service: Indicates the name of your Azure container registry. Required.
    :vartype service: str
    :ivar aad_access_token: AAD access token, mandatory when grant_type is
     access_token_refresh_token or access_token. Required.
    :vartype aad_access_token: str
    """

    _validation = {
        "grant_type": {"required": True, "constant": True},
        "service": {"required": True},
        "aad_access_token": {"required": True},
    }

    _attribute_map = {
        "grant_type": {"key": "grant_type", "type": "str"},
        "service": {"key": "service", "type": "str"},
        "aad_access_token": {"key": "access_token", "type": "str"},
    }

    grant_type = "access_token"

    def __init__(self, *, service: str, aad_access_token: str, **kwargs):
        """
        :keyword service: Indicates the name of your Azure container registry. Required.
        :paramtype service: str
        :keyword aad_access_token: AAD access token, mandatory when grant_type is
         access_token_refresh_token or access_token. Required.
        :paramtype aad_access_token: str
        """
        super().__init__(**kwargs)
        self.service = service
        self.aad_access_token = aad_access_token
