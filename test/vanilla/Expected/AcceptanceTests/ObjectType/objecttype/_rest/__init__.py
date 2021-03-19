# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._preparers_py3 import prepare_get
    from ._preparers_py3 import prepare_put
except (SyntaxError, ImportError):
    from ._preparers import prepare_get  # type: ignore
    from ._preparers import prepare_put  # type: ignore

__all__ = [
    "prepare_get",
    "prepare_put",
]
