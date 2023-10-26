# coding=utf-8


from ._models import Bird
from ._models import Dinosaur
from ._models import Eagle
from ._models import Goose
from ._models import SeaGull
from ._models import Sparrow
from ._models import TRex
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Bird",
    "Dinosaur",
    "Eagle",
    "Goose",
    "SeaGull",
    "Sparrow",
    "TRex",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
