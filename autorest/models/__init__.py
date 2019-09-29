from .codemodel import CodeModel
from .classtype import ClassType
from .dictionarytype import DictionaryType
from .enumtype import EnumType
from .basetype import BaseType
from .sequencetype import SequenceType
from ..common.utils import to_python_case

__all__ = [
    "BaseType",
    "CodeModel",
    "ClassType",
    "DictionaryType",
    "EnumType",
    "SequenceType"
]

def build_property(name, prop, required_list):
    prop_type = prop['type']
    if prop_type == 'array':
        final_property = SequenceType.from_yaml(
            name=name,
            yaml_data=prop,
            required_list=required_list
        )
    elif prop_type == 'dictionary':
        final_property = DictionaryType.from_yaml(
            name=name,
            yaml_data=prop,
            required_list=required_list
        )
    elif prop_type == 'sealed-choice' or prop_type == 'choice':
        final_property = EnumType.from_yaml(
            name=name,
            yaml_data=prop,
            required_list=required_list
        )
    else:
        final_property = ClassType.from_yaml(
            name=name,
            yaml_data=prop,
            required_list=required_list
        )
    return final_property