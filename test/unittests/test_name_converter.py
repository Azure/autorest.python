from autorest.namer.name_converter import NameConverter, PadType

def test_escaped_reserved_words():
    expected_conversion_model = {
        "self": "self_model",
        "and": "and_model"
    }
    for name in expected_conversion_model:
        assert NameConverter._to_valid_python_name(name, pad_string=PadType.Model) == expected_conversion_model[name]


    expected_conversion_method = {
        "self": "self_method",
        "and": "and_method"
    }
    for name in expected_conversion_method:
        assert NameConverter._to_valid_python_name(name, pad_string=PadType.Method) == expected_conversion_method[name]

    expected_conversion_enum = {
        "self": "self",
        "mro": "mro_enum"
    }
    for name in expected_conversion_enum:
        assert NameConverter._to_valid_python_name(name, pad_string=PadType.Enum) == expected_conversion_enum[name]