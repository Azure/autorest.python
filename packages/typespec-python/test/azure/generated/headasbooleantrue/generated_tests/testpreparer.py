# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from headasbooleantrue import VisibilityClient


class VisibilityClientTestBase(AzureRecordedTestCase):
    def create_client(self, endpoint):
        credential = self.get_credential(VisibilityClient)
        return self.create_client_from_credential(
            VisibilityClient,
            credential=credential,
            endpoint=endpoint,
        )


VisibilityPreparer = functools.partial(
    PowerShellPreparer, "visibility", visibility_endpoint="https://fake_visibility_endpoint.com"
)
