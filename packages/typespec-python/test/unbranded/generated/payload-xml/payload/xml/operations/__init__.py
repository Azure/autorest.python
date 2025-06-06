# coding=utf-8
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._operations import SimpleModelValueOperations  # type: ignore
from ._operations import ModelWithSimpleArraysValueOperations  # type: ignore
from ._operations import ModelWithArrayOfModelValueOperations  # type: ignore
from ._operations import ModelWithOptionalFieldValueOperations  # type: ignore
from ._operations import ModelWithAttributesValueOperations  # type: ignore
from ._operations import ModelWithUnwrappedArrayValueOperations  # type: ignore
from ._operations import ModelWithRenamedArraysValueOperations  # type: ignore
from ._operations import ModelWithRenamedFieldsValueOperations  # type: ignore
from ._operations import ModelWithEmptyArrayValueOperations  # type: ignore
from ._operations import ModelWithTextValueOperations  # type: ignore
from ._operations import ModelWithDictionaryValueOperations  # type: ignore
from ._operations import ModelWithEncodedNamesValueOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "SimpleModelValueOperations",
    "ModelWithSimpleArraysValueOperations",
    "ModelWithArrayOfModelValueOperations",
    "ModelWithOptionalFieldValueOperations",
    "ModelWithAttributesValueOperations",
    "ModelWithUnwrappedArrayValueOperations",
    "ModelWithRenamedArraysValueOperations",
    "ModelWithRenamedFieldsValueOperations",
    "ModelWithEmptyArrayValueOperations",
    "ModelWithTextValueOperations",
    "ModelWithDictionaryValueOperations",
    "ModelWithEncodedNamesValueOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
