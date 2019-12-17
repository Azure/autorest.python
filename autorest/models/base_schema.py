from .imports import FileImport

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, List


class BaseSchema(ABC):
    """This is the base class for all schema models.

    :param yaml_data: the yaml data for this schema
    :type yaml_data: dict[str, Any]
    """
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        **kwargs
    ):
        self.yaml_data = yaml_data
        self.default_value = yaml_data.get('defaultValue', None)
        self.xml_metadata = yaml_data.get('serialization', {}).get('xml', {})

    def imports(self):
        return FileImport()

    def xml_serialization_ctxt(self) -> Optional[str]:
        """Return the serialization context in case this schema is used in an operation.
        """
        attrs_list = []
        if self.xml_metadata.get('name'):
            attrs_list.append(f"'name': '{self.xml_metadata['name']}'")
        if self.xml_metadata.get('attribute', False):
            attrs_list.append("'attr': True")
        if self.xml_metadata.get('prefix', False):
            attrs_list.append(f"'prefix': '{self.xml_metadata['prefix']}'")
        if self.xml_metadata.get('namespace', False):
            attrs_list.append(f"'ns': '{self.xml_metadata['namespace']}'")
        return ", ".join(attrs_list)

    @property
    def id(self):
        return id(self.yaml_data)

    @abstractmethod
    def get_serialization_type(self) -> str:
        """The tag recognized by 'msrest' as a serialization/deserialization.

        'str', 'int', 'float', 'bool' or
        https://github.com/Azure/msrest-for-python/blob/b505e3627b547bd8fdc38327e86c70bdb16df061/msrest/serialization.py#L407-L416

        or the object schema name (e.g. DotSalmon).

        If list: '[str]'
        If dict: '{str}'
        """
        ...

    @abstractmethod
    def get_python_type(self, namespace: Optional[str] = None) -> str:
        """The python type used for RST syntax input.

        Special case for enum, for instance: 'str or ~namespace.EnumName'
        """
        ...

    def get_python_type_annotation(self) -> str:
        """The python type used for type annotation

        Special case for enum, for instance: Union[str, "EnumName"]
        """
        return self.get_python_type()

    def get_declaration(self, value) -> str:
        """Return the current value from YAML as a Python string that represents the constant.

        Example, if schema is "bytearray" and value is "foo",
        should return bytearray("foo", encoding="utf-8")
        as a string.

        This is important for constant serialization.

        By default, return value, since it works sometimes (integer)
        """
        return str(value)

    def get_validation_map(self) -> Dict[str, Any]:
        return None

    def get_serialization_constraints(self) -> List[str]:
        return None

    def __repr__(self):
        return f"<{self.__class__.__name__}>"