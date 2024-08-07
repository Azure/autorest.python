# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.core.model import ModelClient


class ModelClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ModelClient)
        return self.create_client_from_credential(
            ModelClient,
            credential=credential,
            endpoint=endpoint,
        )


ModelPreparer = functools.partial(PowerShellPreparer, "model", model_endpoint="https://fake_model_endpoint.com")
