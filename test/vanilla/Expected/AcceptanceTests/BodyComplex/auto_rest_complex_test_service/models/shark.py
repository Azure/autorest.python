# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .fish import Fish


class Shark(Fish):
    """Shark.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Sawshark, Goblinshark, Cookiecuttershark

    :param species:
    :type species: str
    :param length:
    :type length: float
    :param siblings:
    :type siblings: list[~fixtures.acceptancetestsbodycomplex.models.Fish]
    :param fishtype: Constant filled by server.
    :type fishtype: str
    :param age:
    :type age: int
    :param birthday:
    :type birthday: datetime
    """

    _validation = {
        'length': {'required': True},
        'fishtype': {'required': True},
        'birthday': {'required': True},
    }

    _attribute_map = {
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
        'fishtype': {'key': 'fishtype', 'type': 'str'},
        'age': {'key': 'age', 'type': 'int'},
        'birthday': {'key': 'birthday', 'type': 'iso-8601'},
    }

    _subtype_map = {
        'fishtype': {'sawshark': 'Sawshark', 'goblin': 'Goblinshark', 'cookiecuttershark': 'Cookiecuttershark'}
    }

    def __init__(self, length, birthday, species=None, siblings=None, age=None):
        super(Shark, self).__init__(species=species, length=length, siblings=siblings)
        self.age = age
        self.birthday = birthday
        self.fishtype = 'shark'
