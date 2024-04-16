# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typetest.property.valuetypes.models import ModelProperty, InnerModel

def test_model_init_remove_deepcopy():
    origin = {"property": InnerModel(property="hello")}
    assert origin["property"].property == "hello"

    dpg_model = ModelProperty(origin)
    assert origin["property"]["property"] == "hello"
    assert dpg_model["property"]["property"] == "hello"

    origin["property"]["property"] = "world"
    # After remove deepcopy for model init, value change of original input will also influence the model
    assert dpg_model["property"]["property"] == "world"
