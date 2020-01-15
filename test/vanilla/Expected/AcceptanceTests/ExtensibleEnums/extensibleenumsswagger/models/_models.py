# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model

class Pet(Model):
    """Pet.

    All required parameters must be populated in order to send to Azure.

    :param name:
    :type name: str
    :param days_of_week: Type of Pet. Possible values include: 'Monday', 'Tuesday',
	 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'. Default value:
	 "Friday".
    :type days_of_week: str or
	 ~extensibleenumsswagger.models.DaysOfWeekExtensibleEnum
    :param int_enum: Required.  Possible values include: '1', '2', '3'.
    :type int_enum: str or ~extensibleenumsswagger.models.IntEnum
    """

    _validation = {
        'int_enum': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'days_of_week': {'key': 'DaysOfWeek', 'type': 'str'},
        'int_enum': {'key': 'IntEnum', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Pet, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.days_of_week = kwargs.get('days_of_week', "Friday")
        self.int_enum = kwargs.get('int_enum', None)

