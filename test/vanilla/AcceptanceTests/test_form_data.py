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
    with AutoRestSwaggerBATFormDataService(base_url="http://localhost:3000") as client:
        client._config.connection.data_block_size = 2
        client._config.retry_policy.retries = 50  # Be agressive on this test, sometimes testserver DDOS :-p
        client._config.retry_policy.backoff_factor = 1.6
        yield client    

class TestFormData(object):

    def test_file_upload_stream(self, client):

        def test_callback(data, response, progress = [0]):
            assert len(data) > 0
            progress[0] += len(data)
            total = float(response.headers.get('Content-Length', 100))
            print("Progress... {}%".format(int(progress[0]*100/total)))
            assert response is not None


        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')
        result = io.BytesIO()
        with io.BytesIO(test_bytes) as stream_data:
            resp = client.formdata.upload_file(stream_data, "UploadFile.txt")
            for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  test_string

    def test_file_upload_file_stream(self, client, dummy_file):

        def test_callback(data, response, progress = [0]):
            assert len(data) > 0
            progress[0] += len(data)
            total = float(response.headers.get('Content-Length', 100))
            print("Progress... {}%".format(int(progress[0]*100/total)))
            assert response is not None

        name = os.path.basename(dummy_file)
        result = io.BytesIO()
        with open(dummy_file, 'rb') as upload_data:
            resp = client.formdata.upload_file(upload_data, name)
            for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  "Test file"

    def test_file_body_upload(self, client, dummy_file):

        test_string = "Upload file test case"
        test_bytes = bytearray(test_string, encoding='utf-8')

        def test_callback(data, response, progress = [0]):
            assert len(data) > 0
            progress[0] += len(data)
            total = float(len(test_bytes))
            if response:
                print("Downloading... {}%".format(int(progress[0]*100/total)))
            else:
                print("Uploading... {}%".format(int(progress[0]*100/total)))

        result = io.BytesIO()
        with io.BytesIO(test_bytes) as stream_data:
            resp = client.formdata.upload_file_via_body(stream_data, callback=test_callback)
            for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  test_string

        result = io.BytesIO()
        with open(dummy_file, 'rb') as upload_data:
            resp = client.formdata.upload_file_via_body(upload_data)
            for r in resp:
                result.write(r)
            assert result.getvalue().decode() ==  "Test file"
