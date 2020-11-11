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
import sys

from azure.core.exceptions import HttpResponseError, ResourceNotFoundError

from xmserrorresponse import XMSErrorResponseExtensions
from xmserrorresponse.models import NotFoundErrorBase, AnimalNotFound, LinkNotFound, PetActionError, PetSadError, PetHungryOrThirstyError

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

        assert issubclass(AnimalNotFound, NotFoundErrorBase)
        assert issubclass(LinkNotFound, NotFoundErrorBase)

        with pytest.raises(HttpResponseError) as excinfo:
            client.pet.get_pet_by_id("coyoteUgly")
        assert isinstance(excinfo.value.model, AnimalNotFound)
        assert excinfo.value.model.reason == "the type of animal requested is not available"

        with pytest.raises(HttpResponseError) as excinfo:
            client.pet.get_pet_by_id("weirdAlYankovic")
        assert isinstance(excinfo.value.model, LinkNotFound)
        assert excinfo.value.model.reason == "link to pet not found"

    def test_get_by_pet_id_basic_types(self, client):

        with pytest.raises(Exception) as excinfo:
            client.pet.get_pet_by_id("ringo")
        assert excinfo.value.model is None  # no model attached
        assert json.loads(excinfo.value.response.text()) == "ringo is missing"

        with pytest.raises(Exception) as excinfo:
            client.pet.get_pet_by_id("alien123")
        assert excinfo.value.model is None  # no model attached
        assert json.loads(excinfo.value.response.text()) == 123

    def test_do_something_success(self, client):
        result = client.pet.do_something("stay")
        assert result.action_response is None

    def test_do_something_error(self, client):

        assert issubclass(PetSadError, PetActionError)
        assert issubclass(PetHungryOrThirstyError, PetActionError)

        with pytest.raises(HttpResponseError) as excinfo:
            client.pet.do_something("jump")
        assert isinstance(excinfo.value.model, PetSadError)
        assert excinfo.value.model.reason == "need more treats"

        with pytest.raises(ResourceNotFoundError) as excinfo:
            client.pet.do_something("fetch")

    def test_error_deserialization_with_param_name_models(self, client):
        with pytest.raises(HttpResponseError) as excinfo:
            client.pet.has_models_param()
        assert isinstance(excinfo.value.model, PetSadError)
        assert excinfo.value.status_code == 500

    def test_models(self):
        from xmserrorresponse.models import Animal

        if sys.version_info >= (3,5):
            from xmserrorresponse.models._models_py3 import Animal as AnimalPy3
            assert Animal == AnimalPy3
        else:
            from xmserrorresponse.models._models import Animal as AnimalPy2
            assert Animal == AnimalPy2
