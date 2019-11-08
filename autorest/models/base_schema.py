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
        self.discriminator = yaml_data.get('discriminator', None)
        self.discriminator_value = yaml_data.get('discriminator_value', None)

    @property
    def id(self):
        return id(self.yaml_data)

    @abstractmethod
    def get_serialization_type(self):
        ...

    @abstractmethod
    def get_doc_string_type(self, namespace=None):
        ...
