# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional, Union, Type, TYPE_CHECKING
from .base_schema import BaseSchema
from .dictionary_schema import DictionarySchema
from .property import Property
from .imports import FileImport, ImportModel, ImportType, TypingSection

if TYPE_CHECKING:
    from .code_model import CodeModel


class ObjectSchema(BaseSchema):  # pylint: disable=too-many-instance-attributes
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
        **kwargs,
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.name = self.yaml_data["name"]
        self.max_properties: Optional[int] = kwargs.pop("max_properties", None)
        self.min_properties: Optional[int] = kwargs.pop("min_properties", None)
        self.properties: List[Property] = kwargs.pop("properties", [])
        self.base_models: Union[List[int], List["ObjectSchema"]] = kwargs.pop(
            "base_models", []
        )
        self.subtype_map: Optional[Dict[str, str]] = kwargs.pop("subtype_map", None)
        self.discriminator_name: Optional[str] = kwargs.pop("discriminator_name", None)
        self.discriminator_value: Optional[str] = kwargs.pop(
            "discriminator_value", None
        )
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
        return "" if is_operation_file else self.yaml_data["description"]

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
    ) -> "ObjectSchema":
        """Returns a ClassType from the dict object constructed from a yaml file.

        WARNING: This guy might create an infinite loop.

        :param str name: The name of the class type.
        :param yaml_data: A representation of the schema of a class type from a yaml file.
        :type yaml_data: dict(str, str)
        :returns: A ClassType.
        :rtype: ~autorest.models.schema.ClassType
        """
        obj = cls(yaml_data, code_model, "", description="")
        obj.fill_instance_from_yaml(yaml_data, code_model)
        return obj

    def fill_instance_from_yaml(
        self, yaml_data: Dict[str, Any], code_model: "CodeModel"
    ) -> None:
        name = yaml_data["name"]
        # checking to see if there is a parent class and / or additional properties
        base_models = [
            ObjectSchema.from_yaml(bm, code_model)
            for bm in yaml_data.get("baseModels", [])
        ]
        properties = [
            Property.from_yaml(p, code_model) for p in yaml_data["properties"]
        ]

        # checking to see if this is a polymorphic class
        subtype_map = None
        if yaml_data.get("discriminator"):
            subtype_map = {}
            # map of discriminator value to child's name
            for children_yaml in yaml_data["discriminator"]["immediate"].values():
                subtype_map[children_yaml["discriminatorValue"]] = children_yaml[
                    "language"
                ]["python"]["name"]
        # this is to ensure that the attribute map type and property type are generated correctly

        self.yaml_data = yaml_data
        self.name = name
        self.properties = properties
        self.base_models = base_models
        self.subtype_map = subtype_map
        self.discriminator_name = (
            yaml_data["discriminator"]["property"]["language"]["python"]["name"]
            if yaml_data.get("discriminator")
            else None
        )
        self.discriminator_value = yaml_data.get("discriminatorValue", None)

    @property
    def has_readonly_or_constant_property(self) -> bool:
        return any(x.readonly or x.constant for x in self.properties)

    @property
    def property_with_discriminator(self) -> Any:
        try:
            return next(
                p
                for p in self.properties
                if getattr(p.type, "discriminator_name", None)
            )
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
