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
from bodycomplexversiontolerant.aio import AutoRestComplexTestService
from azure.core.pipeline.policies import CustomHookPolicy
try:
    from urlparse import urlparse  # type: ignore
except ImportError:
    from urllib.parse import urlparse

def get_client(callback):
    return AutoRestComplexTestService(policies=[CustomHookPolicy(raw_request_hook=callback)])

@pytest.mark.asyncio
async def test_header_input():
    def get_headers(pipeline_request):
        assert pipeline_request.http_request.headers["Accept"] == "my/content-type"
        raise ValueError("Passed!")
    client = get_client(callback=get_headers)
    with pytest.raises(ValueError) as ex:
        await client.basic.get_empty(headers={"Accept": "my/content-type"})
    assert str(ex.value) == "Passed!"
    await client.close()

@pytest.mark.asyncio
async def test_header_none_input():
    async with AutoRestComplexTestService() as client:
        await client.basic.get_empty(headers=None)

@pytest.mark.asyncio
async def test_query_input():
    def get_query(pipeline_request):
        assert urlparse(pipeline_request.http_request.url).query == "foo=bar"
        raise ValueError("Passed!")
    client = get_client(callback=get_query)
    with pytest.raises(ValueError) as ex:
        await client.basic.get_empty(params={"foo": "bar"})
    assert str(ex.value) == "Passed!"
    await client.close()

@pytest.mark.asyncio
async def test_query_none_input():
    async with AutoRestComplexTestService() as client:
        await client.basic.get_empty(params=None)
