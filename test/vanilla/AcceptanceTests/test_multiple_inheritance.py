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


from multipleinheritance import MultipleInheritanceServiceClient
from multipleinheritance.models import *
import pytest
import sys

@pytest.fixture
def client():
    with MultipleInheritanceServiceClient(base_url="http://localhost:3000") as client:
        yield client

class TestMultipleInheritance(object):

    def test_get_pet(self, client):
        assert Pet(name="Peanut") == client.get_pet()

    def test_put_pet(self, client):
        result = client.put_pet(name="Butter")
        assert result == "Pet was correct!"

    def test_get_horse(self, client):
        assert Horse(name="Fred", is_a_show_horse=True) == client.get_horse()

    def test_put_horse(self, client):
        result = client.put_horse(Horse(name="General", is_a_show_horse=False))
        assert result == "Horse was correct!"

    def test_get_feline(self, client):
        assert Feline(meows=True, hisses=True) == client.get_feline()

    def test_put_feline(self, client):
        result = client.put_feline(Feline(meows=False, hisses=True))
        assert result == "Feline was correct!"

    def test_get_cat(self, client):
        assert Cat(name="Whiskers", likes_milk=True, meows=True, hisses=True) == client.get_cat()

    def test_put_cat(self, client):
        result = client.put_cat(Cat(name="Boots", likes_milk=False, meows=True, hisses=False))
        assert result == "Cat was correct!"

    def test_get_kitten(self, client):
        assert Kitten(name="Gatito", likes_milk=True, meows=True, hisses=True, eats_mice_yet=False) == client.get_kitten()

    def test_put_kitten(self, client):
        result = client.put_kitten(Kitten(name="Kitty", likes_milk=False, meows=True, hisses=False, eats_mice_yet=True))
        assert result == "Kitten was correct!"

    def test_models(self):
        from multipleinheritance.models import Error

        if sys.version_info >= (3,5):
            from multipleinheritance.models._models_py3 import Error as ErrorPy3
            assert Error == ErrorPy3
        else:
            from multipleinheritance.models._models import Error as ErrorPy2
            assert Error == ErrorPy2
