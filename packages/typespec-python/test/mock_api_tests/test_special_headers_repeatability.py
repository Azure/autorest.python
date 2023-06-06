# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from datetime import datetime

import pytest
from specialheaders.repeatability import RepeatabilityClient


@pytest.fixture
def client():
    with RepeatabilityClient() as client:
        yield client


def test_immediate_success(client: RepeatabilityClient):
    result, header = client.immediate_success(cls=lambda x, y, z: (y, z),)
    assert result is None
    assert header["Repeatability-Result"] == "accepted"

