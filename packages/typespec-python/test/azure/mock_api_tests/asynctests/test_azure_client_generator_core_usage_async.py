# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from specs.azure.clientgenerator.core.usage.aio import UsageClient
from specs.azure.clientgenerator.core.usage import models


@pytest.fixture
async def client():
    async with UsageClient() as client:
        yield client


@pytest.mark.asyncio
async def test_input_to_input_output(client: UsageClient):
    await client.input_to_input_output(models.InputModel(name="Madge"))

@pytest.mark.asyncio
async def test_output_to_input_output(client: UsageClient):
    assert models.OutputModel(name="Madge") == await client.output_to_input_output()
