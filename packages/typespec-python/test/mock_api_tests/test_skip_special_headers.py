# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from skip.special.headers import TraitsClient


@pytest.fixture
def client():
    with TraitsClient() as client:
        yield client

def test_skip_special_headers(client: TraitsClient):
    with pytest.raises(TypeError):
        client.smoke_test(
            id=1,
            foo="123",
            if_match='"valid"',
        )
    
    with pytest.raises(TypeError):
        client.smoke_test(
            id=1,
            foo="123",
            client_request_id="test-id",
        )
