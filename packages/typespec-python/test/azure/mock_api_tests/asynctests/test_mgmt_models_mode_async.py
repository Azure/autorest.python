# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import inspect
from azure.mgmt.spheredpg.aio import AzureSphereClient as MsrestModelClient
from azure.mgmt.spheremsrest.aio import AzureSphereClient as DpgModelClient
from azure.mgmt.spherejson.aio import AzureSphereClient as JsonModelClient
from ..utils.validation import overload_count


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


def test_overload():
    from azure.mgmt.spherejson.aio.operations import DevicesOperations

    source_lines = inspect.getsourcelines(DevicesOperations)[0]
    assert overload_count(source_lines, "create_or_update") == 3
    # Because of name duplication between body parameter name and body parameter properties name
    # there shall be only 2 overload
    assert overload_count(source_lines, "update") == 2
