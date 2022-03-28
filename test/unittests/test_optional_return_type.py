# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
from autorest.codegen.models import (
    Operation, LROOperation, PagingOperation, SchemaResponse, ParameterList, CodeModel, SchemaRequest
)

@pytest.fixture
def code_model():
    return CodeModel(
        options={
            "show_send_request": True,
            "builders_visibility": "embedded",
        }
    )

@pytest.fixture
def operation(code_model):
    return Operation(
        code_model,
        yaml_data={},
        name="optional_return_type_test",
        description="Operation to test optional return types",
        api_versions=set(["2020-05-01"]),
        parameters=ParameterList(code_model),
        multiple_content_type_parameters=ParameterList(code_model),
        schema_requests=[SchemaRequest({}, ["application/json"], ParameterList(code_model))]
    )

@pytest.fixture
def lro_operation(code_model):
    return LROOperation(
        code_model,
        yaml_data={},
        name="lro_optional_return_type_test",
        description="LRO Operation to test optional return types",
        api_versions=set(["2020-05-01"]),
        parameters=ParameterList(code_model),
        multiple_content_type_parameters=ParameterList(code_model),
        schema_requests=[SchemaRequest({}, ["application/json"], ParameterList(code_model))]
    )

@pytest.fixture
def paging_operation(code_model):
    return PagingOperation(
        code_model,
        yaml_data={"extensions": {"x-ms-pageable": {}}},
        name="paging_optional_return_type_test",
        description="Paging Operation to test optional return types",
        api_versions=set(["2020-05-01"]),
        parameters=ParameterList(code_model),
        multiple_content_type_parameters=ParameterList(code_model),
        schema_requests=[SchemaRequest({}, ["application/json"], ParameterList(code_model))]
    )

def test_success_with_body_and_fail_no_body(code_model, operation):
    operation.responses = [
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/xml", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=[200]
        ),
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/xml", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=[202]
        ),
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/json", "text/json"], headers=[], binary=False, schema=None, status_codes=["default"]
        )
    ]

    assert operation.has_optional_return_type is False

def test_success_no_body_fail_with_body(code_model, operation):
    operation.responses = [
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/xml", "text/json"], headers=[], binary=False, schema=None, status_codes=[200]
        ),
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/json", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=["default"]
        )
    ]

    assert operation.has_optional_return_type is False

def test_optional_return_type_operation(code_model, operation):
    operation.responses = [
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/xml", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=[200]
        ),
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/json", "text/json"], headers=[], binary=False, schema=None, status_codes=[202]
        ),
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/json", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=["default"]
        )
    ]

    assert operation.has_optional_return_type is True

def test_lro_operation(code_model, lro_operation):
    lro_operation.responses = [
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/xml", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=[200]
        ),
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/json", "text/json"], headers=[], binary=False, schema=None, status_codes=[202]
        ),
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/json", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=["default"]
        )
    ]

    assert lro_operation.has_optional_return_type is False

def test_paging_operation(code_model, paging_operation):
    paging_operation.responses = [
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/xml", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=[200]
        ),
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/json", "text/json"], headers=[], binary=False, schema=None, status_codes=[202]
        ),
        SchemaResponse(
            code_model=code_model, yaml_data={}, content_types=["application/json", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=["default"]
        )
    ]

    assert paging_operation.has_optional_return_type is False
