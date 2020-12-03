# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Optional, Union

import msrest.serialization

from ._pet_store_inc_enums import *


class Pet(msrest.serialization.Model):
    """Pet.

    All required parameters must be populated in order to send to Azure.

    :param name: name.
    :type name: str
    :param days_of_week: Type of Pet. Possible values include: "Monday", "Tuesday", "Wednesday",
     "Thursday", "Friday", "Saturday", "Sunday". Default value: "Friday".
    :type days_of_week: str or ~extensibleenumsswagger.models.DaysOfWeekExtensibleEnum
    :param int_enum: Required.  Possible values include: "1", "2", "3".
    :type int_enum: str or ~extensibleenumsswagger.models.IntEnum
    """

    _validation = {
        "int_enum": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "days_of_week": {"key": "DaysOfWeek", "type": "str"},
        "int_enum": {"key": "IntEnum", "type": "str"},
    }

    def __init__(
        self,
        *,
        int_enum: Union[str, "IntEnum"],
        name: Optional[str] = None,
        days_of_week: Optional[Union[str, "DaysOfWeekExtensibleEnum"]] = "Friday",
        **kwargs
    ):
        super(Pet, self).__init__(**kwargs)
        self.name = name
        self.days_of_week = days_of_week
        self.int_enum = int_enum
