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


class Feline(msrest.serialization.Model):
    """Feline.

    :param hisses:
    :type hisses: bool
    :param meows:
    :type meows: bool
    """

    _attribute_map = {
        'hisses': {'key': 'hisses', 'type': 'bool'},
        'meows': {'key': 'meows', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        hisses: Optional[bool] = None,
        meows: Optional[bool] = None,
        **kwargs
    ):
        super(Feline, self).__init__(**kwargs)
        self.hisses = hisses
        self.meows = meows


class Pet(msrest.serialization.Model):
    """Pet.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        **kwargs
    ):
        super(Pet, self).__init__(**kwargs)
        self.name = name


class Cat(Pet, Feline):
    """Cat.

    All required parameters must be populated in order to send to Azure.

    :param hisses:
    :type hisses: bool
    :param meows:
    :type meows: bool
    :param name: Required.
    :type name: str
    :param likes_milk:
    :type likes_milk: bool
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'hisses': {'key': 'hisses', 'type': 'bool'},
        'meows': {'key': 'meows', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'likes_milk': {'key': 'likesMilk', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        name: str,
        hisses: Optional[bool] = None,
        meows: Optional[bool] = None,
        likes_milk: Optional[bool] = None,
        **kwargs
    ):
        super(Cat, self).__init__(name=name, hisses=hisses, meows=meows, **kwargs)
        self.hisses = hisses
        self.meows = meows
        self.likes_milk = likes_milk
        self.name = name
        self.likes_milk = likes_milk


class Error(msrest.serialization.Model):
    """Error.

    :param message:
    :type message: str
    :param status:
    :type status: int
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'status': {'key': 'status', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        message: Optional[str] = None,
        status: Optional[int] = None,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.message = message
        self.status = status


class Horse(Pet):
    """Horse.

    All required parameters must be populated in order to send to Azure.

    :param name: Required.
    :type name: str
    :param is_a_show_horse:
    :type is_a_show_horse: bool
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'is_a_show_horse': {'key': 'isAShowHorse', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        name: str,
        is_a_show_horse: Optional[bool] = None,
        **kwargs
    ):
        super(Horse, self).__init__(name=name, **kwargs)
        self.is_a_show_horse = is_a_show_horse


class Kitten(Cat):
    """Kitten.

    All required parameters must be populated in order to send to Azure.

    :param hisses:
    :type hisses: bool
    :param meows:
    :type meows: bool
    :param name: Required.
    :type name: str
    :param likes_milk:
    :type likes_milk: bool
    :param eats_mice_yet:
    :type eats_mice_yet: bool
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'hisses': {'key': 'hisses', 'type': 'bool'},
        'meows': {'key': 'meows', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'likes_milk': {'key': 'likesMilk', 'type': 'bool'},
        'eats_mice_yet': {'key': 'eatsMiceYet', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        name: str,
        hisses: Optional[bool] = None,
        meows: Optional[bool] = None,
        likes_milk: Optional[bool] = None,
        eats_mice_yet: Optional[bool] = None,
        **kwargs
    ):
        super(Kitten, self).__init__(hisses=hisses, meows=meows, name=name, likes_milk=likes_milk, **kwargs)
        self.eats_mice_yet = eats_mice_yet
