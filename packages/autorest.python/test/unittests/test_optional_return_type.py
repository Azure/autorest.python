# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
from autorest.codegen.models import (
    Operation,
    LROOperation,
    PagingOperation,
    Response,
    ParameterList,
    NamespaceModel,
    RequestBuilder,
    Client,
)
from autorest.codegen.models.parameter_list import RequestBuilderParameterList
from autorest.codegen.models.primitive_types import StringType


@pytest.fixture
def namespace_model():
    return NamespaceModel(
        {"clients": [{"name": "cient", "namespace": "blah", "moduleName": "blah"}]},
        options={
            "show_send_request": True,
            "builders_visibility": "public",
            "version_tolerant": True,
        },
        namespace="namespace",
    )


@pytest.fixture
def client(namespace_model):
    return Client(
        {"name": "client", "url": "http://localhost", "parameters": []},
        namespace_model,
        parameters=[],
    )


@pytest.fixture
def request_builder(namespace_model, client):
    return RequestBuilder(
        yaml_data={
            "url": "http://fake.com",
            "method": "GET",
            "groupName": "blah",
            "isOverload": False,
            "apiVersions": [],
        },
        client=client,
        namespace_model=namespace_model,
        name="optional_return_type_test",
        parameters=RequestBuilderParameterList({}, namespace_model, parameters=[]),
    )


@pytest.fixture
def operation(namespace_model, request_builder, client):
    return Operation(
        yaml_data={
            "url": "http://fake.com",
            "method": "GET",
            "groupName": "blah",
            "isOverload": False,
            "apiVersions": [],
        },
        client=client,
        namespace_model=namespace_model,
        request_builder=request_builder,
        name="optional_return_type_test",
        parameters=ParameterList({}, namespace_model, []),
        responses=[],
        exceptions=[],
    )


@pytest.fixture
def lro_operation(namespace_model, request_builder, client):
    return LROOperation(
        yaml_data={
            "url": "http://fake.com",
            "method": "GET",
            "groupName": "blah",
            "isOverload": False,
            "apiVersions": [],
        },
        client=client,
        namespace_model=namespace_model,
        request_builder=request_builder,
        name="lro_optional_return_type_test",
        parameters=ParameterList({}, namespace_model, []),
        responses=[],
        exceptions=[],
    )


@pytest.fixture
def paging_operation(namespace_model, request_builder, client):
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
        client=client,
        namespace_model=namespace_model,
        request_builder=request_builder,
        name="paging_optional_return_type_test",
        parameters=ParameterList({}, namespace_model, []),
        responses=[],
        exceptions=[],
    )


@pytest.fixture
def base_type(namespace_model):
    return StringType({"type": "string"}, namespace_model)


def test_success_with_body_and_fail_no_body(namespace_model, operation, base_type):
    operation.responses = [
        Response(
            yaml_data={"statusCodes": [200]},
            namespace_model=namespace_model,
            headers=[],
            type=base_type,
        ),
        Response(
            yaml_data={"statusCodes": [202]},
            namespace_model=namespace_model,
            headers=[],
            type=base_type,
        ),
    ]
    operation.exceptions = [
        Response(
            yaml_data={"statusCodes": ["default"]},
            namespace_model=namespace_model,
            headers=[],
            type=None,
        )
    ]

    assert operation.has_optional_return_type is False


def test_success_no_body_fail_with_body(namespace_model, operation, base_type):
    operation.responses = [
        Response(
            yaml_data={"statusCodes": [200]},
            namespace_model=namespace_model,
            headers=[],
            type=None,
        )
    ]
    operation.exceptions = [
        Response(
            yaml_data={"statusCodes": ["default"]},
            namespace_model=namespace_model,
            headers=[],
            type=base_type,
        )
    ]

    assert operation.has_optional_return_type is False


def test_optional_return_type_operation(namespace_model, operation, base_type):
    operation.responses = [
        Response(
            yaml_data={"statusCodes": [200]},
            namespace_model=namespace_model,
            headers=[],
            type=base_type,
        ),
        Response(
            yaml_data={"statusCodes": [202]},
            namespace_model=namespace_model,
            headers=[],
            type=None,
        ),
        Response(
            yaml_data={"statusCodes": ["default"]},
            namespace_model=namespace_model,
            headers=[],
            type=base_type,
        ),
    ]

    assert operation.has_optional_return_type is True


def test_lro_operation(namespace_model, lro_operation, base_type):
    lro_operation.responses = [
        Response(
            yaml_data={"statusCodes": [200]},
            namespace_model=namespace_model,
            headers=[],
            type=base_type,
        ),
        Response(
            yaml_data={"statusCodes": [202]},
            namespace_model=namespace_model,
            headers=[],
            type=None,
        ),
        Response(
            yaml_data={"statusCodes": ["default"]},
            namespace_model=namespace_model,
            headers=[],
            type=base_type,
        ),
    ]

    assert lro_operation.has_optional_return_type is False


def test_paging_operation(namespace_model, paging_operation, base_type):
    paging_operation.responses = [
        Response(
            yaml_data={"statusCodes": [200]},
            namespace_model=namespace_model,
            headers=[],
            type=base_type,
        ),
        Response(
            yaml_data={"statusCodes": [202]},
            namespace_model=namespace_model,
            headers=[],
            type=None,
        ),
        Response(
            yaml_data={"statusCodes": ["default"]},
            namespace_model=namespace_model,
            headers=[],
            type=base_type,
        ),
    ]

    assert paging_operation.has_optional_return_type is False
