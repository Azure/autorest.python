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
import logging
from datetime import date
from async_generator import yield_, async_generator

from xmlserviceversiontolerant.aio import AutoRestSwaggerBATXMLService
from xmlserviceversiontolerant.models import BlobType, ModelWithByteProperty, ModelWithUrlProperty
import pytest

_LOGGER = logging.getLogger(__name__)


@pytest.fixture
@async_generator
async def client():
    async with AutoRestSwaggerBATXMLService() as client:
        await yield_(client)


async def _assert_with_log(func, *args, **kwargs):
    def raise_for_status(response, deserialized, headers):
        response.http_response._internal_response.raise_for_status()

    try:
        http_response = await func(*args, cls=raise_for_status, **kwargs)
    except Exception as err:
        print(err.response.text())
        pytest.fail()


@pytest.mark.asyncio
async def test_json_xml(client):
    await client.xml.json_input({"id": 42})

    result = await client.xml.json_output()
    assert result.id == 42


@pytest.mark.asyncio
async def test_simple(client):
    # Slideshow

    slideshow = await client.xml.get_simple()
    assert slideshow.title == "Sample Slide Show"
    assert slideshow.date == "Date of publication"
    assert slideshow.author == "Yours Truly"
    assert len(slideshow.slides) == 2
    slides = slideshow.slides

    slide1 = slides[0]
    assert slide1.type == "all"
    assert slide1.title == "Wake up to WonderWidgets!"
    assert len(slide1.items) == 0

    slide2 = slides[1]
    assert slide2.type == "all"
    assert slide2.title == "Overview"
    assert len(slide2.items) == 3
    assert slide2.items[0] == "Why WonderWidgets are great"
    assert slide2.items[1] == ""
    assert slide2.items[2] == "Who buys WonderWidgets"

    await _assert_with_log(client.xml.put_simple, slideshow)


@pytest.mark.asyncio
async def test_empty_child_element(client):
    banana = await client.xml.get_empty_child_element()
    # That's the point of this test, it was an empty node.
    assert banana.flavor == ""
    await _assert_with_log(client.xml.put_empty_child_element, banana)


@pytest.mark.asyncio
async def test_empty_root_list(client):
    bananas = await client.xml.get_empty_root_list()
    assert bananas == []
    await _assert_with_log(client.xml.put_empty_root_list, bananas)


@pytest.mark.asyncio
async def test_root_list_single_item(client):
    bananas = await client.xml.get_root_list_single_item()
    assert len(bananas) == 1
    assert bananas[0].name == "Cavendish"
    await _assert_with_log(client.xml.put_root_list_single_item, bananas)


@pytest.mark.asyncio
async def test_root_list(client):
    bananas = await client.xml.get_root_list()
    assert len(bananas) == 2
    await _assert_with_log(client.xml.put_root_list, bananas)


@pytest.mark.asyncio
async def test_empty_wrapped_lists(client):
    bananas = await client.xml.get_empty_wrapped_lists()
    assert bananas.good_apples == []
    assert bananas.bad_apples == []
    await _assert_with_log(client.xml.put_empty_wrapped_lists, bananas)


@pytest.mark.asyncio
async def test_get_empty(client):
    slideshow = await client.xml.get_empty_list()
    await _assert_with_log(client.xml.put_empty_list, slideshow)


@pytest.mark.asyncio
async def test_wrapped_lists(client):
    bananas = await client.xml.get_wrapped_lists()
    assert bananas.good_apples == ["Fuji", "Gala"]
    assert bananas.bad_apples == ["Red Delicious"]
    await _assert_with_log(client.xml.put_wrapped_lists, bananas)


@pytest.mark.asyncio
async def test_complex_types(client):
    root = await client.xml.get_complex_type_ref_no_meta()
    assert root.ref_to_model.id == "myid"
    await client.xml.put_complex_type_ref_no_meta(root)

    root = await client.xml.get_complex_type_ref_with_meta()
    assert root.ref_to_model.id == "myid"
    await client.xml.put_complex_type_ref_with_meta(root)


@pytest.mark.asyncio
async def test_list_containers(client):
    containers = await client.xml.list_containers()
    assert len(containers.containers) == 3


@pytest.mark.asyncio
async def test_list_blobs(client):
    blobs = await client.xml.list_blobs()
    assert len(blobs.blobs.blob) == 5
    assert not blobs.blobs.blob_prefix
    assert len(blobs.blobs.blob) == 5
    blob = blobs.blobs.blob[0]
    assert blob.name == "blob1.txt"
    assert blob.properties.last_modified.date() == date(2009, 9, 9)
    assert blob.properties.etag == "0x8CBFF45D8A29A19"
    assert blob.properties.content_length == 100
    assert blob.properties.content_type == "text/html"
    # Check that an empty field in the XML is empty string
    assert blob.properties.content_encoding == ""
    assert blob.properties.content_language == "en-US"
    assert blob.properties.content_md5 == ""
    assert blob.properties.cache_control == "no-cache"
    assert blob.properties.blob_type == BlobType.block_blob
    # Check that a field NOT in the XML is None
    assert blob.properties.destination_snapshot is None
    assert len(blob.metadata) == 3
    assert blob.metadata["Color"] == "blue"
    assert blob.metadata["BlobNumber"] == "01"
    assert blob.metadata["SomeMetadataName"] == "SomeMetadataValue"


@pytest.mark.asyncio
async def test_service_properties(client):
    properties = await client.xml.get_service_properties()
    assert properties.hour_metrics is not None
    assert properties.minute_metrics is not None
    await _assert_with_log(client.xml.put_service_properties, properties)


@pytest.mark.asyncio
async def test_acls(client):
    acls = await client.xml.get_acls()
    assert len(acls) == 1
    assert acls[0].id == "MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI="
    await _assert_with_log(client.xml.put_acls, acls)


@pytest.mark.asyncio
async def test_xms_text(client):
    xml_object = await client.xml.get_xms_text()
    assert xml_object.language == "english"
    assert xml_object.content == "I am text"


@pytest.mark.asyncio
async def test_bytes(client):
    bytes_object = await client.xml.get_bytes()
    assert isinstance(bytes_object, ModelWithByteProperty)
    assert bytes_object.bytes == b"Hello world"
    await client.xml.put_binary(bytes_object)


@pytest.mark.asyncio
async def test_url(client):
    url_object = await client.xml.get_uri()
    assert isinstance(url_object, ModelWithUrlProperty)
    assert url_object.url == "https://myaccount.blob.core.windows.net/"
    await client.xml.put_uri(url_object)
