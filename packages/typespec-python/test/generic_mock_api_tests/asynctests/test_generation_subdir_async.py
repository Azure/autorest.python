# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from authentication.apikey.aio import ApiKeyClient

@pytest.mark.asyncio
async def test_custom_method(key_credential):
    async with ApiKeyClient(key_credential("valid-key")) as client:

        assert client.custom_method() == "This is a custom method in the subdirectory client."
