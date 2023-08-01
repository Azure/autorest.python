# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.property.valuetypes import ValueTypesClient, models
from azure.core.exceptions import HttpResponseError

@pytest.fixture
def client():
    with ValueTypesClient() as client:
        yield client

def test_stream(client):
    # normal response
    response = client.string.get(stream=True)
    result = b""
    for item in response:
        result += item
    assert result == b'{"property":"hello"}'

    # raise exception
    try:
        client.string.put(models.StringProperty(property="wrong"), stream=True)
    except HttpResponseError as err:
        assert err.error is not None
    else:
        raise Exception("HttpResponseError not raised")
