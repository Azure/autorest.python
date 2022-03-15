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
from securityaadswagger.aio import AutorestSecurityAad
from securitykeyswagger.aio import AutorestSecurityKey
from azure.core.credentials import AzureKeyCredential
from azure.core.pipeline.policies import AzureKeyCredentialPolicy
from azure.core.pipeline.policies import AsyncBearerTokenCredentialPolicy

@pytest.mark.asyncio
async def test_security_aad_swagger(credential, authentication_policy):
    client = AutorestSecurityAad(credential=credential)
    assert isinstance(client._config.authentication_policy, AsyncBearerTokenCredentialPolicy)
    # the test is temporary and it will be updated later
    client = AutorestSecurityAad(credential=credential, authentication_policy=authentication_policy)
    await client.head()

@pytest.mark.asyncio
async def test_security_key_swagger():
    # the key value shall keep same with https://github.com/Azure/autorest.testserver/tree/main/src/test-routes/security.ts
    client = AutorestSecurityKey(credential=AzureKeyCredential('123456789'))
    assert isinstance(client._config.authentication_policy, AzureKeyCredentialPolicy)
    await client.head()
