# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from headasboolean import VisibilityClient, models

@pytest.fixture
def client():
    with VisibilityClient() as client:
        yield client

def test_head(client):
    body = models.VisibilityModel(query_prop=123)
    assert client.head_model(body) is None
