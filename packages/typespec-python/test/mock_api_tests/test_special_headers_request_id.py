# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import functools

import pytest
from azure.core.pipeline import PipelineRequest

from specialheaders.requestid import RequestIdClient
from .utils.validation import validate_format, Format


@pytest.fixture
def client():
    with RequestIdClient() as client:
        yield client


def check_header(request: PipelineRequest, header: str, checked: dict):
    validate_format(request.http_request.headers[header], Format.UUID)
    checked[header] = request.http_request.headers[header]


def test_non_standard(client: RequestIdClient):
    # checked = {}
    # result, resp = client.non_standard(
    #     cls=lambda x, y, z: (y, x),
    #     raw_request_hook=functools.partial(
    #         check_header, header="client-request-id", checked=checked
    #     ),
    # )
    # assert result is None
    # assert (
    #     resp.http_response.headers["client-request-id"]
    #     == checked["client-request-id"]
    # )
    pass
