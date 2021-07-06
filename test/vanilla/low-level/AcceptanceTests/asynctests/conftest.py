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
import pytest
from msrest import Serializer, Deserializer

@pytest.fixture()
def base_make_request():
    async def make_request(client, request):
        response = await client.send_request(request)
        response.raise_for_status()
        return response
    return make_request

@pytest.fixture()
def base_make_request_json_response():
    async def make_request_json_response(client, request):
        response = await client.send_request(request)
        response.raise_for_status()
        return response.json()
    return make_request_json_response

@pytest.fixture()
def base_make_stream_request():
    async def make_stream_request(client, request):
        response = await client.send_request(request, stream=True)
        response.raise_for_status()
        return response.stream_download()
    return make_stream_request

@pytest.fixture
def msrest_serializer():
    return Serializer()

@pytest.fixture
def msrest_deserializer():
    return Deserializer
