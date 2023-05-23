# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.property.additionalproperties import AdditionalPropertiesClient, models


@pytest.fixture
def client():
    with AdditionalPropertiesClient() as client:
        yield client


@pytest.mark.parametrize(
    "og_name,val, model_name", [
        ("extends_record_unknown", {'name': 'ModelExtendsRecordUnknown', 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.ModelExtendsRecordUnknown),
        ("is_record_unknown", {'name': 'ModelIsRecordUnknown', 'prop1': 32, 'prop2': True, 'prop3': 'abc'}, models.ModelIsRecordUnknown),
    ]
)
def test_json(client, og_name, val, model_name):
    body = model_name(val)
    og_group = getattr(client, og_name)
    assert og_group.get() == body
    og_group.put(val)

