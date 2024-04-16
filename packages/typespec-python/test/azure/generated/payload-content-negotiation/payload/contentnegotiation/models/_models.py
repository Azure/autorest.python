# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class PngImageAsJson(_model_base.Model):
    """PngImageAsJson.

    All required parameters must be populated in order to send to server.

    :ivar content: Required.
    :vartype content: bytes
    """

    content: bytes = rest_field(format="base64")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        content: bytes,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        Warning: we don't make deepcopy for mapping so if you change value of mapping after init,
        value of the model will be changed, too.

        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
