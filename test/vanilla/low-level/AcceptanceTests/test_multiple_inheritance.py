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


from multipleinheritancelowlevel import MultipleInheritanceServiceClient
from multipleinheritancelowlevel.rest import *
import pytest

@pytest.fixture
def client():
    with MultipleInheritanceServiceClient() as client:
        yield client

@pytest.fixture
def send_request_json_response(client, base_send_request_json_response):
    def _send_request(request):
        return base_send_request_json_response(client, request)
    return _send_request

def test_get_pet(send_request_json_response):
    request = build_get_pet_request()
    assert {"name": "Peanut"} == send_request_json_response(request)

def test_put_pet(send_request_json_response):
    request = build_put_pet_request(json={"name": "Butter"})
    result = send_request_json_response(request)
    assert result == "Pet was correct!"

def test_get_horse(send_request_json_response):
    request = build_get_horse_request()
    assert {"name": "Fred", "isAShowHorse": True} == send_request_json_response(request)

def test_put_horse(send_request_json_response):
    request = build_put_horse_request(json={"name": "General", "isAShowHorse": False})
    result = send_request_json_response(request)
    assert result == "Horse was correct!"

def test_get_feline(send_request_json_response):
    request = build_get_feline_request()
    assert {"meows": True, "hisses": True} == send_request_json_response(request)

def test_put_feline(send_request_json_response):
    request = build_put_feline_request(json={"meows": False, "hisses": True})
    result = send_request_json_response(request)
    assert result == "Feline was correct!"

def test_get_cat(send_request_json_response):
    request = build_get_cat_request()
    assert {"name": "Whiskers", "likesMilk": True, "meows": True, "hisses": True} == send_request_json_response(request)

def test_put_cat(send_request_json_response):
    request = build_put_cat_request(json={"name": "Boots", "likesMilk": False, "meows": True, "hisses": False})
    assert send_request_json_response(request) == "Cat was correct!"

def test_get_kitten(send_request_json_response):
    request = build_get_kitten_request()
    assert {"name": "Gatito", "likesMilk": True, "meows": True, "hisses": True, "eatsMiceYet": False} == send_request_json_response(request)

def test_put_kitten(send_request_json_response):
    request = build_put_kitten_request(json={"name": "Kitty", "likesMilk": False, "meows": True, "hisses": False, "eatsMiceYet": True})
    assert "Kitten was correct!" == send_request_json_response(request)
