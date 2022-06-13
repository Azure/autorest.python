# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import os

from azure.identity import DefaultAzureCredential
from head import AutoRestHeadTestService

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install azure-identity
    pip install autorestheadtestservice
# USAGE
    python http_success_head404.py
"""


def main():
    client = AutoRestHeadTestService(
        credential=DefaultAzureCredential(),
    )

    response = client.http_success.head404()
    print(response)


if __name__ == "__main__":
    if not (os.getenv("AZURE_CLIENT_ID") and os.getenv("AZURE_TENANT_ID") and os.getenv("AZURE_CLIENT_SECRET")):
        raise Exception(
            "Please set the values of the client ID, tenant ID and client secret "
            "of the AAD application as environment variables: AZURE_CLIENT_ID, "
            " AZURE_TENANT_ID, AZURE_CLIENT_SECRET. For more info about how to get the value, "
            "please see https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal"
        )
    main()
