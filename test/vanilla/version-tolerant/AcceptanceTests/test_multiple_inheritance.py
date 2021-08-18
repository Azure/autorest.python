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
from multipleinheritanceversiontolerant import MultipleInheritanceServiceClient
import pytest

@pytest.fixture
def client():
    with MultipleInheritanceServiceClient(endpoint="http://localhost:3000") as client:
        yield client

def test_get_pet(client):
    assert {"name": "Peanut"} == client.get_pet()

def test_put_pet(client):
    result = client.put_pet({"name": "Butter"})
    assert result == "Pet was correct!"

def test_get_horse(client):
    assert {"name": "Fred", "isAShowHorse": True} == client.get_horse()

def test_put_horse(client):
    result = client.put_horse({"name": "General", "isAShowHorse": False})
    assert result == "Horse was correct!"

def test_get_feline(client):
    assert {"meows": True, "hisses": True} == client.get_feline()

def test_put_feline(client):
    result = client.put_feline({"meows": False, "hisses": True})
    assert result == "Feline was correct!"

def test_get_cat(client):
    assert {"name": "Whiskers", "likesMilk": True, "meows": True, "hisses": True} == client.get_cat()

def test_put_cat(client):
    result = client.put_cat({"name": "Boots", "likesMilk": False, "meows": True, "hisses": False})
    assert result == "Cat was correct!"

def test_get_kitten(client):
    assert {"name": "Gatito", "likesMilk": True, "meows": True, "hisses": True, "eatsMiceYet": False} == client.get_kitten()

def test_put_kitten(client):
    result = client.put_kitten({"name": "Kitty", "likesMilk": False, "meows": True, "hisses": False, "eatsMiceYet": True})
    assert result == "Kitten was correct!"
