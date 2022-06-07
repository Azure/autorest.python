# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from bodybyte import AutoRestSwaggerBATByteService

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install AutoRestSwaggerBATByteService
# USAGE
    python byte_get_null.py
"""


def main():
    client = AutoRestSwaggerBATByteService()

    response = client.byte.get_null()
    print(response)


if __name__ == "__main__":
    main()
