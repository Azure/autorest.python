# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, Optional

import msrest.serialization

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports


class Error(msrest.serialization.Model):
    """Error.

    :ivar status:
    :vartype status: int
    :ivar message:
    :vartype message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword status:
        :paramtype status: int
        :keyword message:
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.status = status
        self.message = message


class FirstParameterGroup(msrest.serialization.Model):
    """Parameter group.

    :ivar header_one:
    :vartype header_one: str
    :ivar query_one: Query parameter with default.
    :vartype query_one: int
    """

    _attribute_map = {
        "header_one": {"key": "header-one", "type": "str"},
        "query_one": {"key": "query-one", "type": "int"},
    }

    def __init__(self, *, header_one: Optional[str] = None, query_one: int = 30, **kwargs: Any) -> None:
        """
        :keyword header_one:
        :paramtype header_one: str
        :keyword query_one: Query parameter with default.
        :paramtype query_one: int
        """
        super().__init__(**kwargs)
        self.header_one = header_one
        self.query_one = query_one


class Grouper(msrest.serialization.Model):
    """Parameter group.

    :ivar grouped_constant: A grouped parameter that is a constant. Default value is "foo".
    :vartype grouped_constant: str
    :ivar grouped_parameter: Optional parameter part of a parameter grouping.
    :vartype grouped_parameter: str
    """

    _attribute_map = {
        "grouped_constant": {"key": "groupedConstant", "type": "str"},
        "grouped_parameter": {"key": "groupedParameter", "type": "str"},
    }

    def __init__(
        self,
        *,
        grouped_constant: Optional[Literal["foo"]] = None,
        grouped_parameter: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword grouped_constant: A grouped parameter that is a constant. Default value is "foo".
        :paramtype grouped_constant: str
        :keyword grouped_parameter: Optional parameter part of a parameter grouping.
        :paramtype grouped_parameter: str
        """
        super().__init__(**kwargs)
        self.grouped_constant = grouped_constant
        self.grouped_parameter = grouped_parameter


class ParameterGroupingPostMultiParamGroupsSecondParamGroup(msrest.serialization.Model):
    """Parameter group.

    :ivar header_two:
    :vartype header_two: str
    :ivar query_two: Query parameter with default.
    :vartype query_two: int
    """

    _attribute_map = {
        "header_two": {"key": "header-two", "type": "str"},
        "query_two": {"key": "query-two", "type": "int"},
    }

    def __init__(self, *, header_two: Optional[str] = None, query_two: int = 30, **kwargs: Any) -> None:
        """
        :keyword header_two:
        :paramtype header_two: str
        :keyword query_two: Query parameter with default.
        :paramtype query_two: int
        """
        super().__init__(**kwargs)
        self.header_two = header_two
        self.query_two = query_two


class ParameterGroupingPostOptionalParameters(msrest.serialization.Model):
    """Parameter group.

    :ivar custom_header:
    :vartype custom_header: str
    :ivar query: Query parameter with default.
    :vartype query: int
    """

    _attribute_map = {
        "custom_header": {"key": "customHeader", "type": "str"},
        "query": {"key": "query", "type": "int"},
    }

    def __init__(self, *, custom_header: Optional[str] = None, query: int = 30, **kwargs: Any) -> None:
        """
        :keyword custom_header:
        :paramtype custom_header: str
        :keyword query: Query parameter with default.
        :paramtype query: int
        """
        super().__init__(**kwargs)
        self.custom_header = custom_header
        self.query = query


class ParameterGroupingPostRequiredParameters(msrest.serialization.Model):
    """Parameter group.

    All required parameters must be populated in order to send to Azure.

    :ivar custom_header:
    :vartype custom_header: str
    :ivar query: Query parameter with default.
    :vartype query: int
    :ivar path: Path parameter. Required.
    :vartype path: str
    :ivar body: Required.
    :vartype body: int
    """

    _validation = {
        "path": {"required": True},
        "body": {"required": True},
    }

    _attribute_map = {
        "custom_header": {"key": "customHeader", "type": "str"},
        "query": {"key": "query", "type": "int"},
        "path": {"key": "path", "type": "str"},
        "body": {"key": "body", "type": "int"},
    }

    def __init__(
        self, *, path: str, body: int, custom_header: Optional[str] = None, query: int = 30, **kwargs: Any
    ) -> None:
        """
        :keyword custom_header:
        :paramtype custom_header: str
        :keyword query: Query parameter with default.
        :paramtype query: int
        :keyword path: Path parameter. Required.
        :paramtype path: str
        :keyword body: Required.
        :paramtype body: int
        """
        super().__init__(**kwargs)
        self.custom_header = custom_header
        self.query = query
        self.path = path
        self.body = body


class ParameterGroupingPostReservedWordsParameters(msrest.serialization.Model):
    """Parameter group.

    :ivar from_property: 'from' is a reserved word. Pass in 'bob' to pass.
    :vartype from_property: str
    :ivar accept: 'accept' is a reserved word. Pass in 'yes' to pass.
    :vartype accept: str
    """

    _attribute_map = {
        "from_property": {"key": "from", "type": "str"},
        "accept": {"key": "accept", "type": "str"},
    }

    def __init__(self, *, from_property: Optional[str] = None, accept: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword from_property: 'from' is a reserved word. Pass in 'bob' to pass.
        :paramtype from_property: str
        :keyword accept: 'accept' is a reserved word. Pass in 'yes' to pass.
        :paramtype accept: str
        """
        super().__init__(**kwargs)
        self.from_property = from_property
        self.accept = accept
