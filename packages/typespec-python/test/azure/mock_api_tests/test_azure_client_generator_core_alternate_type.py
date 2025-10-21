# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from specs.azure.clientgenerator.core.alternatetype import AlternateTypeClient
from specs.azure.clientgenerator.core.alternatetype import models


@pytest.fixture
def client():
    with AlternateTypeClient() as client:
        yield client


def test_external_type_get_model(client: AlternateTypeClient):
    """Test getting a Feature object with geometry, properties, and optional id fields."""
    result = client.external_type.get_model()

    # Validate the response structure based on the TypeSpec example
    assert result.type == "Feature"
    assert result.geometry.type == "Point"
    assert result.geometry.coordinates == [-122.25, 37.87]
    assert result.properties["name"] == "A single point of interest"
    assert result.properties["category"] == "landmark"
    assert result.properties["elevation"] == 100
    assert result.id == "feature-1"


def test_external_type_put_model(client: AlternateTypeClient):
    """Test putting a Feature object in request body."""
    feature = {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [-122.25, 37.87]},
        "properties": {"name": "A single point of interest", "category": "landmark", "elevation": 100},
        "id": "feature-1",
    }

    # Should return None (204/empty response)
    result = client.external_type.put_model(body=feature)
    assert result is None


def test_external_type_get_property(client: AlternateTypeClient):
    """Test getting a ModelWithFeatureProperty object with feature and additionalProperty fields."""
    result = client.external_type.get_property()

    # Validate the response structure based on the TypeSpec example
    assert result.feature.type == "Feature"
    assert result.feature.geometry.type == "Point"
    assert result.feature.geometry.coordinates == [-122.25, 37.87]
    assert result.feature.properties["name"] == "A single point of interest"
    assert result.feature.properties["category"] == "landmark"
    assert result.feature.properties["elevation"] == 100
    assert result.feature.id == "feature-1"
    assert result.additional_property == "extra"


def test_external_type_put_property(client: AlternateTypeClient):
    """Test putting a ModelWithFeatureProperty object in request body."""
    model_with_feature = {
        "feature": {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [-122.25, 37.87]},
            "properties": {"name": "A single point of interest", "category": "landmark", "elevation": 100},
            "id": "feature-1",
        },
        "additionalProperty": "extra",
    }

    # Should return None (204/empty response)
    result = client.external_type.put_property(body=model_with_feature)
    assert result is None
