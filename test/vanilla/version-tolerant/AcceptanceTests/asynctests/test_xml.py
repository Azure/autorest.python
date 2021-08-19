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
from ..serializer import deserialize_base64
from async_generator import yield_, async_generator

from xmlserviceversiontolerant.aio import AutoRestSwaggerBATXMLService

import pytest

_LOGGER = logging.getLogger(__name__)

@pytest.fixture
@async_generator
async def client():
    async with AutoRestSwaggerBATXMLService(endpoint="http://localhost:3000") as client:
        await yield_(client)

async def _assert_with_log(func, *args, **kwargs):
    def raise_for_status(response, deserialized, headers):
        response.http_response._internal_response.raise_for_status()
    try:
        http_response = await func(*args, cls=raise_for_status, **kwargs)
    except Exception as err:
        print(err.response.text)
        pytest.fail()

@pytest.mark.asyncio
async def test_json_xml(client):
    await client.xml.json_input({"id": 42})

    result = await client.xml.json_output()
    assert result['id'] == 42

@pytest.mark.asyncio
async def test_simple(client):
    # Slideshow

    slideshow = await client.xml.get_simple()
    assert slideshow.attrib['title'] == "Sample Slide Show"
    assert slideshow.attrib['date'] == "Date of publication"
    assert slideshow.attrib['author'] == "Yours Truly"
    slides = list(slideshow.iterfind('slide'))
    assert len(slides) == 2

    slide1 = slides[0]
    assert slide1.attrib['type'] == "all"
    assert next(slide1.iterfind('title')).text == "Wake up to WonderWidgets!"
    assert len(list(slide1.iterfind('item'))) == 0

    slide2 = slides[1]
    assert slide2.attrib['type'] == "all"
    assert next(slide2.iterfind('title')).text == "Overview"
    items = list(slide2.iterfind('item'))
    assert len(items) == 3
    assert items[0].text == "Why WonderWidgets are great"
    assert items[1].text == None
    assert items[2].text == "Who buys WonderWidgets"

    await _assert_with_log(client.xml.put_simple, slideshow)

@pytest.mark.asyncio
async def test_empty_child_element(client):
    banana = await client.xml.get_empty_child_element()
    assert banana.attrib == {} # That's the point of this test, it was an empty node.
    await _assert_with_log(client.xml.put_empty_child_element, banana)

@pytest.mark.asyncio
async def test_empty_root_list(client):
    bananas = await client.xml.get_empty_root_list()
    assert bananas.tag == 'bananas'
    assert bananas.attrib == {}
    await _assert_with_log(client.xml.put_empty_root_list, bananas)

@pytest.mark.asyncio
async def test_root_list_single_item(client):
    xml_body = await client.xml.get_root_list_single_item()
    bananas = list(xml_body.iterfind('banana'))
    assert len(bananas) == 1
    assert next(bananas[0].iterfind('name')).text == "Cavendish"
    await _assert_with_log(client.xml.put_root_list_single_item, xml_body)

@pytest.mark.asyncio
async def test_root_list(client):
    xml_body = await client.xml.get_root_list()
    bananas = list(xml_body.iterfind('banana'))
    assert len(bananas) == 2
    await _assert_with_log(client.xml.put_root_list, xml_body)

@pytest.mark.asyncio
async def test_empty_wrapped_lists(client):
    bananas = await client.xml.get_empty_wrapped_lists()
    assert [a for a in bananas.iterfind('GoodApples') if a.text] == []
    assert [a for a in bananas.iterfind('BadApples') if a.text] == []
    await _assert_with_log(client.xml.put_empty_wrapped_lists, bananas)

@pytest.mark.asyncio
async def test_get_empty(client):
    slideshow = await client.xml.get_empty_list()
    await _assert_with_log(client.xml.put_empty_list, slideshow)

@pytest.mark.asyncio
async def test_wrapped_lists(client):
    bananas = await client.xml.get_wrapped_lists()
    good_apples = bananas.find('GoodApples')
    assert [a.text for a in good_apples.iterfind('Apple')] == ['Fuji', 'Gala']
    bad_apples = bananas.find('BadApples')
    assert [a.text for a in bad_apples.iterfind('Apple')] == ['Red Delicious']
    await _assert_with_log(client.xml.put_wrapped_lists, bananas)

@pytest.mark.asyncio
async def test_complex_types(client):
    root = await client.xml.get_complex_type_ref_no_meta()
    ref_to_model = root.find('RefToModel')
    assert ref_to_model.find('ID').text == "myid"
    await client.xml.put_complex_type_ref_no_meta(root)

    root = await client.xml.get_complex_type_ref_with_meta()
    ref_to_model = root.find('XMLComplexTypeWithMeta')
    assert ref_to_model.find('ID').text == "myid"
    await client.xml.put_complex_type_ref_with_meta(root)

@pytest.mark.asyncio
async def test_list_containers(client):
    xml_body = await client.xml.list_containers()
    containers = xml_body.find('Containers')
    container_list = list(containers.iterfind('Container'))
    assert len(container_list) == 3

@pytest.mark.asyncio
async def test_list_blobs(client):
    xml_body = await client.xml.list_blobs()
    blobs_xml_body = xml_body.find('Blobs')
    blobs = list(blobs_xml_body.iterfind('Blob'))
    assert len(blobs) == 5
    assert blobs_xml_body.find('BlobPrefix') is None
    blob = blobs[0]
    assert blob.find('Name').text == "blob1.txt"
    properties = blob.find('Properties')
    assert properties.find('Last-Modified').text == 'Wed, 09 Sep 2009 09:20:02 GMT'
    assert properties.find('Etag').text == "0x8CBFF45D8A29A19"
    assert properties.find('Content-Length').text == "100"
    assert properties.find('Content-Type').text == "text/html"
    # Check that an empty field in the XML is empty string
    assert properties.find('Content-Encoding').text is None
    assert properties.find('Content-Language').text == "en-US"
    assert properties.find('Content-MD5').text is None
    assert properties.find('Cache-Control').text == "no-cache"
    assert properties.find('BlobType').text == "BlockBlob"
    # Check that a field NOT in the XML is None
    assert properties.find('Destination-Snapshot') is None
    metadata_body = blob.find('Metadata')
    assert metadata_body.find("Color").text == "blue"
    assert metadata_body.find("BlobNumber").text == "01"
    assert metadata_body.find("SomeMetadataName").text == "SomeMetadataValue"

@pytest.mark.asyncio
async def test_service_properties(client):
    properties = await client.xml.get_service_properties()
    assert properties.find('HourMetrics') is not None
    assert properties.find('MinuteMetrics') is not None
    await _assert_with_log(client.xml.put_service_properties, properties)

@pytest.mark.asyncio
async def test_acls(client):
    acls = await client.xml.get_acls()
    signed_identifiers = list(acls.iterfind('SignedIdentifier'))
    assert len(signed_identifiers) == 1
    assert signed_identifiers[0].find('Id').text == 'MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI='
    await _assert_with_log(client.xml.put_acls, acls)

@pytest.mark.asyncio
async def test_xms_text(client):
    xml_object = await client.xml.get_xms_text()
    assert xml_object.attrib['language'] == "english"
    assert xml_object.text == "I am text"

@pytest.mark.asyncio
async def test_bytes(client):
    bytes_object = await client.xml.get_bytes()
    assert bytes_object.tag == 'ModelWithByteProperty'
    assert deserialize_base64(bytes_object.find('Bytes').text) == b"Hello world"
    await client.xml.put_binary(bytes_object)

@pytest.mark.asyncio
async def test_url(client):
    url_object = await client.xml.get_uri()
    assert url_object.tag == 'ModelWithUrlProperty'
    assert url_object.find('Url').text == 'https://myaccount.blob.core.windows.net/'
    await client.xml.put_uri(url_object)
