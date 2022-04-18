# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
import abc
from enum import Enum, auto

from typing import Dict, Any, TYPE_CHECKING, List, Set, Union

from .imports import FileImport, ImportType, TypingSection
from .base_model import BaseModel
from .base_type import BaseType
from .constant_type import ConstantType

if TYPE_CHECKING:
    from .code_model import CodeModel

_LOGGER = logging.getLogger(__name__)

class ParameterLocation(str, Enum):
    HEADER = "header"
    PATH = "path"
    QUERY = "query"
    BODY = "body"

class ParameterMethodLocation(Enum):
    POSITIONAL = auto()
    KEYWORD_ONLY = auto()
    KWARG = auto()

class _BaseParameter(BaseModel, abc.ABC):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel"
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.client_name = yaml_data["clientName"]
        self.optional = yaml_data["optional"]
        self.client_default_value = yaml_data.get("clientDefaultValue", None)
        self.location = yaml_data["location"]

    @property
    def description(self) -> str:
        description = self.yaml_data["description"]
        if self.client_default_value:
            description += f" Default value is {self.client_default_value_declaration}"
        return description

    @property
    def method_location(self) -> ParameterMethodLocation:
        raise NotImplementedError("Please implement in children")

    @property
    def description_keyword(self) -> str:
        return "param" if self.method_location == ParameterMethodLocation.POSITIONAL else "keyword"

    @property
    def docstring_type_keyword(self) -> str:
        return "type" if self.method_location == ParameterMethodLocation.POSITIONAL else "paramtype"

    @abc.abstractmethod
    def type_annotation(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def client_default_value_declaration(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def in_method_signature(self) -> bool:
        ...

    def method_signature(self, is_python3_file: bool) -> str:
        type_annot = self.type_annotation()
        if is_python3_file:
            if self.client_default_value:
                return f"{self.client_name}: {type_annot} = {self.client_default_value_declaration},"
            return f"{self.client_name}: {type_annot},"
        if self.client_default_value:
            return f"{self.client_name}={self.client_default_value_declaration},  # type: {type_annot}"
        return f"{self.client_name},  # type: {type_annot}"

class _BodyParameter(_BaseParameter):
    """Base parent for SingleTypeBodyParameter and MultipleTypeBodyParameter"""

    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel") -> None:
        super().__init__(yaml_data, code_model)
        self.location = ParameterLocation.BODY

    @property
    def method_location(self) -> ParameterMethodLocation:
        return ParameterMethodLocation.POSITIONAL

    @property
    def flattened(self) -> bool:
        raise NotImplementedError("Haven't implemented flattening yet")

    @property
    def in_method_signature(self) -> bool:
        return True

class MultipleTypeBodyParameter(_BodyParameter):
    """Polymorphic base parent for SingleTypeBodyParameter and MultipleTypeBodyParameter
    """
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel", content_type_to_type: Dict[str, BaseType]):
        super().__init__(yaml_data, code_model)
        self.content_type_to_type = content_type_to_type
        self.types = self._create_types_property()

    def _create_types_property(self) -> List[BaseType]:
        types: List[BaseType] = []
        seen_ids: Set[int] = set()
        for type in self.content_type_to_type.values():
            if id(type.yaml_data) not in seen_ids:
                types.append(type)
            seen_ids.add(id(type.yaml_data))
        return types

    def serialization_type(self, content_type: str) -> str:
        return self.content_type_to_type[content_type].serialization_type

    def type_annotation(self) -> str:
        return f'Union[{", ".join(type.type_annotation(is_operation_file=True) for type in self.types)}]'

    @property
    def docstring_text(self) -> str:
        return " or ".join(t.docstring_text for t in self.types)

    @property
    def docstring_type(self) -> str:
        return " or ".join(t.docstring_type for t in self.types)

    @property
    def client_default_value_declaration(self):
        return self.types[0].get_declaration(self.client_default_value)

    def type_to_content_types(self, yaml_id: int) -> List[str]:
        return [
            k for k, v in self.content_type_to_type.items()
            if id(v.yaml_data) == yaml_id
        ]

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import("typing", "Union", ImportType.STDLIB)
        for type in self.types:
            file_import.merge(type.imports(is_operation_file=True))
        return file_import

    @property
    def constant(self) -> bool:
        return not self.optional and all(t for t in self.types if isinstance(t, ConstantType))

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "MultipleTypeBodyParameter":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            content_type_to_type={
                k: code_model.lookup_type(id(v))
                for k, v in yaml_data["contentTypeToType"].items()
            }
        )

class SingleTypeBodyParameter(_BodyParameter):
    """Body parameters for the overload operations. Only has one type per overload
    """
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseType,
        content_types: List[str],
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.type = type
        self.content_types = content_types

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.merge(self.type.imports(is_operation_file=True))
        return file_import

    @property
    def client_default_value_declaration(self):
        return self.type.get_declaration(self.client_default_value)

    def type_annotation(self) -> str:
        return self.type.type_annotation(is_operation_file=True)

    @property
    def docstring_text(self) -> str:
        return self.type.docstring_text

    @property
    def docstring_type(self) -> str:
        return self.type.docstring_type

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "SingleTypeBodyParameter":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_type(id(yaml_data["type"])),
            content_types=yaml_data["contentTypes"],
        )

class MultipartBodyParameter(_BaseParameter):
    ...

class UrlEncodedBodyParameter(_BaseParameter):
    ...

class Parameter(_BaseParameter):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseType,
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.type = type
        self.rest_api_name = yaml_data["restApiName"]
        self.implementation = yaml_data["implementation"]
        self.skip_url_encoding = self.yaml_data.get("skipUrlEncoding", False)
        self.explode: bool = self.yaml_data.get("explode", False)

    @property
    def constraints(self):
        raise NotImplementedError("Haven't done constraints yet")

    @property
    def target_property_name(self):
        raise NotImplementedError("Haven't done parameter grouping yet")

    @property
    def description(self):
        description = super().description
        description += (". " + self.type.description(is_operation_file=True))
        if self.constant:
            description += " Note that overriding this default value may result in unsuported behavior."
        return description

    @property
    def constant(self) -> bool:
        """Returns whether a parameter is a constant or not.
        Checking to see if it's required, because if not, we don't consider it
        a constant because it can have a value of None.
        """
        return not self.optional and isinstance(self.type, ConstantType)

    @property
    def in_method_signature(self) -> bool:
        return self.rest_api_name != "Accept"  # hiding accept header from users

    def type_annotation(self) -> str:
        return self.type.type_annotation(is_operation_file=True)

    @property
    def client_default_value_declaration(self):
        return self.type.get_declaration(self.client_default_value)

    @property
    def serialization_type(self) -> str:
        return self.type.serialization_type

    @property
    def docstring_type(self) -> str:
        return self.type.docstring_type

    @property
    def full_client_name(self) -> str:
        if self.implementation == "Client":
            return f"self._config.{self.client_name}"
        return self.client_name

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
        if self.location == ParameterLocation.PATH:
            return ParameterMethodLocation.POSITIONAL
        # i'm a header
        if self.rest_api_name == "Content-Type":
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

    def imports(self) -> FileImport:
        file_import = self.type.imports(is_operation_file=True)
        if self.optional:
            file_import.add_submodule_import(
                "typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL
            )
        return file_import

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
