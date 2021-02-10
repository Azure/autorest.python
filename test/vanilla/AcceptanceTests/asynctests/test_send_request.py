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
import json
import pytest
from azure.core.pipeline.transport import HttpRequest

from os.path import dirname, pardir, join, realpath
import pytest

cwd = dirname(realpath(__file__))

class TestSendRequest(object):

    @pytest.mark.asyncio
    async def test_send_request_with_body_get_model_deserialize(self):
        from bodycomplex.aio import AutoRestComplexTestService
        from bodycomplex.models import Siamese

        client = AutoRestComplexTestService(base_url="http://localhost:3000")

        request = HttpRequest("GET", "/complex/inheritance/valid",
            headers={
                'Accept': 'application/json'
            },
        )

        response = await client._send_request(request)
        await response.load_body()
        deserialized = Siamese.deserialize(response)
        assert 2 ==  deserialized.id
        assert "Siameeee" ==  deserialized.name
        assert -1 ==  deserialized.hates[1].id
        assert "Tomato" == deserialized.hates[1].name

    @pytest.mark.asyncio
    async def test_send_request_with_body_get_direct_json(self):
        from bodycomplex.aio import AutoRestComplexTestService
        from bodycomplex.models import Siamese

        client = AutoRestComplexTestService(base_url="http://localhost:3000")

        request = HttpRequest("GET", "/complex/inheritance/valid",
            headers={
                'Accept': 'application/json'
            },
        )

        response = await client._send_request(request)

        data = b''
        async for chunk in response.stream_download(None):
            data += chunk
        json_response = json.loads(data.decode('utf-8'))
        assert 2 == json_response['id']
        assert "Siameeee" == json_response['name']
        assert - 1 == json_response['hates'][1]['id']
        assert "Tomato" == json_response['hates'][1]['name']

    @pytest.mark.asyncio
    async def test_send_request_with_body_put_json_dumps(self):
        from bodycomplex.aio import AutoRestComplexTestService

        client = AutoRestComplexTestService(base_url="http://localhost:3000")

        siamese_body = {
            "id": 2,
            "name": "Siameeee",
            "color": "green",
            "hates":
                [
                    {
                        "id": 1,
                        "name": "Potato",
                        "food": "tomato"
                    },
                    {
                        "id": -1,
                        "name": "Tomato",
                        "food": "french fries"
                    }
                ],
            "breed": "persian"
        }

        request = HttpRequest("PUT", "/complex/inheritance/valid",
            headers={
                'Content-Type': 'application/json'
            }
        )
        request.set_json_body(siamese_body)

        response = await client._send_request(request)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_send_request_with_body_serialize(self):
        from bodycomplex.aio import AutoRestComplexTestService
        from bodycomplex.models import Siamese, Dog

        client = AutoRestComplexTestService(base_url="http://localhost:3000")

        siamese = Siamese(
            id=2,
            name="Siameeee",
            color="green",
            hates=[
                Dog(
                    id=1,
                    name="Potato",
                    food="tomato"
                ),
                Dog(
                    id=-1,
                    name="Tomato",
                    food="french fries"
                )
            ],
            breed="persian"
        )

        request = HttpRequest("PUT", "/complex/inheritance/valid",
            headers={
                'Content-Type': 'application/json'
            }
        )
        request.set_json_body(siamese.serialize())

        response = await client._send_request(request)
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_send_request_with_stream(self):
        from bodyfile.aio import AutoRestSwaggerBATFileService

        client = AutoRestSwaggerBATFileService(base_url="http://localhost:3000", connection_data_block_size=1000)
        file_length = 0
        with io.BytesIO() as file_handle:

            request = HttpRequest("GET", "http://localhost:3000/files/stream/nonempty",
                headers={
                    'Accept': 'image/png, application/json'
                },
            )

            response = await client._send_request(request, stream=True)
            assert response.status_code == 200

            stream = response.stream_download(None)

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
    async def test_send_request_put_stream(self):
        from bodyformdata.aio import AutoRestSwaggerBATFormDataService

        client = AutoRestSwaggerBATFormDataService(
            base_url="http://localhost:3000",
        )

        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')
        with io.BytesIO(test_bytes) as stream_data:
            request = HttpRequest("PUT", '/formdata/stream/uploadfile',
                headers={
                    'Content-Type': 'application/octet-stream'
                },
                data=stream_data,
            )
            response = await client._send_request(request)
            assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_send_request_with_client_path_format_arguments(self):
        from validation.aio import AutoRestValidationTest

        client = AutoRestValidationTest("mySubscriptionId", base_url="http://localhost:3000")

        request = HttpRequest("GET", "/fakepath/{subscriptionId}/123/150",
            headers={
                'Accept': 'application/json'
            },
        )

        response = await client._send_request(request)
        assert response.request.url == 'http://localhost:3000/fakepath/mySubscriptionId/123/150'

    @pytest.mark.asyncio
    async def test_send_request_full_url(self):
        from bodycomplex import AutoRestComplexTestService
        from bodycomplex.models import Siamese

        client = AutoRestComplexTestService(base_url="http://fakeUrl")

        request = HttpRequest("GET", "http://localhost:3000/complex/inheritance/valid",
            headers={
                'Accept': 'application/json'
            },
        )

        response = client._send_request(request)

        deserialized = Siamese.deserialize(response)
        assert 2 ==  deserialized.id
        assert "Siameeee" ==  deserialized.name
        assert -1 ==  deserialized.hates[1].id
        assert "Tomato" ==  deserialized.hates[1].name