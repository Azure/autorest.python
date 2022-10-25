# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import os

from azure.core.credentials import AzureKeyCredential
from headwithazurekeycredentialpolicy import AutoRestHeadTestService

"""
# PREREQUISITES
    pip install autorestheadtestservice
# USAGE
    python http_success_head200.py

    Before run the sample, please set environment variables AZURE_KEY with real value
    which can access your service
"""


def main():
    client = AutoRestHeadTestService(
        credential=AzureKeyCredential(key=os.getenv("AZURE_KEY")),
    )

    response = client.http_success.head200()
    print(response)


if __name__ == "__main__":
    main()
