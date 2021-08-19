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
import io

from msrest.exceptions import ValidationError
from azure.core.exceptions import HttpResponseError

from requiredoptionalversiontolerant import AutoRestRequiredOptionalTestService

import pytest

@pytest.fixture
def client_required():
    with AutoRestRequiredOptionalTestService(
            "required_path",
            "required_query",
            endpoint="http://localhost:3000") as client:
        client._config.required_global_path = "required_path"
        client._config.required_global_query = "required_query"
        yield client

@pytest.fixture
def client():
    with AutoRestRequiredOptionalTestService(
            "required_path",
            "required_query",
            endpoint="http://localhost:3000") as client:
        client._config.required_global_path = None
        client._config.required_global_query = None
        yield client

# These clients have a required global path and query
def test_put_optional(client_required):
    client_required.implicit.put_optional_query(query_parameter=None)
    client_required.implicit.put_optional_body(None)
    client_required.implicit.put_optional_header(query_parameter=None)

def test_get_optional_global_query(client_required):
    client_required.implicit.get_optional_global_query(cls=None)

def test_post_optional_integer(client_required):
    client_required.explicit.post_optional_integer_parameter(None)
    client_required.explicit.post_optional_integer_property({"value": None})
    client_required.explicit.post_optional_integer_header(header_parameter=None)

def test_post_optional_string(client_required):
    client_required.explicit.post_optional_string_parameter(None)
    client_required.explicit.post_optional_string_property({"value": None})
    client_required.explicit.post_optional_string_header(body_parameter=None)  # header param that's called bodyParameter. confusing, but c'est la vie

def test_post_optional_class(client_required):
    client_required.explicit.post_optional_class_parameter(None)
    client_required.explicit.post_optional_class_property({"value": None})

def test_post_optional_array(client_required):
    client_required.explicit.post_optional_array_parameter(None)
    client_required.explicit.post_optional_array_property({"value": None})
    client_required.explicit.post_optional_array_header(header_parameter=None)

def test_implicit_get_required(client):
    with pytest.raises(ValidationError):
        client.implicit.get_required_path(None)

    with pytest.raises(ValidationError):
        client.implicit.get_required_global_path()

    with pytest.raises(ValidationError):
        client.implicit.get_required_global_query()

def test_post_required_string(client):
    with pytest.raises(ValidationError):
        client.explicit.post_required_string_header(header_parameter=None)

    with pytest.raises(HttpResponseError) as ex:
        client.explicit.post_required_string_parameter(None)
    assert "Not Found" in str(ex.value)

    with pytest.raises(HttpResponseError) as ex:
        client.explicit.post_required_string_property(None)
    assert "Not Found" in str(ex.value)

def test_post_required_array(client):
    with pytest.raises(ValidationError):
        client.explicit.post_required_array_header(header_parameter=None)

    with pytest.raises(HttpResponseError) as ex:
        client.explicit.post_required_array_parameter(None)
    assert "Not Found" in str(ex.value)

    with pytest.raises(HttpResponseError) as ex:
        client.explicit.post_required_array_property({"value": None})
    assert "Not Found" in str(ex.value)

def test_post_required_class(client):
    with pytest.raises(HttpResponseError) as ex:
        client.explicit.post_required_class_parameter(None)

    assert "Not Found" in str(ex.value)

    with pytest.raises(HttpResponseError) as ex:
        client.explicit.post_required_class_property(None)

    assert "Not Found" in str(ex.value)

def test_explict_put_optional_binary_body(client):
    client.explicit.put_optional_binary_body()

def test_explict_put_required_binary_body(client):
    test_string = "Upload file test case"
    test_bytes = bytearray(test_string, encoding='utf-8')
    with io.BytesIO(test_bytes) as stream_data:
        client.explicit.put_required_binary_body(stream_data)

def test_implicit_put_optional_binary_body(client):
    client.implicit.put_optional_binary_body()
