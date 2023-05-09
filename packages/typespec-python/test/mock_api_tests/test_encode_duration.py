# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import datetime

import pytest
from encode.duration import DurationClient
from encode.duration.models import Int32SecondsDurationProperty, \
    ISO8601DurationProperty, FloatSecondsDurationProperty


@pytest.fixture
def client():
    with DurationClient() as client:
        yield client


def test_query(client: DurationClient):
    client.query.default(input=datetime.timedelta(days=40))
    client.query.iso8601(input=datetime.timedelta(days=40))
    client.query.int32_seconds(input=36)
    client.query.float_seconds(input=35.621)


def test_property(client: DurationClient):
    result = client.property.iso8601(ISO8601DurationProperty(value=datetime.timedelta(days=40)))
    assert result.value == datetime.timedelta(days=40)
    result = client.property.default(ISO8601DurationProperty(value="P40D"))
    assert result.value == datetime.timedelta(days=40)
    result = client.property.iso8601(ISO8601DurationProperty(value="P40D"))
    assert result.value == datetime.timedelta(days=40)
    result = client.property.int32_seconds(Int32SecondsDurationProperty(value=36))
    assert result.value == 36
    result = client.property.float_seconds(FloatSecondsDurationProperty(value=35.621))
    assert abs(result.value - 35.621) < 0.0001
