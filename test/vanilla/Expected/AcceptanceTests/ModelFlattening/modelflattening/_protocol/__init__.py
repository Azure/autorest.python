# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import prepare_put_array
    from ._preparers_py3 import prepare_get_array
    from ._preparers_py3 import prepare_put_wrapped_array
    from ._preparers_py3 import prepare_get_wrapped_array
    from ._preparers_py3 import prepare_put_dictionary
    from ._preparers_py3 import prepare_get_dictionary
    from ._preparers_py3 import prepare_put_resource_collection
    from ._preparers_py3 import prepare_get_resource_collection
    from ._preparers_py3 import prepare_put_simple_product
    from ._preparers_py3 import prepare_post_flattened_simple_product
    from ._preparers_py3 import prepare_put_simple_product_with_grouping
except (SyntaxError, ImportError):
    from ._preparers import prepare_put_array  # type: ignore
    from ._preparers import prepare_get_array  # type: ignore
    from ._preparers import prepare_put_wrapped_array  # type: ignore
    from ._preparers import prepare_get_wrapped_array  # type: ignore
    from ._preparers import prepare_put_dictionary  # type: ignore
    from ._preparers import prepare_get_dictionary  # type: ignore
    from ._preparers import prepare_put_resource_collection  # type: ignore
    from ._preparers import prepare_get_resource_collection  # type: ignore
    from ._preparers import prepare_put_simple_product  # type: ignore
    from ._preparers import prepare_post_flattened_simple_product  # type: ignore
    from ._preparers import prepare_put_simple_product_with_grouping  # type: ignore

__all__ = [
    "prepare_put_array",
    "prepare_get_array",
    "prepare_put_wrapped_array",
    "prepare_get_wrapped_array",
    "prepare_put_dictionary",
    "prepare_get_dictionary",
    "prepare_put_resource_collection",
    "prepare_get_resource_collection",
    "prepare_put_simple_product",
    "prepare_post_flattened_simple_product",
    "prepare_put_simple_product_with_grouping",
]
