# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from types.enum.extensible import ExtensibleClient, models

@pytest.fixture
def client():
    with ExtensibleClient() as client:
        yield client

def test_known_value(client):
    assert client.get_known_value() == models.DaysOfWeekExtensibleEnum.MONDAY
    client.put_known_value(models.DaysOfWeekExtensibleEnum.MONDAY)

def test_unknown_value(client):
    assert client.get_unknown_value() == "Weekend"
    client.put_unknown_value("Weekend")
