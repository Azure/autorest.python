# coding=utf-8
# pylint: disable=too-many-lines


from typing import Any, Mapping, overload

from .. import _model_base
from .._model_base import rest_field


class ClientProjectedNameModel(_model_base.Model):
    """ClientProjectedNameModel.

    All required parameters must be populated in order to send to Azure.

    :ivar client_name: Pass in true. Required.
    :vartype client_name: bool
    """

    client_name: bool = rest_field(name="defaultName")
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        client_name: bool,
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


class JsonAndClientProjectedNameModel(_model_base.Model):
    """JsonAndClientProjectedNameModel.

    All required parameters must be populated in order to send to Azure.

    :ivar client_name: Pass in true. Required.
    :vartype client_name: bool
    """

    client_name: bool = rest_field(name="wireName")
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        client_name: bool,
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


class JsonProjectedNameModel(_model_base.Model):
    """JsonProjectedNameModel.

    All required parameters must be populated in order to send to Azure.

    :ivar default_name: Pass in true. Required.
    :vartype default_name: bool
    """

    default_name: bool = rest_field(name="wireName")
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        default_name: bool,
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


class LanguageProjectedNameModel(_model_base.Model):
    """LanguageProjectedNameModel.

    All required parameters must be populated in order to send to Azure.

    :ivar python_name: Pass in true. Required.
    :vartype python_name: bool
    """

    python_name: bool = rest_field(name="defaultName")
    """Pass in true. Required."""

    @overload
    def __init__(
        self,
        *,
        python_name: bool,
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
