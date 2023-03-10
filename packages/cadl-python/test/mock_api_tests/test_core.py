# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from _specs_.azure.core import CoreClient


@pytest.fixture
def client():
    with CoreClient() as client:
        yield client


def test_create_or_update(client: CoreClient):
    result = client.create_or_update(id=1, resource={"name": "Madge"})
    assert result.id == 1
    assert result.name == "Madge"


def test_create_or_replace(client: CoreClient):
    result = client.create_or_replace(id=1, resource={"name": "Madge"})
    assert result.id == 1
    assert result.name == "Madge"


def test_get(client: CoreClient):
    result = client.get(id=1)
    assert result.id == 1
    assert result.name == "Madge"


def test_list(client: CoreClient):
    result = list(
        client.list(
            top=5,
            skip=10,
            orderby=["id"],
            filter="id lt 10",
            select=["id", "orders", "etag"],
            expand=["orders"],
        )
    )
    assert len(result) == 2
    assert result[0].id == 1
    assert result[0].name == "Madge"
    assert result[0].etag == "11bdc430-65e8-45ad-81d9-8ffa60d55b59"
    assert result[0].orders[0].id == 1
    assert result[0].orders[0].user_id == 1
    assert result[0].orders[0].detail == "a recorder"
    assert result[1].id == 2
    assert result[1].name == "John"
    assert result[1].etag == "11bdc430-65e8-45ad-81d9-8ffa60d55b5a"
    assert result[1].orders[0].id == 2
    assert result[1].orders[0].user_id == 2
    assert result[1].orders[0].detail == "a TV"


def test_list_with_page(client: CoreClient):
    result = list(client.list_with_page())
    assert len(result) == 1
    assert result[0].id == 1
    assert result[0].name == "Madge"
    assert result[0].etag == "11bdc430-65e8-45ad-81d9-8ffa60d55b59"
    assert result[0].orders is None


def test_delete(client: CoreClient):
    client.delete(id=1)


def test_export(client: CoreClient):
    result = client.export(id=1, format="json")
    assert result.id == 1
    assert result.name == "Madge"
