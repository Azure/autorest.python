# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from bodytime import AutoRestTimeTestService

"""
The sample just shows how to use the method and may not run successfully.
# PREREQUISITES
    pip install AutoRestTimeTestService
# USAGE
    python time_put.py
"""


def main():
    client = AutoRestTimeTestService()

    response = client.time.put(
        time_body="08:07:56",
    )
    print(response)


if __name__ == "__main__":
    main()
