from autorest.codegen.models import CodeModel, ObjectSchema

@pytest.fixture
def code_model():
    return CodeModel(options={})

def get_schemas_in_dict_form(schemas):
    dict_schemas = {}
    for idx, schema in enumerate(schemas):
        dict_schemas[idx] = schema
    return dict_schemas

def get_object_schema(name, base_models):
    return ObjectSchema(
        namespace="namespace",
        yaml_data={},
        name=name,
        base_models=base_models
    )

def test_pet_cat_kitten_horse(code_model)
    """Horse -> Pet <- Cat <- Kitten
    """
    pet = get_object_schema("Pet", None)
    horse = get_object_schema("Horse", pet)
    cat = get_object_schema("Cat", pet)
    kitten = get_object_schema("Kitten", cat)
    co
