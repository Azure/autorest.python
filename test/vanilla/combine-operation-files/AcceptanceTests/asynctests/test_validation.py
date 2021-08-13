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
import unittest
import subprocess
import sys
import isodate
import tempfile
import json
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

from msrest.exceptions import DeserializationError, ValidationError

from validationcombineoperationfiles.aio import AutoRestValidationTest
from validationcombineoperationfiles.models import (
    Product,
    ConstantProduct,
    ChildProduct)

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestValidationTest(
            "abc123",
            base_url="http://localhost:3000") as client:
        client.api_version = "12-34-5678"
        await yield_(client)

@pytest.fixture
def constant_body():
    """This is NOT considering the constant body, this should work with
    the commented line.
    See https://github.com/Azure/autorest.modelerfour/issues/83
    """
    #return Product(child=ChildProduct())
    return Product(
        child=ChildProduct(),
        const_child=ConstantProduct(),
    )

class TestValidation(object):

    @pytest.mark.asyncio
    async def test_with_constant_in_path(self, client):
        await client.get_with_constant_in_path()

    @pytest.mark.asyncio
    async def test_post_with_constant_in_body(self, client, constant_body):
        product = await client.post_with_constant_in_body(body=constant_body)
        assert product is not None

    @pytest.mark.asyncio
    async def test_min_length_validation(self, client):
        try:
            await client.validation_of_method_parameters("1", 100)
        except ValidationError as err:
            assert err.rule ==  "min_length"
            assert err.target ==  "resource_group_name"

    @pytest.mark.asyncio
    async def test_max_length_validation(self, client):
        try:
            await client.validation_of_method_parameters("1234567890A", 100)
        except ValidationError as err:
            assert err.rule ==  "max_length"
            assert err.target ==  "resource_group_name"

    @pytest.mark.asyncio
    async def test_pattern_validation(self, client):
        try:
            await client.validation_of_method_parameters("!@#$", 100)
        except ValidationError as err:
            assert err.rule ==  "pattern"
            assert err.target ==  "resource_group_name"

    @pytest.mark.asyncio
    async def test_multiple_validation(self, client):
        try:
            await client.validation_of_method_parameters("123", 105)
        except ValidationError as err:
            assert err.rule ==  "multiple"
            assert err.target ==  "id"

    @pytest.mark.asyncio
    async def test_minimum_validation(self, client):
        try:
            await client.validation_of_method_parameters("123", 0)
        except ValidationError as err:
            assert err.rule ==  "minimum"
            assert err.target ==  "id"

    @pytest.mark.asyncio
    async def test_maximum_validation(self, client):
        try:
            await client.validation_of_method_parameters("123", 2000)
        except ValidationError as err:
            assert err.rule ==  "maximum"
            assert err.target ==  "id"

    @pytest.mark.asyncio
    async def test_minimum_ex_validation(self, client, constant_body):
        try:
            constant_body.capacity = 0
            await client.validation_of_body("123", 150, constant_body)
        except ValidationError as err:
            assert err.rule ==  "minimum_ex"
            assert "capacity" in  err.target

    @pytest.mark.asyncio
    async def test_maximum_ex_validation(self, client, constant_body):
        try:
            constant_body.capacity = 100
            await client.validation_of_body("123", 150, constant_body)
        except ValidationError as err:
            assert err.rule ==  "maximum_ex"
            assert "capacity" in  err.target

    @pytest.mark.asyncio
    async def test_max_items_validation(self, client, constant_body):
        try:
            constant_body.display_names = ["item1","item2","item3","item4","item5","item6","item7"]
            await client.validation_of_body("123", 150, constant_body)
        except ValidationError as err:
            assert err.rule ==  "max_items"
            assert "display_names" in  err.target

    @pytest.mark.xfail(reason="https://github.com/Azure/autorest.modelerfour/issues/90")
    @pytest.mark.asyncio
    async def test_api_version_validation(self):
        with AutoRestValidationTest(
            "abc123",
            base_url="http://localhost:3000") as client:
            client.api_version = "abc"
            try:
                await client.validation_of_method_parameters("123", 150)
            except ValidationError as err:
                assert err.rule ==  "pattern"
                assert err.target ==  "self.api_version"
