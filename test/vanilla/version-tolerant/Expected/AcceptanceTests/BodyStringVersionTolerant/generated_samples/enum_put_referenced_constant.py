# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from bodystringversiontolerant import AutoRestSwaggerBATService

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install AutoRestSwaggerBATService
# USAGE
    python enum_put_referenced_constant.py
"""


def main():
    client = AutoRestSwaggerBATService()

    response = client.enum.put_referenced_constant(
        enum_string_body="green-color",
    )
    print(response)


if __name__ == "__main__":
    main()
