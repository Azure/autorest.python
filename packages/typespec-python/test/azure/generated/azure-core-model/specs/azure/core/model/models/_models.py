# coding=utf-8
None
# pylint: disable=useless-super-delegation

from typing import Any, List, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class AzureEmbeddingModel(_model_base.Model):
    """AzureEmbeddingModel.

    :ivar embedding: Required.
    :vartype embedding: list[int]
    """

    embedding: List[int] = rest_field(visibility=["read", "create", "update", "delete", "query"])
    """Required."""

    @overload
    def __init__(
        self,
        *,
        embedding: List[int],
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
