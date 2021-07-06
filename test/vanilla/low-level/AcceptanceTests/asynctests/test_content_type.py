# coding=utf-8
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
from mediatypeslowlevel.aio import MediaTypesClient
from mediatypeslowlevel.rest import *
from async_generator import yield_, async_generator

@pytest.mark.asyncio
async def test_stream_unread_until_send_request():
    class FakeStream:
        def __init__(self):
            self.call_count = 0

        @async_generator
        async def streaming_body(self, data):
            self.call_count += 1
            await yield_(data)

    fake_stream = FakeStream()
    request = build_analyze_body_request(content=fake_stream.streaming_body(b"PDF"))
    assert not request.headers.get("Content-Type")
    assert fake_stream.call_count == 0
    await MediaTypesClient().send_request(request)
    assert fake_stream.call_count == 1
