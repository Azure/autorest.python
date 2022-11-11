# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import BodyParam
from ._models_py3 import CustomParameterGroup
from ._models_py3 import OdataProductResult
from ._models_py3 import OperationResult
from ._models_py3 import PagingGetMultiplePagesLroOptions
from ._models_py3 import PagingGetMultiplePagesOptions
from ._models_py3 import PagingGetMultiplePagesWithOffsetOptions
from ._models_py3 import PagingGetOdataMultiplePagesOptions
from ._models_py3 import Product
from ._models_py3 import ProductProperties
from ._models_py3 import ProductResult
from ._models_py3 import ProductResultValue
from ._models_py3 import ProductResultValueWithXMSClientName

from ._paging_client_enums import OperationResultStatus
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "BodyParam",
    "CustomParameterGroup",
    "OdataProductResult",
    "OperationResult",
    "PagingGetMultiplePagesLroOptions",
    "PagingGetMultiplePagesOptions",
    "PagingGetMultiplePagesWithOffsetOptions",
    "PagingGetOdataMultiplePagesOptions",
    "Product",
    "ProductProperties",
    "ProductResult",
    "ProductResultValue",
    "ProductResultValueWithXMSClientName",
    "OperationResultStatus",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
