# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from apitest.limit import LimitClient
from azure.core.exceptions import HttpResponseError

@pytest.fixture
def client():
    with LimitClient() as client:
        yield client

# actually SDK does not validate the length of the name
def test_limit_length(client: LimitClient):
    with pytest.raises(HttpResponseError):
        client.length(name="ok")
