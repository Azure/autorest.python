# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from devtools_testutils import AzureRecordedTestCase
from typetest.enum.extensible.aio import ExtensibleClient


class ExtensibleClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ExtensibleClient, is_async=True)
        return self.create_client_from_credential(
            ExtensibleClient,
            credential=credential,
            endpoint=endpoint,
        )
