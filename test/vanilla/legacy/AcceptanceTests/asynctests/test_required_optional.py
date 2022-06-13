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

from async_generator import yield_, async_generator
import unittest
import subprocess
import sys
import isodate
import os
import io
from datetime import date, datetime, timedelta
from os.path import dirname, pardir, join, realpath

from azure.core.exceptions import DeserializationError, SerializationError
from msrest.exceptions import ValidationError

from requiredoptional.aio import AutoRestRequiredOptionalTestService
from requiredoptional.models import StringWrapper, ArrayWrapper, ClassWrapper

import pytest

@pytest.fixture
@async_generator
async def client_required():
    async with AutoRestRequiredOptionalTestService(
            "required_path",
            "required_query",
            base_url="http://localhost:3000") as client:
        client._config.required_global_path = "required_path"
        client._config.required_global_query = "required_query"
        await yield_(client)

@pytest.fixture
@async_generator
async def client():
    async with AutoRestRequiredOptionalTestService(
            "required_path",
            "required_query",
            base_url="http://localhost:3000") as client:
        client._config.required_global_path = None
        client._config.required_global_query = None
        await yield_(client)

class TestRequiredOptional(object):
    # These clients have a required global path and query

    @pytest.mark.asyncio
    async def test_put_optional(self, client_required):
        await client_required.implicit.put_optional_query(None)
        await client_required.implicit.put_optional_body(None)
        await client_required.implicit.put_optional_header(None)

    @pytest.mark.asyncio
    async def test_get_optional_global_query(self, client_required):
        await client_required.implicit.get_optional_global_query(headers={})

    @pytest.mark.asyncio
    async def test_post_optional_integer(self, client_required):
        await client_required.explicit.post_optional_integer_parameter(None)
        await client_required.explicit.post_optional_integer_property(None)
        await client_required.explicit.post_optional_integer_header(None)

    @pytest.mark.asyncio
    async def test_post_optional_string(self, client_required):
        await client_required.explicit.post_optional_string_parameter(None)
        await client_required.explicit.post_optional_string_property(None)
        await client_required.explicit.post_optional_string_header(None)

    @pytest.mark.asyncio
    async def test_post_optional_class(self, client_required):
        await client_required.explicit.post_optional_class_parameter(None)
        await client_required.explicit.post_optional_class_property(None)

    @pytest.mark.asyncio
    async def test_post_optional_array(self, client_required):
        await client_required.explicit.post_optional_array_parameter(None)
        await client_required.explicit.post_optional_array_property(None)
        await client_required.explicit.post_optional_array_header(None)

    @pytest.mark.asyncio
    async def test_implicit_get_required(self, client):
        with pytest.raises(ValidationError):
            await client.implicit.get_required_path(None)

        with pytest.raises(ValidationError):
            await client.implicit.get_required_global_path()

        with pytest.raises(ValidationError):
            await client.implicit.get_required_global_query()

    @pytest.mark.asyncio
    async def test_post_required_string(self, client):
        with pytest.raises(ValidationError):
            await client.explicit.post_required_string_header(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_string_parameter(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_string_property(None)

    @pytest.mark.asyncio
    async def test_post_required_array(self, client):
        with pytest.raises(ValidationError):
            await client.explicit.post_required_array_header(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_array_parameter(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_array_property(None)

    @pytest.mark.asyncio
    async def test_post_required_class(self, client):
        with pytest.raises(ValidationError):
            await client.explicit.post_required_class_parameter(None)

        with pytest.raises(ValidationError):
            await client.explicit.post_required_class_property(None)

    @pytest.mark.asyncio
    async def test_explict_put_optional_binary_body(self, client):
        await client.explicit.put_optional_binary_body()

    @pytest.mark.asyncio
    async def test_explict_put_required_binary_body(self, client):
        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')
        result = io.BytesIO()
        with io.BytesIO(test_bytes) as stream_data:
            await client.explicit.put_required_binary_body(stream_data)


    @pytest.mark.asyncio
    async def test_implicit_put_optional_binary_body(self, client):
        await client.implicit.put_optional_binary_body()