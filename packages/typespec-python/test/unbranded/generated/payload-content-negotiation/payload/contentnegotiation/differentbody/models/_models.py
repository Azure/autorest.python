# coding=utf-8

from typing import Any, Literal, Mapping, overload

from ..._utils.model_base import Model as _Model, rest_field


class PngImageAsJson(_Model):
    """PngImageAsJson.

    :ivar content_type: Required. Default value is "application/json".
    :vartype content_type: str
    :ivar content: Required.
    :vartype content: bytes
    """

    content_type: Literal["application/json"] = rest_field(
        name="contentType", visibility=["read", "create", "update", "delete", "query"]
    )
    """Required. Default value is \"application/json\"."""
    content: bytes = rest_field(visibility=["read", "create", "update", "delete", "query"], format="base64")
    """Required."""

    @overload
    def __init__(
        self,
        *,
        content: bytes,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.content_type: Literal["application/json"] = "application/json"
