from .code_namer import CodeNamer

def to_python_case(name):
    return CodeNamer.to_python_case(name)

known_primary_types_mapping = {
    "none": "",
    "object": "object",
    "int": "int",
    "integer": "int",
    "long": "long",
    "double": "float",
    "decimal": "decimal.Decimal",
    "string": "str",
    "stream": "Generator",
    "bytearray": "bytearray",
    "date": "date",
    "dateTime": "datetime",
    "datetimerfc1123": "datetime",
    "timespan": "timedelta",
    "boolean": "bool",
    "credentials": "",
    "uuid": "str",
    "base64url": "bytes",
    "unixtime": "datetime"
}

def to_python_type(original_type):
    try:
        return known_primary_types_mapping[original_type]
    except KeyError as e:
        print("The type you are trying to convert to Python is not a known type")
        raise