# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from routes import RoutesClient


class RoutesClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(RoutesClient)
        return self.create_client_from_credential(
            RoutesClient,
            credential=credential,
            endpoint=endpoint,
        )


RoutesPreparer = functools.partial(PowerShellPreparer, "routes", routes_endpoint="https://fake_routes_endpoint.com")
