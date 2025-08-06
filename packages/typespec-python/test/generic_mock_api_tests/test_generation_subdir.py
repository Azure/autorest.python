# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from generation.subdir import CustomizedApiKeyClient


def test_custom_method(key_credential):
    client = CustomizedApiKeyClient(key_credential("valid-key"))
    assert client.custom_method()


def test_custom_model():
    try:
        from authentication.api.key.subdir import InvalidAuth

        assert InvalidAuth is not None
    except ImportError:
        pytest.fail("InvalidAuth could not be imported")
