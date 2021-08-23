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
from extensibleenumsswaggerversiontolerant.aio import PetStoreInc

import pytest

@pytest.fixture
@async_generator
async def client():
    async with PetStoreInc() as client:
        await yield_(client)

@pytest.mark.asyncio
async def test_get_by_pet_id(client):
    # Now enum return are always string (Autorest.Python 3.0)

    tommy = await client.pet.get_by_pet_id('tommy')
    assert tommy["DaysOfWeek"] ==  "Monday"
    assert tommy["IntEnum"] ==  "1"

    casper = await client.pet.get_by_pet_id('casper')
    assert casper["DaysOfWeek"] ==  "Weekend"
    assert casper["IntEnum"] ==  "2"

    scooby = await client.pet.get_by_pet_id('scooby')
    assert scooby["DaysOfWeek"] ==  "Thursday"
    # https://github.com/Azure/autorest.csharp/blob/e5f871b7433e0f6ca6a17307fba4a2cfea4942b4/test/vanilla/AcceptanceTests.cs#L429
    # "allowedValues" of "x-ms-enum" is not supported in Python
    assert scooby["IntEnum"] ==  "2.1" # Might be "2" if one day Python is supposed to support "allowedValues"

@pytest.mark.asyncio
async def test_add_pet(client):
    retriever = {
        "name": "Retriever",
        "IntEnum": "3",
        "DaysOfWeek": "Friday"
    }
    returned_pet = await client.pet.add_pet(retriever)
    assert returned_pet["DaysOfWeek"] ==  "Friday"
    assert returned_pet["IntEnum"] ==  "3"
    assert returned_pet['name'] ==  "Retriever"
