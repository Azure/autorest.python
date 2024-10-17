# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models_py3 import BaseProduct
from ._models_py3 import Error
from ._models_py3 import FlattenParameterGroup
from ._models_py3 import FlattenedProduct
from ._models_py3 import GenericUrl
from ._models_py3 import ProductUrl
from ._models_py3 import ProductWrapper
from ._models_py3 import Resource
from ._models_py3 import ResourceCollection
from ._models_py3 import SimpleProduct
from ._models_py3 import WrappedProduct

from ._auto_rest_resource_flattening_test_service_enums import FlattenedProductPropertiesProvisioningStateValues
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BaseProduct",
    "Error",
    "FlattenParameterGroup",
    "FlattenedProduct",
    "GenericUrl",
    "ProductUrl",
    "ProductWrapper",
    "Resource",
    "ResourceCollection",
    "SimpleProduct",
    "WrappedProduct",
    "FlattenedProductPropertiesProvisioningStateValues",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
