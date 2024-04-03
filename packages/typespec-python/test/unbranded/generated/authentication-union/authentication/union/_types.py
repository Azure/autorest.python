# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING, Union

from corehttp.credentials import ServiceKeyCredential

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from corehttp.credentials import TokenCredential
UnionCredentialUnion = Union[ServiceKeyCredential, "TokenCredential"]