from .imports import FileImport

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseSchema(ABC):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        name,
        **kwargs
    ):
        self.yaml_data = yaml_data
        self.name = name
        self.default_value = yaml_data.get('defaultValue', None)
        self.discriminator_name = yaml_data['discriminator']['property']['language']['default']['name'] if yaml_data.get('discriminator') else None
        self.discriminator_value = yaml_data.get('discriminatorValue', None)

    def imports(self):
        return FileImport()

    @property
    def id(self):
        return id(self.yaml_data)

    @abstractmethod
    def get_serialization_type(self):
        ...

    @abstractmethod
    def get_doc_string_type(self, namespace=None):
        ...
