# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, TYPE_CHECKING, Union, overload

from ..._utils.model_base import Model as _Model, rest_field

if TYPE_CHECKING:
    from ..sub import models as _sub_models2


class SecondClientResult(_Model):
    """SecondClientResult.

    :ivar type: Required. "second"
    :vartype type: str or ~client.clientnamespace.second.sub.models.SecondClientEnumType
    """

    type: Union[str, "_sub_models2.SecondClientEnumType"] = rest_field(
        visibility=["read", "create", "update", "delete", "query"]
    )
    """Required. \"second\""""

    @overload
    def __init__(
        self,
        *,
        type: Union[str, "_sub_models2.SecondClientEnumType"],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
