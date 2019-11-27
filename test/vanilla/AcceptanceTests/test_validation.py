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
import json
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 10))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "Validation"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError, ValidationError

from validation import AutoRestValidationTest
from validation.models import (
    Product,
    ConstantProduct,
    ChildProduct)

import pytest

@pytest.fixture
def client():
    with AutoRestValidationTest("abc123", base_url="http://localhost:3000") as client:
        client.api_version = "12-34-5678"
        yield client

class TestValidation(object):

    def test_with_constant_in_path(self, client):
        client.get_with_constant_in_path()

        body = Product(child=ChildProduct())
        product = client.post_with_constant_in_body(body=body)
        assert product is not None

    def test_min_length_validation(self, client):
        try:
            client.validation_of_method_parameters("1", 100)
        except ValidationError as err:
            assert err.rule ==  "min_length"
            assert err.target ==  "resource_group_name"

    def test_max_length_validation(self, client):
        try:
            client.validation_of_method_parameters("1234567890A", 100)
        except ValidationError as err:
            assert err.rule ==  "max_length"
            assert err.target ==  "resource_group_name"

    def test_pattern_validation(self, client):
        try:
            client.validation_of_method_parameters("!@#$", 100)
        except ValidationError as err:
            assert err.rule ==  "pattern"
            assert err.target ==  "resource_group_name"

    def test_multiple_validation(self, client):
        try:
            client.validation_of_method_parameters("123", 105)
        except ValidationError as err:
            assert err.rule ==  "multiple"
            assert err.target ==  "id"

    def test_minimum_validation(self, client):
        try:
            client.validation_of_method_parameters("123", 0)
        except ValidationError as err:
            assert err.rule ==  "minimum"
            assert err.target ==  "id"

    def test_maximum_validation(self, client):
        try:
            client.validation_of_method_parameters("123", 2000)
        except ValidationError as err:
            assert err.rule ==  "maximum"
            assert err.target ==  "id"

    def test_minimum_ex_validation(self, client):
        try:
            tempproduct=Product(child=ChildProduct(), capacity=0)
            client.validation_of_body("123", 150, tempproduct)
        except ValidationError as err:
            assert err.rule ==  "minimum_ex"
            assert "capacity" in  err.target

    def test_maximum_ex_validation(self, client):
        try:
            tempproduct=Product(child=ChildProduct(), capacity=100)
            client.validation_of_body("123", 150, tempproduct)
        except ValidationError as err:
            assert err.rule ==  "maximum_ex"
            assert "capacity" in  err.target

    def test_max_items_validation(self, client):
        try:
            tempproduct=Product(child=ChildProduct(),
                display_names=["item1","item2","item3","item4","item5","item6","item7"])
            client.validation_of_body("123", 150, tempproduct)
        except ValidationError as err:
            assert err.rule ==  "max_items"
            assert "display_names" in  err.target

    def test_api_version_validation(self):
        client = AutoRestValidationTest(
            "abc123",
            base_url="http://localhost:3000")
        client.api_version = "abc"

        try:
            client.validation_of_method_parameters("123", 150)
        except ValidationError as err:
            assert err.rule ==  "pattern"
            assert err.target ==  "self.api_version"
