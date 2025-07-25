# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from authentication.apikey import ApiKeyClient


def test_custom_method(key_credential):
    with ApiKeyClient(key_credential("valid-key")) as client:
        assert client.custom_method() == "This is a custom method in the subdirectory client."

def test_custom_model():
    try:
        from authentication.apikey import InvalidAuth
        assert InvalidAuth is not None
    except ImportError:
        pytest.fail("InvalidAuth could not be imported")

