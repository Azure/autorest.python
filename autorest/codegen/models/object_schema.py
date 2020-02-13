# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional
from .base_schema import BaseSchema
from .dictionary_schema import DictionarySchema
from .property import Property


class ObjectSchema(BaseSchema):  # pylint: disable=too-many-instance-attributes
    """Represents a class ready to be serialized in Python.

    :param str name: The name of the class.
    :param str description: The description of the class.
    :param properties: the optional properties of the class.
    :type properties: dict(str, str)
    """

    def __init__(self, namespace: str, yaml_data: Dict[str, Any], name: str, description: str = "", **kwargs):
        super(ObjectSchema, self).__init__(namespace=namespace, yaml_data=yaml_data)
        self.name = name
        self.description = description
        self.max_properties = kwargs.pop("max_properties", None)
        self.min_properties = kwargs.pop("min_properties", None)
        self.properties = kwargs.pop("properties", None)
        self.is_exception = kwargs.pop("is_exception", False)
        self.base_model = kwargs.pop("base_model", None)
        self.subtype_map = kwargs.pop("subtype_map", None)
        self.discriminator_name = kwargs.pop("discriminator_name", None)
        self.discriminator_value = kwargs.pop("discriminator_value", None)

    @property
    def serialization_type(self) -> str:
        return self.name

    @property
    def type_annotation(self) -> str:
        return f'"{self.name}"'

    @property
    def operation_type_annotation(self) -> str:
        return f'"models.{self.name}"'

    @property
    def docstring_type(self):
        return f"~{self.namespace}.models.{self.name}"

    @property
    def docstring_text(self) -> str:
        return self.name

    def get_declaration(self, value: Any) -> str:
        return f"{self.name}()"

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name}>"

    @property
    def has_xml_serialization_ctxt(self):
        return False

    def xml_serialization_ctxt(self) -> Optional[str]:
        # object schema contains _xml_map, they don't need serialization context
        return ""

    def xml_map_content(self):
        if not self.xml_metadata:
            raise ValueError("This object does not contain XML metadata")
        # This is NOT an error on the super call, we use the serialization context for "xml_map",
        # but we don't want to write a serialization context for an object.
        return super().xml_serialization_ctxt()

    @classmethod
    def from_yaml(cls, namespace: str, yaml_data: Dict[str, Any], **kwargs) -> "ObjectSchema":
        """Returns a ClassType from the dict object constructed from a yaml file.

        WARNING: This guy might create an infinite loop.

        :param str name: The name of the class type.
        :param yaml_data: A representation of the schema of a class type from a yaml file.
        :type yaml_data: dict(str, str)
        :returns: A ClassType.
        :rtype: ~autorest.models.schema.ClassType
        """
        obj = cls(namespace, yaml_data, "", description="")
        obj.fill_instance_from_yaml(namespace, yaml_data)
        return obj

    def fill_instance_from_yaml(self, namespace: str, yaml_data: Dict[str, Any], **kwargs) -> None:
        properties = []
        base_model = None

        # checking to see if there is a parent class and / or additional properties
        if yaml_data.get("parents"):
            immediate_parents = yaml_data["parents"]["immediate"]
            # checking if object has a parent
            if immediate_parents:
                for immediate_parent in immediate_parents:
                    if immediate_parent["type"] == "dictionary":
                        additional_properties_schema = DictionarySchema.from_yaml(
                            namespace=namespace, yaml_data=immediate_parent, for_additional_properties=True, **kwargs
                        )
                        properties.append(
                            Property(
                                name="additional_properties",
                                schema=additional_properties_schema,
                                original_swagger_name="",
                                yaml_data={},
                                description="Unmatched properties from the message are deserialized to this collection."
                            )
                        )
                    elif immediate_parent["language"]["default"]["name"] != yaml_data["language"]["default"]["name"]:
                        base_model = id(immediate_parent)

        # checking to see if this is a polymorphic class
        subtype_map = None
        if yaml_data.get("discriminator"):
            subtype_map = {}
            # map of discriminator value to child's name
            for children_yaml in yaml_data["discriminator"]["immediate"].values():
                subtype_map[children_yaml["discriminatorValue"]] = children_yaml["language"]["python"]["name"]

        if yaml_data.get("properties"):
            properties += [
                Property.from_yaml(p, has_additional_properties=len(properties) > 0, **kwargs)
                for p in yaml_data["properties"]
            ]
        # this is to ensure that the attribute map type and property type are generated correctly

        name = yaml_data["language"]["python"]["name"]

        description = yaml_data["language"]["python"]["description"]
        is_exception = None
        exceptions_set = kwargs.pop("exceptions_set", None)
        if exceptions_set:
            if yaml_data["language"]["python"]["name"] in exceptions_set:
                is_exception = True

        self.yaml_data = yaml_data
        self.name = name
        self.description = description
        self.properties = properties
        self.base_model = base_model
        self.is_exception = is_exception
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
