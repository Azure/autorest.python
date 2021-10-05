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
import json
from bodybinarylowlevel.aio import BinaryWithContentTypeApplicationJson
from bodybinarylowlevel.rest import upload

@pytest.fixture
async def client():
    async with BinaryWithContentTypeApplicationJson() as client:
        yield client

@pytest.fixture
def send_request(client, base_send_request):
    async def _send_request(request):
        return await base_send_request(client, request)
    return _send_request

async def test_upload_file(send_request):
    request = upload.build_file_request(content=json.dumps({"more": "cowbell"}), headers={"Content-Type": "application/json"})
    await send_request(request)

async def test_upload_binary(send_request):
    request = upload.build_binary_request(content=b"Hello, world!", headers={"Content-Type": "application/octet-stream"})
    await send_request(request)
