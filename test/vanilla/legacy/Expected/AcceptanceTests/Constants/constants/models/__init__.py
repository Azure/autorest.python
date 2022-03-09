# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ModelAsStringNoRequiredOneValueDefault
    from ._models_py3 import ModelAsStringNoRequiredOneValueNoDefault
    from ._models_py3 import ModelAsStringNoRequiredTwoValueDefault
    from ._models_py3 import ModelAsStringNoRequiredTwoValueNoDefault
    from ._models_py3 import ModelAsStringRequiredOneValueDefault
    from ._models_py3 import ModelAsStringRequiredOneValueNoDefault
    from ._models_py3 import ModelAsStringRequiredTwoValueDefault
    from ._models_py3 import ModelAsStringRequiredTwoValueNoDefault
    from ._models_py3 import NoModelAsStringNoRequiredOneValueDefault
    from ._models_py3 import NoModelAsStringNoRequiredOneValueNoDefault
    from ._models_py3 import NoModelAsStringNoRequiredTwoValueDefault
    from ._models_py3 import NoModelAsStringNoRequiredTwoValueNoDefault
    from ._models_py3 import NoModelAsStringRequiredOneValueDefault
    from ._models_py3 import NoModelAsStringRequiredOneValueNoDefault
    from ._models_py3 import NoModelAsStringRequiredTwoValueDefault
    from ._models_py3 import NoModelAsStringRequiredTwoValueNoDefault
except (SyntaxError, ImportError):
    from ._models import ModelAsStringNoRequiredOneValueDefault  # type: ignore
    from ._models import ModelAsStringNoRequiredOneValueNoDefault  # type: ignore
    from ._models import ModelAsStringNoRequiredTwoValueDefault  # type: ignore
    from ._models import ModelAsStringNoRequiredTwoValueNoDefault  # type: ignore
    from ._models import ModelAsStringRequiredOneValueDefault  # type: ignore
    from ._models import ModelAsStringRequiredOneValueNoDefault  # type: ignore
    from ._models import ModelAsStringRequiredTwoValueDefault  # type: ignore
    from ._models import ModelAsStringRequiredTwoValueNoDefault  # type: ignore
    from ._models import NoModelAsStringNoRequiredOneValueDefault  # type: ignore
    from ._models import NoModelAsStringNoRequiredOneValueNoDefault  # type: ignore
    from ._models import NoModelAsStringNoRequiredTwoValueDefault  # type: ignore
    from ._models import NoModelAsStringNoRequiredTwoValueNoDefault  # type: ignore
    from ._models import NoModelAsStringRequiredOneValueDefault  # type: ignore
    from ._models import NoModelAsStringRequiredOneValueNoDefault  # type: ignore
    from ._models import NoModelAsStringRequiredTwoValueDefault  # type: ignore
    from ._models import NoModelAsStringRequiredTwoValueNoDefault  # type: ignore

from ._auto_rest_swagger_constant_service_enums import (
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
from ._patch import *  # pylint: disable=unused-wildcard-import
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
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
