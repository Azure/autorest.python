# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from client.naming.enumconflict import EnumConflictClient
from client.naming.enumconflict import models


@pytest.fixture
def client():
    with EnumConflictClient() as client:
        yield client


def test_first_operations_first(client: EnumConflictClient):
    """Test enum with same name in different namespace - first namespace."""
    body = models.FirstModel(status=models.Status.ACTIVE, name="test")

    response = client.first_operations.first(body=body)

    assert response.status == "active"
    assert response.name == "test"


def test_second_operations_second(client: EnumConflictClient):
    """Test enum with same name in different namespace - second namespace."""
    body = models.SecondModel(status=models.SecondStatus.RUNNING, description="test description")

    response = client.second_operations.second(body=body)

    assert response.status == "running"
    assert response.description == "test description"
