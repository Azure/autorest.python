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
from constantsversiontolerant.aio import AutoRestSwaggerConstantService

@pytest.mark.asyncio
async def test_put_client_constants():
    async with AutoRestSwaggerConstantService(
        header_constant=True,
        query_constant=100,
        path_constant="path"
    ) as client:
        await client.contants.put_client_constants()
        assert client._config.header_constant == True
        assert client._config.query_constant == 100
        assert client._config.path_constant == "path"

@pytest.mark.asyncio
async def test_put_client_constants_override():
    async with AutoRestSwaggerConstantService(
        header_constant=False,
        query_constant=0,
        path_constant="new_path"
    ) as client:
        assert client._config.header_constant == False
        assert client._config.query_constant == 0
        assert client._config.path_constant == "new_path"
