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
import unittest
import subprocess
import sys
import isodate
import tempfile
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "Xml"))

from xmlservice import AutoRestSwaggerBATXMLService
from xmlservice.models import BlobType

import pytest

_LOGGER = logging.getLogger(__name__)

@pytest.fixture
def client():
    with AutoRestSwaggerBATXMLService(base_url="http://localhost:3000") as client:
        yield client

def _assert_with_log(func, *args, **kwargs):
    def raise_for_status(response, deserialized, headers):
        response.internal_response.raise_for_status()
    try:
        http_response = func(*args, cls=raise_for_status, **kwargs)
    except Exception as err:
        print(err.response.text)
        pytest.fail()

class TestXml(object):

    def test_json_xml(self, client):
        client.xml.json_input(id=42)

        result = client.xml.json_output()
        assert result.id == 42

    def test_simple(self, client):
        # Slideshow

        slideshow = client.xml.get_simple()
        assert slideshow.title == "Sample Slide Show"
        assert slideshow.date_property == "Date of publication"
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

        _assert_with_log(client.xml.put_simple, slideshow)

    def test_empty_child_element(self, client):
        banana = client.xml.get_empty_child_element()
        assert banana.flavor == '' # That's the point of this test, it was an empty node.
        _assert_with_log(client.xml.put_empty_child_element, banana)

    def test_empty_root_list(self, client):
        bananas = client.xml.get_empty_root_list()
        assert bananas == []
        _assert_with_log(client.xml.put_empty_root_list, bananas)

    def test_root_list_single_item(self, client):
        bananas = client.xml.get_root_list_single_item()
        assert len(bananas) == 1
        assert bananas[0].name == "Cavendish"
        _assert_with_log(client.xml.put_root_list_single_item, bananas)

    def test_root_list(self, client):
        bananas = client.xml.get_root_list()
        assert len(bananas) == 2
        _assert_with_log(client.xml.put_root_list, bananas)

    def test_empty_wrapped_lists(self, client):
        bananas = client.xml.get_empty_wrapped_lists()
        assert bananas.good_apples == []
        assert bananas.bad_apples == []
        _assert_with_log(client.xml.put_empty_wrapped_lists, bananas)

    def test_get_empty(self, client):
        slideshow = client.xml.get_empty_list()
        _assert_with_log(client.xml.put_empty_list, slideshow)

    def test_wrapped_lists(self, client):
        bananas = client.xml.get_wrapped_lists()
        assert bananas.good_apples == ['Fuji', 'Gala']
        assert bananas.bad_apples == ['Red Delicious']
        _assert_with_log(client.xml.put_wrapped_lists, bananas)

    def test_complex_types(self, client):
        root = client.xml.get_complex_type_ref_no_meta()
        assert root.ref_to_model.id == "myid"
        client.xml.put_complex_type_ref_no_meta(root)

        root = client.xml.get_complex_type_ref_with_meta()
        assert root.ref_to_model.id == "myid"
        client.xml.put_complex_type_ref_with_meta(root)

    def test_list_containers(self, client):
        containers = client.xml.list_containers()
        assert len(containers.containers) == 3

    def test_list_blobs(self, client):
        blobs = client.xml.list_blobs()
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

    def test_service_properties(self, client):
        properties = client.xml.get_service_properties()
        assert properties.hour_metrics is not None
        assert properties.minute_metrics is not None
        _assert_with_log(client.xml.put_service_properties, properties)

    def test_acls(self, client):
        acls = client.xml.get_acls()
        assert len(acls) == 1
        assert acls[0].id == 'MTIzNDU2Nzg5MDEyMzQ1Njc4OTAxMjM0NTY3ODkwMTI='
        _assert_with_log(client.xml.put_acls, acls)
