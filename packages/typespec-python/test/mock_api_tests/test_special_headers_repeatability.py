# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from datetime import datetime

import pytest
from azure.core.exceptions import HttpResponseError

from specialheaders.repeatability import RepeatabilityClient


@pytest.fixture
def client():
    with RepeatabilityClient() as client:
        yield client


def test_immediate_success(client: RepeatabilityClient):
    result, header = client.immediate_success(cls=lambda x, y, z: (y, z),)
    assert result is None
    assert header["Repeatability-Result"] == "accepted"

    result, header = client.immediate_success(
        cls=lambda x, y, z: (y, z),
        headers={
            "Repeatability-Request-ID": "5942d803-e3fa-4f96-8f67-607d7bd607f5",
            "Repeatability-First-Sent": "Sun, 06 Nov 1994 08:49:37 GMT",
        },
    )
    assert result is None
    assert header["Repeatability-Result"] == "accepted"

    with pytest.raises(HttpResponseError):
        client.immediate_success(
            cls=lambda x, y, z: (y, z),
            headers={"Repeatability-Request-ID": "wrong-id"},
        )

    with pytest.raises(HttpResponseError):
        client.immediate_success(
            cls=lambda x, y, z: (y, z),
            headers={"Repeatability-First-Sent": "wrong-datetime"},
        )
