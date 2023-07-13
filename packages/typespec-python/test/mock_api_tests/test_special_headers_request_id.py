# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest

from specialheaders.requestid import RequestIdClient


@pytest.fixture
def client():
    with RequestIdClient() as client:
        yield client


def test_non_standard(client: RequestIdClient):
    # checked = {}
    # result, resp = client.non_standard(
    #     cls=lambda x, y, z: (y, x),
    #     raw_request_hook=functools.partial(
    #         check_request_id_header, header="client-request-id", checked=checked
    #     ),
    # )
    # assert result is None
    # assert (
    #     resp.http_response.headers["client-request-id"]
    #     == checked["client-request-id"]
    # )
    pass
