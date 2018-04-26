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
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "Xml"))

from xmlservice import AutoRestSwaggerBATXMLService

import pytest

@pytest.fixture
def client():
    with AutoRestSwaggerBATXMLService(base_url="http://localhost:3000") as client:
        yield client

class TestXml(object):

    def test_xmlservice(self, client):

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
        assert slide2.items[1] == None  # Empty node in XML is explicit None here
        assert slide2.items[2] == "Who buys WonderWidgets"

        try:
            http_response = client.xml.put_simple(slideshow, raw=True)
        except Exception as err:
            print(err.response.text)
            pytest.fail()
        assert http_response.response.status_code == 201