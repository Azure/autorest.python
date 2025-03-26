# coding=utf-8
None
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._operations import TopLevelOperations  # type: ignore
from ._operations import NestedOperations  # type: ignore
from ._operations import SingletonOperations  # type: ignore
from ._operations import ExtensionsResourcesOperations  # type: ignore
from ._operations import LocationResourcesOperations  # type: ignore

from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "TopLevelOperations",
    "NestedOperations",
    "SingletonOperations",
    "ExtensionsResourcesOperations",
    "LocationResourcesOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
