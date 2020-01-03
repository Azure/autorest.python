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
import json
import pytest


from xmserrorresponse import XMSErrorResponseExtensions
from xmserrorresponse.models import NotFoundErrorBaseException, AnimalNotFoundException, LinkNotFoundException, PetActionErrorException, PetSadErrorException, PetHungryOrThirstyErrorException

@pytest.fixture
def client():
    with XMSErrorResponseExtensions(base_url="http://localhost:3000") as client:
        yield client


class TestXmsErrorResponse(object):

    def test_get_by_pet_id_success(self, client):

        pet = client.pet.get_pet_by_id("tommy")
        assert pet.name == "Tommy Tomson"

        client.pet.get_pet_by_id('django')  # no fail, 202


    def test_get_by_pet_id_discriminator(self, client):

        assert issubclass(AnimalNotFoundException, NotFoundErrorBaseException)
        assert issubclass(LinkNotFoundException, NotFoundErrorBaseException)

        with pytest.raises(AnimalNotFoundException) as excinfo:
            client.pet.get_pet_by_id("coyoteUgly")
        assert excinfo.value.error.reason == "the type of animal requested is not available"

        with pytest.raises(LinkNotFoundException) as excinfo:
            client.pet.get_pet_by_id("weirdAlYankovic")
        assert excinfo.value.error.reason == "link to pet not found"

    def test_get_by_pet_id_basic_types(self, client):

        with pytest.raises(Exception) as excinfo:
            client.pet.get_pet_by_id("ringo")
        assert excinfo.value.error is None  # no model attached
        assert json.loads(excinfo.value.response.text()) == "ringo is missing"

        with pytest.raises(Exception) as excinfo:
            client.pet.get_pet_by_id("alien123")
        assert excinfo.value.error is None  # no model attached
        assert json.loads(excinfo.value.response.text()) == 123

    def test_do_something_success(self, client):
        result = client.pet.do_something("stay")
        assert result.action_response is None

    def test_do_something_error(self, client):

        assert issubclass(PetSadErrorException, PetActionErrorException)
        assert issubclass(PetHungryOrThirstyErrorException, PetActionErrorException)

        with pytest.raises(PetSadErrorException) as excinfo:
            client.pet.do_something("jump")
        assert excinfo.value.error.reason == "need more treats"

        with pytest.raises(PetHungryOrThirstyErrorException) as excinfo:
            client.pet.do_something("fetch")
        assert excinfo.value.error.hungry_or_thirsty == "hungry and thirsty"