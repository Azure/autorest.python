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

import unittest
import subprocess
import sys
import isodate
import tempfile
import json
from uuid import uuid4
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "Paging"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError
from msrestazure.azure_exceptions import CloudError
from msrest.authentication import BasicTokenAuthentication

from paging import AutoRestPagingTestService
from paging.models import PagingGetMultiplePagesWithOffsetOptions

import pytest

@pytest.fixture
def paging_client():
    cred = BasicTokenAuthentication({"access_token" :str(uuid4())})
    client = AutoRestPagingTestService(cred, base_url="http://localhost:3000")
    from .conftest import TestAuthentication  # Ugly, should migrate this file to pytest as I did for async.
    client._client.creds = TestAuthentication()
    return client


def test_paging_happy_path(paging_client):

    pages = paging_client.paging.get_single_pages()
    items = [i for i in pages]
    assert pages.next_link is None
    assert len(items) == 1

    assert items[0].properties.id == 1
    assert items[0].properties.name == "Product"

    pages = paging_client.paging.get_multiple_pages()
    assert pages.next_link is not None
    items = [i for i in pages]
    assert pages.next_link is None
    assert len(items) == 10

    pages.reset()
    more_items = [i for i in pages]
    eq = [e for e in items if e not in more_items]
    assert len(eq) == 0

    with pytest.raises(StopIteration):
        next(pages)

    pages = paging_client.paging.get_odata_multiple_pages()
    assert pages.next_link is not None
    items = [i for i in pages]
    assert pages.next_link is None
    assert len(items) == 10

    pages = paging_client.paging.get_multiple_pages_retry_first()
    assert pages.next_link is not None
    items = [i for i in pages]
    assert pages.next_link is None
    assert len(items) == 10

    pages = paging_client.paging.get_multiple_pages_retry_second()
    assert pages.next_link is not None
    items = [i for i in pages]
    assert pages.next_link is None
    assert len(items) == 10

    pages = paging_client.paging.get_single_pages(raw=True)
    items = [i for i in pages]
    assert pages.next_link is None
    assert len(items) == 1
    assert items == pages.raw.output

    pages = paging_client.paging.get_multiple_pages(raw=True)
    assert pages.next_link is not None
    items = [i for i in pages]
    assert len(items) == 10
    assert pages.raw.response is not None

    options = PagingGetMultiplePagesWithOffsetOptions(offset=100)
    pages = paging_client.paging.get_multiple_pages_with_offset(paging_get_multiple_pages_with_offset_options=options)
    assert pages.next_link is not None
    items = [i for i in pages]
    assert len(items) == 10
    assert items[-1].properties.id == 110

    pages = paging_client.paging.get_multiple_pages_retry_first(raw=True)
    assert pages.next_link is not None
    items = [i for i in pages]
    assert len(items) == 10

    pages = paging_client.paging.get_multiple_pages_retry_second(raw=True)
    assert pages.next_link is not None
    items = [i for i in pages]
    assert len(items) == 10

def test_paging_sad_path(paging_client):

    pages = paging_client.paging.get_single_pages_failure()
    with pytest.raises(CloudError):
        list(pages)

    pages = paging_client.paging.get_multiple_pages_failure()
    assert pages.next_link is not None

    with pytest.raises(CloudError):
        list(pages)

    pages = paging_client.paging.get_multiple_pages_failure_uri()
    with pytest.raises(CloudError):
        list(pages)

    pages = paging_client.paging.get_single_pages_failure(raw=True)
    with pytest.raises(CloudError):
        list(pages)

    pages = paging_client.paging.get_multiple_pages_failure(raw=True)
    assert pages.next_link is not None

    with pytest.raises(CloudError):
        list(pages)

    pages = paging_client.paging.get_multiple_pages_failure_uri(raw=True)

    with pytest.raises(CloudError):
        list(pages)

def test_paging_fragment_path(paging_client):

    pages = paging_client.paging.get_multiple_pages_fragment_next_link("1.6", "test_user")
    items = [i for i in pages]
    assert pages.next_link is None
    assert len(items) == 10

    with pytest.raises(AttributeError):
        # Be sure this method is not generated (Transform work)
        paging_client.paging.get_multiple_pages_fragment_next_link_next()  # pylint: disable=E1101
