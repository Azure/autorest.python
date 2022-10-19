# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from custombaseurl import AutoRestParameterizedHostTestClient

"""
# PREREQUISITES
    pip install autorestparameterizedhosttestclient
# USAGE
    python paths_get_empty.py
"""


def main():
    client = AutoRestParameterizedHostTestClient()

    response = client.paths.get_empty(
        account_name="testaccount",
    )
    print(response)


if __name__ == "__main__":
    main()
