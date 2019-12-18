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
import sys
import os
from os.path import dirname, pardir, join, realpath
import inspect

from paging.aio import AutoRestPagingTestService
from subscriptionidapiversion.aio import MicrosoftAzureTestUrl
from lro.aio import AutoRestLongRunningOperationTestService
import asyncio

import pytest


def has_tracing_decorator(function):
    lines = []
    source = inspect.getsource(function)
    decorator = "@distributed_trace_async" if asyncio.iscoroutinefunction(function) else "@distributed_trace"
    return "def wrapper_use_tracer" in source or decorator in source


@pytest.mark.asyncio
async def test_paging():
    async with AutoRestPagingTestService("cred", base_url="dummy url") as client:
        assert has_tracing_decorator(client.paging.get_single_pages)


@pytest.mark.asyncio
async def test_lro():
    async with AutoRestLongRunningOperationTestService("cred", base_url="dummy url") as client:
        assert not has_tracing_decorator(client.lros._put201_creating_succeeded200_initial)
        assert has_tracing_decorator(client.lros.put201_creating_succeeded200)
        assert not has_tracing_decorator(client.lros._put201_creating_succeeded200_initial)


def test_azure_url():
    client = MicrosoftAzureTestUrl("cred", "sub_id", base_url="dummy url")
    assert has_tracing_decorator(client.group.get_sample_resource_group)