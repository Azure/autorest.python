# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from specs.azure.encode.duration import DurationClient


class DurationClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(DurationClient)
        return self.create_client_from_credential(
            DurationClient,
            credential=credential,
            endpoint=endpoint,
        )


DurationPreparer = functools.partial(
    PowerShellPreparer, "duration", duration_endpoint="https://fake_duration_endpoint.com"
)
