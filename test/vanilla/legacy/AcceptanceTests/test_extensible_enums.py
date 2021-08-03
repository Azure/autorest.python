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
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath
import unittest
import sys

from extensibleenumsswagger import PetStoreInc
from extensibleenumsswagger.models import (
    Pet,
    DaysOfWeekExtensibleEnum,
    IntEnum,
)

import pytest

@pytest.fixture
def client():
    with PetStoreInc(base_url="http://localhost:3000") as client:
        yield client

class TestExtensibleEnums(object):

    def test_get_by_pet_id(self, client):
        # Now enum return are always string (Autorest.Python 3.0)

        tommy = client.pet.get_by_pet_id('tommy')
        assert tommy.days_of_week ==  "Monday"
        assert tommy.int_enum ==  "1"

        casper = client.pet.get_by_pet_id('casper')
        assert casper.days_of_week ==  "Weekend"
        assert casper.int_enum ==  "2"

        scooby = client.pet.get_by_pet_id('scooby')
        assert scooby.days_of_week ==  "Thursday"
        # https://github.com/Azure/autorest.csharp/blob/e5f871b7433e0f6ca6a17307fba4a2cfea4942b4/test/vanilla/AcceptanceTests.cs#L429
        # "allowedValues" of "x-ms-enum" is not supported in Python
        assert scooby.int_enum ==  "2.1" # Might be "2" if one day Python is supposed to support "allowedValues"

    def test_add_pet(self, client):
        retriever = Pet(
            name="Retriever",
            int_enum=IntEnum.three,
            days_of_week=DaysOfWeekExtensibleEnum.friday
        )
        returned_pet = client.pet.add_pet(retriever)
        assert returned_pet.days_of_week ==  "Friday"
        assert returned_pet.int_enum ==  "3"
        assert returned_pet.name ==  "Retriever"

    def test_models(self):
        from extensibleenumsswagger.models import Pet

        if sys.version_info >= (3,5):
            from extensibleenumsswagger.models._models_py3 import Pet as PetPy3
            assert Pet == PetPy3
        else:
            from extensibleenumsswagger.models._models import Pet as PetPy2
            assert Pet == PetPy2

    def test_operation_groups(self):
        from extensibleenumsswagger.operations import PetOperations

        with pytest.raises(ImportError):
            from extensibleenumsswagger.operations import _pet_operations_py3

        from extensibleenumsswagger.operations._pet_operations import PetOperations as PetOperationsPy2
        assert PetOperations == PetOperationsPy2
