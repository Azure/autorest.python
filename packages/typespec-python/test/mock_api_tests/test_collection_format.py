# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from collectionformat import CollectionFormatClient


@pytest.fixture
def client():
    with CollectionFormatClient() as client:
        yield client


def test_multi(client: CollectionFormatClient):
    client.test_multi(colors=["blue", "red", "green"])


def test_csv(client: CollectionFormatClient):
    client.test_csv(colors=["blue", "red", "green"])


def test_csv_header(client: CollectionFormatClient):
    client.test_csv_header(colors=["blue", "red", "green"])


def test_default_header(client: CollectionFormatClient):
    client.test_default_header(colors=["blue", "red", "green"])
