# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import ExtendsFloatAdditionalProperties
from ._models import ExtendsModelAdditionalProperties
from ._models import ExtendsModelArrayAdditionalProperties
from ._models import ExtendsStringAdditionalProperties
from ._models import ExtendsUnknownAdditionalProperties
from ._models import ExtendsUnknownAdditionalPropertiesDerived
from ._models import ExtendsUnknownAdditionalPropertiesDiscriminated
from ._models import ExtendsUnknownAdditionalPropertiesDiscriminatedDerived
from ._models import IsFloatAdditionalProperties
from ._models import IsModelAdditionalProperties
from ._models import IsModelArrayAdditionalProperties
from ._models import IsStringAdditionalProperties
from ._models import IsUnknownAdditionalProperties
from ._models import IsUnknownAdditionalPropertiesDerived
from ._models import IsUnknownAdditionalPropertiesDiscriminated
from ._models import IsUnknownAdditionalPropertiesDiscriminatedDerived
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ExtendsFloatAdditionalProperties",
    "ExtendsModelAdditionalProperties",
    "ExtendsModelArrayAdditionalProperties",
    "ExtendsStringAdditionalProperties",
    "ExtendsUnknownAdditionalProperties",
    "ExtendsUnknownAdditionalPropertiesDerived",
    "ExtendsUnknownAdditionalPropertiesDiscriminated",
    "ExtendsUnknownAdditionalPropertiesDiscriminatedDerived",
    "IsFloatAdditionalProperties",
    "IsModelAdditionalProperties",
    "IsModelArrayAdditionalProperties",
    "IsStringAdditionalProperties",
    "IsUnknownAdditionalProperties",
    "IsUnknownAdditionalPropertiesDerived",
    "IsUnknownAdditionalPropertiesDiscriminated",
    "IsUnknownAdditionalPropertiesDiscriminatedDerived",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
