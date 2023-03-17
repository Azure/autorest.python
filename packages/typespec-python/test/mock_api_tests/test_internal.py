# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from internal import InternalClient


@pytest.fixture
def client():
    with InternalClient() as client:
        yield client


def test_get(client: InternalClient):
    result = client._get_internal(name="test")
    assert result.name == "test"
