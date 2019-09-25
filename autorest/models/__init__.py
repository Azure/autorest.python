from .codemodel import CodeModel
from .compositetype import CompositeType
from .dictionarytype import DictionaryType
from .enumtype import EnumType
from .modeltype import ModelType
from .sequencetype import SequenceType
from ..common.utils import to_python_case

__all__ = [
    "CodeModel",
    "CompositeType",
    "DictionaryType",
    "EnumType",
    "ExtendedModelType",
    "ModelType",
    "SequenceType"
]

def build_property(prop):
    ct_property = None
    name = to_python_case(prop['$key'])
    prop_type = prop['schema']['type']
    if prop_type == 'array':
        ct_property = SequenceType.from_yaml(yaml_data=prop, name=name)
    elif prop_type == 'dictionary':
        ct_property = DictionaryType.from_yaml(yaml_data=prop, name=name)
    elif prop_type == 'choice':
        ct_property = EnumType.from_yaml(yaml_data=prop, name=name)
    else:
        ct_property = CompositeType.from_yaml(yaml_data=prop, name=name)
    return ct_property