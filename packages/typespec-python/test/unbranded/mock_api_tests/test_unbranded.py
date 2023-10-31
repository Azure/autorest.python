# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import os
import traceback
from importlib import import_module
import pytest
import pytest
from typetest.scalar import ScalarClient
from corehttp.exceptions import HttpResponseError


@pytest.fixture
def client():
    with ScalarClient() as client:
        yield client


def test_module():
    with pytest.raises(ModuleNotFoundError):
        import_module("azure")

def test_track_back(client: ScalarClient):
    try:
        client.string.put("to raise exception")
    except HttpResponseError:
        track_back = traceback.format_exc().lower()
        assert "azure" not in track_back
        assert "microsoft" not in track_back
