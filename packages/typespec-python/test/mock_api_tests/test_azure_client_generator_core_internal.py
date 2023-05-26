# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from _specs_.azure.clientgenerator.core.internal import InternalClient


@pytest.fixture
def client():
    with InternalClient() as client:
        yield client


def test_public_only(client: InternalClient):
    result = client.public_only(name="test")
    assert result.name == "test"


def test_internal_only(client: InternalClient):
    result = client._internal_only(name="test")
    assert result.name == "test"


def test_shared_public(client: InternalClient):
    result = client.shared.public(name="test")
    assert result.name == "test"


def test_shared_internal(client: InternalClient):
    result = client.shared._internal(name="test")
    assert result.name == "test"


def test_visibility(client: InternalClient):
    from _specs_.azure.clientgenerator.core.internal.models import (
        PublicModel,
        SharedModel,
    )

    with pytest.raises(ImportError):
        from _specs_.azure.clientgenerator.core.internal.models import InternalModel

    with pytest.raises(AttributeError):
        client.internal_only(name="test")

    with pytest.raises(AttributeError):
        client.shared.internal(name="test")
