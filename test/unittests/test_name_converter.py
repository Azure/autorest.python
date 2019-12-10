from autorest import NameConverter

def test_pascal_case():
    expected_conversion = {
        "pascal": "Pascal",
        "pascalCase": "PascalCase",
        "PascalCase": "PascalCase",
        "pascalcase": "Pascalcase",
        "Pascalcase": "Pascalcase",
        "pascal_case": "PascalCase",
        "pascal_case_": "PascalCase",
        "_pascal_case": "PascalCase",
        "LROs": "LROs",
        "___pascal____case6666": "PascalCase6666",
    }

    incorrect_conversions = []

    for name in expected_conversion:
        if NameConverter._to_pascal_case(name) != expected_conversion[name]:
            incorrect_conversions.append(name)

    assert not incorrect_conversions, incorrect_conversions

def test_to_python_case():
    expected_conversion = {
        "snake_case": "snake_case",
        "snakeCase": "snake_case",
        "SnakeCase": "snake_case",
        "snake_Case": "snake_case",
        "Snake": "snake",
        "s_nake": "s_nake",
        "SNaKE": "sna_ke" ,
        "SNaKEr": "sna_ker",
        "s_na_k_er": "s_na_k_er",
        "snakeSnakECase": "snake_snak_ecase",
        "MikhailGorbachevUSSR": "mikhail_gorbachev_ussr",
        "MAX_of_MLD": "max_of_mld"
    }

    for name in expected_conversion:
        assert NameConverter._to_valid_python_name(name) == expected_conversion[name]