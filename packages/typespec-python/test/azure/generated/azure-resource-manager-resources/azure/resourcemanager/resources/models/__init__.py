# coding=utf-8
None
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models import (  # type: ignore
    ErrorAdditionalInfo,
    ErrorDetail,
    ErrorResponse,
    ExtensionResource,
    ExtensionsResource,
    ExtensionsResourceProperties,
    LocationResource,
    LocationResourceProperties,
    NestedProxyResource,
    NestedProxyResourceProperties,
    NotificationDetails,
    ProxyResource,
    Resource,
    SingletonTrackedResource,
    SingletonTrackedResourceProperties,
    SystemData,
    TopLevelTrackedResource,
    TopLevelTrackedResourceProperties,
    TrackedResource,
)

from ._enums import (  # type: ignore
    CreatedByType,
    ProvisioningState,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ExtensionResource",
    "ExtensionsResource",
    "ExtensionsResourceProperties",
    "LocationResource",
    "LocationResourceProperties",
    "NestedProxyResource",
    "NestedProxyResourceProperties",
    "NotificationDetails",
    "ProxyResource",
    "Resource",
    "SingletonTrackedResource",
    "SingletonTrackedResourceProperties",
    "SystemData",
    "TopLevelTrackedResource",
    "TopLevelTrackedResourceProperties",
    "TrackedResource",
    "CreatedByType",
    "ProvisioningState",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
