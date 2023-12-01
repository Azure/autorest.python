# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.model.usage import models
from typetest.model.usage.aio import UsageClient

@pytest.fixture
async def client():
    async with UsageClient() as client:
        yield client

@pytest.mark.asyncio
@pytest.mark.parametrize(
"op_name, input,output", [
    ("input", models.InputRecord(required_prop="example-value"), None),
    ("output", None, models.OutputRecord(required_prop="example-value")),
    ("input_and_output", models.InputOutputRecord(required_prop="example-value"), models.InputOutputRecord(required_prop="example-value")),
]
)
async def test_input_output(client, op_name, input, output):
    op = getattr(client, op_name)
    if input:
        assert output == await op(input)
    else:
        assert output == await op()
