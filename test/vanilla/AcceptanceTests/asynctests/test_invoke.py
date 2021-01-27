# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import io
import pytest
from azure.core.pipeline.transport import HttpRequest

from os.path import dirname, pardir, join, realpath
import pytest

cwd = dirname(realpath(__file__))

class TestInvoke(object):

    @pytest.mark.asyncio
    async def test_invoke_with_body_get(self):
        from bodycomplex.aio import AutoRestComplexTestService
        from bodycomplex.models import Siamese

        client = AutoRestComplexTestService(base_url="http://localhost:3000")

        request = HttpRequest("GET", "http://localhost:3000/complex/inheritance/valid",
            headers={
                'Accept': 'application/json'
            },
        )

        response = await client.invoke(request)
        deserialized = Siamese.deserialize(response)
        assert 2 ==  deserialized.id
        assert "Siameeee" ==  deserialized.name
        assert -1 ==  deserialized.hates[1].id
        assert "Tomato" ==  deserialized.hates[1].name

    @pytest.mark.asyncio
    async def test_invoke_with_body_put(self):
        from bodycomplex.aio import AutoRestComplexTestService

        client = AutoRestComplexTestService(base_url="http://localhost:3000")
        request = HttpRequest("PUT", "http://localhost:3000/complex/inheritance/valid",
            headers={
                'Accept': 'application/json',
                'Content-Length': '179',
                'Content-Type': 'application/json'
            },
            data='{"id": 2, "name": "Siameeee", "color": "green", "hates": [{"id": 1, "name": "Potato", "food": "tomato"}, {"id": -1, "name": "Tomato", "food": "french fries"}], "breed": "persian"}'
        )

        response = await client.invoke(request)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_invoke_with_stream(self):
        from bodyfile.aio import AutoRestSwaggerBATFileService

        client = AutoRestSwaggerBATFileService(base_url="http://localhost:3000", connection_data_block_size=1000)
        file_length = 0
        with io.BytesIO() as file_handle:

            request = HttpRequest("GET", "http://localhost:3000/files/stream/nonempty",
                headers={
                    'Accept': 'image/png, application/json'
                },
            )

            response = await client.invoke(request, stream=True)
            assert response.status_code == 200

            stream = response.stream_download(client._client._pipeline)

            total = len(stream)
            assert not stream.response.internal_response._released

            async for data in stream:
                assert 0 < len(data) <= stream.block_size
                file_length += len(data)
                print("Downloading... {}%".format(int(file_length*100/total)))
                file_handle.write(data)

            assert file_length !=  0

            sample_file = realpath(
                join(cwd, pardir, pardir, pardir, pardir,
                     "node_modules", "@microsoft.azure", "autorest.testserver", "routes", "sample.png"))

            with open(sample_file, 'rb') as data:
                sample_data = hash(data.read())
            assert sample_data == hash(file_handle.getvalue())

    @pytest.mark.asyncio
    async def test_invoke_with_client_path_format_arguments(self):
        from validation.aio import AutoRestValidationTest

        client = AutoRestValidationTest("mySubscriptionId", base_url="http://localhost:3000")

        request = HttpRequest("GET", "http://localhost:3000/fakepath/{subscriptionId}/123/150",
            headers={
                'Accept': 'application/json'
            },
        )

        response = await client.invoke(request)
        assert response.request.url == 'http://localhost:3000/fakepath/mySubscriptionId/123/150'