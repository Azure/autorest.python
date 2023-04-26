# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import datetime

import pytest
from _specs_.azure.clientgenerator.core.clientformat.duration import DurationClient
from _specs_.azure.clientgenerator.core.clientformat.duration.models import SecondsDurationProperty, \
    ISO8601DurationProperty


@pytest.fixture
def client():
    with DurationClient() as client:
        yield client


def test_query(client: DurationClient):
    client.query.iso8601(input=datetime.timedelta(days=40))
    client.query.seconds(input=35.6)


def test_property(client: DurationClient):
    # result = client.property.iso8601(ISO8601DurationProperty(value=datetime.timedelta(days=40)))
    # assert result.value == datetime.timedelta(days=40)
    result = client.property.iso8601(ISO8601DurationProperty(value="P40D"))
    assert result.value == datetime.timedelta(days=40)
    result = client.property.seconds(SecondsDurationProperty(value=35.6))
    assert abs(result.value - 35.6) < 0.0001
