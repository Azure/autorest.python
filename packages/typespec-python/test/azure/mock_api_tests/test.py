# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
import geojson
from specs.azure.clientgenerator.core.alternatetype import AlternateTypeClient
from specs.azure.clientgenerator.core.alternatetype import models


# Shared test data
PROPERTIES = {
    "name": "A single point of interest",
    "category": "landmark",
    "elevation": 100
}

GEOMETRY = geojson.Point((-122.25, 37.87))

FEATURE_ID = "feature-1"

feature_geojson = geojson.Feature(
        type="Feature",
        geometry=GEOMETRY,
        properties=PROPERTIES,
        id=FEATURE_ID
    )

print(feature_geojson.type)

model_with_feature = models.ModelWithFeatureProperty(
    feature=feature_geojson,
    additional_property="extra"
)

print(model_with_feature.feature.type)
    

# with AlternateTypeClient(endpoint="http://localhost:3000") as client:

#     """Test getting a ModelWithFeatureProperty object with feature and additionalProperty fields."""
#     result = client.external_type.get_property()
    
#     # Validate the response structure based on the TypeSpec example
#     assert result.feature.type == "Feature"
#     assert result.feature.geometry.type == "Point"
#     assert result.feature.geometry.coordinates == [-122.25, 37.87]
#     assert result.feature.properties == PROPERTIES
#     assert result.feature.id == FEATURE_ID
#     assert result.additional_property == "extra"

