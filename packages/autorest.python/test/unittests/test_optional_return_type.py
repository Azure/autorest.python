# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
from autorest.codegen.models import (
    Operation, LROOperation, PagingOperation, Response, ParameterList, CodeModel, RequestBuilder
)
from autorest.codegen.models.base_type import BaseType
from autorest.codegen.models.parameter_list import RequestBuilderParameterList
from autorest.codegen.models.primitive_types import StringType

@pytest.fixture
def code_model():
    return CodeModel(
        {"client": {
            "namespace": "blah",
            "moduleName": "blah"
        }},
        options={
            "show_send_request": True,
            "builders_visibility": "public",
            "version_tolerant": True
        },
    )

@pytest.fixture
def request_builder(code_model):
    return RequestBuilder(
        yaml_data={
            "url": "http://fake.com",
            "method": "GET",
            "groupName": "blah",
            "isOverload": False,
            "apiVersions": [],
        },
        code_model=code_model,
        name="optional_return_type_test",
        parameters=RequestBuilderParameterList({}, code_model, parameters=[]),
    )

@pytest.fixture
def operation(code_model, request_builder):
    return Operation(
        yaml_data={
            "url": "http://fake.com",
            "method": "GET",
            "groupName": "blah",
            "isOverload": False,
            "apiVersions": [],
        },
        code_model=code_model,
        request_builder=request_builder,
        name="optional_return_type_test",
        parameters=ParameterList({}, code_model, []),
        responses=[],
        exceptions=[],
    )

@pytest.fixture
def lro_operation(code_model, request_builder):
    return LROOperation(
        yaml_data={
            "url": "http://fake.com",
            "method": "GET",
            "groupName": "blah",
            "isOverload": False,
            "apiVersions": [],
        },
        code_model=code_model,
        request_builder=request_builder,
        name="lro_optional_return_type_test",
        parameters=ParameterList({}, code_model, []),
        responses=[],
        exceptions=[],
    )

@pytest.fixture
def paging_operation(code_model, request_builder):
    return PagingOperation(
        yaml_data={
            "url": "http://fake.com",
            "method": "GET",
            "groupName": "blah",
            "isOverload": False,
            "apiVersions": [],
            "pagerSync": "blah",
            "pagerAsync": "blah",
        },
        code_model=code_model,
        request_builder=request_builder,
        name="paging_optional_return_type_test",
        parameters=ParameterList({}, code_model, []),
        responses=[],
        exceptions=[],
    )

@pytest.fixture
def base_type(code_model):
    return StringType(
        {"type": "string"}, code_model
    )

def test_success_with_body_and_fail_no_body(code_model, operation, base_type):
    operation.responses = [
        Response(
            yaml_data={"statusCodes": [200]}, code_model=code_model, headers=[], type=base_type
        ),
        Response(
            yaml_data={"statusCodes": [202]}, code_model=code_model, headers=[], type=base_type
        )
    ]
    operation.exceptions = [
        Response(
            yaml_data={"statusCodes": ["default"]}, code_model=code_model, headers=[], type=None
        )
    ]

    assert operation.has_optional_return_type is False

def test_success_no_body_fail_with_body(code_model, operation, base_type):
    operation.responses = [
        Response(
            yaml_data={"statusCodes": [200]}, code_model=code_model, headers=[], type=None
        )
    ]
    operation.exceptions = [
        Response(
            yaml_data={"statusCodes": ["default"]}, code_model=code_model, headers=[], type=base_type
        )
    ]

    assert operation.has_optional_return_type is False

def test_optional_return_type_operation(code_model, operation, base_type):
    operation.responses = [
        Response(
            yaml_data={"statusCodes": [200]}, code_model=code_model, headers=[], type=base_type
        ),
        Response(
            yaml_data={"statusCodes": [202]}, code_model=code_model, headers=[], type=None
        ),
        Response(
            yaml_data={"statusCodes": ["default"]}, code_model=code_model, headers=[], type=base_type
        )
    ]

    assert operation.has_optional_return_type is True

def test_lro_operation(code_model, lro_operation, base_type):
    lro_operation.responses = [
        Response(
            yaml_data={"statusCodes": [200]}, code_model=code_model, headers=[], type=base_type
        ),
        Response(
            yaml_data={"statusCodes": [202]}, code_model=code_model, headers=[], type=None
        ),
        Response(
            yaml_data={"statusCodes": ["default"]}, code_model=code_model, headers=[], type=base_type
        )
    ]

    assert lro_operation.has_optional_return_type is False

def test_paging_operation(code_model, paging_operation, base_type):
    paging_operation.responses = [
        Response(
            yaml_data={"statusCodes": [200]}, code_model=code_model, headers=[], type=base_type
        ),
        Response(
            yaml_data={"statusCodes": [202]}, code_model=code_model, headers=[], type=None
        ),
        Response(
            yaml_data={"statusCodes": ["default"]}, code_model=code_model, headers=[], type=base_type
        )
    ]

    assert paging_operation.has_optional_return_type is False
