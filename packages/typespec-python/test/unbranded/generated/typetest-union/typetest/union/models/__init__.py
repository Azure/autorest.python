# coding=utf-8


from ._models import BaseModel
from ._models import Model1
from ._models import Model2
from ._models import ModelWithNamedUnionProperty
from ._models import ModelWithNamedUnionPropertyInResponse
from ._models import ModelWithSimpleUnionProperty
from ._models import ModelWithSimpleUnionPropertyInResponse
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BaseModel",
    "Model1",
    "Model2",
    "ModelWithNamedUnionProperty",
    "ModelWithNamedUnionPropertyInResponse",
    "ModelWithSimpleUnionProperty",
    "ModelWithSimpleUnionPropertyInResponse",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
