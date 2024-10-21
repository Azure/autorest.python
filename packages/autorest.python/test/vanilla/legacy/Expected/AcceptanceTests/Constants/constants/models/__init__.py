# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models_py3 import (  # type: ignore
    ModelAsStringNoRequiredOneValueDefault,
    ModelAsStringNoRequiredOneValueNoDefault,
    ModelAsStringNoRequiredTwoValueDefault,
    ModelAsStringNoRequiredTwoValueNoDefault,
    ModelAsStringRequiredOneValueDefault,
    ModelAsStringRequiredOneValueNoDefault,
    ModelAsStringRequiredTwoValueDefault,
    ModelAsStringRequiredTwoValueNoDefault,
    NoModelAsStringNoRequiredOneValueDefault,
    NoModelAsStringNoRequiredOneValueNoDefault,
    NoModelAsStringNoRequiredTwoValueDefault,
    NoModelAsStringNoRequiredTwoValueNoDefault,
    NoModelAsStringRequiredOneValueDefault,
    NoModelAsStringRequiredOneValueNoDefault,
    NoModelAsStringRequiredTwoValueDefault,
    NoModelAsStringRequiredTwoValueNoDefault,
)

from ._auto_rest_swagger_constant_service_enums import (  # type: ignore
    ModelAsStringNoRequiredOneValueDefaultEnum,
    ModelAsStringNoRequiredOneValueDefaultOpEnum,
    ModelAsStringNoRequiredOneValueNoDefaultEnum,
    ModelAsStringNoRequiredOneValueNoDefaultOpEnum,
    ModelAsStringNoRequiredTwoValueDefaultEnum,
    ModelAsStringNoRequiredTwoValueDefaultOpEnum,
    ModelAsStringNoRequiredTwoValueNoDefaultEnum,
    ModelAsStringNoRequiredTwoValueNoDefaultOpEnum,
    ModelAsStringRequiredOneValueDefaultEnum,
    ModelAsStringRequiredOneValueDefaultOpEnum,
    ModelAsStringRequiredOneValueNoDefaultEnum,
    ModelAsStringRequiredOneValueNoDefaultOpEnum,
    ModelAsStringRequiredTwoValueDefaultEnum,
    ModelAsStringRequiredTwoValueDefaultOpEnum,
    ModelAsStringRequiredTwoValueNoDefaultEnum,
    ModelAsStringRequiredTwoValueNoDefaultOpEnum,
    NoModelAsStringNoRequiredTwoValueDefaultEnum,
    NoModelAsStringNoRequiredTwoValueDefaultOpEnum,
    NoModelAsStringNoRequiredTwoValueNoDefaultEnum,
    NoModelAsStringNoRequiredTwoValueNoDefaultOpEnum,
    NoModelAsStringRequiredTwoValueDefaultEnum,
    NoModelAsStringRequiredTwoValueDefaultOpEnum,
    NoModelAsStringRequiredTwoValueNoDefaultEnum,
    NoModelAsStringRequiredTwoValueNoDefaultOpEnum,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ModelAsStringNoRequiredOneValueDefault",
    "ModelAsStringNoRequiredOneValueNoDefault",
    "ModelAsStringNoRequiredTwoValueDefault",
    "ModelAsStringNoRequiredTwoValueNoDefault",
    "ModelAsStringRequiredOneValueDefault",
    "ModelAsStringRequiredOneValueNoDefault",
    "ModelAsStringRequiredTwoValueDefault",
    "ModelAsStringRequiredTwoValueNoDefault",
    "NoModelAsStringNoRequiredOneValueDefault",
    "NoModelAsStringNoRequiredOneValueNoDefault",
    "NoModelAsStringNoRequiredTwoValueDefault",
    "NoModelAsStringNoRequiredTwoValueNoDefault",
    "NoModelAsStringRequiredOneValueDefault",
    "NoModelAsStringRequiredOneValueNoDefault",
    "NoModelAsStringRequiredTwoValueDefault",
    "NoModelAsStringRequiredTwoValueNoDefault",
    "ModelAsStringNoRequiredOneValueDefaultEnum",
    "ModelAsStringNoRequiredOneValueDefaultOpEnum",
    "ModelAsStringNoRequiredOneValueNoDefaultEnum",
    "ModelAsStringNoRequiredOneValueNoDefaultOpEnum",
    "ModelAsStringNoRequiredTwoValueDefaultEnum",
    "ModelAsStringNoRequiredTwoValueDefaultOpEnum",
    "ModelAsStringNoRequiredTwoValueNoDefaultEnum",
    "ModelAsStringNoRequiredTwoValueNoDefaultOpEnum",
    "ModelAsStringRequiredOneValueDefaultEnum",
    "ModelAsStringRequiredOneValueDefaultOpEnum",
    "ModelAsStringRequiredOneValueNoDefaultEnum",
    "ModelAsStringRequiredOneValueNoDefaultOpEnum",
    "ModelAsStringRequiredTwoValueDefaultEnum",
    "ModelAsStringRequiredTwoValueDefaultOpEnum",
    "ModelAsStringRequiredTwoValueNoDefaultEnum",
    "ModelAsStringRequiredTwoValueNoDefaultOpEnum",
    "NoModelAsStringNoRequiredTwoValueDefaultEnum",
    "NoModelAsStringNoRequiredTwoValueDefaultOpEnum",
    "NoModelAsStringNoRequiredTwoValueNoDefaultEnum",
    "NoModelAsStringNoRequiredTwoValueNoDefaultOpEnum",
    "NoModelAsStringRequiredTwoValueDefaultEnum",
    "NoModelAsStringRequiredTwoValueDefaultOpEnum",
    "NoModelAsStringRequiredTwoValueNoDefaultEnum",
    "NoModelAsStringRequiredTwoValueNoDefaultOpEnum",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
