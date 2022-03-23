# coding=utf-8
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
import pytest
from bodyformurlencodeddata.aio import BodyFormsDataURLEncoded
from bodyformurlencodeddata.models import PetFood, PetType

@pytest.fixture
async def client():
    async with BodyFormsDataURLEncoded() as client:
        yield client

@pytest.mark.asyncio
async def test_update_pet_with_form(client):
    await client.formdataurlencoded.update_pet_with_form(
        pet_id=1,
        pet_type=PetType.DOG,
        pet_food=PetFood.MEAT,
        pet_age=42,
        name="Fido",
    )

@pytest.mark.asyncio
async def test_partial_constant_body(client):
    await client.formdataurlencoded.partial_constant_body(access_token="foo", service="bar", grant_type="access_token")
