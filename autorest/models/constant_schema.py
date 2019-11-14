import logging
from .base_schema import BaseSchema
from .primitive_schemas import get_primitive_schema
from typing import Dict, Any, Optional

_LOGGER = logging.getLogger(__name__)

class ConstantSchema(BaseSchema):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        value: str,
        schema: Optional["PrimitiveSchema"]
    ):
        super(ConstantSchema, self).__init__(yaml_data)
        self.value = value
        self.schema = schema

    def get_serialization_type(self):
        return self.schema.get_serialization_type()

    def get_python_type(self, namespace=None):
        return self.schema.get_python_type(namespace)

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs) -> "ConstantSchema":
        name = yaml_data["language"]["default"]["name"] if yaml_data["language"]["default"].get('name') else ""
        _LOGGER.info("Parsing %s constant", name)
        return cls(
            yaml_data=yaml_data,
            value=yaml_data.get("value", {}).get("value", None),
            schema=get_primitive_schema(yaml_data['valueType'])
        )