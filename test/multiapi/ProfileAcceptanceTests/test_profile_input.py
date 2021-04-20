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
from multiapi import MultiapiServiceClient
from azure.profiles import ProfileDefinition, KnownProfiles

@pytest.fixture
def profile_definition():
    return ProfileDefinition({
        "MyTest": {
            None: "5.2.1",
            'begin_test_lro': '1.0.0',
            'begin_test_lro_and_paging': '1.0.0',
            'test_one': '2.0.0',
        }},
        "MyTest"
    )

def test_profile_input(credential, profile_definition):
    client = MultiapiServiceClient(credential, profile=profile_definition)
    assert client.profile == profile_definition

def test_known_profiles_default_input(credential):
    client = MultiapiServiceClient(credential=credential, profile=KnownProfiles.default)
    assert client.profile == KnownProfiles.default

def test_profile_api_version(credential, profile_definition):
    with pytest.raises(ValueError) as error:
        MultiapiServiceClient(credential, api_version="3.0.0", profile=profile_definition)
    assert "Cannot use api-version and profile parameters at the same time" in str(error.value)
