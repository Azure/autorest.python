# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, overload

from ... import _model_base
from ..._model_base import rest_field
from ..._vendor import FileType


class AnonymousModelRequest(_model_base.Model):
    """AnonymousModelRequest.

    :ivar profile_image: Required.
    :vartype profile_image: ~payload.multipart._vendor.FileType
    """

    profile_image: FileType = rest_field(
        name="profileImage", visibility=["read", "create", "update", "delete", "query"], is_multipart_file_input=True
    )
    """Required."""

    @overload
    def __init__(
        self,
        *,
        profile_image: FileType,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
