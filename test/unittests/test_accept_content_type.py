import pytest
from autorest.codegen.models import Operation, SchemaResponse
from autorest.codegen.models.operation import _non_binary_schema_media_types

@pytest.fixture
def operation():
    return Operation(
        yaml_data={},
        name="accept_content_type_test",
        description="Operation to test accept_content_type",
        url="http://www.accept_content_type.com",
        method="method",
        api_versions=set(["2020-03-01"]),
        requests=[]
    )

def _get_sorted_content_types(operation):
    accept_content_type = operation.accept_content_type.split(",")
    accept_content_type.sort()
    return accept_content_type

def test_multiple_binary(operation):
    operation.responses = [
        SchemaResponse(
            yaml_data={}, media_types=["image/png", "application/json"], headers=[], binary=True, schema=None, status_codes=[204]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["image/png", "application/pdf", "application/xml"], headers=[], binary=True, schema=None, status_codes=[200]
        )
    ]

    assert ["application/pdf", "image/png"] == _get_sorted_content_types(operation)

def test_multiple_non_binary(operation):
    operation.responses = [
        SchemaResponse(
            yaml_data={}, media_types=["application/xml", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=[200]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["application/json", "text/json"], headers=[], binary=False, schema=None, status_codes=[200]
        )
    ]

    assert ["application/json", "application/xml"] == _get_sorted_content_types(operation)

def test_non_binary_single_response_with_schema(operation):
    operation.responses = [
        SchemaResponse(yaml_data={}, media_types=["image/png", "application/json", "application/xml"], headers=[], binary=False, schema={"a": "b"}, status_codes=[200])
    ]

    assert ["application/json", "application/xml"] == _get_sorted_content_types(operation)

def test_binary_and_non_binary_response_with_schema(operation):
    operation.responses = [
        SchemaResponse(
            yaml_data={}, media_types=["image/png"], headers=[], binary=True, schema=None, status_codes=[204]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["application/pdf", "application/xml", "text/xml"], headers=[], binary=False, schema=None, status_codes=[200]
        )
    ]

    assert ["application/pdf", "application/xml", "image/png"] == _get_sorted_content_types(operation)

def test_multiple_json_types():
    assert ["application/json"] == _non_binary_schema_media_types(["text/json", "application/json"])

def test_no_media_types_schema_error(operation):
    operation.responses = [
        SchemaResponse(
            yaml_data={}, media_types=[], headers=[], binary=True, schema=None, status_codes=[204]
        )
    ]

    with pytest.raises(TypeError):
        operation.accept_content_type

def test_no_response_body_error(operation):
    # There shouldn't be a case where we have media_types and no headers, but
    # adding this in case of bug in code model and making sure we raise it
    operation.responses = [
        SchemaResponse(
            yaml_data={}, media_types=["application/pdf"], headers=[], binary=False, schema=None, status_codes=[204]
        )
    ]

    with pytest.raises(TypeError):
        operation.accept_content_type
