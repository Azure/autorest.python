# coding=utf-8
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models import (  # type: ignore
    CheckNameAvailabilityRequest,
    CheckNameAvailabilityResponse,
    ErrorAdditionalInfo,
    ErrorDetail,
    ErrorResponse,
    ExportRequest,
    Operation,
    OperationDisplay,
    Order,
    OrderProperties,
    Resource,
    SystemData,
    TrackedResource,
)

from ._enums import (  # type: ignore
    ActionType,
    CheckNameAvailabilityReason,
    CreatedByType,
    Origin,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CheckNameAvailabilityRequest",
    "CheckNameAvailabilityResponse",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ExportRequest",
    "Operation",
    "OperationDisplay",
    "Order",
    "OrderProperties",
    "Resource",
    "SystemData",
    "TrackedResource",
    "ActionType",
    "CheckNameAvailabilityReason",
    "CreatedByType",
    "Origin",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
