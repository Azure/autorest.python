# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from typetest.property.valuetypes.models import ModelProperty, InnerModel, BytesProperty
import io
from pathlib import Path

JPG = Path(__file__).parent.parent / "data/image.jpg"

def test_model_init_remove_deepcopy():
    origin = {"property": InnerModel(property="hello")}
    assert origin["property"].property == "hello"

    dpg_model = ModelProperty(origin)
    assert origin["property"]["property"] == "hello"
    assert dpg_model["property"]["property"] == "hello"

    origin["property"]["property"] = "world"
    # After remove deepcopy for model init, value change of original input will also influence the model
    assert dpg_model["property"]["property"] == "world"

def test_model_init_io():
    # it is OK to use io when model init after remove deepcopy
    with open(JPG, "rb") as file:
        BytesProperty(property=file)
