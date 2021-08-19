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

from extensibleenumsswaggerlowlevel.aio import PetStoreInc
from extensibleenumsswaggerlowlevel.rest import pet

import pytest

@pytest.fixture
@async_generator
async def client():
    async with PetStoreInc(endpoint="http://localhost:3000") as client:
        await yield_(client)

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    def _send_request(request):
        return base_send_request_json_response(client, request)
    return _send_request

@pytest.mark.asyncio
async def test_get_by_pet_id(send_request_json_response):
    # Now enum return are always string (Autorest.Python 3.0)

    request = pet.build_get_by_pet_id_request(pet_id="tommy")
    tommy = await send_request_json_response(request)
    assert tommy["DaysOfWeek"] == "Monday"
    assert tommy["IntEnum"] == "1"

    request = pet.build_get_by_pet_id_request(pet_id="casper")
    casper = await send_request_json_response(request)
    assert casper["DaysOfWeek"] ==  "Weekend"
    assert casper["IntEnum"] ==  "2"

    request = pet.build_get_by_pet_id_request(pet_id="scooby")
    scooby = await send_request_json_response(request)
    assert scooby["DaysOfWeek"] ==  "Thursday"
    # https://github.com/Azure/autorest.csharp/blob/e5f871b7433e0f6ca6a17307fba4a2cfea4942b4/test/vanilla/AcceptanceTests.cs#L429
    # "allowedValues" of "x-ms-enum" is not supported in Python
    assert scooby["IntEnum"] ==  "2.1" # Might be "2" if one day Python is supposed to support "allowedValues"

@pytest.mark.asyncio
async def test_add_pet(send_request_json_response):
    retriever = {
        "name": "Retriever",
        "IntEnum": "3",
        "DaysOfWeek": "Friday"
    }
    request = pet.build_add_pet_request(json=retriever)
    returned_pet = await send_request_json_response(request)
    assert returned_pet["DaysOfWeek"] ==  "Friday"
    assert returned_pet["IntEnum"] ==  "3"
    assert returned_pet["name"] ==  "Retriever"
