# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.core.credentials import AzureKeyCredential, AccessToken
from azure.core.exceptions import HttpResponseError
from authentication.apikey import ApiKeyClient
from authentication.oauth2 import OAuth2Client
from authentication.union import UnionClient


# Utilities functions

@pytest.fixture
def api_key_client():
    client = None
    def _build_client(client_type):
        client = client_type(AzureKeyCredential("valid-key"))
        return client
    yield _build_client
    if client:
        client.close()

def generate_token(*scopes) -> AccessToken:
    return AccessToken(token=''.join(scopes), expires_on=1800)

@pytest.fixture
def token_credential():
    class FakeCredential:
        @staticmethod
        def get_token(*scopes) -> AccessToken:
            return generate_token(*scopes)
    return FakeCredential()

@pytest.fixture
def oauth2_client(token_credential):
    client = None
    def _build_client(client_type):
        client = client_type(token_credential)
        return client
    yield _build_client
    if client:
        client.close()


# Tests

def test_api_key_valid(api_key_client):
    client = api_key_client(ApiKeyClient)
    client.valid()

def test_api_key_invalid(api_key_client):
    client = api_key_client(ApiKeyClient)
    with pytest.raises(HttpResponseError) as ex:
        client.invalid()
    assert ex.value.status_code == 403
    assert ex.value.reason == "Forbidden"

def test_oauth2_valid(oauth2_client):
    client = oauth2_client(OAuth2Client)
    client.valid(enforce_https=False)

def test_oauth2_invalid(oauth2_client):
    client = oauth2_client(OAuth2Client)
    with pytest.raises(HttpResponseError) as ex:
        client.invalid(enforce_https=False)
    assert ex.value.status_code == 403
