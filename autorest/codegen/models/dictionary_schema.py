# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional
from .base_schema import BaseSchema
from .imports import FileImport, ImportType

class DictionarySchema(BaseSchema):
    """Schema for dictionaries that will be serialized.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    :param element_type: The type of the value for the dictionary
    :type element_type: ~autorest.models.BaseSchema
    """
    def __init__(
        self,
        namespace: str,
        yaml_data: Dict[str, Any],
        element_type: "BaseSchema",
        *,
        additional_properties: bool = False
    ):
        super(DictionarySchema, self).__init__(namespace=namespace, yaml_data=yaml_data)
        self.element_type = element_type
        self.additional_properties = additional_properties


    @property
    def serialization_type(self) -> str:
        """Returns the serialization value for msrest.

        :return: The serialization value for msrest
        :rtype: str
        """
        return f"{{{self.element_type.serialization_type}}}"

    @property
    def type_annotation(self) -> str:
        """The python type used for type annotation

        :return: The type annotation for this schema
        :rtype: str
        """
        return f'Dict[str, {self.element_type.type_annotation}]'

    @property
    def docstring_text(self) -> str:
        return "dict"

    @property
    def docstring_type(self) -> str:
        """The python type used for RST syntax input and type annotation.

        :param str namespace: Optional. The namespace for the models.
        """
        return f'dict[str, {self.element_type.docstring_type}]'

    def xml_serialization_ctxt(self) -> Optional[str]:
        raise NotImplementedError("Dictionary schema does not support XML serialization.")

    @classmethod
    def from_yaml(cls, namespace: str, yaml_data: Dict[str, Any], **kwargs: Any) -> "DictionarySchema":
        """Constructs a DictionarySchema from yaml data.

        :param yaml_data: the yaml data from which we will construct this schema
        :type yaml_data: dict[str, Any]

        :return: A created DictionarySchema
        :rtype: ~autorest.models.DictionarySchema
        """
        for_additional_properties = kwargs.pop('for_additional_properties', False)

        element_schema = yaml_data['elementType']

        from . import build_schema  # pylint: disable=import-outside-toplevel
        element_type = build_schema(
            yaml_data=element_schema,
            for_additional_properties=for_additional_properties,
            **kwargs
        )

        return cls(
            namespace=namespace,
            yaml_data=yaml_data,
            element_type=element_type,
            additional_properties=for_additional_properties
        )

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_from_import("typing", "Dict", ImportType.STDLIB)
        file_import.merge(self.element_type.imports())
        return file_import
