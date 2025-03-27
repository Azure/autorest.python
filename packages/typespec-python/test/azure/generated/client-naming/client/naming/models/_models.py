# coding=utf-8
# pylint: disable=useless-super-delegation

from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class ClientModel(_model_base.Model):
    """ClientModel.

    :ivar default_name: Pass in true. Required.
    :vartype default_name: bool
    """

    default_name: bool = rest_field(name="defaultName", visibility=["read", "create", "update", "delete", "query"])
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        default_name: bool,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ClientNameAndJsonEncodedNameModel(_model_base.Model):
    """ClientNameAndJsonEncodedNameModel.

    :ivar client_name: Pass in true. Required.
    :vartype client_name: bool
    """

    client_name: bool = rest_field(name="wireName", visibility=["read", "create", "update", "delete", "query"])
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        client_name: bool,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class ClientNameModel(_model_base.Model):
    """ClientNameModel.

    :ivar client_name: Pass in true. Required.
    :vartype client_name: bool
    """

    client_name: bool = rest_field(name="defaultName", visibility=["read", "create", "update", "delete", "query"])
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        client_name: bool,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class LanguageClientNameModel(_model_base.Model):
    """LanguageClientNameModel.

    :ivar python_name: Pass in true. Required.
    :vartype python_name: bool
    """

    python_name: bool = rest_field(name="defaultName", visibility=["read", "create", "update", "delete", "query"])
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        python_name: bool,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)


class PythonModel(_model_base.Model):
    """PythonModel.

    :ivar default_name: Pass in true. Required.
    :vartype default_name: bool
    """

    default_name: bool = rest_field(name="defaultName", visibility=["read", "create", "update", "delete", "query"])
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        default_name: bool,
    ) -> None: ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]) -> None:
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
