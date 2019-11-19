from autorest import NameConverter

def test_pascal_case():
    expected_conversion = {
        "pascal": "Pascal",
        "pascalCase": "PascalCase",
        "PascalCase": "PascalCase",
        "PASCALCASE": "Pascalcase",
        "pascalcase": "Pascalcase",
        "Pascalcase": "Pascalcase",
        "pascal_case": "PascalCase",
        "pascal_case_": "PascalCase",
        "_pascal_case": "PascalCase",
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
        # "_": "",
        "SNake": "s_nake",
        "Snake": "snake",
        "s_nake": "s_nake",
        "SNaKE": "s_na_ke" ,
        "SNaKEr": "s_na_k_er",
        "s_na_k_er": "s_na_k_er",
        "SNAKE SNAKE CASE": "snake_snake_case",
        "snakeSnakECase": "snake_snak_e_case",
        "next.text": "next_text",
        "zip code": "zip_code",
        "MikhailGorbachevUSSR": "mikhail_gorbachev_ussr",
        "MAX_of_MLD": "max_of_mld",
        "Age.Group": "age_group",
    }

    incorrect_conversions = []

    for name in expected_conversion:
        if NameConverter._to_valid_python_name(name) != expected_conversion[name]:
            incorrect_conversions.append(name)

    assert not incorrect_conversions, incorrect_conversions