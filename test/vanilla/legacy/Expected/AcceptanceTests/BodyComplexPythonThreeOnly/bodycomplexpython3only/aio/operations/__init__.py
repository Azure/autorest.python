# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._basic_operations import BasicOperations
from ._primitive_operations import PrimitiveOperations
from ._array_operations import ArrayOperations
from ._dictionary_operations import DictionaryOperations
from ._inheritance_operations import InheritanceOperations
from ._polymorphism_operations import PolymorphismOperations
from ._polymorphicrecursive_operations import PolymorphicrecursiveOperations
from ._readonlyproperty_operations import ReadonlypropertyOperations
from ._flattencomplex_operations import FlattencomplexOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import

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
__all__.extend(_patch_all)
