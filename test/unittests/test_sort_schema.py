import pytest
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

def test_pet_cat_kitten_horse_wood(code_model):
    """Horse -> Pet <- Cat <- Kitten, Wood
    """
    pet = get_object_schema("Pet", None)
    horse = get_object_schema("Horse", [pet])
    cat = get_object_schema("Cat", [pet])
    kitten = get_object_schema("Kitten", [cat])
    wood = get_object_schema("Wood", None)
    code_model.schemas = get_schemas_in_dict_form(
        [wood, horse, cat, pet, kitten]
    )
    code_model.sort_schemas()
    sorted_schemas = code_model.sorted_schemas
    # assert pet is before cat
    assert sorted_schemas.index(pet) < sorted_schemas.index(cat)
    # assert pet is before horse
    assert sorted_schemas.index(pet) < sorted_schemas.index(horse)
    # assert cat is before kitten
    assert sorted_schemas.index(cat) < sorted_schemas.index(kitten)
    # assert wood in list
    assert wood in sorted_schemas

def test_multiple_inheritance(code_model):
    """CarbonObject <- Person <- Teacher -> Employee, Person <- Kid
                        |
                        ObjectOnEarth
    """
    carbon_object = get_object_schema("CarbonObject", [])
    object_on_earth = get_object_schema("ObjectOnEarth", [])
    person = get_object_schema("Person", [carbon_object, object_on_earth])
    employee = get_object_schema("Employee", [])
    teacher = get_object_schema("Teacher", [person, employee])
    kid = get_object_schema("Kid", [person])

    code_model.schemas = get_schemas_in_dict_form(
        [kid, person, teacher, carbon_object, employee, object_on_earth]
    )
    code_model.sort_schemas()
    sorted_schemas = code_model.sorted_schemas
    # assert carbon object and object on earth is in front of person
    assert sorted_schemas.index(carbon_object) < sorted_schemas.index(person)
    assert sorted_schemas.index(object_on_earth) < sorted_schemas.index(person)
    # assert person and employee are in front of teacher
    assert sorted_schemas.index(person) < sorted_schemas.index(teacher)
    assert sorted_schemas.index(employee) < sorted_schemas.index(teacher)
    # assert person is before kid
    assert sorted_schemas.index(person) < sorted_schemas.index(kid)
