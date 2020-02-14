from autorest.namer.name_converter import NameConverter

def test_escaped_reserved_words():
    expected_conversion = {
        "self": "self_model",
        "break": "break_model"
    }

    for name in expected_conversion:
        assert NameConverter._to_valid_python_name(name, pad_string="Model") == expected_conversion[name]