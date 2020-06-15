# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta

class CaseInsensitiveEnumMeta(EnumMeta):
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
            raise AttributeError(name) from None


class FloatEnum(float, Enum, metaclass=CaseInsensitiveEnumMeta):
    """List of float enums
    """

    TWO_HUNDRED4 = 200.4
    FOUR_HUNDRED_THREE4 = 403.4
    FOUR_HUNDRED_FIVE3 = 405.3
    FOUR_HUNDRED_SIX2 = 406.2
    FOUR_HUNDRED_TWENTY_NINE1 = 429.1

class IntEnum(int, Enum, metaclass=CaseInsensitiveEnumMeta):
    """List of integer enums
    """

    TWO_HUNDRED = 200
    FOUR_HUNDRED_THREE = 403
    FOUR_HUNDRED_FIVE = 405
    FOUR_HUNDRED_SIX = 406
    FOUR_HUNDRED_TWENTY_NINE = 429
