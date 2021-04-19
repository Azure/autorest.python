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
from xmlservice import AutoRestSwaggerBATXMLService
from xmlservice._rest import xml
from xmlservice.models import *

from datetime import date

import pytest


@pytest.fixture
def client():
    with AutoRestSwaggerBATXMLService(base_url="http://localhost:3000") as client:
        yield client

@pytest.fixture
def make_request(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request)
    return _make_request

@pytest.fixture
def make_request_text_response(client, base_make_request):
    def _make_request(request):
        return base_make_request(client, request).text
    return _make_request

def test_json_xml(make_request):
    request = xml.build_json_input_request(json=JSONInput(id=42).serialize())
    make_request(request)

    request = xml.build_json_output_request()
    assert make_request(request).json()['id'] == 42

def test_simple(make_request, make_request_text_response):
    # Slideshow

    request = xml.build_get_simple_request()
    slideshow = Slideshow.deserialize(make_request_text_response(request), content_type="application/xml")
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
    assert slide2.items[1] == ''
    assert slide2.items[2] == "Who buys WonderWidgets"

    request = xml.build_put_simple_request(content=slideshow.serialize(is_xml=True))
    make_request(request)

def test_empty_child_element(make_request, make_request_text_response):
    request = xml.build_get_empty_child_element_request()
    banana = Banana.deserialize(make_request_text_response(request), content_type="application/xml")
    assert banana.flavor == '' # That's the point of this test, it was an empty node.
    request = xml.build_put_empty_child_element_request(content=banana.serialize(is_xml=True))
    make_request(request)

def test_empty_root_list(make_request_text_response):
    request = xml.build_get_empty_root_list_request()
    bananas = Banana.deserialize(make_request_text_response(request), content_type="application/xml")
    assert bananas == []
    request = xml.build_put_empty_root_list_request(content=bananas.serialize(is_xml=True))

def test_root_list_single_item(make_request, make_request_text_response):
    request = xml.build_get_root_list_single_item_request()
    bananas = Banana.deserialize(make_request_text_response(request), content_type="application/xml")
    assert len(bananas) == 1
    assert bananas[0].name == "Cavendish"
    request = xml.build_put_root_list_single_item_request(content=bananas.serialize(is_xml=True))
    make_request(request)

def test_root_list(make_request, make_request_text_response):
    request = xml.build_get_root_list_request()
    bananas = Banana.deserialize(make_request_text_response(request), content_type="application/xml")
    assert len(bananas) == 2
    request = xml.build_put_root_list_request(content=bananas.serialize(is_xml=True))
    make_request(request)

def test_empty_wrapped_lists(make_request, make_request_text_response):
    request = xml.build_get_empty_wrapped_lists_request()
    bananas = Banana.deserialize(make_request_text_response(request), content_type="application/xml")
    assert bananas.good_apples == []
    assert bananas.bad_apples == []
    request = xml.build_put_empty_wrapped_lists_request(content=bananas.serialize(is_xml=True))
    make_request(request)

def test_get_empty(make_request, make_request_text_response):
    request = xml.build_get_empty_list_request()
    slideshow = Slideshow.deserialize(make_request_text_response(request), content_type="application/xml")
    request = xml.build_put_empty_list_request(content=slideshow.serialize(is_xml=True))
    make_request(request)

def test_wrapped_lists(make_request, make_request_text_response):
    request = xml.build_get_wrapped_lists_request()
    bananas = Banana.deserialize(make_request_text_response(request), content_type="application/xml")
    assert bananas.good_apples == ['Fuji', 'Gala']
    assert bananas.bad_apples == ['Red Delicious']
    request = xml.build_put_wrapped_lists_request(content=bananas.serialize(is_xml=True))
    make_request(request)

def test_complex_types(make_request, make_request_text_response):
    request = xml.build_get_complex_type_ref_no_meta_request()
    root = RootWithRefAndNoMeta.deserialize(make_request_text_response(request), content_type="application/xml")
    assert root.ref_to_model.id == "myid"
    request = xml.build_put_complex_type_ref_no_meta_request(content=root.serialize(is_xml=True))
    make_request(request)

    request = xml.build_get_complex_type_ref_with_meta_request()
    root = RootWithRefAndMeta.deserialize(make_request_text_response(request), content_type="application/xml")
    assert root.ref_to_model.id == "myid"
    request = xml.build_put_complex_type_ref_with_meta_request(content=root.serialize(is_xml=True))
    make_request(request)

def test_list_containers(make_request_text_response):
    request = xml.build_list_containers_request()
    containers = ListContainersResponse.deserialize(make_request_text_response(request), content_type="application/xml")
    assert len(containers.containers) == 3

def test_list_blobs(make_request_text_response):
    request = xml.build_list_blobs_request()
    blobs = ListBlobsResponse.deserialize(make_request_text_response(request), content_type="application/xml")
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
    assert blob.properties.content_encoding == ''
    assert blob.properties.content_language == "en-US"
    assert blob.properties.content_md5 == ''
    assert blob.properties.cache_control == "no-cache"
    assert blob.properties.blob_type == BlobType.block_blob
    # Check that a field NOT in the XML is None
    assert blob.properties.destination_snapshot is None
    assert len(blob.metadata) == 3
    assert blob.metadata["Color"] == "blue"
    assert blob.metadata["BlobNumber"] == "01"
    assert blob.metadata["SomeMetadataName"] == "SomeMetadataValue"

def test_service_properties(make_request, make_request_text_response):
    request = xml.build_get_service_properties_request()
    properties = StorageServiceProperties.deserialize(make_request_text_response(request), content_type="application/xml")
    assert properties.hour_metrics is not None
    assert properties.minute_metrics is not None
    request = xml.build_put_service_properties_request(content=properties.serialize(is_xml=True))
    make_request(request)

# def test_acls(make_request, make_request_text_response):
#     request = xml.build_get_acls_request()
#     acls = [Sign]
#     assert len(acls) == 1
#     assert acls[0].id == 'MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI='
#     _assert_with_log(client.xml.put_acls, acls)

def test_xms_text(make_request_text_response):
    request = xml.build_get_xms_text_request()
    xml_object = ObjectWithXMsTextProperty.deserialize(make_request_text_response(request), content_type="application/xml")
    assert xml_object.language == "english"
    assert xml_object.content == "I am text"

def test_get_bytes(make_request_text_response):
    request = xml.build_get_bytes_request()
    bytes_object = ModelWithByteProperty.deserialize(make_request_text_response(request), content_type="application/xml")
    assert isinstance(bytes_object, ModelWithByteProperty)
    assert bytes_object.bytes == b"Hello world"

def test_put_bytes(make_request, make_request_text_response):
    request = xml.build_put_binary_request(content=b"Hello world")
    make_request(request)

def test_get_url(make_request_text_response):
    request = xml.build_get_uri_request()
    url_object = ModelWithUrlProperty.deserialize(make_request_text_response(request), content_type="application/xml")
    assert isinstance(url_object, ModelWithUrlProperty)
    assert url_object.url == 'https://myaccount.blob.core.windows.net/'

def test_put_url(make_request, make_request_text_response):
    request = xml.build_put_uri_request(content='https://myaccount.blob.core.windows.net/')
    make_request(request)
