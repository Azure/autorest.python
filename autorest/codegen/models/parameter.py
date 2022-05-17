# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import abc
from enum import Enum, auto

from typing import (
    Dict,
    Any,
    TYPE_CHECKING,
    List,
    Optional,
    TypeVar,
    Union,
    Generic,
)

from .imports import FileImport, ImportType
from .base_model import BaseModel
from .base_type import BaseType
from .constant_type import ConstantType
from .utils import add_to_description

if TYPE_CHECKING:
    from .code_model import CodeModel
    from .request_builder_parameter import RequestBuilderBodyParameter


class ParameterLocation(str, Enum):
    HEADER = "header"
    PATH = "path"
    ENDPOINT_PATH = "endpointPath"
    QUERY = "query"
    BODY = "body"
    OTHER = "other"


class ParameterMethodLocation(Enum):
    POSITIONAL = auto()
    KEYWORD_ONLY = auto()
    KWARG = auto()


class ParameterDelimeter(str, Enum):
    SPACE = "space"
    PIPE = "pipe"
    TAB = "tab"
    COMMA = "comma"


class _ParameterBase(
    BaseModel, abc.ABC
):  # pylint: disable=too-many-instance-attributes
    """Base class for all parameters"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseType,
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.rest_api_name: str = yaml_data["restApiName"]
        self.client_name: str = self.yaml_data["clientName"]
        self.optional: bool = self.yaml_data["optional"]
        self.location: ParameterLocation = self.yaml_data["location"]
        self.client_default_value = self.yaml_data.get("clientDefaultValue", None)
        self.in_docstring = self.yaml_data.get("inDocstring", True)
        self.type = type
        if self.client_default_value is None:
            self.client_default_value = self.type.client_default_value
        # name of grouper if it is grouped by another parameter
        self.grouped_by: Optional[str] = self.yaml_data.get("groupedBy")
        # property matching property name to parameter name for grouping params
        # and flattened body params
        self.property_to_parameter_name: Optional[Dict[str, str]] = self.yaml_data.get(
            "propertyToParameterName"
        )
        self.flattened: bool = self.yaml_data.get("flattened", False)
        self.in_flattened_body: bool = self.yaml_data.get("inFlattenedBody", False)
        self.grouper: bool = self.yaml_data.get("grouper", False)

    @property
    def constant(self) -> bool:
        """Returns whether a parameter is a constant or not.
        Checking to see if it's required, because if not, we don't consider it
        a constant because it can have a value of None.
        """
        return not self.optional and isinstance(self.type, ConstantType)

    @property
    def description(self) -> str:
        base_description = self.yaml_data["description"]
        type_description = self.type.description(is_operation_file=True)
        if type_description:
            base_description = add_to_description(base_description, type_description)
        if self.optional and isinstance(self.type, ConstantType):
            base_description = add_to_description(
                base_description,
                f"Known values are {self.type.get_declaration()} and None.",
            )
        if not (self.optional or self.client_default_value):
            base_description = add_to_description(base_description, "Required.")
        if self.client_default_value is not None:
            base_description = add_to_description(
                base_description,
                f"Default value is {self.client_default_value_declaration}.",
            )
        if self.optional and self.client_default_value is None:
            base_description = add_to_description(
                base_description,
                f"Default value is {self.client_default_value_declaration}.",
            )
        if self.constant:
            base_description = add_to_description(
                base_description,
                "Note that overriding this default value may result in unsupported behavior.",
            )
        return base_description

    @property
    def client_default_value_declaration(self):
        """Declaration of parameter's client default value"""
        if self.client_default_value is None:
            return None
        return self.type.get_declaration(self.client_default_value)

    def type_annotation(self, **kwargs: Any) -> str:
        kwargs["is_operation_file"] = True
        type_annot = self.type.type_annotation(**kwargs)
        if self.optional and self.client_default_value is None:
            return f"Optional[{type_annot}]"
        return type_annot

    def docstring_text(self, **kwargs: Any) -> str:
        return self.type.docstring_text(**kwargs)

    def docstring_type(self, **kwargs: Any) -> str:
        return self.type.docstring_type(**kwargs)

    @property
    def serialization_type(self) -> str:
        return self.type.serialization_type

    def imports(self, async_mode: bool) -> FileImport:
        file_import = FileImport()
        file_import.merge(
            self.type.imports(is_operation_file=True, async_mode=async_mode)
        )
        if self.optional and self.client_default_value is None:
            file_import.add_submodule_import("typing", "Optional", ImportType.STDLIB)
        return file_import

    @property
    def method_location(self) -> ParameterMethodLocation:
        raise NotImplementedError("Please implement in children")

    @property
    def description_keyword(self) -> str:
        return (
            "param"
            if self.method_location == ParameterMethodLocation.POSITIONAL
            else "keyword"
        )

    @property
    def docstring_type_keyword(self) -> str:
        return (
            "type"
            if self.method_location == ParameterMethodLocation.POSITIONAL
            else "paramtype"
        )

    @property
    @abc.abstractmethod
    def in_method_signature(self) -> bool:
        ...

    def method_signature(self, is_python3_file: bool, async_mode: bool) -> str:
        type_annot = self.type_annotation(async_mode=async_mode)
        if is_python3_file:
            if self.client_default_value is not None or self.optional:
                return f"{self.client_name}: {type_annot} = {self.client_default_value_declaration},"
            return f"{self.client_name}: {type_annot},"
        if self.client_default_value is not None or self.optional:
            return f"{self.client_name}={self.client_default_value_declaration},  # type: {type_annot}"
        return f"{self.client_name},  # type: {type_annot}"


class _BodyParameterBase(_ParameterBase):
    """Base class for body parameters"""

    @property
    def is_partial_body(self) -> bool:
        """Whether it's part of a bigger body parameter, i.e. a MultipartBodyParameter"""
        return self.yaml_data.get("isPartialBody", False)

    @property
    def method_location(self) -> ParameterMethodLocation:
        return (
            ParameterMethodLocation.KWARG
            if self.constant
            else ParameterMethodLocation.POSITIONAL
        )

    @property
    def in_method_signature(self) -> bool:
        return not (self.flattened or self.grouped_by)


class BodyParameter(_BodyParameterBase):
    """Body parameter."""

    @property
    def content_types(self) -> List[str]:
        return self.yaml_data["contentTypes"]

    @property
    def default_content_type(self) -> str:
        return self.yaml_data["defaultContentType"]

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "BodyParameter":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_type(id(yaml_data["type"])),
        )


EntryBodyParameterType = TypeVar(
    "EntryBodyParameterType", bound=Union[BodyParameter, "RequestBuilderBodyParameter"]
)


class _MultipartBodyParameter(BodyParameter, Generic[EntryBodyParameterType]):
    """Base class for MultipartBodyParameter and RequestBuilderMultipartBodyParameter"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseType,
        entries: List[EntryBodyParameterType],
    ) -> None:
        super().__init__(yaml_data, code_model, type)
        self.entries = entries

    @property
    def in_method_signature(self) -> bool:
        # Right now, only legacy generates with multipart bodies
        # and legacy generates with the multipart body arguments splatted out
        return False


class MultipartBodyParameter(
    _MultipartBodyParameter[BodyParameter]  # pylint: disable=unsubscriptable-object
):
    """Multipart body parameter for Operation. Used for files and data input."""

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "MultipartBodyParameter":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_type(id(yaml_data["type"])),
            entries=[
                BodyParameter.from_yaml(entry, code_model)
                for entry in yaml_data["entries"]
            ],
        )


class Parameter(_ParameterBase):
    """Basic Parameter class"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseType,
    ) -> None:
        super().__init__(yaml_data, code_model, type=type)

        self.implementation: str = yaml_data["implementation"]
        self.skip_url_encoding: bool = self.yaml_data.get("skipUrlEncoding", False)
        self.explode: bool = self.yaml_data.get("explode", False)
        self.in_overload: bool = self.yaml_data["inOverload"]
        self.in_overriden: bool = self.yaml_data.get("inOverriden", False)
        self.delimiter: Optional[ParameterDelimeter] = self.yaml_data.get("delimiter")

    @property
    def in_method_signature(self) -> bool:
        return not (self.rest_api_name == "Accept" or self.grouped_by or self.flattened)

    @property
    def full_client_name(self) -> str:
        if self.implementation == "Client":
            return f"self._config.{self.client_name}"
        return self.client_name

    @property
    def xml_serialization_ctxt(self) -> str:
        return self.type.xml_serialization_ctxt or ""

    @property
    def method_location(self) -> ParameterMethodLocation:
        if not self.in_method_signature:
            raise ValueError(f"Parameter '{self.client_name}' is not in the method.")
        if self.grouper:
            return ParameterMethodLocation.POSITIONAL
        if self.constant:
            return ParameterMethodLocation.KWARG
        if self.rest_api_name == "Content-Type":
            if self.in_overload:
                return ParameterMethodLocation.KEYWORD_ONLY
            return ParameterMethodLocation.KWARG
        query_or_header = self.location in (
            ParameterLocation.HEADER,
            ParameterLocation.QUERY,
        )
        if (
            self.code_model.options["only_path_and_body_params_positional"]
            and query_or_header
        ):
            return ParameterMethodLocation.KEYWORD_ONLY
        return ParameterMethodLocation.POSITIONAL

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel"):
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_type(id(yaml_data["type"])),
        )


class ClientParameter(Parameter):
    """Client parameter"""

    @property
    def is_host(self) -> bool:
        return self.rest_api_name == "$host"

    @property
    def method_location(self) -> ParameterMethodLocation:
        if self.constant:
            return ParameterMethodLocation.KWARG
        if self.is_host and (
            self.code_model.options["version_tolerant"]
            or self.code_model.options["low_level_client"]
        ):
            # this means i am the base url
            return ParameterMethodLocation.KEYWORD_ONLY
        return ParameterMethodLocation.POSITIONAL


class ConfigParameter(Parameter):
    """Config Parameter"""

    @property
    def in_method_signature(self) -> bool:
        return not self.is_host

    @property
    def is_host(self) -> bool:
        return self.rest_api_name == "$host"

    @property
    def method_location(self) -> ParameterMethodLocation:
        if self.constant:
            return ParameterMethodLocation.KWARG
        return ParameterMethodLocation.POSITIONAL


def get_body_parameter(
    yaml_data: Dict[str, Any], code_model: "CodeModel"
) -> Union[BodyParameter, MultipartBodyParameter]:
    """Creates a regular body parameter or Multipart body parameter"""
    if yaml_data.get("entries"):
        return MultipartBodyParameter.from_yaml(yaml_data, code_model)
    return BodyParameter.from_yaml(yaml_data, code_model)
