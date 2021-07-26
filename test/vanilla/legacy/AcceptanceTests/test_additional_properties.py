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
import pytest
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

from msrest.exceptions import DeserializationError

from additionalproperties import AdditionalPropertiesClient
from additionalproperties.models import (
    PetAPTrue,
    CatAPTrue,
    PetAPObject,
    PetAPString,
    PetAPInProperties,
    PetAPInPropertiesWithAPString
)

@pytest.fixture
def client():
    with AdditionalPropertiesClient(base_url="http://localhost:3000") as client:
        yield client

class TestAdditionalProperties(object):

    def test_create_ap_true(self, client):
        input_ap_true = PetAPTrue(
            id = 1,
            name = 'Puppy',
            additional_properties = {
                'birthdate': '2017-12-13T02:29:51Z',
                'complexProperty': {
                    'color': 'Red'
                }
            }
        )
        output_ap_true = client.pets.create_ap_true(input_ap_true)
        assert output_ap_true.additional_properties['birthdate'] ==  '2017-12-13T02:29:51Z'

    def test_create_cat_ap_true(self, client):
        input_ap_true = CatAPTrue(
            id = 1,
            name = 'Lisa',
            friendly = True,
            additional_properties = {
                'birthdate': '2017-12-13T02:29:51Z',
                'complexProperty': {
                    'color': 'Red'
                }
            }
        )
        output_ap_true = client.pets.create_cat_ap_true(input_ap_true)
        assert output_ap_true.additional_properties['birthdate'] ==  '2017-12-13T02:29:51Z'

    def test_create_ap_object(self, client):
        input_ap_obj = PetAPObject(
            id = 2,
            name = 'Hira',
            additional_properties = {
                'siblings': [{
                    'id': 1,
                    'name': 'Puppy',
                    'birthdate': '2017-12-13T02:29:51Z',
                    'complexProperty': {
                        'color': 'Red'
                    }
                }],
                'picture': '//////4='
            }
        )
        output_ap_obj = client.pets.create_ap_object(input_ap_obj)
        assert output_ap_obj.additional_properties['siblings'][0]['birthdate'] ==  '2017-12-13T02:29:51Z'

    def test_create_ap_string(self, client):
        input_ap_str = PetAPString(
            id = 3,
            name = 'Tommy',
            additional_properties = {
                'color': 'red',
                'weight': '10 kg',
                'city': 'Bombay'
            }
        )
        output_ap_str = client.pets.create_ap_string(input_ap_str)
        assert output_ap_str.additional_properties['color'] ==  'red'

    def test_create_ap_in_properties(self, client):
        input_ap_int = PetAPInProperties(
            id = 4,
            name = 'Bunny',
            additional_properties = {
                'height': 5.61,
                'weight': 599,
                'footsize': 11.5
            }
        )
        output_ap_int = client.pets.create_ap_in_properties(input_ap_int)
        assert output_ap_int.additional_properties['weight'] ==  599

    def test_create_ap_in_properties_with_ap_string(self, client):
        input_ap_str_add = PetAPInPropertiesWithAPString(
            id = 5,
            name = 'Funny',
            odata_location = 'westus',
            additional_properties = {
                'color': 'red',
                'city': 'Seattle',
                'food': 'tikka masala'
            },
            additional_properties1 = {
                'height': 5.61,
                'weight': 599,
                'footsize': 11.5
            }
        )
        output_ap_str_add = client.pets.create_ap_in_properties_with_ap_string(input_ap_str_add)
        assert output_ap_str_add.additional_properties['color'] ==  'red'
        assert output_ap_str_add.additional_properties1['weight'] ==  599

    def test_models(self):
        from additionalproperties.models import Error

        if sys.version_info >= (3,5):
            from additionalproperties.models._models_py3 import Error as ErrorPy3
            assert Error == ErrorPy3
        else:
            from additionalproperties.models._models import Error as ErrorPy2
            assert Error == ErrorPy2

    def test_operation_groups(self):
        from additionalproperties.operations import PetsOperations

        if sys.version_info >= (3, 5):
            from additionalproperties.operations._pets_operations_py3 import PetsOperations as PetsOperationsPy3
            assert PetsOperations == PetsOperationsPy3
        else:
            from additionalproperties.operations._pets_operations import PetsOperations as PetsOperationsPy2
            assert PetsOperations == PetsOperationsPy2
