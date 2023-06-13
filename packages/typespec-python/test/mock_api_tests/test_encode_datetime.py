# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import datetime

import pytest
from encode.datetime import DatetimeClient
from encode.datetime.models import (
    DatetimeProperty,
)


@pytest.fixture
def client():
    with DatetimeClient() as client:
        yield client


def test_query(client: DatetimeClient):
    client.query(
        default=datetime.datetime(2022, 8, 26, 18, 38, 0),
        rfc3339=datetime.datetime(2022, 8, 26, 18, 38, 0),
        rfc7231=datetime.datetime(2022, 8, 26, 14, 38, 0),
        unix_timestamp=1686566864,
        rfc3339_array=[
            datetime.datetime(2022, 8, 26, 18, 38, 0),
            datetime.datetime(2022, 9, 26, 18, 38, 0),
        ],
    )


def test_property(client: DatetimeClient):
    result = client.property(
        DatetimeProperty(
            default=datetime.datetime(2022, 8, 26, 18, 38, 0),
            rfc3339=datetime.datetime(2022, 8, 26, 18, 38, 0),
            rfc7231=datetime.datetime(2022, 8, 26, 14, 38, 0),
            unix_timestamp=1686566864,
            rfc3339_array=[
                datetime.datetime(2022, 8, 26, 18, 38, 0),
                datetime.datetime(2022, 9, 26, 18, 38, 0),
            ],
        )
    )
    assert result.default == datetime.datetime(2022, 8, 26, 18, 38, 0)
    assert result.rfc3339 == datetime.datetime(2022, 8, 26, 18, 38, 0)
    assert result.rfc7231 == datetime.datetime(2022, 8, 26, 14, 38, 0)
    assert result.unix_timestamp == 1686566864
    assert result.rfc3339_array == [
        datetime.datetime(2022, 8, 26, 18, 38, 0),
        datetime.datetime(2022, 9, 26, 18, 38, 0),
    ]


def test_header(client: DatetimeClient):
    client.header(
        default=datetime.datetime(2022, 8, 26, 14, 38, 0),
        rfc3339=datetime.datetime(2022, 8, 26, 18, 38, 0),
        rfc7231=datetime.datetime(2022, 8, 26, 14, 38, 0),
        unix_timestamp=1686566864,
        rfc3339_array=[
            datetime.datetime(2022, 8, 26, 18, 38, 0),
            datetime.datetime(2022, 9, 26, 18, 38, 0),
        ],
    )
