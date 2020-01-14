# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict

from .base_model import BaseModel
from .constant_schema import ConstantSchema
from .base_schema import BaseSchema


class Property(BaseModel):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        schema: BaseSchema,
        original_swagger_name: str,
        *,
        description: str = None
    ):
        super().__init__(yaml_data)
        self.name = name
        self.schema = schema
        self.original_swagger_name = original_swagger_name

        self.required: bool = yaml_data.get('required', False)
        self.readonly: bool = yaml_data.get('readOnly', False)
        self.is_discriminator: bool = yaml_data.get('isDiscriminator', False)
        # this bool doesn't consider you to be constant if you are a discriminator
        self.constant: bool = isinstance(self.schema, ConstantSchema) and not self.is_discriminator

        if description:
            self.description = description
        else:
            yaml_description = yaml_data['language']['python']['description'].strip()
            if yaml_description == 'MISSING-SCHEMA-DESCRIPTION-OBJECTSCHEMA':
                self.description = name + "."
            elif 'MISSING' in yaml_description:
                self.description = ""
            else:
                self.description = yaml_description

        validation_map: Dict[str, Any] = {}
        if self.required:
            validation_map['required'] = True
        if self.readonly:
            validation_map['readonly'] = True
        if self.constant:
            validation_map['constant'] = True
        if self.schema.get_validation_map():
            validation_map.update(self.schema.get_validation_map()) # type: ignore
        self.validation_map = validation_map or None

    @property
    def escaped_swagger_name(self) -> str:
        """Return the RestAPI name correctly escaped for serialization.
        """
        return self.original_swagger_name.replace('.', '\\\\.')

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], **kwargs) -> "Property":
        from . import build_schema  # pylint: disable=import-outside-toplevel
        name = yaml_data['language']['python']['name']
        has_additional_properties = kwargs.pop("has_additional_properties", None)
        if name == 'additional_properties' and has_additional_properties:
            name = 'additional_properties1'
        schema = build_schema(yaml_data=yaml_data['schema'], **kwargs)
        return cls(
            name=name,
            schema=schema,
            original_swagger_name=yaml_data['serializedName'],
            yaml_data=yaml_data
        )
