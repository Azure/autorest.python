# coding=utf-8


from ._operations import PropertyOperations
from ._operations import ProjectedNameClientOperationsMixin

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "PropertyOperations",
    "ProjectedNameClientOperationsMixin",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
