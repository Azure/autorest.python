from .code_namer import CodeNamer
from .known_primary_types_mapping import known_primary_types_mapping

def to_python_case(name):
    return CodeNamer.to_python_case(name)

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