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

from xmlservicelowlevel.aio import AutoRestSwaggerBATXMLService

import xml.etree.ElementTree as ET
from xmlservicelowlevel.rest import xml
from base64 import b64decode

import pytest
@pytest.fixture
@async_generator
async def client():
    async with AutoRestSwaggerBATXMLService(base_url="http://localhost:3000") as client:
        await yield_(client)

@pytest.fixture
def make_request(client, base_make_request):
    async def _make_request(request):
        return await base_make_request(client, request)
    return _make_request

@pytest.fixture
def make_request_text_response(client, base_make_request):
    async def _make_request(request):
        return (await base_make_request(client, request)).text
    return _make_request



@pytest.mark.asyncio
async def test_json_xml(make_request, make_request_text_response):
    request = xml.build_json_input_request(json={"id": 42})
    await make_request(request)

    request = xml.build_json_output_request()
    assert (await make_request(request)).json()['id'] == 42

@pytest.mark.asyncio
async def test_simple(make_request, make_request_text_response):
    # Slideshow

    request = xml.build_get_simple_request()
    slideshow = ET.fromstring(await make_request_text_response(request))
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

    request = xml.build_put_simple_request(content=slideshow, headers={"Content-Type": "application/xml"})
    await make_request(request)

@pytest.mark.asyncio
async def test_empty_child_element(make_request, make_request_text_response):
    request = xml.build_get_empty_child_element_request()
    banana = ET.fromstring(await make_request_text_response(request))
    assert banana.attrib == {}# That's the point of this test, it was an empty node.
    request = xml.build_put_empty_child_element_request(content=banana, headers={"Content-Type": "application/xml"})
    await make_request(request)

@pytest.mark.asyncio
async def test_empty_root_list(make_request, make_request_text_response):
    request = xml.build_get_empty_root_list_request()
    empty = ET.fromstring(await make_request_text_response(request))
    assert empty.tag == 'bananas'
    assert empty.attrib == {}
    assert await make_request_text_response(request) == "<?xml version='1.0' encoding='UTF-8'?>\n<bananas/>"
    request = xml.build_put_empty_root_list_request(content=empty, headers={"Content-Type": "application/xml"})
    await make_request(request)

@pytest.mark.asyncio
async def test_root_list_single_item(make_request, make_request_text_response):
    request = xml.build_get_root_list_single_item_request()
    xml_body = ET.fromstring(await make_request_text_response(request))
    bananas = list(xml_body.iterfind('banana'))
    assert len(bananas) == 1
    assert next(bananas[0].iterfind('name')).text == "Cavendish"
    request = xml.build_put_root_list_single_item_request(content=xml_body, headers={"Content-Type": "application/xml"})
    await make_request(request)

@pytest.mark.asyncio
async def test_root_list(make_request, make_request_text_response):
    request = xml.build_get_root_list_request()
    xml_body = ET.fromstring(await make_request_text_response(request))
    bananas = list(xml_body.iterfind('banana'))
    assert len(bananas) == 2
    request = xml.build_put_root_list_request(content=xml_body, headers={"Content-Type": "application/xml"})
    await make_request(request)

@pytest.mark.asyncio
async def test_empty_wrapped_lists(make_request, make_request_text_response):
    request = xml.build_get_empty_wrapped_lists_request()
    bananas = ET.fromstring(await make_request_text_response(request))
    """
    <AppleBarrel>
        <GoodApples></GoodApples>
        <BadApples/>
    </AppleBarrel>`;
    """
    good_apples = [a for a in bananas.iterfind('GoodApples') if a.text]
    assert len(good_apples) == 0
    bad_apples = [a for a in bananas.iterfind('BadApples') if a.text]
    assert len(bad_apples) == 0
    request = xml.build_put_empty_wrapped_lists_request(content=bananas, headers={"Content-Type": "application/xml"})
    await make_request(request)

@pytest.mark.asyncio
async def test_get_empty(make_request, make_request_text_response):
    request = xml.build_get_empty_list_request()
    slideshow = ET.fromstring(await make_request_text_response(request))
    request = xml.build_put_empty_list_request(content=slideshow, headers={"Content-Type": "application/xml"})
    await make_request(request)

@pytest.mark.asyncio
async def test_wrapped_lists(make_request, make_request_text_response):
    request = xml.build_get_wrapped_lists_request()
    bananas = ET.fromstring(await make_request_text_response(request))
    good_apples = bananas.find('GoodApples')
    assert [a.text for a in good_apples.iterfind('Apple')] == ['Fuji', 'Gala']

    bad_apples = bananas.find('BadApples')
    assert [a.text for a in bad_apples.iterfind('Apple')] == ['Red Delicious']
    request = xml.build_put_wrapped_lists_request(content=bananas, headers={"Content-Type": "application/xml"})
    await make_request(request)

@pytest.mark.asyncio
async def test_complex_types(make_request, make_request_text_response):
    request = xml.build_get_complex_type_ref_no_meta_request()
    root = ET.fromstring(await make_request_text_response(request))
    ref_to_model = root.find('RefToModel')
    assert ref_to_model.find('ID').text == "myid"
    request = xml.build_put_complex_type_ref_no_meta_request(content=root, headers={"Content-Type": "application/xml"})
    await make_request(request)

    request = xml.build_get_complex_type_ref_with_meta_request()
    root = ET.fromstring(await make_request_text_response(request))
    ref_to_model = root.find('XMLComplexTypeWithMeta')
    assert ref_to_model.find('ID').text == "myid"
    request = xml.build_put_complex_type_ref_with_meta_request(content=root, headers={"Content-Type": "application/xml"})
    await make_request(request)

@pytest.mark.asyncio
async def test_list_containers(make_request, make_request_text_response):
    request = xml.build_list_containers_request()
    xml_body = ET.fromstring(await make_request_text_response(request))
    containers = xml_body.find('Containers')
    container_list = list(containers.iterfind('Container'))
    assert len(container_list) == 3

@pytest.mark.asyncio
async def test_list_blobs(make_request, make_request_text_response):
    request = xml.build_list_blobs_request()
    xml_body = ET.fromstring(await make_request_text_response(request))
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
async def test_service_properties(make_request, make_request_text_response):
    request = xml.build_get_service_properties_request()
    properties = ET.fromstring(await make_request_text_response(request))
    assert properties.find('HourMetrics') is not None
    assert properties.find('MinuteMetrics') is not None
    request = xml.build_put_service_properties_request(content=properties, headers={"Content-Type": "application/xml"})
    await make_request(request)

@pytest.mark.asyncio
async def test_acls(make_request, make_request_text_response):
    request = xml.build_get_acls_request()
    acls = ET.fromstring(await make_request_text_response(request))
    signed_identifiers = list(acls.iterfind('SignedIdentifier'))
    assert len(signed_identifiers) == 1
    assert signed_identifiers[0].find('Id').text == 'MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI='
    request = xml.build_put_acls_request(content=acls, headers={"Content-Type": "application/xml"})
    await make_request(request)


@pytest.mark.asyncio
async def test_xms_text(make_request, make_request_text_response):
    request = xml.build_get_xms_text_request()
    xml_object = ET.fromstring(await make_request_text_response(request))
    assert xml_object.attrib['language'] == "english"
    assert xml_object.text == "I am text"

@pytest.mark.asyncio
async def test_bytes(make_request, make_request_text_response):
    request = xml.build_get_bytes_request()
    bytes_object = ET.fromstring(await make_request_text_response(request))
    assert bytes_object.tag == 'ModelWithByteProperty'
    assert b64decode(bytes_object.find('Bytes').text) == b"Hello world"

    request = xml.build_put_binary_request(content=bytes_object, headers={"Content-Type": "application/xml"})
    await make_request(request)

@pytest.mark.asyncio
async def test_url(make_request, make_request_text_response):
    request = xml.build_get_uri_request()
    url_object = ET.fromstring(await make_request_text_response(request))
    assert url_object.tag == 'ModelWithUrlProperty'
    assert url_object.find('Url').text == 'https://myaccount.blob.core.windows.net/'

    request = xml.build_put_uri_request(content=url_object, headers={"Content-Type": "application/xml"})
    await make_request(request)
