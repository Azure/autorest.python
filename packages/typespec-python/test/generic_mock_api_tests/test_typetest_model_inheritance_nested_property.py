# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from typetest.model.nestedproperty import NestedPropertyClient
from typetest.model.nestedproperty.models import Extension


@pytest.fixture
def client():
    with NestedPropertyClient() as client:
        yield client

@pytest.fixture
def expected():
    return Extension({
  "extension": [
    {
      "level": 1,
      "extension": [
        {
          "level": 2
        }
      ]
    },
    {
      "level": 1
    }
  ]
})

def test_put(client: NestedPropertyClient, expected: Extension):
    client.put(expected)


def test_get(client: NestedPropertyClient, expected: Extension):
    assert client.get() == expected

