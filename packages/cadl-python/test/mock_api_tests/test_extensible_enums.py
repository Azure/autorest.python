# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from extensibleenums import ExtensibleEnumsClient, models

@pytest.fixture
def client():
    with ExtensibleEnumsClient() as client:
        yield client

def test_known_value(client):
    assert client.get_known_value() == models.DaysOfWeekExtensibleEnum.MONDAY
    client.put_known_value(models.DaysOfWeekExtensibleEnum.MONDAY)

def test_unknown_value(client):
    assert client.get_unknown_value() == "Weekend"
    client.put_unknown_value("Weekend")
