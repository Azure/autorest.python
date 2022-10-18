# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from resiliency.servicedriven2.aio import ServiceDriven2Client

@pytest.fixture
async def initial_client():
    async with ServiceDriven2Client(api_version="1.0.0") as client:
        yield client

@pytest.fixture
async def updated_client():
    async with ServiceDriven2Client() as client:
        yield client

@pytest.mark.asyncio
async def test_added_params(initial_client, updated_client):
    with pytest.raises(ValueError):
        await initial_client.get_required(parameter="foo", new_parameter="bar")
    # initial_client.get_required(parameter="foo")
    # updated_client.get_required(parameter="foo")
    # updated_client.get_required(parameter="foo", new_parameter="bar")

@pytest.mark.asyncio
async def test_added_method(initial_client, updated_client):
    with pytest.raises(ValueError):
        await initial_client.get_new_operation()
    # updated_client.get_new_operation()
