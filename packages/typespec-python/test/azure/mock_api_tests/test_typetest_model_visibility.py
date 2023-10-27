# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest

from typetest.model.visibility import VisibilityClient, models


@pytest.fixture
def client():
    with VisibilityClient() as client:
        yield client


def check_no_read_prop(request):
    assert "will_be_ignored" not in request.http_request.body


def test_read(client):
    body = models.VisibilityModel(read_prop="will_be_ignored", query_prop=123)
    assert (
        client.get_model(body, raw_request_hook=check_no_read_prop).read_prop == "abc"
    )


def test_head(client):
    body = models.VisibilityModel(read_prop="will_be_ignored", query_prop=123)
    client.head_model(body)


def test_put(client):
    body = models.VisibilityModel(
        read_prop="will_be_ignored",
        create_prop=["foo", "bar"],
        update_prop=[1, 2],
    )
    client.put_model(body)


def test_patch(client):
    body = models.VisibilityModel(
        read_prop="will_be_ignored",
        update_prop=[1, 2],
    )
    client.patch_model(body)


def test_post(client):
    body = models.VisibilityModel(
        read_prop="will_be_ignored",
        create_prop=["foo", "bar"],
    )
    client.post_model(body)


def test_delete(client):
    body = models.VisibilityModel(
        read_prop="will_be_ignored",
        delete_prop=True,
    )
    client.delete_model(body)
