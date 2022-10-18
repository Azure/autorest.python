# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.core.credentials import AzureKeyCredential, AccessToken
from azure.core.exceptions import HttpResponseError
from authentication.apikey.aio import ApiKeyClient
from authentication.oauth2.aio import OAuth2Client

@pytest.fixture
async def api_key_client():
    async with ApiKeyClient(AzureKeyCredential("valid-key")) as client:
        yield client

def generate_token(*scopes) -> AccessToken:
    return AccessToken(token=''.join(scopes), expires_on=1800)

@pytest.fixture()
def token_credential():
    class FakeCredential:
        @staticmethod
        async def get_token(*scopes) -> AccessToken:
            return generate_token(*scopes)
    return FakeCredential()

@pytest.fixture
async def oauth2_client(token_credential):
    async with OAuth2Client(token_credential) as client:
        yield client

@pytest.mark.asyncio
async def test_api_key_valid(api_key_client):
    await api_key_client.valid()

@pytest.mark.asyncio
async def test_api_key_invalid(api_key_client):
    with pytest.raises(HttpResponseError) as ex:
        await api_key_client.invalid()
    assert ex.value.status_code == 403
    assert ex.value.reason == "Forbidden"

@pytest.mark.asyncio
async def test_oauth2_valid(oauth2_client):
    await oauth2_client.valid(enforce_https=False)

@pytest.mark.asyncio
async def test_oauth2_invalid(oauth2_client):
    with pytest.raises(HttpResponseError) as ex:
        await oauth2_client.invalid(enforce_https=False)
    assert ex.value.status_code == 403
