# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, List, Optional, TYPE_CHECKING, cast
from .base_type import BaseType
from .property import Property
from .imports import FileImport, ImportType, TypingSection

if TYPE_CHECKING:
    from .code_model import CodeModel


def _get_properties(type: "ModelType", properties: List[Property]) -> List[Property]:
    for parent in type.parents:
        # here we're adding the properties from our parents

        # need to make sure that the properties we choose from our parent also don't contain
        # any of our own properties
        property_names = set(
            [p.client_name for p in properties]
            + [p.client_name for p in type.properties]
        )
        chosen_parent_properties = [
            p for p in parent.properties if p.client_name not in property_names
        ]
        properties = _get_properties(parent, chosen_parent_properties) + properties
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
        discriminated_subtypes: Optional[Dict[str, str]] = None,
    ) -> None:
        super().__init__(yaml_data=yaml_data, code_model=code_model)
        self.name: str = self.yaml_data["name"]
        self.max_properties: Optional[int] = self.yaml_data.get("maxProperties")
        self.min_properties: Optional[int] = self.yaml_data.get("minProperties")
        self.properties = properties or []
        self.parents = parents or []
        self.discriminated_subtypes = discriminated_subtypes or {}
        self.discriminator_value: Optional[str] = self.yaml_data.get(
            "discriminatorValue"
        )
        self._created_json_template_representation = False

    @property
    def is_xml(self) -> bool:
        return self.yaml_data.get("isXml", False)

    @property
    def serialization_type(self) -> str:
        if self.code_model.options["models_mode"]:
            return self.name
        return "object"

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        if self.code_model.options["models_mode"]:
            retval = f"_models.{self.name}"
            return retval if is_operation_file else f'"{retval}"'
        return "ET.Element" if self.is_xml else "JSON"

    @property
    def docstring_type(self) -> str:
        if self.code_model.options["models_mode"]:
            return f"~{self.code_model.namespace}.models.{self.name}"
        return "ET.Element" if self.is_xml else "JSON"

    def description(self, *, is_operation_file: bool = False) -> str:
        return "" if is_operation_file else self.yaml_data.get("description", self.name)

    @property
    def docstring_text(self) -> str:
        if self.code_model.options["models_mode"]:
            return self.name
        return "XML Element" if self.is_xml else "JSON object"

    def get_declaration(self, value: Any) -> str:
        return f"{self.name}()"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.name}>"

    @property
    def xml_serialization_ctxt(self) -> Optional[str]:
        # object schema contains _xml_map, they don't need serialization context
        return ""

    @property
    def xml_map_content(self) -> Optional[str]:
        # This is NOT an error on the super call, we use the serialization context for "xml_map",
        # but we don't want to write a serialization context for an object.
        return super().xml_serialization_ctxt

    def get_json_template_representation(
        self,
        *,
        optional: bool = True,
        client_default_value_declaration: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Any:
        if self._created_json_template_representation:
            return "..."  # do this to avoid loop
        self._created_json_template_representation = True
        # don't add additional properties, because there's not really a concept of
        # additional properties in the template
        representation = {
            f'"{prop.rest_api_name}"': prop.get_json_template_representation(
                optional=optional,
                client_default_value_declaration=client_default_value_declaration,
                description=description,
            )
            for prop in [
                p
                for p in self.properties
                if not (p.is_discriminator or p.client_name == "additional_properties")
            ]
        }
        try:
            # add discriminator prop if there is one
            discriminator = next(p for p in self.properties if p.is_discriminator)
            representation[discriminator.rest_api_name] = (
                self.discriminator_value or discriminator.rest_api_name
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
        self.discriminated_subtypes = self.yaml_data.get("discriminatedSubtypes", {})

    @property
    def has_readonly_or_constant_property(self) -> bool:
        return any(x.readonly or x.constant for x in self.properties)

    @property
    def discriminator(self) -> Optional[Property]:
        try:
            return next(p for p in self.properties if p.is_discriminator)
        except StopIteration:
            return None

    @property
    def instance_check_template(self) -> str:
        if self.code_model.options["models_mode"]:
            return "isinstance({}, msrest.Model)"
        return "isinstance({}, MutableMapping)"

    def imports(self, **kwargs: Any) -> FileImport:
        file_import = FileImport()
        if self.code_model.options["models_mode"]:
            return file_import
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.add_import("sys", ImportType.STDLIB)
        file_import.define_mutable_mapping_type()
        if self.is_xml:
            file_import.add_submodule_import(
                "xml.etree", "ElementTree", ImportType.STDLIB, alias="ET"
            )
        return file_import
