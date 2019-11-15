from .imports import FileImport
from ..common.utils import get_property_name

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseSchema(ABC):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        **kwargs
    ):
        self.yaml_data = yaml_data
        self.default_value = yaml_data.get('defaultValue', None)

    def imports(self):
        return FileImport()

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
    def get_python_type(self, namespace=None):
        """That the python type if used for input using RST syntax.

        Special case for enum, for instance: 'str or ~namespace.EnumName'
        """
        ...

    def get_python_type_annotation(self):
        """That the python type if used for input using "typing" syntax

        Special case for enum, for instance: Union[str, "EnumName"]
        """
        return self.get_python_type()
