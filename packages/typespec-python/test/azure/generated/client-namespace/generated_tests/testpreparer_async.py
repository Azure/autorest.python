# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from client.clientnamespace.aio import ClientNamespaceFirstClient
from client.clientnamespace.second.aio import ClientNamespaceSecondClient
from devtools_testutils import AzureRecordedTestCase


class ClientNamespaceSecondClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ClientNamespaceSecondClient, is_async=True)
        return self.create_client_from_credential(
            ClientNamespaceSecondClient,
            credential=credential,
            endpoint=endpoint,
        )


class ClientNamespaceFirstClientTestBaseAsync(AzureRecordedTestCase):

    def create_async_client(self, endpoint):
        credential = self.get_credential(ClientNamespaceFirstClient, is_async=True)
        return self.create_client_from_credential(
            ClientNamespaceFirstClient,
            credential=credential,
            endpoint=endpoint,
        )
