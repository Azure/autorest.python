# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from resiliency.servicedriven2 import ResiliencyServiceDriven2

@pytest.fixture
def client():
    with ResiliencyServiceDriven2() as client:
        yield client

def test(client: ResiliencyServiceDriven2):
    client.params.get_new_operation()
