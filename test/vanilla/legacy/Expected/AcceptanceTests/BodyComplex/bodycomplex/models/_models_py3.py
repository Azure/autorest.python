# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

import msrest.serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ArrayWrapper(msrest.serialization.Model):
    """ArrayWrapper.

    :ivar array:
    :vartype array: list[str]
    """

    _attribute_map = {
        "array": {"key": "array", "type": "[str]"},
    }

    def __init__(
        self,
        *,
        array: Optional[List[str]] = None,
        **kwargs
    ):
        """
        :keyword array:
        :paramtype array: list[str]
        """
        super().__init__(**kwargs)
        self.array = array


class Basic(msrest.serialization.Model):
    """Basic.

    :ivar id: Basic Id.
    :vartype id: int
    :ivar name: Name property with a very long description that does not fit on a single line and a
     line break.
    :vartype name: str
    :ivar color: Known values are: "cyan", "Magenta", "YELLOW", and "blacK".
    :vartype color: str or ~bodycomplex.models.CMYKColors
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "color": {"key": "color", "type": "str"},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,  # pylint: disable=redefined-builtin
        name: Optional[str] = None,
        color: Optional[Union[str, "_models.CMYKColors"]] = None,
        **kwargs
    ):
        """
        :keyword id: Basic Id.
        :paramtype id: int
        :keyword name: Name property with a very long description that does not fit on a single line
         and a line break.
        :paramtype name: str
        :keyword color: Known values are: "cyan", "Magenta", "YELLOW", and "blacK".
        :paramtype color: str or ~bodycomplex.models.CMYKColors
        """
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.color = color


class BooleanWrapper(msrest.serialization.Model):
    """BooleanWrapper.

    :ivar field_true:
    :vartype field_true: bool
    :ivar field_false:
    :vartype field_false: bool
    """

    _attribute_map = {
        "field_true": {"key": "field_true", "type": "bool"},
        "field_false": {"key": "field_false", "type": "bool"},
    }

    def __init__(
        self,
        *,
        field_true: Optional[bool] = None,
        field_false: Optional[bool] = None,
        **kwargs
    ):
        """
        :keyword field_true:
        :paramtype field_true: bool
        :keyword field_false:
        :paramtype field_false: bool
        """
        super().__init__(**kwargs)
        self.field_true = field_true
        self.field_false = field_false


class ByteWrapper(msrest.serialization.Model):
    """ByteWrapper.

    :ivar field:
    :vartype field: bytes
    """

    _attribute_map = {
        "field": {"key": "field", "type": "bytearray"},
    }

    def __init__(
        self,
        *,
        field: Optional[bytes] = None,
        **kwargs
    ):
        """
        :keyword field:
        :paramtype field: bytes
        """
        super().__init__(**kwargs)
        self.field = field


class Pet(msrest.serialization.Model):
    """Pet.

    :ivar id:
    :vartype id: int
    :ivar name:
    :vartype name: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,  # pylint: disable=redefined-builtin
        name: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword id:
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        """
        super().__init__(**kwargs)
        self.id = id
        self.name = name


class Cat(Pet):
    """Cat.

    :ivar id:
    :vartype id: int
    :ivar name:
    :vartype name: str
    :ivar color:
    :vartype color: str
    :ivar hates:
    :vartype hates: list[~bodycomplex.models.Dog]
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "color": {"key": "color", "type": "str"},
        "hates": {"key": "hates", "type": "[Dog]"},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,  # pylint: disable=redefined-builtin
        name: Optional[str] = None,
        color: Optional[str] = None,
        hates: Optional[List["_models.Dog"]] = None,
        **kwargs
    ):
        """
        :keyword id:
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        :keyword color:
        :paramtype color: str
        :keyword hates:
        :paramtype hates: list[~bodycomplex.models.Dog]
        """
        super().__init__(id=id, name=name, **kwargs)
        self.color = color
        self.hates = hates


class Fish(msrest.serialization.Model):
    """Fish.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    Salmon, Shark

    All required parameters must be populated in order to send to Azure.

    :ivar fishtype: Required.
    :vartype fishtype: str
    :ivar species:
    :vartype species: str
    :ivar length: Required.
    :vartype length: float
    :ivar siblings:
    :vartype siblings: list[~bodycomplex.models.Fish]
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
    }

    _subtype_map = {
        'fishtype': {'salmon': 'Salmon', 'shark': 'Shark'}
    }

    def __init__(
        self,
        *,
        length: float,
        species: Optional[str] = None,
        siblings: Optional[List["_models.Fish"]] = None,
        **kwargs
    ):
        """
        :keyword species:
        :paramtype species: str
        :keyword length: Required.
        :paramtype length: float
        :keyword siblings:
        :paramtype siblings: list[~bodycomplex.models.Fish]
        """
        super().__init__(**kwargs)
        self.fishtype = None  # type: Optional[str]
        self.species = species
        self.length = length
        self.siblings = siblings


class Shark(Fish):
    """Shark.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    Cookiecuttershark, Goblinshark, Sawshark

    All required parameters must be populated in order to send to Azure.

    :ivar fishtype: Required.
    :vartype fishtype: str
    :ivar species:
    :vartype species: str
    :ivar length: Required.
    :vartype length: float
    :ivar siblings:
    :vartype siblings: list[~bodycomplex.models.Fish]
    :ivar age:
    :vartype age: int
    :ivar birthday: Required.
    :vartype birthday: ~datetime.datetime
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
        'birthday': {'required': True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "age": {"key": "age", "type": "int"},
        "birthday": {"key": "birthday", "type": "iso-8601"},
    }

    _subtype_map = {
        'fishtype': {'cookiecuttershark': 'Cookiecuttershark', 'goblin': 'Goblinshark', 'sawshark': 'Sawshark'}
    }

    def __init__(
        self,
        *,
        length: float,
        birthday: datetime.datetime,
        species: Optional[str] = None,
        siblings: Optional[List["_models.Fish"]] = None,
        age: Optional[int] = None,
        **kwargs
    ):
        """
        :keyword species:
        :paramtype species: str
        :keyword length: Required.
        :paramtype length: float
        :keyword siblings:
        :paramtype siblings: list[~bodycomplex.models.Fish]
        :keyword age:
        :paramtype age: int
        :keyword birthday: Required.
        :paramtype birthday: ~datetime.datetime
        """
        super().__init__(species=species, length=length, siblings=siblings, **kwargs)
        self.fishtype = 'shark'  # type: str
        self.age = age
        self.birthday = birthday


class Cookiecuttershark(Shark):
    """Cookiecuttershark.

    All required parameters must be populated in order to send to Azure.

    :ivar fishtype: Required.
    :vartype fishtype: str
    :ivar species:
    :vartype species: str
    :ivar length: Required.
    :vartype length: float
    :ivar siblings:
    :vartype siblings: list[~bodycomplex.models.Fish]
    :ivar age:
    :vartype age: int
    :ivar birthday: Required.
    :vartype birthday: ~datetime.datetime
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
        'birthday': {'required': True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "age": {"key": "age", "type": "int"},
        "birthday": {"key": "birthday", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        length: float,
        birthday: datetime.datetime,
        species: Optional[str] = None,
        siblings: Optional[List["_models.Fish"]] = None,
        age: Optional[int] = None,
        **kwargs
    ):
        """
        :keyword species:
        :paramtype species: str
        :keyword length: Required.
        :paramtype length: float
        :keyword siblings:
        :paramtype siblings: list[~bodycomplex.models.Fish]
        :keyword age:
        :paramtype age: int
        :keyword birthday: Required.
        :paramtype birthday: ~datetime.datetime
        """
        super().__init__(species=species, length=length, siblings=siblings, age=age, birthday=birthday, **kwargs)
        self.fishtype = 'cookiecuttershark'  # type: str


class Datetimerfc1123Wrapper(msrest.serialization.Model):
    """Datetimerfc1123Wrapper.

    :ivar field:
    :vartype field: ~datetime.datetime
    :ivar now:
    :vartype now: ~datetime.datetime
    """

    _attribute_map = {
        "field": {"key": "field", "type": "rfc-1123"},
        "now": {"key": "now", "type": "rfc-1123"},
    }

    def __init__(
        self,
        *,
        field: Optional[datetime.datetime] = None,
        now: Optional[datetime.datetime] = None,
        **kwargs
    ):
        """
        :keyword field:
        :paramtype field: ~datetime.datetime
        :keyword now:
        :paramtype now: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.field = field
        self.now = now


class DatetimeWrapper(msrest.serialization.Model):
    """DatetimeWrapper.

    :ivar field:
    :vartype field: ~datetime.datetime
    :ivar now:
    :vartype now: ~datetime.datetime
    """

    _attribute_map = {
        "field": {"key": "field", "type": "iso-8601"},
        "now": {"key": "now", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        field: Optional[datetime.datetime] = None,
        now: Optional[datetime.datetime] = None,
        **kwargs
    ):
        """
        :keyword field:
        :paramtype field: ~datetime.datetime
        :keyword now:
        :paramtype now: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.field = field
        self.now = now


class DateWrapper(msrest.serialization.Model):
    """DateWrapper.

    :ivar field:
    :vartype field: ~datetime.date
    :ivar leap:
    :vartype leap: ~datetime.date
    """

    _attribute_map = {
        "field": {"key": "field", "type": "date"},
        "leap": {"key": "leap", "type": "date"},
    }

    def __init__(
        self,
        *,
        field: Optional[datetime.date] = None,
        leap: Optional[datetime.date] = None,
        **kwargs
    ):
        """
        :keyword field:
        :paramtype field: ~datetime.date
        :keyword leap:
        :paramtype leap: ~datetime.date
        """
        super().__init__(**kwargs)
        self.field = field
        self.leap = leap


class DictionaryWrapper(msrest.serialization.Model):
    """DictionaryWrapper.

    :ivar default_program: Dictionary of :code:`<string>`.
    :vartype default_program: dict[str, str]
    """

    _attribute_map = {
        "default_program": {"key": "defaultProgram", "type": "{str}"},
    }

    def __init__(
        self,
        *,
        default_program: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword default_program: Dictionary of :code:`<string>`.
        :paramtype default_program: dict[str, str]
        """
        super().__init__(**kwargs)
        self.default_program = default_program


class Dog(Pet):
    """Dog.

    :ivar id:
    :vartype id: int
    :ivar name:
    :vartype name: str
    :ivar food:
    :vartype food: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "food": {"key": "food", "type": "str"},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,  # pylint: disable=redefined-builtin
        name: Optional[str] = None,
        food: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword id:
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        :keyword food:
        :paramtype food: str
        """
        super().__init__(id=id, name=name, **kwargs)
        self.food = food


class DotFish(msrest.serialization.Model):
    """DotFish.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    DotSalmon

    All required parameters must be populated in order to send to Azure.

    :ivar fish_type: Required.
    :vartype fish_type: str
    :ivar species:
    :vartype species: str
    """

    _validation = {
        'fish_type': {'required': True},
    }

    _attribute_map = {
        "fish_type": {"key": "fish\\.type", "type": "str"},
        "species": {"key": "species", "type": "str"},
    }

    _subtype_map = {
        'fish_type': {'DotSalmon': 'DotSalmon'}
    }

    def __init__(
        self,
        *,
        species: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword species:
        :paramtype species: str
        """
        super().__init__(**kwargs)
        self.fish_type = None  # type: Optional[str]
        self.species = species


class DotFishMarket(msrest.serialization.Model):
    """DotFishMarket.

    :ivar sample_salmon:
    :vartype sample_salmon: ~bodycomplex.models.DotSalmon
    :ivar salmons:
    :vartype salmons: list[~bodycomplex.models.DotSalmon]
    :ivar sample_fish:
    :vartype sample_fish: ~bodycomplex.models.DotFish
    :ivar fishes:
    :vartype fishes: list[~bodycomplex.models.DotFish]
    """

    _attribute_map = {
        "sample_salmon": {"key": "sampleSalmon", "type": "DotSalmon"},
        "salmons": {"key": "salmons", "type": "[DotSalmon]"},
        "sample_fish": {"key": "sampleFish", "type": "DotFish"},
        "fishes": {"key": "fishes", "type": "[DotFish]"},
    }

    def __init__(
        self,
        *,
        sample_salmon: Optional["_models.DotSalmon"] = None,
        salmons: Optional[List["_models.DotSalmon"]] = None,
        sample_fish: Optional["_models.DotFish"] = None,
        fishes: Optional[List["_models.DotFish"]] = None,
        **kwargs
    ):
        """
        :keyword sample_salmon:
        :paramtype sample_salmon: ~bodycomplex.models.DotSalmon
        :keyword salmons:
        :paramtype salmons: list[~bodycomplex.models.DotSalmon]
        :keyword sample_fish:
        :paramtype sample_fish: ~bodycomplex.models.DotFish
        :keyword fishes:
        :paramtype fishes: list[~bodycomplex.models.DotFish]
        """
        super().__init__(**kwargs)
        self.sample_salmon = sample_salmon
        self.salmons = salmons
        self.sample_fish = sample_fish
        self.fishes = fishes


class DotSalmon(DotFish):
    """DotSalmon.

    All required parameters must be populated in order to send to Azure.

    :ivar fish_type: Required.
    :vartype fish_type: str
    :ivar species:
    :vartype species: str
    :ivar location:
    :vartype location: str
    :ivar iswild:
    :vartype iswild: bool
    """

    _validation = {
        'fish_type': {'required': True},
    }

    _attribute_map = {
        "fish_type": {"key": "fish\\.type", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "iswild": {"key": "iswild", "type": "bool"},
    }

    def __init__(
        self,
        *,
        species: Optional[str] = None,
        location: Optional[str] = None,
        iswild: Optional[bool] = None,
        **kwargs
    ):
        """
        :keyword species:
        :paramtype species: str
        :keyword location:
        :paramtype location: str
        :keyword iswild:
        :paramtype iswild: bool
        """
        super().__init__(species=species, **kwargs)
        self.fish_type = 'DotSalmon'  # type: str
        self.location = location
        self.iswild = iswild


class DoubleWrapper(msrest.serialization.Model):
    """DoubleWrapper.

    :ivar field1:
    :vartype field1: float
    :ivar
     field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose:
    :vartype
     field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose:
     float
    """

    _attribute_map = {
        "field1": {"key": "field1", "type": "float"},
        "field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose": {"key": "field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose", "type": "float"},
    }

    def __init__(
        self,
        *,
        field1: Optional[float] = None,
        field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose: Optional[float] = None,
        **kwargs
    ):
        """
        :keyword field1:
        :paramtype field1: float
        :keyword
         field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose:
        :paramtype
         field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose:
         float
        """
        super().__init__(**kwargs)
        self.field1 = field1
        self.field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose = field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose


class DurationWrapper(msrest.serialization.Model):
    """DurationWrapper.

    :ivar field:
    :vartype field: ~datetime.timedelta
    """

    _attribute_map = {
        "field": {"key": "field", "type": "duration"},
    }

    def __init__(
        self,
        *,
        field: Optional[datetime.timedelta] = None,
        **kwargs
    ):
        """
        :keyword field:
        :paramtype field: ~datetime.timedelta
        """
        super().__init__(**kwargs)
        self.field = field


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

    def __init__(
        self,
        *,
        status: Optional[int] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.status = status
        self.message = message


class FloatWrapper(msrest.serialization.Model):
    """FloatWrapper.

    :ivar field1:
    :vartype field1: float
    :ivar field2:
    :vartype field2: float
    """

    _attribute_map = {
        "field1": {"key": "field1", "type": "float"},
        "field2": {"key": "field2", "type": "float"},
    }

    def __init__(
        self,
        *,
        field1: Optional[float] = None,
        field2: Optional[float] = None,
        **kwargs
    ):
        """
        :keyword field1:
        :paramtype field1: float
        :keyword field2:
        :paramtype field2: float
        """
        super().__init__(**kwargs)
        self.field1 = field1
        self.field2 = field2


class Goblinshark(Shark):
    """Goblinshark.

    All required parameters must be populated in order to send to Azure.

    :ivar fishtype: Required.
    :vartype fishtype: str
    :ivar species:
    :vartype species: str
    :ivar length: Required.
    :vartype length: float
    :ivar siblings:
    :vartype siblings: list[~bodycomplex.models.Fish]
    :ivar age:
    :vartype age: int
    :ivar birthday: Required.
    :vartype birthday: ~datetime.datetime
    :ivar jawsize:
    :vartype jawsize: int
    :ivar color: Colors possible. Known values are: "pink", "gray", "brown", "RED", and "red".
    :vartype color: str or ~bodycomplex.models.GoblinSharkColor
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
        'birthday': {'required': True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "age": {"key": "age", "type": "int"},
        "birthday": {"key": "birthday", "type": "iso-8601"},
        "jawsize": {"key": "jawsize", "type": "int"},
        "color": {"key": "color", "type": "str"},
    }

    def __init__(
        self,
        *,
        length: float,
        birthday: datetime.datetime,
        species: Optional[str] = None,
        siblings: Optional[List["_models.Fish"]] = None,
        age: Optional[int] = None,
        jawsize: Optional[int] = None,
        color: Union[str, "_models.GoblinSharkColor"] = "gray",
        **kwargs
    ):
        """
        :keyword species:
        :paramtype species: str
        :keyword length: Required.
        :paramtype length: float
        :keyword siblings:
        :paramtype siblings: list[~bodycomplex.models.Fish]
        :keyword age:
        :paramtype age: int
        :keyword birthday: Required.
        :paramtype birthday: ~datetime.datetime
        :keyword jawsize:
        :paramtype jawsize: int
        :keyword color: Colors possible. Known values are: "pink", "gray", "brown", "RED", and "red".
        :paramtype color: str or ~bodycomplex.models.GoblinSharkColor
        """
        super().__init__(species=species, length=length, siblings=siblings, age=age, birthday=birthday, **kwargs)
        self.fishtype = 'goblin'  # type: str
        self.jawsize = jawsize
        self.color = color


class IntWrapper(msrest.serialization.Model):
    """IntWrapper.

    :ivar field1:
    :vartype field1: int
    :ivar field2:
    :vartype field2: int
    """

    _attribute_map = {
        "field1": {"key": "field1", "type": "int"},
        "field2": {"key": "field2", "type": "int"},
    }

    def __init__(
        self,
        *,
        field1: Optional[int] = None,
        field2: Optional[int] = None,
        **kwargs
    ):
        """
        :keyword field1:
        :paramtype field1: int
        :keyword field2:
        :paramtype field2: int
        """
        super().__init__(**kwargs)
        self.field1 = field1
        self.field2 = field2


class LongWrapper(msrest.serialization.Model):
    """LongWrapper.

    :ivar field1:
    :vartype field1: int
    :ivar field2:
    :vartype field2: int
    """

    _attribute_map = {
        "field1": {"key": "field1", "type": "int"},
        "field2": {"key": "field2", "type": "int"},
    }

    def __init__(
        self,
        *,
        field1: Optional[int] = None,
        field2: Optional[int] = None,
        **kwargs
    ):
        """
        :keyword field1:
        :paramtype field1: int
        :keyword field2:
        :paramtype field2: int
        """
        super().__init__(**kwargs)
        self.field1 = field1
        self.field2 = field2


class MyBaseType(msrest.serialization.Model):
    """MyBaseType.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    MyDerivedType

    All required parameters must be populated in order to send to Azure.

    :ivar kind: Required. "Kind1"
    :vartype kind: str or ~bodycomplex.models.MyKind
    :ivar prop_b1:
    :vartype prop_b1: str
    :ivar prop_bh1:
    :vartype prop_bh1: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        "kind": {"key": "kind", "type": "str"},
        "prop_b1": {"key": "propB1", "type": "str"},
        "prop_bh1": {"key": "helper.propBH1", "type": "str"},
    }

    _subtype_map = {
        'kind': {'Kind1': 'MyDerivedType'}
    }

    def __init__(
        self,
        *,
        prop_b1: Optional[str] = None,
        prop_bh1: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword prop_b1:
        :paramtype prop_b1: str
        :keyword prop_bh1:
        :paramtype prop_bh1: str
        """
        super().__init__(**kwargs)
        self.kind = None  # type: Optional[str]
        self.prop_b1 = prop_b1
        self.prop_bh1 = prop_bh1


class MyDerivedType(MyBaseType):
    """MyDerivedType.

    All required parameters must be populated in order to send to Azure.

    :ivar kind: Required. "Kind1"
    :vartype kind: str or ~bodycomplex.models.MyKind
    :ivar prop_b1:
    :vartype prop_b1: str
    :ivar prop_bh1:
    :vartype prop_bh1: str
    :ivar prop_d1:
    :vartype prop_d1: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        "kind": {"key": "kind", "type": "str"},
        "prop_b1": {"key": "propB1", "type": "str"},
        "prop_bh1": {"key": "helper.propBH1", "type": "str"},
        "prop_d1": {"key": "propD1", "type": "str"},
    }

    def __init__(
        self,
        *,
        prop_b1: Optional[str] = None,
        prop_bh1: Optional[str] = None,
        prop_d1: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword prop_b1:
        :paramtype prop_b1: str
        :keyword prop_bh1:
        :paramtype prop_bh1: str
        :keyword prop_d1:
        :paramtype prop_d1: str
        """
        super().__init__(prop_b1=prop_b1, prop_bh1=prop_bh1, **kwargs)
        self.kind = 'Kind1'  # type: str
        self.prop_d1 = prop_d1


class ReadonlyObj(msrest.serialization.Model):
    """ReadonlyObj.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id:
    :vartype id: str
    :ivar size:
    :vartype size: int
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "size": {"key": "size", "type": "int"},
    }

    def __init__(
        self,
        *,
        size: Optional[int] = None,
        **kwargs
    ):
        """
        :keyword size:
        :paramtype size: int
        """
        super().__init__(**kwargs)
        self.id = None
        self.size = size


class Salmon(Fish):
    """Salmon.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    SmartSalmon

    All required parameters must be populated in order to send to Azure.

    :ivar fishtype: Required.
    :vartype fishtype: str
    :ivar species:
    :vartype species: str
    :ivar length: Required.
    :vartype length: float
    :ivar siblings:
    :vartype siblings: list[~bodycomplex.models.Fish]
    :ivar location:
    :vartype location: str
    :ivar iswild:
    :vartype iswild: bool
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "location": {"key": "location", "type": "str"},
        "iswild": {"key": "iswild", "type": "bool"},
    }

    _subtype_map = {
        'fishtype': {'smart_salmon': 'SmartSalmon'}
    }

    def __init__(
        self,
        *,
        length: float,
        species: Optional[str] = None,
        siblings: Optional[List["_models.Fish"]] = None,
        location: Optional[str] = None,
        iswild: Optional[bool] = None,
        **kwargs
    ):
        """
        :keyword species:
        :paramtype species: str
        :keyword length: Required.
        :paramtype length: float
        :keyword siblings:
        :paramtype siblings: list[~bodycomplex.models.Fish]
        :keyword location:
        :paramtype location: str
        :keyword iswild:
        :paramtype iswild: bool
        """
        super().__init__(species=species, length=length, siblings=siblings, **kwargs)
        self.fishtype = 'salmon'  # type: str
        self.location = location
        self.iswild = iswild


class Sawshark(Shark):
    """Sawshark.

    All required parameters must be populated in order to send to Azure.

    :ivar fishtype: Required.
    :vartype fishtype: str
    :ivar species:
    :vartype species: str
    :ivar length: Required.
    :vartype length: float
    :ivar siblings:
    :vartype siblings: list[~bodycomplex.models.Fish]
    :ivar age:
    :vartype age: int
    :ivar birthday: Required.
    :vartype birthday: ~datetime.datetime
    :ivar picture:
    :vartype picture: bytes
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
        'birthday': {'required': True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "age": {"key": "age", "type": "int"},
        "birthday": {"key": "birthday", "type": "iso-8601"},
        "picture": {"key": "picture", "type": "bytearray"},
    }

    def __init__(
        self,
        *,
        length: float,
        birthday: datetime.datetime,
        species: Optional[str] = None,
        siblings: Optional[List["_models.Fish"]] = None,
        age: Optional[int] = None,
        picture: Optional[bytes] = None,
        **kwargs
    ):
        """
        :keyword species:
        :paramtype species: str
        :keyword length: Required.
        :paramtype length: float
        :keyword siblings:
        :paramtype siblings: list[~bodycomplex.models.Fish]
        :keyword age:
        :paramtype age: int
        :keyword birthday: Required.
        :paramtype birthday: ~datetime.datetime
        :keyword picture:
        :paramtype picture: bytes
        """
        super().__init__(species=species, length=length, siblings=siblings, age=age, birthday=birthday, **kwargs)
        self.fishtype = 'sawshark'  # type: str
        self.picture = picture


class Siamese(Cat):
    """Siamese.

    :ivar id:
    :vartype id: int
    :ivar name:
    :vartype name: str
    :ivar color:
    :vartype color: str
    :ivar hates:
    :vartype hates: list[~bodycomplex.models.Dog]
    :ivar breed:
    :vartype breed: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "color": {"key": "color", "type": "str"},
        "hates": {"key": "hates", "type": "[Dog]"},
        "breed": {"key": "breed", "type": "str"},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,  # pylint: disable=redefined-builtin
        name: Optional[str] = None,
        color: Optional[str] = None,
        hates: Optional[List["_models.Dog"]] = None,
        breed: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword id:
        :paramtype id: int
        :keyword name:
        :paramtype name: str
        :keyword color:
        :paramtype color: str
        :keyword hates:
        :paramtype hates: list[~bodycomplex.models.Dog]
        :keyword breed:
        :paramtype breed: str
        """
        super().__init__(id=id, name=name, color=color, hates=hates, **kwargs)
        self.breed = breed


class SmartSalmon(Salmon):
    """SmartSalmon.

    All required parameters must be populated in order to send to Azure.

    :ivar fishtype: Required.
    :vartype fishtype: str
    :ivar species:
    :vartype species: str
    :ivar length: Required.
    :vartype length: float
    :ivar siblings:
    :vartype siblings: list[~bodycomplex.models.Fish]
    :ivar location:
    :vartype location: str
    :ivar iswild:
    :vartype iswild: bool
    :ivar additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :vartype additional_properties: dict[str, any]
    :ivar college_degree:
    :vartype college_degree: str
    """

    _validation = {
        'fishtype': {'required': True},
        'length': {'required': True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "location": {"key": "location", "type": "str"},
        "iswild": {"key": "iswild", "type": "bool"},
        "additional_properties": {"key": "", "type": "{object}"},
        "college_degree": {"key": "college_degree", "type": "str"},
    }

    def __init__(
        self,
        *,
        length: float,
        species: Optional[str] = None,
        siblings: Optional[List["_models.Fish"]] = None,
        location: Optional[str] = None,
        iswild: Optional[bool] = None,
        additional_properties: Optional[Dict[str, Any]] = None,
        college_degree: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword species:
        :paramtype species: str
        :keyword length: Required.
        :paramtype length: float
        :keyword siblings:
        :paramtype siblings: list[~bodycomplex.models.Fish]
        :keyword location:
        :paramtype location: str
        :keyword iswild:
        :paramtype iswild: bool
        :keyword additional_properties: Unmatched properties from the message are deserialized to this
         collection.
        :paramtype additional_properties: dict[str, any]
        :keyword college_degree:
        :paramtype college_degree: str
        """
        super().__init__(species=species, length=length, siblings=siblings, location=location, iswild=iswild, **kwargs)
        self.fishtype = 'smart_salmon'  # type: str
        self.additional_properties = additional_properties
        self.college_degree = college_degree


class StringWrapper(msrest.serialization.Model):
    """StringWrapper.

    :ivar field:
    :vartype field: str
    :ivar empty:
    :vartype empty: str
    :ivar null:
    :vartype null: str
    """

    _attribute_map = {
        "field": {"key": "field", "type": "str"},
        "empty": {"key": "empty", "type": "str"},
        "null": {"key": "null", "type": "str"},
    }

    def __init__(
        self,
        *,
        field: Optional[str] = None,
        empty: Optional[str] = None,
        null: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword field:
        :paramtype field: str
        :keyword empty:
        :paramtype empty: str
        :keyword null:
        :paramtype null: str
        """
        super().__init__(**kwargs)
        self.field = field
        self.empty = empty
        self.null = null
