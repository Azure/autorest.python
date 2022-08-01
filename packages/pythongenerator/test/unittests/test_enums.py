# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)

class EnumsWithCallableNames(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the unit of measurement.
    """

    COUNT = "count"
    ENCODE = "encode"
    FIND = "find"
    JOIN = "join"

def test_count():
    assert EnumsWithCallableNames.COUNT == "count"
    assert callable(EnumsWithCallableNames.count)

def test_encode():
    assert EnumsWithCallableNames.ENCODE == "encode"
    assert callable(EnumsWithCallableNames.encode)

def test_find():
    assert EnumsWithCallableNames.FIND == "find"
    assert callable(EnumsWithCallableNames.find)

def test_join():
    assert EnumsWithCallableNames.JOIN == "join"
    assert callable(EnumsWithCallableNames.join)