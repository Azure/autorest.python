# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from authentication.apikey.aio import AuthenticationApiKey

@pytest.fixture
async def api_key_client():
    async with AuthenticationApiKey(AzureKeyCredential("valid-key")) as client:
        yield client

@pytest.mark.asyncio
async def test_api_key_authenticated(api_key_client):
    await api_key_client.authenticated()

@pytest.mark.asyncio
async def test_api_key_invalid_authentication(api_key_client):
    with pytest.raises(HttpResponseError) as ex:
        await api_key_client.invalid_authentication()
    assert ex.value.status_code == 403
    assert ex.value.reason == "Forbidden"
    assert ex.value.error.code == "InvalidApiKey"
