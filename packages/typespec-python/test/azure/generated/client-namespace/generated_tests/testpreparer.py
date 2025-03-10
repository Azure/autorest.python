# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from client.clientnamespace import ClientNamespaceFirstClient
from client.clientnamespace.second import ClientNamespaceSecondClient
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools


class ClientNamespaceSecondClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ClientNamespaceSecondClient)
        return self.create_client_from_credential(
            ClientNamespaceSecondClient,
            credential=credential,
            endpoint=endpoint,
        )


NamespaceSecondPreparer = functools.partial(
    PowerShellPreparer, "namespacesecond", namespacesecond_endpoint="https://fake_namespacesecond_endpoint.com"
)


class ClientNamespaceFirstClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ClientNamespaceFirstClient)
        return self.create_client_from_credential(
            ClientNamespaceFirstClient,
            credential=credential,
            endpoint=endpoint,
        )


NamespaceFirstPreparer = functools.partial(
    PowerShellPreparer, "namespacefirst", namespacefirst_endpoint="https://fake_namespacefirst_endpoint.com"
)
