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
from msrest.exceptions import ValidationError

from validationversiontolerant import AutoRestValidationTest

import pytest

@pytest.fixture
def client():
    with AutoRestValidationTest("abc123") as client:
        client.api_version = "12-34-5678"
        yield client

@pytest.fixture
def constant_body():
    """This is NOT considering the constant body, this should work with
    the commented line.
    See https://github.com/Azure/autorest.modelerfour/issues/83
    """
    return {
        'child': {
            'constProperty': 'constant'
        },
        'constChild': {
            'constProperty': 'constant',
            'constProperty2': 'constant2'
        },
        'constInt': 0,
        'constString': 'constant',
        'constStringAsEnum': 'constant_string_as_enum'
    }


def test_with_constant_in_path(client):
    client.get_with_constant_in_path()

def test_post_with_constant_in_body(client, constant_body):
    product = client.post_with_constant_in_body(body=constant_body)
    assert product is not None

def test_min_length_validation(client):
    with pytest.raises(ValidationError) as ex:
        client.validation_of_method_parameters("1", 100)
    assert ex.value.rule ==  "min_length"
    assert ex.value.target ==  "resource_group_name"

def test_max_length_validation(client):
    with pytest.raises(ValidationError) as ex:
        client.validation_of_method_parameters("1234567890A", 100)
    assert ex.value.rule ==  "max_length"
    assert ex.value.target ==  "resource_group_name"

def test_pattern_validation(client):
    with pytest.raises(ValidationError) as ex:
        client.validation_of_method_parameters("!@#$", 100)
    assert ex.value.rule ==  "pattern"
    assert ex.value.target ==  "resource_group_name"

def test_multiple_validation(client):
    with pytest.raises(ValidationError) as ex:
        client.validation_of_method_parameters("123", 105)
    assert ex.value.rule ==  "multiple"
    assert ex.value.target ==  "id"

def test_minimum_validation(client):
    with pytest.raises(ValidationError) as ex:
        client.validation_of_method_parameters("123", 0)
    assert ex.value.rule ==  "minimum"
    assert ex.value.target ==  "id"

def test_maximum_validation(client):
    with pytest.raises(ValidationError) as ex:
        client.validation_of_method_parameters("123", 2000)
    assert ex.value.rule ==  "maximum"
    assert ex.value.target ==  "id"

@pytest.mark.skip(reason="Not generating models yet, can't validate")
def test_minimum_ex_validation(client, constant_body):
    with pytest.raises(ValidationError) as ex:
        constant_body['capacity'] = 0
        client.validation_of_body("123", 150, constant_body)
    assert ex.value.rule ==  "minimum_ex"
    assert "capacity" in  ex.value.target

@pytest.mark.skip(reason="Not generating models yet, can't validate")
def test_maximum_ex_validation(client, constant_body):
    with pytest.raises(ValidationError) as ex:
        constant_body['capacity'] = 100
        client.validation_of_body("123", 150, constant_body)
    assert ex.value.rule ==  "maximum_ex"
    assert "capacity" in  ex.value.target

@pytest.mark.skip(reason="Not generating models yet, can't validate")
def test_max_items_validation(client, constant_body):
    with pytest.raises(ValidationError) as ex:
        constant_body.display_names = ["item1","item2","item3","item4","item5","item6","item7"]
        client.validation_of_body("123", 150, constant_body)
    assert ex.value.rule ==  "max_items"
    assert "display_names" in  ex.value.target

@pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/90")
def test_api_version_validation(client):
    client = AutoRestValidationTest(
        "abc123",
    )
    client.api_version = "abc"
    with pytest.raises(ValidationError) as ex:
        client.validation_of_method_parameters("123", 150)
    assert ex.value.rule ==  "pattern"
    assert ex.value.target ==  "self.api_version"
