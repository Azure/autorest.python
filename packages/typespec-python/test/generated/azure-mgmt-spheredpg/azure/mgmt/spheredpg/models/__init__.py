# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models import ArmResource
from ._models import CatalogProperties
from ._models import CertificateChainResponse
from ._models import CertificateProperties
from ._models import ClaimDevicesRequest
from ._models import CountDeviceResponse
from ._models import CountElementsResponse
from ._models import DeviceInsight
from ._models import ErrorAdditionalInfo
from ._models import ErrorDetail
from ._models import ErrorResponse
from ._models import GenerateCapabilityImageRequest
from ._models import ImageProperties
from ._models import ListDeviceGroupsRequest
from ._models import Operation
from ._models import OperationDisplay
from ._models import ProofOfPossessionNonceRequest
from ._models import ProofOfPossessionNonceResponse
from ._models import ProxyResource
from ._models import ProxyResourceBase
from ._models import ResourceUpdateModel
from ._models import SignedCapabilityImageResponse
from ._models import SystemData
from ._models import TrackedResource
from ._models import TrackedResourceBase

from ._enums import ActionType
from ._enums import CapabilityType
from ._enums import CertificateStatus
from ._enums import ImageType
from ._enums import Origin
from ._enums import ProvisioningState
from ._enums import RegionalDataBoundary
from ._enums import createdByType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ArmResource",
    "CatalogProperties",
    "CertificateChainResponse",
    "CertificateProperties",
    "ClaimDevicesRequest",
    "CountDeviceResponse",
    "CountElementsResponse",
    "DeviceInsight",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "GenerateCapabilityImageRequest",
    "ImageProperties",
    "ListDeviceGroupsRequest",
    "Operation",
    "OperationDisplay",
    "ProofOfPossessionNonceRequest",
    "ProofOfPossessionNonceResponse",
    "ProxyResource",
    "ProxyResourceBase",
    "ResourceUpdateModel",
    "SignedCapabilityImageResponse",
    "SystemData",
    "TrackedResource",
    "TrackedResourceBase",
    "ActionType",
    "CapabilityType",
    "CertificateStatus",
    "ImageType",
    "Origin",
    "ProvisioningState",
    "RegionalDataBoundary",
    "createdByType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
