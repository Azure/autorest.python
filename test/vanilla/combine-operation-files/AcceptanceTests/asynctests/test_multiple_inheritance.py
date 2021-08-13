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

from async_generator import yield_, async_generator
from multipleinheritancecombineoperationfiles.aio import MultipleInheritanceServiceClient
from multipleinheritancecombineoperationfiles.models import *
import pytest

@pytest.fixture
@async_generator
async def client():
    async with MultipleInheritanceServiceClient(base_url="http://localhost:3000") as client:
        await yield_(client)

class TestMultipleInheritance(object):

    @pytest.mark.asyncio
    async def test_get_pet(self, client):
        assert Pet(name="Peanut") == await client.get_pet()

    @pytest.mark.asyncio
    async def test_put_pet(self, client):
        result = await client.put_pet(name="Butter")
        assert result == "Pet was correct!"

    @pytest.mark.asyncio
    async def test_get_horse(self, client):
        assert Horse(name="Fred", is_a_show_horse=True) == await client.get_horse()

    @pytest.mark.asyncio
    async def test_put_horse(self, client):
        result = await client.put_horse(Horse(name="General", is_a_show_horse=False))
        assert result == "Horse was correct!"

    @pytest.mark.asyncio
    async def test_get_feline(self, client):
        assert Feline(meows=True, hisses=True) == await client.get_feline()

    @pytest.mark.asyncio
    async def test_put_feline(self, client):
        result = await client.put_feline(Feline(meows=False, hisses=True))
        assert result == "Feline was correct!"

    @pytest.mark.asyncio
    async def test_get_cat(self, client):
        assert Cat(name="Whiskers", likes_milk=True, meows=True, hisses=True) == await client.get_cat()

    @pytest.mark.asyncio
    async def test_put_cat(self, client):
        result = await client.put_cat(Cat(name="Boots", likes_milk=False, meows=True, hisses=False))
        assert result == "Cat was correct!"

    @pytest.mark.asyncio
    async def test_get_kitten(self, client):
        assert Kitten(name="Gatito", likes_milk=True, meows=True, hisses=True, eats_mice_yet=False) == await client.get_kitten()

    @pytest.mark.asyncio
    async def test_put_kitten(self, client):
        result = await client.put_kitten(Kitten(name="Kitty", likes_milk=False, meows=True, hisses=False, eats_mice_yet=True))
        assert result == "Kitten was correct!"
