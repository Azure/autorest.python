# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Dict, List, Union

from azure.core.exceptions import HttpResponseError
from msrest.serialization import Model


class ArrayWrapper(Model):
    """ArrayWrapper.

    :param array:
    :type array: list[str]
    """

    _attribute_map = {
        'array': {'key': 'array', 'type': '[str]'},
    }

    def __init__(self, *, array: List[str]=None, **kwargs) -> None:
        super(ArrayWrapper, self).__init__(**kwargs)
        self.array = array


class Basic(Model):
    """Basic.

    :param id: Basic Id.
    :type id: int
    :param name: Name property with a very long description that does not fit on a
	 single line and a line break.
    :type name: str
    :param color:  Possible values include: 'cyan', 'Magenta', 'YELLOW', 'blacK'.
    :type color: str or ~bodycomplex.models.CMYKColors
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'color': {'key': 'color', 'type': 'str'},
    }

    def __init__(self, *, id: int=None, name: str=None, color: Union[str, "CMYKColors"]=None, **kwargs) -> None:
        super(Basic, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.color = color


class BooleanWrapper(Model):
    """BooleanWrapper.

    :param field_true:
    :type field_true: bool
    :param field_false:
    :type field_false: bool
    """

    _attribute_map = {
        'field_true': {'key': 'field_true', 'type': 'bool'},
        'field_false': {'key': 'field_false', 'type': 'bool'},
    }

    def __init__(self, *, field_true: bool=None, field_false: bool=None, **kwargs) -> None:
        super(BooleanWrapper, self).__init__(**kwargs)
        self.field_true = field_true
        self.field_false = field_false


class ByteWrapper(Model):
    """ByteWrapper.

    :param field:
    :type field: bytearray
    """

    _attribute_map = {
        'field': {'key': 'field', 'type': 'bytearray'},
    }

    def __init__(self, *, field: bytearray=None, **kwargs) -> None:
        super(ByteWrapper, self).__init__(**kwargs)
        self.field = field


class Pet(Model):
    """Pet.

    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, id: int=None, name: str=None, **kwargs) -> None:
        super(Pet, self).__init__(**kwargs)
        self.id = id
        self.name = name


class Cat(Pet):
    """Cat.

    :param id:
    :type id: int
    :param name:
    :type name: str
    :param color:
    :type color: str
    :param hates:
    :type hates: list[~bodycomplex.models.Dog]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'color': {'key': 'color', 'type': 'str'},
        'hates': {'key': 'hates', 'type': '[Dog]'},
    }

    def __init__(self, *, id: int=None, name: str=None, color: str=None, hates: List["Dog"]=None, **kwargs) -> None:
        super(Cat, self).__init__(id=id, name=name, **kwargs)
        self.color = color
        self.hates = hates


class Fish(Model):
    """Fish.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Salmon, Shark.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
    }

    _attribute_map = {
        'fishtype': {'key': 'fishtype', 'type': 'str'},
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
    }

    _subtype_map = {
        'fishtype': {'salmon': 'Salmon', 'shark': 'Shark'}
    }

    def __init__(self, *, length: float, species: str=None, siblings: List["Fish"]=None, **kwargs) -> None:
        super(Fish, self).__init__(**kwargs)
        self.fishtype = 'None'
        self.species = species
        self.length = length
        self.siblings = siblings


class Shark(Fish):
    """Shark.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Cookiecuttershark, Goblinshark, Sawshark.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param age:
    :type age: int
    :param birthday: Required.
    :type birthday: ~datetime.datetime
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
        'birthday': {'required': True},
    }

    _attribute_map = {
        'fishtype': {'key': 'fishtype', 'type': 'str'},
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
        'age': {'key': 'age', 'type': 'int'},
        'birthday': {'key': 'birthday', 'type': 'iso-8601'},
    }

    _subtype_map = {
        'fishtype': {'cookiecuttershark': 'Cookiecuttershark', 'goblin': 'Goblinshark', 'sawshark': 'Sawshark'}
    }

    def __init__(self, *, length: float, birthday: datetime.datetime, species: str=None, siblings: List["Fish"]=None, age: int=None, **kwargs) -> None:
        super(Shark, self).__init__(species=species, length=length, siblings=siblings, **kwargs)
        self.fishtype = 'shark'
        self.age = age
        self.birthday = birthday


class Cookiecuttershark(Shark):
    """Cookiecuttershark.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param age:
    :type age: int
    :param birthday: Required.
    :type birthday: ~datetime.datetime
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
        'birthday': {'required': True},
    }

    _attribute_map = {
        'fishtype': {'key': 'fishtype', 'type': 'str'},
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
        'age': {'key': 'age', 'type': 'int'},
        'birthday': {'key': 'birthday', 'type': 'iso-8601'},
    }

    def __init__(self, *, length: float, birthday: datetime.datetime, species: str=None, siblings: List["Fish"]=None, age: int=None, **kwargs) -> None:
        super(Cookiecuttershark, self).__init__(species=species, length=length, siblings=siblings, age=age, birthday=birthday, **kwargs)
        self.fishtype = 'cookiecuttershark'


class Datetimerfc1123Wrapper(Model):
    """Datetimerfc1123Wrapper.

    :param field:
    :type field: ~datetime.datetime
    :param now:
    :type now: ~datetime.datetime
    """

    _attribute_map = {
        'field': {'key': 'field', 'type': 'rfc-1123'},
        'now': {'key': 'now', 'type': 'rfc-1123'},
    }

    def __init__(self, *, field: datetime.datetime=None, now: datetime.datetime=None, **kwargs) -> None:
        super(Datetimerfc1123Wrapper, self).__init__(**kwargs)
        self.field = field
        self.now = now


class DatetimeWrapper(Model):
    """DatetimeWrapper.

    :param field:
    :type field: ~datetime.datetime
    :param now:
    :type now: ~datetime.datetime
    """

    _attribute_map = {
        'field': {'key': 'field', 'type': 'iso-8601'},
        'now': {'key': 'now', 'type': 'iso-8601'},
    }

    def __init__(self, *, field: datetime.datetime=None, now: datetime.datetime=None, **kwargs) -> None:
        super(DatetimeWrapper, self).__init__(**kwargs)
        self.field = field
        self.now = now


class DateWrapper(Model):
    """DateWrapper.

    :param field:
    :type field: ~datetime.date
    :param leap:
    :type leap: ~datetime.date
    """

    _attribute_map = {
        'field': {'key': 'field', 'type': 'date'},
        'leap': {'key': 'leap', 'type': 'date'},
    }

    def __init__(self, *, field: datetime.date=None, leap: datetime.date=None, **kwargs) -> None:
        super(DateWrapper, self).__init__(**kwargs)
        self.field = field
        self.leap = leap


class DictionaryWrapper(Model):
    """DictionaryWrapper.

    :param default_program: Dictionary of
	 <components·schemas·dictionary_wrapper·properties·defaultprogram·additionalproperties>.
    :type default_program: dict[str, str]
    """

    _attribute_map = {
        'default_program': {'key': 'defaultProgram', 'type': '{str}'},
    }

    def __init__(self, *, default_program: Dict[str, str]=None, **kwargs) -> None:
        super(DictionaryWrapper, self).__init__(**kwargs)
        self.default_program = default_program


class Dog(Pet):
    """Dog.

    :param id:
    :type id: int
    :param name:
    :type name: str
    :param food:
    :type food: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'food': {'key': 'food', 'type': 'str'},
    }

    def __init__(self, *, id: int=None, name: str=None, food: str=None, **kwargs) -> None:
        super(Dog, self).__init__(id=id, name=name, **kwargs)
        self.food = food


class DotFish(Model):
    """DotFish.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: DotSalmon.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    """

    _validation = {
        'fishtype': {'required': True},
    }

    _attribute_map = {
        'fishtype': {'key': 'fish\\.type', 'type': 'str'},
        'species': {'key': 'species', 'type': 'str'},
    }

    _subtype_map = {
        'fishtype': {'DotSalmon': 'DotSalmon'}
    }

    def __init__(self, *, species: str=None, **kwargs) -> None:
        super(DotFish, self).__init__(**kwargs)
        self.fishtype = 'None'
        self.species = species


class DotFishMarket(Model):
    """DotFishMarket.

    :param sample_salmon:
    :type sample_salmon: ~bodycomplex.models.DotSalmon
    :param salmons:
    :type salmons: list[~bodycomplex.models.DotSalmon]
    :param sample_fish:
    :type sample_fish: ~bodycomplex.models.DotFish
    :param fishes:
    :type fishes: list[~bodycomplex.models.DotFish]
    """

    _attribute_map = {
        'sample_salmon': {'key': 'sampleSalmon', 'type': 'DotSalmon'},
        'salmons': {'key': 'salmons', 'type': '[DotSalmon]'},
        'sample_fish': {'key': 'sampleFish', 'type': 'DotFish'},
        'fishes': {'key': 'fishes', 'type': '[DotFish]'},
    }

    def __init__(self, *, sample_salmon: "DotSalmon"=None, salmons: List["DotSalmon"]=None, sample_fish: "DotFish"=None, fishes: List["DotFish"]=None, **kwargs) -> None:
        super(DotFishMarket, self).__init__(**kwargs)
        self.sample_salmon = sample_salmon
        self.salmons = salmons
        self.sample_fish = sample_fish
        self.fishes = fishes


class DotSalmon(DotFish):
    """DotSalmon.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param location:
    :type location: str
    :param iswild:
    :type iswild: bool
    """

    _validation = {
        'fishtype': {'required': True},
    }

    _attribute_map = {
        'fishtype': {'key': 'fish\\.type', 'type': 'str'},
        'species': {'key': 'species', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'iswild': {'key': 'iswild', 'type': 'bool'},
    }

    def __init__(self, *, species: str=None, location: str=None, iswild: bool=None, **kwargs) -> None:
        super(DotSalmon, self).__init__(species=species, **kwargs)
        self.fishtype = 'DotSalmon'
        self.location = location
        self.iswild = iswild


class DoubleWrapper(Model):
    """DoubleWrapper.

    :param field1:
    :type field1: float
    :param
	 field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose:
    :type
	 field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose:
	 float
    """

    _attribute_map = {
        'field1': {'key': 'field1', 'type': 'float'},
        'field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose': {'key': 'field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose', 'type': 'float'},
    }

    def __init__(self, *, field1: float=None, field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose: float=None, **kwargs) -> None:
        super(DoubleWrapper, self).__init__(**kwargs)
        self.field1 = field1
        self.field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose = field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose


class DurationWrapper(Model):
    """DurationWrapper.

    :param field:
    :type field: ~datetime.timedelta
    """

    _attribute_map = {
        'field': {'key': 'field', 'type': 'duration'},
    }

    def __init__(self, *, field: datetime.timedelta=None, **kwargs) -> None:
        super(DurationWrapper, self).__init__(**kwargs)
        self.field = field


class ErrorException(HttpResponseError):
    """Server responded with exception of type: 'Error'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(ErrorException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'Error'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class Error(Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """
    _EXCEPTION_TYPE = ErrorException

    _attribute_map = {
        'status': {'key': 'status', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, status: int=None, message: str=None, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class FloatWrapper(Model):
    """FloatWrapper.

    :param field1:
    :type field1: float
    :param field2:
    :type field2: float
    """

    _attribute_map = {
        'field1': {'key': 'field1', 'type': 'float'},
        'field2': {'key': 'field2', 'type': 'float'},
    }

    def __init__(self, *, field1: float=None, field2: float=None, **kwargs) -> None:
        super(FloatWrapper, self).__init__(**kwargs)
        self.field1 = field1
        self.field2 = field2


class Goblinshark(Shark):
    """Goblinshark.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param age:
    :type age: int
    :param birthday: Required.
    :type birthday: ~datetime.datetime
    :param jawsize:
    :type jawsize: int
    :param color: Colors possible. Possible values include: 'pink', 'gray', 'brown',
	 'RED'. Default value: "gray".
    :type color: str or ~bodycomplex.models.GoblinSharkColor
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
        'birthday': {'required': True},
    }

    _attribute_map = {
        'fishtype': {'key': 'fishtype', 'type': 'str'},
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
        'age': {'key': 'age', 'type': 'int'},
        'birthday': {'key': 'birthday', 'type': 'iso-8601'},
        'jawsize': {'key': 'jawsize', 'type': 'int'},
        'color': {'key': 'color', 'type': 'str'},
    }

    def __init__(self, *, length: float, birthday: datetime.datetime, species: str=None, siblings: List["Fish"]=None, age: int=None, jawsize: int=None, color: Union[str, "GoblinSharkColor"]="gray", **kwargs) -> None:
        super(Goblinshark, self).__init__(species=species, length=length, siblings=siblings, age=age, birthday=birthday, **kwargs)
        self.fishtype = 'goblin'
        self.jawsize = jawsize
        self.color = color


class IntWrapper(Model):
    """IntWrapper.

    :param field1:
    :type field1: int
    :param field2:
    :type field2: int
    """

    _attribute_map = {
        'field1': {'key': 'field1', 'type': 'int'},
        'field2': {'key': 'field2', 'type': 'int'},
    }

    def __init__(self, *, field1: int=None, field2: int=None, **kwargs) -> None:
        super(IntWrapper, self).__init__(**kwargs)
        self.field1 = field1
        self.field2 = field2


class LongWrapper(Model):
    """LongWrapper.

    :param field1:
    :type field1: long
    :param field2:
    :type field2: long
    """

    _attribute_map = {
        'field1': {'key': 'field1', 'type': 'long'},
        'field2': {'key': 'field2', 'type': 'long'},
    }

    def __init__(self, *, field1: int=None, field2: int=None, **kwargs) -> None:
        super(LongWrapper, self).__init__(**kwargs)
        self.field1 = field1
        self.field2 = field2


class MyBaseHelperType(Model):
    """MyBaseHelperType.

    :param prop_bh1:
    :type prop_bh1: str
    """

    _attribute_map = {
        'prop_bh1': {'key': 'propBH1', 'type': 'str'},
    }

    def __init__(self, *, prop_bh1: str=None, **kwargs) -> None:
        super(MyBaseHelperType, self).__init__(**kwargs)
        self.prop_bh1 = prop_bh1


class MyBaseType(Model):
    """MyBaseType.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: MyDerivedType.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    :param prop_b1:
    :type prop_b1: str
    :param helper:
    :type helper: ~bodycomplex.models.MyBaseHelperType
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'prop_b1': {'key': 'propB1', 'type': 'str'},
        'helper': {'key': 'helper', 'type': 'MyBaseHelperType'},
    }

    _subtype_map = {
        'kind': {'Kind1': 'MyDerivedType'}
    }

    def __init__(self, *, prop_b1: str=None, helper: "MyBaseHelperType"=None, **kwargs) -> None:
        super(MyBaseType, self).__init__(**kwargs)
        self.kind = 'None'
        self.prop_b1 = prop_b1
        self.helper = helper


class MyDerivedType(MyBaseType):
    """MyDerivedType.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    :param prop_b1:
    :type prop_b1: str
    :param helper:
    :type helper: ~bodycomplex.models.MyBaseHelperType
    :param prop_d1:
    :type prop_d1: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'prop_b1': {'key': 'propB1', 'type': 'str'},
        'helper': {'key': 'helper', 'type': 'MyBaseHelperType'},
        'prop_d1': {'key': 'propD1', 'type': 'str'},
    }

    def __init__(self, *, prop_b1: str=None, helper: "MyBaseHelperType"=None, prop_d1: str=None, **kwargs) -> None:
        super(MyDerivedType, self).__init__(prop_b1=prop_b1, helper=helper, **kwargs)
        self.kind = 'Kind1'
        self.prop_d1 = prop_d1


class ReadonlyObj(Model):
    """ReadonlyObj.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id:
    :vartype id: str
    :param size:
    :type size: int
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'size': {'key': 'size', 'type': 'int'},
    }

    def __init__(self, *, size: int=None, **kwargs) -> None:
        super(ReadonlyObj, self).__init__(**kwargs)
        self.id = None
        self.size = size


class Salmon(Fish):
    """Salmon.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: SmartSalmon.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param location:
    :type location: str
    :param iswild:
    :type iswild: bool
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
    }

    _attribute_map = {
        'fishtype': {'key': 'fishtype', 'type': 'str'},
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
        'location': {'key': 'location', 'type': 'str'},
        'iswild': {'key': 'iswild', 'type': 'bool'},
    }

    _subtype_map = {
        'fishtype': {'smart_salmon': 'SmartSalmon'}
    }

    def __init__(self, *, length: float, species: str=None, siblings: List["Fish"]=None, location: str=None, iswild: bool=None, **kwargs) -> None:
        super(Salmon, self).__init__(species=species, length=length, siblings=siblings, **kwargs)
        self.fishtype = 'salmon'
        self.location = location
        self.iswild = iswild


class Sawshark(Shark):
    """Sawshark.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param age:
    :type age: int
    :param birthday: Required.
    :type birthday: ~datetime.datetime
    :param picture:
    :type picture: bytearray
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
        'birthday': {'required': True},
    }

    _attribute_map = {
        'fishtype': {'key': 'fishtype', 'type': 'str'},
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
        'age': {'key': 'age', 'type': 'int'},
        'birthday': {'key': 'birthday', 'type': 'iso-8601'},
        'picture': {'key': 'picture', 'type': 'bytearray'},
    }

    def __init__(self, *, length: float, birthday: datetime.datetime, species: str=None, siblings: List["Fish"]=None, age: int=None, picture: bytearray=None, **kwargs) -> None:
        super(Sawshark, self).__init__(species=species, length=length, siblings=siblings, age=age, birthday=birthday, **kwargs)
        self.fishtype = 'sawshark'
        self.picture = picture


class Siamese(Cat):
    """Siamese.

    :param id:
    :type id: int
    :param name:
    :type name: str
    :param color:
    :type color: str
    :param hates:
    :type hates: list[~bodycomplex.models.Dog]
    :param breed:
    :type breed: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'color': {'key': 'color', 'type': 'str'},
        'hates': {'key': 'hates', 'type': '[Dog]'},
        'breed': {'key': 'breed', 'type': 'str'},
    }

    def __init__(self, *, id: int=None, name: str=None, color: str=None, hates: List["Dog"]=None, breed: str=None, **kwargs) -> None:
        super(Siamese, self).__init__(id=id, name=name, color=color, hates=hates, **kwargs)
        self.breed = breed


class SmartSalmon(Salmon):
    """SmartSalmon.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param location:
    :type location: str
    :param iswild:
    :type iswild: bool
    :param additional_properties: Unmatched properties from the message are
	 deserialized to this collection.
    :type additional_properties: dict[str, object]
    :param college_degree:
    :type college_degree: str
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
    }

    _attribute_map = {
        'fishtype': {'key': 'fishtype', 'type': 'str'},
        'species': {'key': 'species', 'type': 'str'},
        'length': {'key': 'length', 'type': 'float'},
        'siblings': {'key': 'siblings', 'type': '[Fish]'},
        'location': {'key': 'location', 'type': 'str'},
        'iswild': {'key': 'iswild', 'type': 'bool'},
        'additional_properties': {'key': '', 'type': '{object}'},
        'college_degree': {'key': 'college_degree', 'type': 'str'},
    }

    def __init__(self, *, length: float, species: str=None, siblings: List["Fish"]=None, location: str=None, iswild: bool=None, additional_properties: Dict[str, object]=None, college_degree: str=None, **kwargs) -> None:
        super(SmartSalmon, self).__init__(species=species, length=length, siblings=siblings, location=location, iswild=iswild, **kwargs)
        self.fishtype = 'smart_salmon'
        self.additional_properties = additional_properties
        self.college_degree = college_degree


class StringWrapper(Model):
    """StringWrapper.

    :param field:
    :type field: str
    :param empty:
    :type empty: str
    :param null:
    :type null: str
    """

    _attribute_map = {
        'field': {'key': 'field', 'type': 'str'},
        'empty': {'key': 'empty', 'type': 'str'},
        'null': {'key': 'null', 'type': 'str'},
    }

    def __init__(self, *, field: str=None, empty: str=None, null: str=None, **kwargs) -> None:
        super(StringWrapper, self).__init__(**kwargs)
        self.field = field
        self.empty = empty
        self.null = null
