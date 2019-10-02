from .code_namer import CodeNamer
from .known_primary_types_mapping import known_primary_types_mapping

def get_property_name(name):
        return CodeNamer().get_valid_python_name(name, "Property")

def get_namespace_name(name):
    return CodeNamer().get_valid_python_name(name, "")

def get_enum_name(name):
    return CodeNamer().get_valid_python_name(name, "Enum")

def get_method_name(name):
    return CodeNamer().get_valid_python_name(name, "Method")

def to_python_type(original_type):
    try:
        return known_primary_types_mapping[original_type]
    except KeyError as e:
        print("The type you are trying to convert to Python is not a known type")
        raise
    except:
        # one entry in the swagger has three types under type[]
        # https://github.com/Azure/perks/blob/master/codemodel/.resources/all-in-one/json/code-model.json#L882
        return "string"