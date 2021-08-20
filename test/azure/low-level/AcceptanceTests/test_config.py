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

from azure.mgmt.core.policies import ARMHttpLoggingPolicy, ARMChallengeAuthenticationPolicy
# Head is azure-arm
from headlowlevel import AutoRestHeadTestService

def test_arm_http_logging_policy_default(credential):
    with AutoRestHeadTestService(credential) as client:
        assert isinstance(client._config.http_logging_policy, ARMHttpLoggingPolicy)
        assert client._config.http_logging_policy.allowed_header_names == ARMHttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST

def test_arm_http_logging_policy_custom(credential):
    http_logging_policy = ARMHttpLoggingPolicy(base_url="test")
    http_logging_policy = ARMHttpLoggingPolicy()
    http_logging_policy.allowed_header_names.update(
        {"x-ms-added-header"}
    )
    with AutoRestHeadTestService(credential, http_logging_policy=http_logging_policy) as client:
        assert isinstance(client._config.http_logging_policy, ARMHttpLoggingPolicy)
        assert client._config.http_logging_policy.allowed_header_names == ARMHttpLoggingPolicy.DEFAULT_HEADERS_WHITELIST.union({"x-ms-added-header"})

def test_credential_scopes_default(credential):
    with AutoRestHeadTestService(credential) as client:
        assert client._config.credential_scopes == ['https://management.azure.com/.default']

def test_credential_scopes_override(credential):
    with AutoRestHeadTestService(credential, credential_scopes=["http://i-should-be-the-only-credential"]) as client:
        assert client._config.credential_scopes == ["http://i-should-be-the-only-credential"]

def test_authentication_policy_default(credential):
    with AutoRestHeadTestService(credential) as client:
        assert isinstance(client._config.authentication_policy, ARMChallengeAuthenticationPolicy)