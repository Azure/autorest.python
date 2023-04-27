# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import isodate

from bodydurationversiontolerant import AutoRestDurationTestService

"""
# PREREQUISITES
    pip install autorestdurationtestservice
# USAGE
    python duration_put_positive_duration.py
"""


def main():
    client = AutoRestDurationTestService()

    client.duration.put_positive_duration(
        duration_body=isodate.parse_duration("P123DT22H14M12.011S"),
    )


if __name__ == "__main__":
    main()
