from .base_schema import BaseSchema
from typing import Any, Dict, Optional

class DictionarySchema(BaseSchema):
    """Schema for dictionaries that will be serialized.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    :param element_type: The type of the value for the dictionary
    :type element_type: ~autorest.models.BaseSchema
    """
    def __init__(self, yaml_data: Dict[str, Any], element_type: "BaseSchema", **kwargs: Any):
        super(DictionarySchema, self).__init__(yaml_data, **kwargs)
        self.element_type = element_type
        self.additional_properties = kwargs.pop('additional_properties', False)


    def get_serialization_type(self) -> str:
        """Returns the serialization value for msrest.

        :return: The serialization value for msrest
        :rtype: str
        """
        return "{{{}}}".format(self.element_type.get_serialization_type())

    def get_python_type_annotation(self) -> str:
        """The python type used for type annotation

        :return: The type annotation for this schema
        :rtype: str
        """
        return f'Dict[str, {self.element_type.get_python_type_annotation()}]'

    def get_python_type(self, namespace: Optional[str] = None) -> str:
        """The python type used for RST syntax input and type annotation.

        :param str namespace: Optional. The namespace for the models.
        """
        return 'dict[str, {}]'.format(self.element_type.get_python_type(namespace))

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, str], **kwargs: Any) -> "DictionarySchema":
        """Constructs a DictionarySchema from yaml data.

        :param yaml_data: the yaml data from which we will construct this schema
        :type yaml_data: dict[str, Any]

        :return: A created DictionarySchema
        :rtype: ~autorest.models.DictionarySchema
        """
        for_additional_properties = kwargs.pop('for_additional_properties', False)

        element_schema = yaml_data['elementType']

        from . import build_schema
        element_type = build_schema(
            yaml_data=element_schema,
            for_additional_properties=for_additional_properties,
            **kwargs
        )

        return cls(
            yaml_data=yaml_data,
            element_type=element_type,
            additional_properties=for_additional_properties
        )