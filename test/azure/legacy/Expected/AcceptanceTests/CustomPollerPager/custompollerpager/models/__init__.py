# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
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
except (SyntaxError, ImportError):
    from ._models import CustomParameterGroup  # type: ignore
    from ._models import OdataProductResult  # type: ignore
    from ._models import OperationResult  # type: ignore
    from ._models import PagingGetMultiplePagesLroOptions  # type: ignore
    from ._models import PagingGetMultiplePagesOptions  # type: ignore
    from ._models import PagingGetMultiplePagesWithOffsetOptions  # type: ignore
    from ._models import PagingGetOdataMultiplePagesOptions  # type: ignore
    from ._models import Product  # type: ignore
    from ._models import ProductProperties  # type: ignore
    from ._models import ProductResult  # type: ignore
    from ._models import ProductResultValue  # type: ignore
    from ._models import ProductResultValueWithXMSClientName  # type: ignore

from ._auto_rest_paging_test_service_enums import (
    OperationResultStatus,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
__all__ = [
    'CustomParameterGroup',
    'OdataProductResult',
    'OperationResult',
    'PagingGetMultiplePagesLroOptions',
    'PagingGetMultiplePagesOptions',
    'PagingGetMultiplePagesWithOffsetOptions',
    'PagingGetOdataMultiplePagesOptions',
    'Product',
    'ProductProperties',
    'ProductResult',
    'ProductResultValue',
    'ProductResultValueWithXMSClientName',
    'OperationResultStatus',
]
__all__.extend(_patch_all)