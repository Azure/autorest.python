# coding=utf-8


from ._models import Cat
from ._models import Pet
from ._models import Siamese
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Cat",
    "Pet",
    "Siamese",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
