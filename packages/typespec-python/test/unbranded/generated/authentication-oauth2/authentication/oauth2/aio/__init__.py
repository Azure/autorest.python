# coding=utf-8
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import

from ._client import OAuth2Client  # type: ignore

try:
    from ._patch import __all__ as _patch_all
    from ._patch import *
except ImportError:
    _patch_all = []
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "OAuth2Client",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore

_patch_sdk()
,line-too-long,useless-suppression