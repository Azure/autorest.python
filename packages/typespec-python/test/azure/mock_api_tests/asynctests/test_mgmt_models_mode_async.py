# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import inspect
from azure.mgmt.spheredpg.aio import AzureSphereClient as MsrestModelClient
from azure.mgmt.spheremsrest.aio import AzureSphereClient as DpgModelClient


def test_client_signature():
    for item in (MsrestModelClient, DpgModelClient):
        signatures = inspect.signature(item).parameters
        expected_signatures = ["credential", "subscription_id", "base_url", "kwargs"]

        assert list(signatures.keys()) == expected_signatures
        assert signatures["subscription_id"].kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
        assert signatures["credential"].kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
        assert signatures["base_url"].kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
        assert signatures["kwargs"].kind == inspect.Parameter.VAR_KEYWORD

        assert signatures["base_url"].default == "https://management.azure.com"
