# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------


def test_azure_mgmt_test_import():
    # just need to check import so that we could make sure the generated code is valid
    from azure.mgmt.test import AutoRestSwaggerBATArrayService
    from azure.mgmt.test import models
    from azure.mgmt.test import operations


def test_azure_test_import():
    # just need to check import so that we could make sure the generated code is valid
    from azure.test._generated import AutoRestSwaggerBATArrayService
    from azure.test._generated import models
    from azure.test._generated import operations

    from azure.test import CustomizeClient
