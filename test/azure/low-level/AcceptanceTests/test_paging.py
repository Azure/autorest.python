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
import functools
import sys
from azure.core.rest import HttpRequest
from azure.core.paging import ItemPaged
from paginglowlevel import AutoRestPagingTestService
from paginglowlevel.rest import paging
from azure.core.exceptions import HttpResponseError


import pytest

@pytest.fixture
def client():
    with AutoRestPagingTestService() as client:
        yield client

@pytest.fixture
def extract_data_fixture(deserializer):
    def _callback(pipeline_response, **kwargs):
        item_name = kwargs.pop("item_name", "value")
        next_link_name = kwargs.pop("next_link_name", "nextLink")
        try:
            deserialized = pipeline_response.http_response.json() # in the case of LRO + paging, the LRO returns an old response to us
        except AttributeError:
            deserialized = deserializer("object", pipeline_response.http_response)
        list_of_elem = deserialized[item_name]
        return deserialized.get(next_link_name, None), iter(list_of_elem)
    return _callback

@pytest.fixture
def get_next_fixture(client):
    def _callback(prepare_request, next_link=None):
        request = prepare_request(next_link)

        pipeline_response = client._client.pipeline.run(request)
        pipeline_response.http_response.raise_for_status()

        return pipeline_response
    return _callback

def default_prepare_request(next_link=None, **kwargs):
    initial_request = kwargs.pop("initial_request")
    next_request = kwargs.pop("next_request", None)
    if not next_link:
        request = initial_request()
    elif next_request:
        try:
            request = next_request(next_link)
        except TypeError:
            request = next_request()  # the query one doesn't take next link
    else:
        request = initial_request(template_url=next_link)
    return request

@pytest.fixture
def get_pager(get_next_fixture, extract_data_fixture):
    def _callback(initial_request, **kwargs):
        prepare_request = functools.partial(
            default_prepare_request,
            initial_request=initial_request,
            **kwargs
        )
        get_next = functools.partial(
            get_next_fixture,
            prepare_request,
        )
        extract_data = kwargs.pop("extract_data", None)
        if not extract_data:
            extract_data = functools.partial(
                extract_data_fixture,
                **kwargs
            )

        return ItemPaged(get_next, extract_data)
    return _callback

def test_get_no_item_name_pages(get_pager):
    pages = get_pager(initial_request=paging.build_get_no_item_name_pages_request)
    items = [i for i in pages]
    assert len(items) == 1
    assert items[0]['properties']['id'] == 1
    assert items[0]['properties']['name'] == "Product"

def test_get_null_next_link_name_pages(get_pager):
    def extract_data(pipeline_response):
        deserialized = pipeline_response.http_response.json()
        list_of_elem = deserialized['values']
        # defined as None next link in swagger
        return None, iter(list_of_elem)
    pages = get_pager(
        initial_request=paging.build_get_null_next_link_name_pages_request,
        item_name="values",
        extract_data=extract_data
    )
    items = [i for i in pages]
    assert len(items) == 1
    assert items[0]['properties']['id'] == 1
    assert items[0]['properties']['name'] == "Product"

def test_get_single_pages(get_pager):
    pages = get_pager(initial_request=paging.build_get_single_pages_request, item_name="values")
    items = [i for i in pages]
    assert len(items) == 1
    assert items[0]['properties']['id'] == 1
    assert items[0]['properties']['name'] == "Product"

def test_get_multiple_pages(get_pager):
    pages = get_pager(initial_request=paging.build_get_multiple_pages_request, item_name="values")
    items = [i for i in pages]
    assert len(items) == 10

def test_query_params(get_pager):
    initial_request = functools.partial(
        paging.build_get_with_query_params_request,
        required_query_parameter='100'
    )
    pages = get_pager(
        initial_request=initial_request,
        next_request=paging.build_next_operation_with_query_params_request,
        item_name="values"
    )
    items = [i for i in pages]
    assert len(items) == 2

def test_get_odata_multiple_pages(get_pager):
    pages = get_pager(
        initial_request=paging.build_get_odata_multiple_pages_request,
        item_name="values",
        next_link_name="odata.nextLink",
    )
    items = [i for i in pages]
    assert len(items) == 10

def test_get_multiple_pages_retry_first(get_pager):
    pages = get_pager(
        initial_request=paging.build_get_multiple_pages_retry_first_request,
        item_name="values",
    )
    items = [i for i in pages]
    assert len(items) == 10

def test_get_multiple_pages_retry_second(get_pager):
    pages = get_pager(
        initial_request=paging.build_get_multiple_pages_retry_second_request,
        item_name="values",
    )
    items = [i for i in pages]
    assert len(items) == 10

def test_get_multiple_pages_with_offset(get_pager):
    initial_request = functools.partial(
        paging.build_get_multiple_pages_with_offset_request,
        100,
    )
    pages = get_pager(
        initial_request=initial_request,
        item_name="values"
    )
    items = [i for i in pages]
    assert len(items) == 10
    assert items[-1]['properties']['id'] == 110


def test_get_single_pages_failure(get_pager):
    pages = get_pager(
        initial_request=paging.build_get_single_pages_failure_request,
        item_name="values"
    )
    with pytest.raises(HttpResponseError):
        list(pages)

def test_get_multiple_pages_failure(get_pager):
    pages = get_pager(
        initial_request=paging.build_get_multiple_pages_failure_request,
        item_name="values"
    )
    with pytest.raises(HttpResponseError):
        list(pages)

def test_get_multiple_pages_failure_uri(get_pager):
    pages = get_pager(
        initial_request=paging.build_get_multiple_pages_failure_uri_request,
        item_name="values"
    )
    with pytest.raises(HttpResponseError):
        list(pages)

def test_paging_fragment_path(get_pager):
    initial_request = functools.partial(
        paging.build_get_multiple_pages_fragment_next_link_request,
        "test_user",
        api_version="1.6"
    )
    next_request = functools.partial(
        paging.build_next_fragment_request,
        "test_user",
        api_version="1.6"
    )
    pages = get_pager(
        initial_request=initial_request,
        next_request=next_request,
        item_name="values",
        next_link_name="odata.nextLink",
    )
    items = [i for i in pages]
    assert len(items) == 10

    with pytest.raises(AttributeError):
        # Be sure this method is not generated (Transform work)
        paging.build_get_multiple_pages_fragment_next_link_next_request

@pytest.mark.skip(reason="Can't figure this out yet, going to add later")
def test_get_multiple_pages_lro(client, get_next_fixture, extract_data_fixture):
    """LRO + Paging at the same time.
    """
    from azure.mgmt.core.polling.arm_polling import ARMPolling
    from azure.core.polling import LROPoller
    # initial LRO call
    pipeline_response = client._client._pipeline.run(
        paging.build_get_multiple_pages_lro_request(),
    )
    pipeline_response.http_response.raise_for_status()
    prepare_request = functools.partial(
        default_prepare_request,
        initial_request=paging.build_get_multiple_pages_lro_request,
    )
    def get_long_running_output(pipeline_response):
        def internal_get_next(next_link=None):
            if next_link is None:
                return pipeline_response
            else:
                return get_next_fixture(prepare_request, next_link)
        extract_data = functools.partial(
            extract_data_fixture,
            item_name="values"
        )
        return ItemPaged(internal_get_next, extract_data)

    polling_method = ARMPolling(timeout=0)
    poller = LROPoller(client._client, pipeline_response, get_long_running_output, polling_method)
    pager = poller.result()

    # paging calls
    items = list(pager)

    assert len(items) == 10
    assert items[0]['properties']['id'] == 1
    assert items[1]['properties']['id'] == 2

def test_initial_response_no_items(get_pager):
    pages = get_pager(
        paging.build_first_response_empty_request,
    )
    items = [i for i in pages]
    assert len(items) == 1
