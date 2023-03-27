# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from internal import models
from internal import InternalClient


@pytest.fixture
def client():
    with InternalClient() as client:
        yield client


def test_get_internal(client: InternalClient):
    result = client._get_internal(name="test")
    assert result.name == "test"


def test_post_internal(client: InternalClient):
    result = client._post_internal(
        models._models.ModelOnlyUsedByInternalOperation(id=1, name="test")
    )
    assert result.name == "test"


def test_visibility(client: InternalClient):
    try:
        from internal.models import InternalModel

        pytest.fail("InternalModel should be hidden")
    except:
        pass

    try:
        from internal.models import ModelOnlyUsedByInternalOperation

        pytest.fail("ModelOnlyUsedByInternalOperation should be hidden")
    except:
        pass

    try:
        client.get_internal(name="test")
        pytest.fail("getInternal should be hidden")
    except:
        pass

    try:
        client.post_internal(
            models._models.ModelOnlyUsedByInternalOperation(id=1, name="test")
        )
        pytest.fail("postInternal should be hidden")
    except:
        pass
