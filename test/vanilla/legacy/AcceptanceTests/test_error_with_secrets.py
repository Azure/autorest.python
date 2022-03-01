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
from errorwithsecrets import ErrorWithSecrets
from azure.core.exceptions import HttpResponseError

@pytest.fixture
def client():
    with ErrorWithSecrets() as client:
        yield client


def test_create_secret(client):
    with pytest.raises(HttpResponseError) as ex:
        client.create_secret()
    # The actual test shouldn't have the secrets in the str output
    # Until we figure out what to do for Python, just asserting
    # what the string currently is for now.
    assert "1c88a67921784300a462b2cb61da2339" in str(ex.value)

def test_raise_error_with_secrets(client):
    with pytest.raises(HttpResponseError) as ex:
        client.get_error_with_secrets()
    # The actual test shouldn't have the secrets in the str output
    # Until we figure out what to do for Python, just asserting
    # what the string currently is for now.
    assert "The user 'user@contoso.com' is unauthorized" in str(ex.value)
