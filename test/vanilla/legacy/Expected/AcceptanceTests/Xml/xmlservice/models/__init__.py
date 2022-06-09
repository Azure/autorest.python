# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AccessPolicy
from ._models_py3 import AppleBarrel
from ._models_py3 import Banana
from ._models_py3 import Blob
from ._models_py3 import BlobPrefix
from ._models_py3 import BlobProperties
from ._models_py3 import Blobs
from ._models_py3 import ComplexTypeNoMeta
from ._models_py3 import ComplexTypeWithMeta
from ._models_py3 import Container
from ._models_py3 import ContainerProperties
from ._models_py3 import CorsRule
from ._models_py3 import Error
from ._models_py3 import JSONInput
from ._models_py3 import JSONOutput
from ._models_py3 import ListBlobsResponse
from ._models_py3 import ListContainersResponse
from ._models_py3 import Logging
from ._models_py3 import Metrics
from ._models_py3 import ModelWithByteProperty
from ._models_py3 import ModelWithUrlProperty
from ._models_py3 import ObjectWithXMsTextProperty
from ._models_py3 import RetentionPolicy
from ._models_py3 import RootWithRefAndMeta
from ._models_py3 import RootWithRefAndNoMeta
from ._models_py3 import SignedIdentifier
from ._models_py3 import Slide
from ._models_py3 import Slideshow
from ._models_py3 import StorageServiceProperties


from ._auto_rest_swagger_batxml_service_enums import AccessTier
from ._auto_rest_swagger_batxml_service_enums import ArchiveStatus
from ._auto_rest_swagger_batxml_service_enums import BlobType
from ._auto_rest_swagger_batxml_service_enums import CopyStatusType
from ._auto_rest_swagger_batxml_service_enums import LeaseDurationType
from ._auto_rest_swagger_batxml_service_enums import LeaseStateType
from ._auto_rest_swagger_batxml_service_enums import LeaseStatusType
from ._auto_rest_swagger_batxml_service_enums import PublicAccessType
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessPolicy",
    "AppleBarrel",
    "Banana",
    "Blob",
    "BlobPrefix",
    "BlobProperties",
    "Blobs",
    "ComplexTypeNoMeta",
    "ComplexTypeWithMeta",
    "Container",
    "ContainerProperties",
    "CorsRule",
    "Error",
    "JSONInput",
    "JSONOutput",
    "ListBlobsResponse",
    "ListContainersResponse",
    "Logging",
    "Metrics",
    "ModelWithByteProperty",
    "ModelWithUrlProperty",
    "ObjectWithXMsTextProperty",
    "RetentionPolicy",
    "RootWithRefAndMeta",
    "RootWithRefAndNoMeta",
    "SignedIdentifier",
    "Slide",
    "Slideshow",
    "StorageServiceProperties",
    "AccessTier",
    "ArchiveStatus",
    "BlobType",
    "CopyStatusType",
    "LeaseDurationType",
    "LeaseStateType",
    "LeaseStatusType",
    "PublicAccessType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
