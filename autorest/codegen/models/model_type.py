# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional, Union, Type, TYPE_CHECKING, cast
from .base_type import BaseType
from .dictionary_type import DictionaryType
from .property import Property
from .imports import FileImport, ImportModel, ImportType, TypingSection

if TYPE_CHECKING:
    from .code_model import CodeModel

def _get_properties(type: "ModelType", properties: List[Property]) -> List[Property]:
    for parent in type.parents:
        # here we're adding the properties from our parents

        # need to make sure that the properties we choose from our parent also don't contain
        # any of our own properties
        property_names = set([p.client_name for p in properties] + [p.client_name for p in type.properties])
        chosen_parent_properties = [p for p in parent.properties if p.client_name not in property_names]
        properties = (
            _get_properties(parent, chosen_parent_properties) + properties
        )
    return properties


class ModelType(BaseType):  # pylint: disable=too-many-instance-attributes
    """Represents a class ready to be serialized in Python.

    :param str name: The name of the class.
    :param str description: The description of the class.
    :param properties: the optional properties of the class.
    :type properties: dict(str, str)
    """

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        *,
        properties: Optional[List[Property]] = None,
        parents: Optional[List["ModelType"]] = None,
        discriminated_subtypes: Optional[Dict[str, "ModelType"]] = None,
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.name = self.yaml_data["name"]
        self.max_properties: Optional[int] = self.yaml_data.get("maxProperties")
        self.min_properties: Optional[int] = self.yaml_data.get("minProperties")
        self.properties = properties or []
        self.parents = parents or []
        self.discriminated_subtypes = discriminated_subtypes or {}
        self.discriminator_value = self.yaml_data.get("discriminatorValue")
        self._created_json_template_representation = False

    @property
    def serialization_type(self) -> str:
        if self.code_model.options["models_mode"]:
            return self.name
        return "object"

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        if self.code_model.options["models_mode"]:
            retval = f"_models.{self.name}"
            return retval if is_operation_file else f'"{retval}"'
        return "JSON"

    @property
    def docstring_type(self) -> str:
        return f"~{self.code_model.namespace}.models.{self.name}" if self.code_model.options["models_mode"] else "JSON"

    def description(self, *, is_operation_file: bool = False) -> str:
        return "" if is_operation_file else self.yaml_data.get("description", self.name)

    @property
    def docstring_text(self) -> str:
        return self.name if self.code_model.options["models_mode"] else "JSON object"

    def get_declaration(self, value: Any) -> str:
        return f"{self.name}()"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    def get_json_template_representation(self, **kwargs: Any) -> Any:
        if self._created_json_template_representation:
            return "..."  # do this to avoid loop
        self._created_json_template_representation = True
        # don't add additional properties, because there's not really a concept of
        # additional properties in the template
        representation = {
            f'"{prop.name}"': prop.get_json_template_representation(
                **kwargs
            )
            for prop in [
                p
                for p in self.properties
                if not (p.is_discriminator or p.name == "additional_properties")
            ]
        }
        try:
            # add discriminator prop if there is one
            discriminator = next(p for p in self.properties if p.is_discriminator)
            representation[discriminator.name] = (
                self.discriminator_value or discriminator.name
            )
        except StopIteration:
            pass

        # once we've finished, we want to reset created_json_template_representation to false
        # so we can call it again
        self._created_json_template_representation = False
        return representation

    @classmethod
    def from_yaml(
        cls, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> "ModelType":
        raise ValueError(
            "You shouldn't call from_yaml for ModelType to avoid recursion. "
            "Please initial a blank ModelType, then call .fill_instance_from_yaml on the created type."
        )

    def fill_instance_from_yaml(
        self, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> None:
        from . import build_type
        self.parents = [
            cast(ModelType, build_type(bm, code_model))
            for bm in yaml_data.get("parents", [])
        ]
        properties = [
            Property.from_yaml(p, code_model) for p in yaml_data["properties"]
        ]
        self.properties = _get_properties(self, properties)
        # checking to see if this is a polymorphic class
        self.discriminated_subtypes = {
            discriminator_value: cast(ModelType, build_type(subtype_yaml_data, code_model))
            for discriminator_value, subtype_yaml_data in yaml_data["discriminatedSubtypes"].items()
        }

    @property
    def has_readonly_or_constant_property(self) -> bool:
        return any(x.readonly or x.constant for x in self.properties)

    @property
    def discriminator(self) -> Optional[Property]:
        try:
            return next(p for p in self.properties if p.is_discriminator)
        except StopIteration:
            return None

    def imports(self, *, is_operation_file: bool) -> FileImport:
        file_import = FileImport()
        if self.code_model.options["models_mode"]:
            if is_operation_file:
                return file_import
            file_import.add_import(
                "__init__",
                ImportType.LOCAL,
                typing_section=TypingSection.TYPING,
                alias="_models",
            )
            return file_import
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.add_import("sys", ImportType.STDLIB)
        file_import.define_mypy_type(
            "JSON",
            "MutableMapping[str, Any] # pylint: disable=unsubscriptable-object",
            None,
            {
                (3, 9): ImportModel(
                    TypingSection.CONDITIONAL,
                    ImportType.STDLIB,
                    "collections.abc",
                    submodule_name="MutableMapping",
                ),
                None: ImportModel(
                    TypingSection.CONDITIONAL,
                    ImportType.STDLIB,
                    "typing",
                    submodule_name="MutableMapping",
                ),
            },
        )
        return file_import
