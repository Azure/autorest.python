# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import os
import traceback
from importlib import import_module
import pytest
from pathlib import Path
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


def test_sensitive_word():
    # we expect generated code don't contain word 'azure', 'microsoft'
    code_folders = [
        s
        for s in (Path(os.path.dirname(__file__)) / "../genereated").glob("**")
        if "__" not in s.name and ".egg-info" not in s.name
    ]
    result_azure = []
    result_microsfot = []
    for folder in code_folders:
        for file in folder.rglob("*"):
            if file.is_dir():
                continue
            flag_azure = False
            flag_microsfot = False
            with open(file, "r", encoding="utf-8") as f:
                content = f.read().lower()
                if not flag_azure and "azure" in content:
                    result_azure.append(folder.parts[0])
                    flag_azure = True
                if not flag_microsfot and "microsoft" in content:
                    result_microsfot.append(folder.parts[0])
                    flag_microsfot = True
            if flag_azure and flag_microsfot:
                break
    assert result_azure == []
    # after cadl-ranch update, it shall also equal to []
    assert result_microsfot == ["authentication-oauth2", "authentication-union"]


def test_track_back(client: ScalarClient):
    try:
        client.string.put("to raise exception")
    except HttpResponseError:
        track_back = traceback.format_exc().lower()
        assert "azure" not in track_back
        assert "microsoft" not in track_back
