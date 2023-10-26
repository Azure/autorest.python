# coding=utf-8


from ._models import DefaultDurationProperty
from ._models import FloatSecondsDurationArrayProperty
from ._models import FloatSecondsDurationProperty
from ._models import ISO8601DurationProperty
from ._models import Int32SecondsDurationProperty
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "DefaultDurationProperty",
    "FloatSecondsDurationArrayProperty",
    "FloatSecondsDurationProperty",
    "ISO8601DurationProperty",
    "Int32SecondsDurationProperty",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
