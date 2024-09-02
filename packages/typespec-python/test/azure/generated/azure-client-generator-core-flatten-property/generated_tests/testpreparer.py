# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from azure.clientgenerator.core.flattenproperty import FlattenPropertyClient
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class FlattenPropertyClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(FlattenPropertyClient)
        return self.create_client_from_credential(
            FlattenPropertyClient,
            credential=credential,
            endpoint=endpoint,
        )


FlattenPropertyPreparer = functools.partial(
    PowerShellPreparer, "flattenproperty", flattenproperty_endpoint="https://fake_flattenproperty_endpoint.com"
)
