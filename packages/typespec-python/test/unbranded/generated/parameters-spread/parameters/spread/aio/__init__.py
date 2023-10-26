# coding=utf-8


from ._client import SpreadClient

try:
    from ._patch import __all__ as _patch_all
    from ._patch import *  # pylint: disable=unused-wildcard-import
except ImportError:
    _patch_all = []
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "SpreadClient",
]
__all__.extend([p for p in _patch_all if p not in __all__])

_patch_sdk()
