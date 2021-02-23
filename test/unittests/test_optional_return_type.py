# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
from autorest.codegen.models import (
    Operation, LROOperation, PagingOperation, SchemaResponse, ParameterList
)


@pytest.fixture
def operation():
    return Operation(
        yaml_data={},
        name="optional_return_type_test",
        description="Operation to test optional return types",
        api_versions=set(["2020-05-01"]),
        parameters=ParameterList(),
        multiple_media_type_parameters=ParameterList(),
    )

@pytest.fixture
def lro_operation():
    return LROOperation(
        yaml_data={},
        name="lro_optional_return_type_test",
        description="LRO Operation to test optional return types",
        api_versions=set(["2020-05-01"]),
        parameters=ParameterList(),
        multiple_media_type_parameters=ParameterList(),
    )

@pytest.fixture
def paging_operation():
    return PagingOperation(
        yaml_data={"extensions": {"x-ms-pageable": {}}},
        name="paging_optional_return_type_test",
        description="Paging Operation to test optional return types",
        api_versions=set(["2020-05-01"]),
        parameters=ParameterList(),
        multiple_media_type_parameters=ParameterList(),
    )

def test_success_with_body_and_fail_no_body(operation):
    operation.responses = [
        SchemaResponse(
            yaml_data={}, media_types=["application/xml", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=[200]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["application/xml", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=[202]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["application/json", "text/json"], headers=[], binary=False, schema=None, status_codes=["default"]
        )
    ]

    assert operation.has_optional_return_type is False

def test_success_no_body_fail_with_body(operation):
    operation.responses = [
        SchemaResponse(
            yaml_data={}, media_types=["application/xml", "text/json"], headers=[], binary=False, schema=None, status_codes=[200]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["application/json", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=["default"]
        )
    ]

    assert operation.has_optional_return_type is False

def test_optional_return_type_operation(operation):
    operation.responses = [
        SchemaResponse(
            yaml_data={}, media_types=["application/xml", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=[200]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["application/json", "text/json"], headers=[], binary=False, schema=None, status_codes=[202]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["application/json", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=["default"]
        )
    ]

    assert operation.has_optional_return_type is True

def test_lro_operation(lro_operation):
    lro_operation.responses = [
        SchemaResponse(
            yaml_data={}, media_types=["application/xml", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=[200]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["application/json", "text/json"], headers=[], binary=False, schema=None, status_codes=[202]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["application/json", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=["default"]
        )
    ]

    assert lro_operation.has_optional_return_type is False

def test_paging_operation(paging_operation):
    paging_operation.responses = [
        SchemaResponse(
            yaml_data={}, media_types=["application/xml", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=[200]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["application/json", "text/json"], headers=[], binary=False, schema=None, status_codes=[202]
        ),
        SchemaResponse(
            yaml_data={}, media_types=["application/json", "text/json"], headers=[], binary=False, schema={"a": "b"}, status_codes=["default"]
        )
    ]

    assert paging_operation.has_optional_return_type is False
