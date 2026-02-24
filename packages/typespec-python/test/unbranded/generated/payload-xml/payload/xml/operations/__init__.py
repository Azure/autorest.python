# coding=utf-8
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._operations import XmlClientSimpleModelValueOperations  # type: ignore
from ._operations import XmlClientModelWithSimpleArraysValueOperations  # type: ignore
from ._operations import XmlClientModelWithArrayOfModelValueOperations  # type: ignore
from ._operations import XmlClientModelWithOptionalFieldValueOperations  # type: ignore
from ._operations import XmlClientModelWithAttributesValueOperations  # type: ignore
from ._operations import XmlClientModelWithUnwrappedArrayValueOperations  # type: ignore
from ._operations import XmlClientModelWithRenamedArraysValueOperations  # type: ignore
from ._operations import XmlClientModelWithRenamedFieldsValueOperations  # type: ignore
from ._operations import XmlClientModelWithEmptyArrayValueOperations  # type: ignore
from ._operations import XmlClientModelWithTextValueOperations  # type: ignore
from ._operations import XmlClientModelWithDictionaryValueOperations  # type: ignore
from ._operations import XmlClientModelWithEncodedNamesValueOperations  # type: ignore
from ._operations import XmlClientXmlErrorValueOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "XmlClientSimpleModelValueOperations",
    "XmlClientModelWithSimpleArraysValueOperations",
    "XmlClientModelWithArrayOfModelValueOperations",
    "XmlClientModelWithOptionalFieldValueOperations",
    "XmlClientModelWithAttributesValueOperations",
    "XmlClientModelWithUnwrappedArrayValueOperations",
    "XmlClientModelWithRenamedArraysValueOperations",
    "XmlClientModelWithRenamedFieldsValueOperations",
    "XmlClientModelWithEmptyArrayValueOperations",
    "XmlClientModelWithTextValueOperations",
    "XmlClientModelWithDictionaryValueOperations",
    "XmlClientModelWithEncodedNamesValueOperations",
    "XmlClientXmlErrorValueOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
