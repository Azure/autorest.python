# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import Cat
from ._models import Fish
from ._models import GoblinShark
from ._models import Pet
from ._models import Salmon
from ._models import SawShark
from ._models import Shark
from ._models import Siamese
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "Cat",
    "Fish",
    "GoblinShark",
    "Pet",
    "Salmon",
    "SawShark",
    "Shark",
    "Siamese",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
