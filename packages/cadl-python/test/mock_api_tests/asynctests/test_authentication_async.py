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
from authentication.union.aio import UnionClient


# Utilities functions

@pytest.fixture
async def api_key_client():
    client = None
    def _build_client(client_type):
        client = client_type(AzureKeyCredential("valid-key"))
        return client
    yield _build_client
    if client:
        await client.close()

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
    client = None
    def _build_client(client_type):
        client = client_type(token_credential)
        return client
    yield _build_client
    if client:
        await client.close()


# Tests

@pytest.mark.asyncio
async def test_api_key_valid(api_key_client):
    client = api_key_client(ApiKeyClient)
    await client.valid()

@pytest.mark.asyncio
async def test_api_key_invalid(api_key_client):
    client = api_key_client(ApiKeyClient)
    with pytest.raises(HttpResponseError) as ex:
        await client.invalid()
    assert ex.value.status_code == 403
    assert ex.value.reason == "Forbidden"

@pytest.mark.asyncio
async def test_oauth2_valid(oauth2_client):
    client = oauth2_client(OAuth2Client)
    await client.valid(enforce_https=False)

@pytest.mark.asyncio
async def test_oauth2_invalid(oauth2_client):
    client = oauth2_client(OAuth2Client)
    with pytest.raises(HttpResponseError) as ex:
        await client.invalid(enforce_https=False)
    assert ex.value.status_code == 403
