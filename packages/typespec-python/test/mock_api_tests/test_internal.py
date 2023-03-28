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
    with pytest.raises(ImportError):
        from internal.models import InternalModel

    with pytest.raises(AttributeError):
        client.get_internal(name="test")

    with pytest.raises(AttributeError):
        client.post_internal(
            models._models.ModelOnlyUsedByInternalOperation(id=1, name="test")
        )
