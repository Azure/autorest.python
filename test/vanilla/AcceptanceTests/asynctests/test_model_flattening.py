﻿# --------------------------------------------------------------------------
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

from msrest.exceptions import DeserializationError

from modelflattening.aio import AutoRestResourceFlatteningTestService
from modelflattening.models import (
    FlattenedProduct,
    ResourceCollection,
    SimpleProduct)

import pytest

@pytest.fixture
@async_generator
async def client():
    async with AutoRestResourceFlatteningTestService(base_url="http://localhost:3000") as client:
        await yield_(client)

class TestModelFlatteningTests(object):

    @pytest.mark.asyncio
    async def test_flattening_array(self, client):

        #Array
        result = await client.get_array()
        assert 3 ==  len(result)
        # Resource 1
        assert "1" ==  result[0].id
        assert "OK" ==  result[0].provisioning_state_values
        assert "Product1" ==  result[0].p_name
        assert "Flat" ==  result[0].type_properties_type
        assert "Building 44" ==  result[0].location
        assert "Resource1" ==  result[0].name
        assert "Succeeded" ==  result[0].provisioning_state
        assert "Microsoft.Web/sites" ==  result[0].type
        assert "value1" ==  result[0].tags["tag1"]
        assert "value3" ==  result[0].tags["tag2"]
        # Resource 2
        assert "2" ==  result[1].id
        assert "Resource2" ==  result[1].name
        assert "Building 44" ==  result[1].location
        # Resource 3
        assert "3" ==  result[2].id
        assert "Resource3" ==  result[2].name

        resourceArray = [
                {
                    'location': "West US",
                    'tags': {"tag1":"value1", "tag2":"value3"}},
                {
                    'location': "Building 44"}]

        await client.put_array(resourceArray)

    @pytest.mark.asyncio
    async def test_flattening_dictionary(self, client):

        #Dictionary
        resultDictionary = await client.get_dictionary()
        assert 3 ==  len(resultDictionary)
        # Resource 1
        assert "1" ==  resultDictionary["Product1"].id
        assert "OK" ==  resultDictionary["Product1"].provisioning_state_values
        assert "Product1" ==  resultDictionary["Product1"].p_name
        assert "Flat" ==  resultDictionary["Product1"].type_properties_type
        assert "Building 44" ==  resultDictionary["Product1"].location
        assert "Resource1" ==  resultDictionary["Product1"].name
        assert "Succeeded" ==  resultDictionary["Product1"].provisioning_state
        assert "Microsoft.Web/sites" ==  resultDictionary["Product1"].type
        assert "value1" ==  resultDictionary["Product1"].tags["tag1"]
        assert "value3" ==  resultDictionary["Product1"].tags["tag2"]
        # Resource 2
        assert "2" ==  resultDictionary["Product2"].id
        assert "Resource2" ==  resultDictionary["Product2"].name
        assert "Building 44" ==  resultDictionary["Product2"].location
        # Resource 3
        assert "3" ==  resultDictionary["Product3"].id
        assert "Resource3" ==  resultDictionary["Product3"].name

        resourceDictionary = {
                "Resource1": {
                    'location': "West US",
                    'tags': {"tag1":"value1", "tag2":"value3"},
                    'p_name': "Product1",
                    'type_properties_type': "Flat"},
                "Resource2": {
                    'location': "Building 44",
                    'p_name': "Product2",
                    'type_properties_type': "Flat"}}

        await client.put_dictionary(resourceDictionary)

    @pytest.mark.asyncio
    async def test_flattening_complex_object(self, client):

        #ResourceCollection
        resultResource = await client.get_resource_collection()

        #dictionaryofresources
        assert 3 ==  len(resultResource.dictionaryofresources)
        # Resource 1
        assert "1" ==  resultResource.dictionaryofresources["Product1"].id
        assert "OK" ==  resultResource.dictionaryofresources["Product1"].provisioning_state_values
        assert "Product1" ==  resultResource.dictionaryofresources["Product1"].p_name
        assert "Flat" ==  resultResource.dictionaryofresources["Product1"].type_properties_type
        assert "Building 44" ==  resultResource.dictionaryofresources["Product1"].location
        assert "Resource1" ==  resultResource.dictionaryofresources["Product1"].name
        assert "Succeeded" ==  resultResource.dictionaryofresources["Product1"].provisioning_state
        assert "Microsoft.Web/sites" ==  resultResource.dictionaryofresources["Product1"].type
        assert "value1" ==  resultResource.dictionaryofresources["Product1"].tags["tag1"]
        assert "value3" ==  resultResource.dictionaryofresources["Product1"].tags["tag2"]
        # Resource 2
        assert "2" ==  resultResource.dictionaryofresources["Product2"].id
        assert "Resource2" ==  resultResource.dictionaryofresources["Product2"].name
        assert "Building 44" ==  resultResource.dictionaryofresources["Product2"].location
        # Resource 3
        assert "3" ==  resultResource.dictionaryofresources["Product3"].id
        assert "Resource3" ==  resultResource.dictionaryofresources["Product3"].name

        #arrayofresources
        assert 3 ==  len(resultResource.arrayofresources)
        # Resource 1
        assert "4" ==  resultResource.arrayofresources[0].id
        assert "OK" ==  resultResource.arrayofresources[0].provisioning_state_values
        assert "Product4" ==  resultResource.arrayofresources[0].p_name
        assert "Flat" ==  resultResource.arrayofresources[0].type_properties_type
        assert "Building 44" ==  resultResource.arrayofresources[0].location
        assert "Resource4" ==  resultResource.arrayofresources[0].name
        assert "Succeeded" ==  resultResource.arrayofresources[0].provisioning_state
        assert "Microsoft.Web/sites" ==  resultResource.arrayofresources[0].type
        assert "value1" ==  resultResource.arrayofresources[0].tags["tag1"]
        assert "value3" ==  resultResource.arrayofresources[0].tags["tag2"]
        # Resource 2
        assert "5" ==  resultResource.arrayofresources[1].id
        assert "Resource5" ==  resultResource.arrayofresources[1].name
        assert "Building 44" ==  resultResource.arrayofresources[1].location
        # Resource 3
        assert "6" ==  resultResource.arrayofresources[2].id
        assert "Resource6" ==  resultResource.arrayofresources[2].name

        #productresource
        assert "7" ==  resultResource.productresource.id
        assert "Resource7" ==  resultResource.productresource.name

        resourceDictionary = {
                "Resource1": FlattenedProduct(
                    location = "West US",
                    tags = {"tag1":"value1", "tag2":"value3"},
                    p_name = "Product1",
                    type_properties_type = "Flat"),
                "Resource2": FlattenedProduct(
                    location = "Building 44",
                    p_name = "Product2",
                    type_properties_type = "Flat")}

        resourceComplexObject = ResourceCollection(
                dictionaryofresources = resourceDictionary,
                arrayofresources = [
                    FlattenedProduct(
                        location = "West US",
                        tags = {"tag1":"value1", "tag2":"value3"},
                        p_name = "Product1",
                        type_properties_type = "Flat"),
                    FlattenedProduct(
                        location = "East US",
                        p_name = "Product2",
                        type_properties_type = "Flat")],
                productresource = FlattenedProduct(
                    location = "India",
                    p_name = "Azure",
                    type_properties_type = "Flat"))

        await client.put_resource_collection(resourceComplexObject)

    @pytest.mark.asyncio
    async def test_model_flattening_simple(self, client):

        simple_product = SimpleProduct(
            product_id = "123",
            description = "product description",
            max_product_display_name = "max name",
            odata_value = "http://foo",
            generic_value = "https://generic"
        )
        simple_product.additional_properties = {} # Not the purpose of this test. This enables the ==.

        result = await client.put_simple_product(simple_product)
        result.additional_properties = {} # Not the purpose of this test. This enables the ==.
        assert result ==  simple_product

    @pytest.mark.asyncio
    async def test_model_flattening_with_parameter_flattening(self, client):

        simple_product = SimpleProduct(
            product_id = "123",
            description = "product description",
            max_product_display_name = "max name",
            odata_value = "http://foo"
        )
        simple_product.additional_properties = {} # Not the purpose of this test. This enables the ==.

        result = await client.post_flattened_simple_product(
            "123", # product_id
            "product description", # description
            "max name", # max_product_display_name
            None, # generic_value
            "http://foo", # odata_value
        )
        result.additional_properties = {} # Not the purpose of this test. This enables the ==.
        assert result ==  simple_product

    @pytest.mark.asyncio
    async def test_model_flattening_with_grouping(self, client):
        from modelflattening.models import FlattenParameterGroup

        simple_product = SimpleProduct(
            product_id = "123",
            description = "product description",
            max_product_display_name = "max name",
            odata_value = "http://foo"
        )
        simple_product.additional_properties = {} # Not the purpose of this test. This enables the ==.

        group = FlattenParameterGroup(
            product_id = "123",
            description = "product description",
            max_product_display_name="max name",
            odata_value="http://foo",
            name="groupproduct")

        result = await client.put_simple_product_with_grouping(group)
        result.additional_properties = {} # Not the purpose of this test. This enables the ==.
        assert result ==  simple_product
