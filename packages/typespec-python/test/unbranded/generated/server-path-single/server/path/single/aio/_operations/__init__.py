# coding=utf-8


from ._operations import SingleClientOperationsMixin

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "SingleClientOperationsMixin",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
