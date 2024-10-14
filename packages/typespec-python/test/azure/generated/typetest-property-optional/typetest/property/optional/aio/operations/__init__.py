# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._operations import StringOperations
from ._operations import BytesOperations
from ._operations import DatetimeOperations
from ._operations import DurationOperations
from ._operations import PlainDateOperations
from ._operations import PlainTimeOperations
from ._operations import CollectionsByteOperations
from ._operations import CollectionsModelOperations
from ._operations import StringLiteralOperations
from ._operations import IntLiteralOperations
from ._operations import FloatLiteralOperations
from ._operations import BooleanLiteralOperations
from ._operations import UnionStringLiteralOperations
from ._operations import UnionIntLiteralOperations
from ._operations import UnionFloatLiteralOperations
from ._operations import RequiredAndOptionalOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "StringOperations",
    "BytesOperations",
    "DatetimeOperations",
    "DurationOperations",
    "PlainDateOperations",
    "PlainTimeOperations",
    "CollectionsByteOperations",
    "CollectionsModelOperations",
    "StringLiteralOperations",
    "IntLiteralOperations",
    "FloatLiteralOperations",
    "BooleanLiteralOperations",
    "UnionStringLiteralOperations",
    "UnionIntLiteralOperations",
    "UnionFloatLiteralOperations",
    "RequiredAndOptionalOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
