# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from bodyinteger import AutoRestIntegerTestService

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install AutoRestIntegerTestService
# USAGE
    python int_get_unix_time.py
"""


def main():
    client = AutoRestIntegerTestService()

    response = client.int.get_unix_time()
    print(response)


if __name__ == "__main__":
    main()
