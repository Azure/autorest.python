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


from multipleinheritance.aio import MultipleInheritanceServiceClient
from multipleinheritance.models import *
from multipleinheritance.rest import *
from async_generator import yield_, async_generator
import pytest

@pytest.fixture
@async_generator
async def client():
    async with MultipleInheritanceServiceClient(base_url="http://localhost:3000") as client:
        await yield_(client)

@pytest.fixture
def make_request_json_response(client, base_make_request_json_response):
    async def _make_request(request):
        return await base_make_request_json_response(client, request)
    return _make_request

@pytest.mark.asyncio
async def test_get_pet(make_request_json_response):
    request = build_get_pet_request()
    assert Pet(name="Peanut") == Pet.deserialize(await make_request_json_response(request))

@pytest.mark.asyncio
async def test_put_pet(make_request_json_response):
    request = build_put_pet_request(json=Pet(name="Butter").serialize())
    result = await make_request_json_response(request)
    assert result == "Pet was correct!"

@pytest.mark.asyncio
async def test_get_horse(make_request_json_response):
    request = build_get_horse_request()
    assert Horse(name="Fred", is_a_show_horse=True) == Horse.deserialize(await make_request_json_response(request))

@pytest.mark.asyncio
async def test_put_horse(make_request_json_response):
    request = build_put_horse_request(json=Horse(name="General", is_a_show_horse=False).serialize())
    result = await make_request_json_response(request)
    assert result == "Horse was correct!"

@pytest.mark.asyncio
async def test_get_feline(make_request_json_response):
    request = build_get_feline_request()
    assert Feline(meows=True, hisses=True) == Feline.deserialize(await make_request_json_response(request))

@pytest.mark.asyncio
async def test_put_feline(make_request_json_response):
    request = build_put_feline_request(json=Feline(meows=False, hisses=True).serialize())
    result = await make_request_json_response(request)
    assert result == "Feline was correct!"

@pytest.mark.asyncio
async def test_get_cat(make_request_json_response):
    request = build_get_cat_request()
    assert Cat(name="Whiskers", likes_milk=True, meows=True, hisses=True) == Cat.deserialize(await make_request_json_response(request))

@pytest.mark.asyncio
async def test_put_cat(make_request_json_response):
    request = build_put_cat_request(json=Cat(name="Boots", likes_milk=False, meows=True, hisses=False).serialize())
    assert await make_request_json_response(request) == "Cat was correct!"

@pytest.mark.asyncio
async def test_get_kitten(make_request_json_response):
    request = build_get_kitten_request()
    assert Kitten(name="Gatito", likes_milk=True, meows=True, hisses=True, eats_mice_yet=False) == Kitten.deserialize(await make_request_json_response(request))

@pytest.mark.asyncio
async def test_put_kitten(make_request_json_response):
    request = build_put_kitten_request(json=Kitten(name="Kitty", likes_milk=False, meows=True, hisses=False, eats_mice_yet=True).serialize())
    assert "Kitten was correct!" == await make_request_json_response(request)
