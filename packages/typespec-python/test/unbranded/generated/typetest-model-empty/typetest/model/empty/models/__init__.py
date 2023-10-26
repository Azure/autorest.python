# coding=utf-8


from ._models import EmptyInput
from ._models import EmptyInputOutput
from ._models import EmptyOutput
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "EmptyInput",
    "EmptyInputOutput",
    "EmptyOutput",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
