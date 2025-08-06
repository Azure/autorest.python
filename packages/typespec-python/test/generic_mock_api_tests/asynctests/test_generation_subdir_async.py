# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from generation.subdir import CustomizedClient, Extension


@pytest.mark.asyncio
async def test_custom_method():
    client = CustomizedClient()
    assert (await client.custom_method()) == Extension(
        {
            "level": 0,
            "extension": [{"level": 1, "extension": [{"level": 2}]}, {"level": 1}],
        }
    )
