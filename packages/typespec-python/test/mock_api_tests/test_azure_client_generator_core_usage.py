# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import pytest
from _specs_.azure.clientgenerator.core.usage import UsageClient
from _specs_.azure.clientgenerator.core.usage import models


@pytest.fixture
def client():
    with UsageClient() as client:
        yield client


def test_input_to_input_output(client: UsageClient):
    client.input_to_input_output(models.InputModel(name="Madge"))

def test_output_to_input_output(client: UsageClient):
    assert models.OutputModel(name="Madge") == client.output_to_input_output()

def test_model_usage():
    from _specs_.azure.clientgenerator.core.usage.models import OrphanModel
