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

from ._basic_operations import BasicOperations  # type: ignore
from ._primitive_operations import PrimitiveOperations  # type: ignore
from ._array_operations import ArrayOperations  # type: ignore
from ._dictionary_operations import DictionaryOperations  # type: ignore
from ._inheritance_operations import InheritanceOperations  # type: ignore
from ._polymorphism_operations import PolymorphismOperations  # type: ignore
from ._polymorphicrecursive_operations import PolymorphicrecursiveOperations  # type: ignore
from ._readonlyproperty_operations import ReadonlypropertyOperations  # type: ignore
from ._flattencomplex_operations import FlattencomplexOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BasicOperations",
    "PrimitiveOperations",
    "ArrayOperations",
    "DictionaryOperations",
    "InheritanceOperations",
    "PolymorphismOperations",
    "PolymorphicrecursiveOperations",
    "ReadonlypropertyOperations",
    "FlattencomplexOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
