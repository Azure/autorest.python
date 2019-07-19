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

import subprocess
import sys
import io
import isodate
import os
import tempfile
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "BodyFormData"))

from msrest.exceptions import DeserializationError

from bodyformdata import AutoRestSwaggerBATFormDataService

import pytest

@pytest.fixture
def dummy_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as dummy:
        dummy.write("Test file")
    # Get outside of the "with", so file can be re-opened on Windows
    yield dummy.name
    os.remove(dummy.name)

@pytest.fixture
def client():
    with AutoRestSwaggerBATFormDataService(
        base_url="http://localhost:3000",
        connection_data_block_size = 2,
        retry_total = 50,  # Be agressive on this test, sometimes testserver DDOS :-p
        retry_backoff_factor = 1.6
    ) as client:

        yield client

class TestFormData(object):

    def test_file_upload_stream(self, client):

        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')
        result = io.BytesIO()
        with io.BytesIO(test_bytes) as stream_data:
            resp = client.formdata.upload_file(stream_data, "UploadFile.txt")
            for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  test_string

    def test_file_upload_stream_raw(self, client):

        def test_callback(response, data, headers):
            return data

        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')
        result = io.BytesIO()
        with io.BytesIO(test_bytes) as stream_data:
            stream = client.formdata.upload_file(stream_data, "UploadFile.txt", cls=test_callback)
            for data in stream:
                result.write(data)
            assert result.getvalue().decode() ==  test_string

    def test_file_upload_file_stream(self, client, dummy_file):

        name = os.path.basename(dummy_file)
        result = io.BytesIO()
        with open(dummy_file, 'rb') as upload_data:
            resp = client.formdata.upload_file(upload_data, name)
            for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  "Test file"

    def test_file_upload_file_stream_raw(self, client, dummy_file):

        def test_callback(response, data, headers):
            return data

        name = os.path.basename(dummy_file)
        result = io.BytesIO()
        with open(dummy_file, 'rb') as upload_data:
            stream = client.formdata.upload_file(upload_data, name, cls=test_callback)
            for data in stream:
                result.write(data)
            assert result.getvalue().decode() ==  "Test file"

    def test_file_body_upload(self, client, dummy_file):

        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')

        result = io.BytesIO()
        with io.BytesIO(test_bytes) as stream_data:
            resp = client.formdata.upload_file_via_body(stream_data)
            for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  test_string

        result = io.BytesIO()
        with open(dummy_file, 'rb') as upload_data:
            resp = client.formdata.upload_file_via_body(upload_data)
            for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  "Test file"

    def test_file_body_upload_generator(self, client, dummy_file):

        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')

        def stream_upload(data, length, block_size):
            progress = 0
            while True:
                block = data.read(block_size)
                progress += len(block)
                print("Progress... {}%".format(int(progress*100/length)))
                if not block:
                    break
                yield block

        result = io.BytesIO()
        with io.BytesIO(test_bytes) as stream_data:
            streamed_upload = stream_upload(stream_data, len(test_string), 2)
            resp = client.formdata.upload_file_via_body(streamed_upload)
            for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  test_string

        result = io.BytesIO()
        with open(dummy_file, 'rb') as upload_data:
            streamed_upload = stream_upload(upload_data, len("Test file"), 2)
            response = client.formdata.upload_file_via_body(streamed_upload)
            for data in response:
                result.write(data)
            assert result.getvalue().decode() == "Test file"
