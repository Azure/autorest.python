# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DurationClientTestBase, DurationPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDurationPropertyOperations(DurationClientTestBase):
    @DurationPreparer()
    @recorded_by_proxy
    def test_default(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.property.default(
            body={"value": "1 day, 0:00:00"},
        )

        # please add some check logic here by yourself

    @DurationPreparer()
    @recorded_by_proxy
    def test_iso8601(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.property.iso8601(
            body={"value": "1 day, 0:00:00"},
        )

        # please add some check logic here by yourself

    @DurationPreparer()
    @recorded_by_proxy
    def test_int32_seconds(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.property.int32_seconds(
            body={"value": 0},
        )

        # please add some check logic here by yourself

    @DurationPreparer()
    @recorded_by_proxy
    def test_float_seconds(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.property.float_seconds(
            body={"value": 0.0},
        )

        # please add some check logic here by yourself

    @DurationPreparer()
    @recorded_by_proxy
    def test_float_seconds_array(self, duration_endpoint):
        client = self.create_client(endpoint=duration_endpoint)
        response = client.property.float_seconds_array(
            body={"value": [0.0]},
        )

        # please add some check logic here by yourself
