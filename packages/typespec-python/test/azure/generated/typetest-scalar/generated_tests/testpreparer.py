# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from typetest.scalar import ScalarClient


class ScalarClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ScalarClient)
        return self.create_client_from_credential(
            ScalarClient,
            credential=credential,
            endpoint=endpoint,
        )


ScalarPreparer = functools.partial(PowerShellPreparer, "scalar", scalar_endpoint="https://fake_scalar_endpoint.com")
