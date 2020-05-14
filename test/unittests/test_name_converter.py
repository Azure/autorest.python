from autorest.namer.name_converter import NameConverter
from autorest.namer.python_mappings import PadType

def test_escaped_reserved_words():
    expected_conversion_model = {
        "self": "self_model",
        "and": "and_model"
    }
    for name in expected_conversion_model:
        assert NameConverter._to_valid_python_name(name, pad_string=PadType.Model) == expected_conversion_model[name]


    expected_conversion_method = {
        "self": "self_method",
        "and": "and_method",
        "content_type": "content_type"
    }
    for name in expected_conversion_method:
        assert NameConverter._to_valid_python_name(name, pad_string=PadType.Method) == expected_conversion_method[name]

    expected_conversion_parameter = {
        "content_type": "content_type_parameter",
        "request_id": "request_id_parameter",
        "elif": "elif_parameter",
        "self": "self_parameter"
    }
    for name in expected_conversion_parameter:
        assert NameConverter._to_valid_python_name(name, pad_string=PadType.Parameter) == expected_conversion_parameter[name]

    expected_conversion_enum = {
        "self": "self",
        "mro": "mro_enum"
    }
    for name in expected_conversion_enum:
        assert NameConverter._to_valid_python_name(name, pad_string=PadType.Enum) == expected_conversion_enum[name]