# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
import abc
from enum import Enum, auto

from typing import Dict, Any, TYPE_CHECKING, List, Optional, Set, TypeVar, Union, Generic

from .imports import FileImport, ImportType, TypingSection
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

class ParameterMethodLocation(Enum):
    POSITIONAL = auto()
    KEYWORD_ONLY = auto()
    KWARG = auto()

class ParameterDelimeter(str, Enum):
    SPACE = "space"
    PIPE = "pipe"
    TAB = "tab"
    COMMA = "comma"

class _ParameterBase(BaseModel, abc.ABC):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseType,
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.client_name: str = self.yaml_data["clientName"]
        self.optional: bool = self.yaml_data["optional"]
        self.location: ParameterLocation = self.yaml_data["location"]
        self.client_default_value = self.yaml_data.get("clientDefaultValue", None)
        self.in_docstring = self.yaml_data.get("inDocstring", True)
        self.type = type
        if self.client_default_value is None:
            self.client_default_value = self.type.client_default_value

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
            base_description = add_to_description(base_description, f"Known values are {self.type.get_declaration()} and None.")
        if not (self.optional or self.client_default_value):
            base_description = add_to_description(base_description, "Required.")
        if self.client_default_value is not None:
            base_description = add_to_description(base_description, f"Default value is {self.client_default_value_declaration}.")
        if self.optional and self.client_default_value is None:
            base_description = add_to_description(base_description, f"Default value is {self.client_default_value_declaration}.")
        if self.constant:
            base_description = add_to_description(base_description, "Note that overriding this default value may result in unsupported behavior.")
        return base_description

    @property
    def client_default_value_declaration(self):
        if self.client_default_value is None:
            return None
        return self.type.get_declaration(self.client_default_value)

    def type_annotation(self) -> str:
        type_annot = self.type.type_annotation(is_operation_file=True)
        if self.optional and self.client_default_value is None:
            return f"Optional[{type_annot}]"
        return type_annot

    @property
    def docstring_text(self) -> str:
        return self.type.docstring_text

    @property
    def docstring_type(self) -> str:
        return self.type.docstring_type

    @property
    def serialization_type(self) -> str:
        return self.type.serialization_type

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.merge(self.type.imports(is_operation_file=True))
        if self.optional and self.client_default_value is None:
            file_import.add_submodule_import("typing", "Optional", ImportType.STDLIB)
        return file_import

    @property
    def method_location(self) -> ParameterMethodLocation:
        raise NotImplementedError("Please implement in children")

    @property
    def description_keyword(self) -> str:
        return "param" if self.method_location == ParameterMethodLocation.POSITIONAL else "keyword"

    @property
    def docstring_type_keyword(self) -> str:
        return "type" if self.method_location == ParameterMethodLocation.POSITIONAL else "paramtype"

    @property
    @abc.abstractmethod
    def in_method_signature(self) -> bool:
        ...

    def method_signature(self, is_python3_file: bool) -> str:
        type_annot = self.type_annotation()
        if is_python3_file:
            if self.client_default_value is not None or self.optional:
                return f"{self.client_name}: {type_annot} = {self.client_default_value_declaration},"
            return f"{self.client_name}: {type_annot},"
        if self.client_default_value is not None or self.optional:
            return f"{self.client_name}={self.client_default_value_declaration},  # type: {type_annot}"
        return f"{self.client_name},  # type: {type_annot}"

class _BodyParameterBase(_ParameterBase):
    @property
    def method_location(self) -> ParameterMethodLocation:
        return ParameterMethodLocation.KWARG if self.constant else ParameterMethodLocation.POSITIONAL

    @property
    def flattened(self) -> bool:
        raise NotImplementedError("Haven't implemented flattening yet")

    @property
    def in_method_signature(self) -> bool:
        return True


class BodyParameter(_BodyParameterBase):
    """Body parameters for the overload operations. Only has one type per overload
    """

    @property
    def content_types(self) -> List[str]:
        return self.yaml_data["contentTypes"]

    @property
    def default_content_type(self) -> str:
        return self.yaml_data["defaultContentType"]

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "BodyParameter":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_type(id(yaml_data["type"])),
        )

EntryBodyParameterType = TypeVar("EntryBodyParameterType", bound=Union[BodyParameter, "RequestBuilderBodyParameter"])

class _MultipartBodyParameter(BodyParameter, Generic[EntryBodyParameterType]):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel", type: BaseType, entries: List[EntryBodyParameterType]) -> None:
        super().__init__(yaml_data, code_model, type)
        self.entries = entries

class MultipartBodyParameter(_MultipartBodyParameter[BodyParameter]):

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "MultipartBodyParameter":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_type(id(yaml_data["type"])),
            entries=[BodyParameter.from_yaml(entry, code_model) for entry in yaml_data["entries"]]
        )

class UrlEncodedBodyParameter(_ParameterBase):
    ...

class Parameter(_ParameterBase):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseType,
    ) -> None:
        super().__init__(yaml_data, code_model, type=type)
        self.rest_api_name: str = yaml_data["restApiName"]
        self.implementation: str = yaml_data["implementation"]
        self.skip_url_encoding: bool = self.yaml_data.get("skipUrlEncoding", False)
        self.explode: bool = self.yaml_data.get("explode", False)
        self.in_overload: bool = self.yaml_data["inOverload"]
        self.in_overriden: bool = self.yaml_data.get("inOverriden", False)
        self.delimiter: Optional[ParameterDelimeter] = self.yaml_data.get("delimiter")

    @property
    def constraints(self):
        raise NotImplementedError("Haven't done constraints yet")

    @property
    def target_property_name(self):
        raise NotImplementedError("Haven't done parameter grouping yet")

    @property
    def in_method_signature(self) -> bool:
        return self.rest_api_name != "Accept"  # hiding accept header from users

    @property
    def full_client_name(self) -> str:
        if self.implementation == "Client":
            return f"self._config.{self.client_name}"
        return self.client_name

    @property
    def xml_serialization_ctxt(self) -> str:
        return self.type.xml_serialization_ctxt() or ""

    @property
    def method_location(self) -> ParameterMethodLocation:
        if not self.in_method_signature:
            raise ValueError(f"Parameter '{self.client_name}' is not in the method.")
        if self.constant:
            return ParameterMethodLocation.KWARG
        if self.location == ParameterLocation.QUERY:
            if self.code_model.options["only_path_and_body_params_positional"]:
                return ParameterMethodLocation.KEYWORD_ONLY
            return ParameterMethodLocation.POSITIONAL
        if self.location in (ParameterLocation.PATH, ParameterLocation.ENDPOINT_PATH):
            return ParameterMethodLocation.POSITIONAL
        # i'm a header
        if self.rest_api_name == "Content-Type":
            if self.in_overload:
                return ParameterMethodLocation.KEYWORD_ONLY
            return ParameterMethodLocation.KWARG
        if self.code_model.options["only_path_and_body_params_positional"]:
            return ParameterMethodLocation.KEYWORD_ONLY
        return ParameterMethodLocation.POSITIONAL

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel"):
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_type(id(yaml_data["type"]))
        )

class ClientParameter(Parameter):

    @property
    def is_host(self) -> bool:
        return self.rest_api_name == "$host"

    @property
    def method_location(self) -> ParameterMethodLocation:
        if self.constant:
            return ParameterMethodLocation.KWARG
        if (
            self.is_host and
            (self.code_model.options["version_tolerant"] or self.code_model.options["low_level_client"])
        ):
            # this means i am the base url
            return ParameterMethodLocation.KEYWORD_ONLY
        return ParameterMethodLocation.POSITIONAL

    def imports(self) -> FileImport:
        file_import = super().imports()
        legacy = not (self.code_model.options["low_level_client"] or self.code_model.options["version_tolerant"])
        if legacy and self.is_host:
            file_import.add_submodule_import("typing", "Optional", ImportType.STDLIB)
        return file_import

class ConfigParameter(Parameter):

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

def get_body_parameter(yaml_data: Dict[str, Any], code_model: "CodeModel") -> Union[BodyParameter, MultipartBodyParameter]:
    if yaml_data.get("entries"):
        return MultipartBodyParameter.from_yaml(yaml_data, code_model)
    return BodyParameter.from_yaml(yaml_data, code_model)
