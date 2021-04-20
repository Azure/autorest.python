# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import pytest
from async_generator import yield_, async_generator
from azure.core.pipeline.policies import AzureKeyCredentialPolicy

@pytest.fixture
@async_generator
async def default_client(credential, authentication_policy):
    from multiapicredentialdefaultpolicy.aio import MultiapiServiceClient
    async with MultiapiServiceClient(
		base_url="http://localhost:3000",
        credential="12345"
    ) as default_client:
        await yield_(default_client)

def test_multiapi_credential_default_policy_type(default_client):
    # making sure that the authentication policy is AzureKeyCredentialPolicy
    assert isinstance(default_client._config.authentication_policy, AzureKeyCredentialPolicy)
    assert default_client._config.authentication_policy._name == "api-key"