# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from overload import OverloadClient
from overload.models import Data

@pytest.fixture
def client():
    with OverloadClient() as client:
        yield client

def test_upload_bytes_or_string(client):
    client.upload_bytes_or_string("hello world")
    client.upload_bytes_or_string(b"hello world")


def test_upload_json_or_string(client):
    client.upload_json_or_string({"hello": "world"})
    client.upload_json_or_string(Data(hello="world"))
    client.upload_json_or_string("hello world")

