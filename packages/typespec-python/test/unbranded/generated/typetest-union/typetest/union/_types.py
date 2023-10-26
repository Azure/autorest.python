# coding=utf-8
# pylint: disable=too-many-lines


from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from . import models as _models
MyNamedUnion = Union["_models.Model1", "_models.Model2"]
