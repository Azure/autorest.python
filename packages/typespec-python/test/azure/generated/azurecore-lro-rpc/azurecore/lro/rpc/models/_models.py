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


class GenerationOptions(_model_base.Model):
    """Options for the generation.

    All required parameters must be populated in order to send to server.

    :ivar prompt: Prompt. Required.
    :vartype prompt: str
    """

    prompt: str = rest_field()
    """Prompt. Required."""

    @overload
    def __init__(
        self,
        *,
        prompt: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class GenerationResult(_model_base.Model):
    """Result of the generation.


    :ivar data: The data. Required.
    :vartype data: str
    """

    data: str = rest_field()
    """The data. Required."""

    @overload
    def __init__(
        self,
        *,
        data: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
