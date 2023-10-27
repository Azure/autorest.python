# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import inspect
import pytest
from azure.mgmt.spheredpg import AzureSphereClient as MsrestModelClient
from azure.mgmt.spheremsrest import AzureSphereClient as DpgModelClient
from azure.mgmt.spherejson import AzureSphereClient as JsonModelClient
from .utils.validation import overload_count


def test_client_signature():
    for item in (MsrestModelClient, DpgModelClient, JsonModelClient):
        signatures = inspect.signature(item).parameters
        expected_signatures = ["credential", "subscription_id", "base_url", "kwargs"]

        assert list(signatures.keys()) == expected_signatures
        assert (
            signatures["subscription_id"].kind
            == inspect.Parameter.POSITIONAL_OR_KEYWORD
        )
        assert signatures["credential"].kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
        assert signatures["base_url"].kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
        assert signatures["kwargs"].kind == inspect.Parameter.VAR_KEYWORD

        assert signatures["base_url"].default == "https://management.azure.com"


def test_model_mode():
    from azure.mgmt.spheredpg import _model_base
    from azure.mgmt.spheredpg.models import ArmResource as ArmResourceDpg

    assert isinstance(ArmResourceDpg(id="", type=""), _model_base.Model)

    from azure.mgmt.spheremsrest import _serialization
    from azure.mgmt.spheremsrest.models import ArmResource as ArmResourceMsrest

    assert isinstance(ArmResourceMsrest(id="", type=""), _serialization.Model)

    with pytest.raises(ImportError):
        from azure.mgmt.spherejson import models


def test_overload():
    from azure.mgmt.spherejson.operations import DevicesOperations

    source_lines = inspect.getsourcelines(DevicesOperations)[0]
    assert overload_count(source_lines, "create_or_update") == 3
    # Because of name duplication between body parameter name and body parameter properties name
    # there shall be only 2 overload
    assert overload_count(source_lines, "update") == 2
