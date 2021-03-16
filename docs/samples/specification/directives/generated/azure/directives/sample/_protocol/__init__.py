# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import prepare_basic_polling_initial_request
    from ._preparers_py3 import prepare_basic_paging_request
except (SyntaxError, ImportError):
    from ._preparers import prepare_basic_polling_initial_request  # type: ignore
    from ._preparers import prepare_basic_paging_request  # type: ignore

__all__ = [
    'prepare_basic_polling_initial_request',
    'prepare_basic_paging_request',
]
