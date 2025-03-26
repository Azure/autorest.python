# coding=utf-8
None
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models import (  # type: ignore
    ChildFlattenModel,
    ChildModel,
    FlattenModel,
    NestedFlattenModel,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ChildFlattenModel",
    "ChildModel",
    "FlattenModel",
    "NestedFlattenModel",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
