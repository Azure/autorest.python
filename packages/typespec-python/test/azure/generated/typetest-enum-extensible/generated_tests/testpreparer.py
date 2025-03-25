# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.enum.extensible import ExtensibleClient


class ExtensibleClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ExtensibleClient)
        return self.create_client_from_credential(
            ExtensibleClient,
            credential=credential,
            endpoint=endpoint,
        )


ExtensiblePreparer = functools.partial(
    PowerShellPreparer, "extensible", extensible_endpoint="https://fake_extensible_endpoint.com"
)
