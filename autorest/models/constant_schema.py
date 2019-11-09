import logging
from .base_schema import BaseSchema
from .primitive_schemas import get_primitive_schema
from typing import Dict, Any, Optional

_LOGGER = logging.getLogger(__name__)

class ConstantSchema(BaseSchema):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name: str,
        value: str,
        schema: Optional["PrimitiveSchema"]
    ):
        super(ConstantSchema, self).__init__(yaml_data, name)
        self.value = value
        self.schema = schema

    def get_serialization_type(self):
        return self.schema.schema_type

    def get_doc_string_type(self, namespace=None):
        return self.schema.get_doc_string_type(namespace)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "ConstantSchema":
        name = yaml_data["language"]["default"]["name"] if yaml_data["language"]["default"].get('name') else ""
        _LOGGER.info("Parsing %s constant", name)
        return cls(
            yaml_data=yaml_data,
            name=name,
            value=yaml_data.get("value"),
            schema=get_primitive_schema(name, yaml_data['valueType'])
        )