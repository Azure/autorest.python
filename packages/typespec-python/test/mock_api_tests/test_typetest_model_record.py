# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.model.record import RecordTestClient, models

@pytest.fixture
def client():
    with RecordTestClient() as client:
        yield client

model_record_unknown = models.ModelRecordUnknown({"prop1": 32, "prop2": True, "prop3": "abc", "name":"ModelRecordUnknown"})

def test_post_model_record_unknown(client):
    client.post_model_record_unknown(model_record_unknown)

def test_get_model_record_unknown(client):
    assert client.get_model_record_unknown() == model_record_unknown
