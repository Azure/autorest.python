from .code_namer import CodeNamer

def to_python_case(name):
    return CodeNamer.to_python_case(name)

known_primary_types_mapping = {
    "none": "",
    "object": "object",
    "int": "int",
    "number": "float",
    "integer": "int",
    "long": "long",
    "double": "float",
    "decimal": "decimal.Decimal",
    "string": "str",
    "stream": "Generator",
    "bytearray": "bytearray",
    "date": "date",
    "date-time": "datetime.datetime",
    "datetimerfc1123": "datetime.datetime",
    "timespan": "timedelta",
    "boolean": "bool",
    "uuid": "str",
    "base64url": "bytes",
    "unixtime": "ddatetime.datetime"
}

# def get_type_documentation(schema):
#     if schema['type'] == 'dictionary':
#             return DictionaryType(schema).type_documentation()
#         if schema['type'] == 'array':
#             return SequenceType(schema).type_documentation()
#         if schema['type'] == 'object':
#             if schema.get('$key'):
#                 # property is of a class in our yaml file
#                 return schema['$key']
#             # TODO: make sure pure objects don't have $key entry
#             return 'object'
#         return to_python_type(schema['type'])

def to_python_type(original_type):
    try:
        return known_primary_types_mapping[original_type]
    except KeyError as e:
        print("The type you are trying to convert to Python is not a known type")
        raise