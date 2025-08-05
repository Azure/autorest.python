# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from authentication.api.key.subdir.aio import CustomizedApiKeyClient


@pytest.mark.asyncio
async def test_custom_method(key_credential):
    client = CustomizedApiKeyClient(key_credential("valid-key"))
    assert await client.custom_method()
