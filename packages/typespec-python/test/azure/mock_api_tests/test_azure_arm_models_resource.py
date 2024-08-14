# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from azure.resourcemanager.models.resources import ResourcesClient
from azure.resourcemanager.models.resources import models

SUBSCRIPTION_ID = "00000000-0000-0000-0000-000000000000"
RESOURCE_GROUP_NAME = "test-rg"


@pytest.fixture
def client(credential, authentication_policy):
    with ResourcesClient(
        credential, SUBSCRIPTION_ID, "http://localhost:3000", authentication_policy=authentication_policy
    ) as client:
        yield client


def test_client_signature(credential, authentication_policy):
    # make sure signautre order is correct
    client1 = ResourcesClient(
        credential, SUBSCRIPTION_ID, "http://localhost:3000", authentication_policy=authentication_policy
    )
    # make sure signautre name is correct
    client2 = ResourcesClient(
        credential=credential,
        subscription_id=SUBSCRIPTION_ID,
        base_url="http://localhost:3000",
        authentication_policy=authentication_policy,
    )
    for client in [client1, client2]:
        # make sure signautre order is correct
        client.top_level_tracked_resources.get(RESOURCE_GROUP_NAME, "top")
        # make sure signautre name is correct
        client.top_level_tracked_resources.get(
            resource_group_name=RESOURCE_GROUP_NAME, top_level_tracked_resource_name="top"
        )


def test_top_level_tracked_resources_begin_create_or_replace(client):
    result = client.top_level_tracked_resources.begin_create_or_replace(
        resource_group_name=RESOURCE_GROUP_NAME,
        top_level_tracked_resource_name="top",
        resource=models.TopLevelTrackedResource(
            location="eastus",
            properties=models.TopLevelTrackedResourceProperties(
                models.TopLevelTrackedResourceProperties(description="valid")
            ),
        ),
        polling_interval=0,  # set polling_interval to 0 s to make the test faster since default is 30s
    ).result()
    assert result.location == "eastus"
    assert result.properties.description == "valid"
    assert result.properties.provisioning_state == "Succeeded"
    assert result.name == "top"
    assert result.type == "Azure.ResourceManager.Models.Resources/topLevelTrackedResources"
    assert result.system_data.created_by == "AzureSDK"
