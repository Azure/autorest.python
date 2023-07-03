# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import functools

import pytest

from specialheaders.requestid import DefaultClient, StandardClient, NonStandardClient
from .test_special_headers_request_id_utils import check_header


@pytest.fixture
def default():
    with DefaultClient() as default:
        yield default


@pytest.fixture
def standard():
    with StandardClient() as standard:
        yield standard


@pytest.fixture
def non_standard():
    with NonStandardClient() as non_standard:
        yield non_standard


def test_default(default: DefaultClient):
    checked = {}
    result, resp = default.default(
        cls=lambda x, y, z: (y, x),
        raw_request_hook=functools.partial(check_header, header="x-ms-client-request-id", checked=checked),
    )
    assert result is None
    assert resp.http_response.headers["x-ms-client-request-id"] == checked["x-ms-client-request-id"]


def test_standard(standard: StandardClient):
    checked = {}
    result, resp = standard.standard(
        cls=lambda x, y, z: (y, x),
        raw_request_hook=functools.partial(check_header, header="x-ms-client-request-id", checked=checked),
    )
    assert result is None
    assert resp.http_response.headers["x-ms-client-request-id"] == checked["x-ms-client-request-id"]


def test_non_standard(non_standard: NonStandardClient):
    checked = {}
    result, resp = non_standard.non_standard(
        cls=lambda x, y, z: (y, x),
        raw_request_hook=functools.partial(check_header, header="client-request-id", checked=checked),
    )
    assert result is None
    assert resp.http_response.headers["x-ms-client-request-id"] == checked["x-ms-client-request-id"]
