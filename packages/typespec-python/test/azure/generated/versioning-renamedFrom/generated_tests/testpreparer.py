# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from versioning.renamedfrom import RenamedFromClient


class RenamedFromClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(RenamedFromClient)
        return self.create_client_from_credential(
            RenamedFromClient,
            credential=credential,
            endpoint=endpoint,
        )


RenamedFromPreparer = functools.partial(
    PowerShellPreparer, "renamedfrom", renamedfrom_endpoint="https://fake_renamedfrom_endpoint.com"
)
