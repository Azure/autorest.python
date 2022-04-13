# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from enum import Enum, auto

from typing import Dict, Any, TYPE_CHECKING, List

from .imports import FileImport, ImportType, TypingSection
from .base_model import BaseModel
from .base_type import BaseType
from .constant_type import ConstantType
from .utils import MultipleTypeModel, UNDEFINED

if TYPE_CHECKING:
    from .code_model import CodeModel

_LOGGER = logging.getLogger(__name__)

class ParameterLocation(str, Enum):
    HEADER = "header"
    PATH = "path"
    QUERY = "query"

class ParameterMethodLocation(Enum):
    POSITIONAL = auto()
    KEYWORD_ONLY = auto()
    KWARG = auto()

class _BaseParameter(BaseModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel"
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.client_name = yaml_data["clientName"]
        self.optional = yaml_data["optional"]
        self.client_default_value = yaml_data.get("clientDefaultValue", UNDEFINED)

    @property
    def description(self) -> str:
        return self.yaml_data["description"]

    @property
    def method_location(self) -> ParameterMethodLocation:
        raise NotImplementedError("Please implement in children")

    @property
    def description_keyword(self) -> str:
        return "param" if self.method_location == ParameterMethodLocation.POSITIONAL else "keyword"

    @property
    def docstring_type_keyword(self) -> str:
        return "type" if self.method_location == ParameterMethodLocation.POSITIONAL else "paramtype"

class BodyParameter(_BaseParameter, MultipleTypeModel):
    def __init__(self, yaml_data: Dict[str, Any], code_model: "CodeModel", content_type_to_type: Dict[str, BaseType]):
        super().__init__(
            yaml_data=yaml_data, code_model=code_model, content_type_to_type=content_type_to_type
        )

    @property
    def method_location(self) -> ParameterMethodLocation:
        return ParameterMethodLocation.POSITIONAL

    @property
    def flattened(self) -> bool:
        raise NotImplementedError("Haven't implemented flattening yet")

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "BodyParameter":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            content_type_to_type={
                k: code_model.lookup_schema(id(v))
                for k, v in yaml_data["content"].items()
            }
        )

class OverloadBodyParameter(_BaseParameter):
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


class MultipartBodyParameter(BodyParameter):
    ...

class UrlEncodedBodyParameter(BodyParameter):
    ...

class Parameter(_BaseParameter):
    """Polymorphic parent of QueryParameter, HeaderParameter, and PathParameter.

    Delegates to them based off of knowledge.
    """
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        type: BaseType,
    ) -> None:
        super().__init__(yaml_data, code_model)
        self.type = type
        self.rest_api_name = yaml_data["restApiName"]
        self.location = None  # discriminator
        self.implementation = yaml_data["implementation"]

    @property
    def constraints(self):
        raise NotImplementedError("Haven't done constraints yet")

    @property
    def target_property_name(self):
        raise NotImplementedError("Haven't done parameter grouping yet")

    @property
    def description(self):
        description = super().description
        description += self.type.description(is_operation_file=True)
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
        return True

    def type_annotation(self) -> str:
        return self.type.type_annotation(is_operation_file=True)

    @property
    def serialization_type(self) -> str:
        return self.type.serialization_type

    @property
    def docstring_type(self) -> str:
        return self.type.docstring_type

    def method_signature(self, is_python3_file: bool) -> str:
        type_annot = self.type_annotation()
        if is_python3_file:
            if self.optional:
                return f"{self.client_name}: {type_annot} = None,"
            return f"{self.client_name}: {type_annot},"
        if self.optional:
            return f"{self.client_name}=None,  # type: {type_annot}"
        return f"{self.client_name},  # type: {type_annot}"

    @property
    def full_client_name(self) -> str:
        if self.implementation == "Client":
            return f"self._config.{self.client_name}"
        return self.client_name

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "Parameter":
        parameter_class = cls
        if yaml_data["location"] == "header":
            parameter_class = HeaderParameter
        elif yaml_data["location"] == "query":
            parameter_class = QueryParameter
        elif yaml_data["location"] == "path":
            parameter_class = PathParameter
        return parameter_class(
            yaml_data=yaml_data,
            code_model=code_model,
            type=code_model.lookup_schema(id(yaml_data["type"]))
        )

    def imports(self) -> FileImport:
        file_import = self.type.imports(is_operation_file=True)
        if self.optional:
            file_import.add_submodule_import(
                "typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL
            )
        return file_import

class QueryParameter(Parameter):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.location = "query"

    @property
    def explode(self):
        raise NotImplementedError("Haven't implemented explode yet")

    @property
    def method_location(self) -> ParameterMethodLocation:
        if self.code_model.options["only_path_and_body_params_positional"]:
            return ParameterMethodLocation.KEYWORD_ONLY
        return ParameterMethodLocation.POSITIONAL

class PathParameter(Parameter):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.location = "path"
        self.skip_url_encoding = self.yaml_data.get("skipUrlEncoding", False)

    @property
    def method_location(self) -> ParameterMethodLocation:
        return ParameterMethodLocation.POSITIONAL

class HeaderParameter(Parameter):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.location = "header"

    @property
    def in_method_signature(self) -> bool:
        return self.rest_api_name != "Accept"  # don't allow users to change accept header right now

    @property
    def method_location(self) -> ParameterMethodLocation:
        if not self.in_method_signature:
            raise ValueError(f"Parameter '{self.client_name}' is not in the method.")
        if self.code_model.options["only_path_and_body_params_positional"]:
            return ParameterMethodLocation.KEYWORD_ONLY
        return ParameterMethodLocation.POSITIONAL
