# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import MediaTypePreparer
from testpreparer_async import MediaTypeClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMediaTypeStringBodyOperationsAsync(MediaTypeClientTestBaseAsync):
    @MediaTypePreparer()
    @recorded_by_proxy_async
    async def test_send_as_text(self, mediatype_endpoint):
        client = self.create_async_client(endpoint=mediatype_endpoint)
        response = client.string_body.send_as_text(
            text="str",
            content_type="str",
        )

        # please add some check logic here by yourself

    @MediaTypePreparer()
    @recorded_by_proxy_async
    async def test_get_as_text(self, mediatype_endpoint):
        client = self.create_async_client(endpoint=mediatype_endpoint)
        response = client.string_body.get_as_text()

        # please add some check logic here by yourself

    @MediaTypePreparer()
    @recorded_by_proxy_async
    async def test_send_as_json(self, mediatype_endpoint):
        client = self.create_async_client(endpoint=mediatype_endpoint)
        response = client.string_body.send_as_json(
            text="str",
            content_type="str",
        )

        # please add some check logic here by yourself

    @MediaTypePreparer()
    @recorded_by_proxy_async
    async def test_get_as_json(self, mediatype_endpoint):
        client = self.create_async_client(endpoint=mediatype_endpoint)
        response = client.string_body.get_as_json()

        # please add some check logic here by yourself
