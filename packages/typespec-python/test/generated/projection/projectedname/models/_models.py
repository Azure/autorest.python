# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Mapping, Optional, overload

from .. import _model_base
from .._model_base import rest_field


class Project(_model_base.Model):
    """Project.

    :ivar produced_by: Only valid value is 'DPG'.
    :vartype produced_by: str
    :ivar created_by: Only valid value is 'DPG'.
    :vartype created_by: str
    :ivar made_for_python: Only valid value is 'customers'.
    :vartype made_for_python: str
    """

    produced_by: Optional[str] = rest_field(name="codegen")
    """Only valid value is 'DPG'."""
    created_by: Optional[str] = rest_field(name="builtfrom")
    """Only valid value is 'DPG'."""
    made_for_python: Optional[str] = rest_field(name="wasMadeFor")
    """Only valid value is 'customers'."""

    @overload
    def __init__(
        self,
        *,
        produced_by: Optional[str] = None,
        created_by: Optional[str] = None,
        made_for_python: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
