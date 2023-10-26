# coding=utf-8


from ._models import Fish
from ._models import GoblinShark
from ._models import Salmon
from ._models import SawShark
from ._models import Shark
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Fish",
    "GoblinShark",
    "Salmon",
    "SawShark",
    "Shark",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
