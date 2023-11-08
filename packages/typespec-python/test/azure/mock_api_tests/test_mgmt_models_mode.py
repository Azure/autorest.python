# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import inspect
from azure.mgmt.spheredpg import AzureSphereClient as MsrestModelClient
from azure.mgmt.spheremsrest import AzureSphereClient as DpgModelClient


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

def test_model_mode():
    from azure.mgmt.spheredpg import _model_base
    from azure.mgmt.spheredpg.models import ArmResource as ArmResourceDpg
    assert isinstance(ArmResourceDpg(id="", type=""), _model_base.Model)

    from azure.mgmt.spheremsrest import _serialization
    from azure.mgmt.spheremsrest.models import ArmResource as ArmResourceMsrest
    assert isinstance(ArmResourceMsrest(id="", type=""), _serialization.Model)

def test_dpg_model():
    from azure.mgmt.spheredpg.models import Catalog, CatalogProperties
    catalog = Catalog(location="eastus", tags={"hello": "world"}, properties=CatalogProperties(provisioning_state="Succeeded"))
    assert catalog.location == "eastus"
    assert catalog.tags == {"hello": "world"}
    assert catalog.properties.provisioning_state == "Succeeded"
    assert catalog.provisioning_state == "Succeeded"

    catalog = Catalog()
    assert catalog.location is None
    assert catalog.tags is None
    assert catalog.properties is None
    assert catalog.provisioning_state is None

    catalog = Catalog(provisioning_state="Succeeded")
    assert catalog.provisioning_state == "Succeeded"
    assert catalog.properties.provisioning_state == "Succeeded"

    catalog.provisioning_state = "Failed"
    assert catalog.properties.provisioning_state == "Failed"
    
    catalog.properties.provisioning_state = "Caceled"
    assert catalog.provisioning_state == "Caceled"
    