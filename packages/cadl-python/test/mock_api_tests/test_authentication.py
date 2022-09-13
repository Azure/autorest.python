# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.core.credentials import AzureKeyCredential, AccessToken
from azure.core.exceptions import HttpResponseError
from authentication.apikey import AuthenticationApiKey
from authentication.oauth2 import AuthenticationOAuth2
import json

@pytest.fixture
def api_key_client():
    with AuthenticationApiKey(AzureKeyCredential("valid-key")) as client:
        yield client

def generate_token(*scopes) -> AccessToken:
    return AccessToken(token=''.join(scopes), expires_on=1800)

@pytest.fixture()
def token_credential():
    class FakeCredential:
        @staticmethod
        def get_token(*scopes) -> AccessToken:
            return generate_token(*scopes)
    return FakeCredential()

@pytest.fixture
def oauth2_client(token_credential):
    with AuthenticationOAuth2(token_credential) as client:
        yield client

def test_api_key_valid(api_key_client):
    api_key_client.valid()

def test_api_key_invalid(api_key_client):
    with pytest.raises(HttpResponseError) as ex:
        api_key_client.invalid()
    assert ex.value.status_code == 403
    assert ex.value.reason == "Forbidden"
    raise ValueError(ex.value)
    assert ex.value.error.code == "InvalidApiKey"

def test_oauth2_valid(oauth2_client):
    oauth2_client.valid(enforce_https=False)

def test_oauth2_invalid(oauth2_client):
    with pytest.raises(HttpResponseError) as ex:
        oauth2_client.invalid(enforce_https=False)
    assert ex.value.status_code == 403
