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
import inspect
import json
from azure.profiles import KnownProfiles


@pytest.fixture
def default_client():
    pass

@pytest.fixture
def client():
    pass

@pytest.fixture
def namespace_models():
    pass

class NotTested(object):

    class TestMultiapiBase(object):
        @pytest.mark.asyncio
        async def test_default_api_version_multiapi_client(self, default_client):
            assert default_client.DEFAULT_API_VERSION == "3.0.0"
            assert default_client.profile == KnownProfiles.default

        @pytest.mark.asyncio
        async def test_default_models(self, default_client):
            default_models = default_client.models()
            default_models.ModelThree

            # check the models from the other api versions can't be accessed
            with pytest.raises(AttributeError):
                default_models.ModelOne

            with pytest.raises(AttributeError):
                default_models.ModelTwo

        @pytest.mark.asyncio
        async def test_specify_api_version_models(self, default_client):
            v2_models = default_client.models(api_version="2.0.0")
            v2_models.ModelTwo(id=2)

            # check the models from the other api versions can't be accessed
            with pytest.raises(AttributeError):
                v2_models.ModelOne()

            with pytest.raises(AttributeError):
                v2_models.ModelThree()

        @pytest.mark.asyncio
        async def test_default_models_from_operation_group(self, default_client):
            models = default_client.operation_group_one.models
            models.ModelThree()

            with pytest.raises(AttributeError):
                models.ModelOne(id=1)

            with pytest.raises(AttributeError):
                models.ModelTwo(id=1)

        @pytest.mark.parametrize('api_version', ["1.0.0"])
        @pytest.mark.asyncio
        async def test_specify_models_from_operation_group(self, client):
            v1_models = client.operation_group_one.models

            # check the models from the other api versions can't be accessed
            with pytest.raises(AttributeError):
                v1_models.ModelTwo(id=2)

            with pytest.raises(AttributeError):
                v1_models.ModelThree()

        # OPERATION MIXINS
        @pytest.mark.asyncio
        async def test_default_operation_mixin(self, default_client, namespace_models):
            response = await default_client.test_one(id=1, message=None)
            assert response == namespace_models.ModelTwo(id=1, message="This was called with api-version 2.0.0")

        @pytest.mark.parametrize('api_version', ["1.0.0"])
        @pytest.mark.asyncio
        async def test_specificy_api_version_operation_mixin(self, client):
            response = await client.test_one(id=1, message="This is from api version One")
            assert response is None

        @pytest.mark.parametrize('api_version', ["3.0.0"])
        @pytest.mark.asyncio
        async def test_specify_api_version_with_no_mixin(self, client):
            with pytest.raises(ValueError):
                await client.test_one(id=1, message="This should throw")

        # OPERATION GROUP ONE
        @pytest.mark.asyncio
        async def test_default_operation_group_one(self, default_client, namespace_models):
            response = await default_client.operation_group_one.test_two()
            assert response == namespace_models.ModelThree(optional_property="This was called with api-version 3.0.0")

            with pytest.raises(AttributeError):
                response = await client.operation_group_one.test_three()

        @pytest.mark.parametrize('api_version', ["1.0.0"])
        @pytest.mark.asyncio
        async def test_version_one_operation_group_one(self, client):
            response = await client.operation_group_one.test_two()
            assert response is None

            with pytest.raises(AttributeError):
                response = await client.operation_group_one.test_three()

        @pytest.mark.parametrize('api_version', ["2.0.0"])
        @pytest.mark.asyncio
        async def test_version_two_operation_group_one(self, client, namespace_models):
            parameter = client.operation_group_one.models.ModelTwo(
                id=1, message="This should be sent from api version 2.0.0"
            )
            response = await client.operation_group_one.test_two(parameter)
            assert response == namespace_models.ModelTwo(id=1, message="This was called with api-version 2.0.0")

            response = await client.operation_group_one.test_three()
            assert response is None

        # OPERATION GROUP TWO
        @pytest.mark.asyncio
        async def test_default_operation_group_two_test_four_json(self, default_client):
            json_input = json.loads('{"source":"foo"}')
            response = await default_client.operation_group_two.test_four(input=json_input)
            assert response is None

        @pytest.mark.asyncio
        async def test_default_operation_group_two_test_four_pdf(self, default_client):
            response = await default_client.operation_group_two.test_four(
                input=b"PDF", content_type="application/pdf"
            )
            assert response is None

        @pytest.mark.asyncio
        async def test_default_operation_group_two_test_five(self, default_client):
            response = await default_client.operation_group_two.test_five()
            assert response is None

        @pytest.mark.parametrize('api_version', ["1.0.0"])
        @pytest.mark.asyncio
        async def test_version_one_operation_group_two_error(self, client):
            with pytest.raises(AttributeError):
                await client.operation_group_one.test_four()

        @pytest.mark.parametrize('api_version', ["2.0.0"])
        @pytest.mark.asyncio
        async def test_version_two_operation_group_two(self, client):
            response = await client.operation_group_two.test_four(parameter_one=True)
            assert response is None

            with pytest.raises(AttributeError):
                response = await client.operation_group_two.test_five()

        @pytest.mark.parametrize('api_version', ["1.0.0"])
        @pytest.mark.asyncio
        async def test_lro(self, client, namespace_models):
            poller = await client.begin_test_lro(namespace_models.Product())
            product = await poller.result()
            assert product.id == 100

        @pytest.mark.asyncio
        async def test_paging(self, default_client, namespace_models):
            pages = default_client.test_paging()
            items = []
            async for item in pages:
                items.append(item)
            assert len(items) == 1
            assert isinstance(items[0], namespace_models.ModelThree)
            assert items[0].optional_property == "paged"

        @pytest.mark.parametrize('api_version', ["1.0.0"])
        @pytest.mark.asyncio
        async def test_lro_and_paging(self, client, namespace_models):
            poller = await client.begin_test_lro_and_paging()
            pager = await poller.result()

            items = []
            async for item in pager:
                items.append(item)

            assert len(items) == 1
            assert isinstance(items[0], namespace_models.Product)
            assert items[0].id == 100

        @pytest.mark.parametrize('api_version', ["1.0.0"])
        @pytest.mark.asyncio
        async def test_different_calls_pass_version_one(self, client):
            await client.test_different_calls(greeting_in_english="hello")

        @pytest.mark.parametrize('api_version', ["1.0.0"])
        @pytest.mark.asyncio
        async def test_different_calls_pass_version_one_incorrect_parameters(self, client):
            with pytest.raises(ValueError) as ex:
                await client.test_different_calls(greeting_in_english="hello", greeting_in_chinese="nihao", greeting_in_french="bonjour")

            expected_error_string = (
                "Passed in parameter(s) 'greeting_in_chinese', 'greeting_in_french' not valid with api version '1.0.0': "
                "'greeting_in_chinese' was added in api version '2.0.0', 'greeting_in_french' was added in api version '3.0.0'"
            )
            assert expected_error_string in str(ex.value)

        @pytest.mark.parametrize('api_version', ["2.0.0"])
        @pytest.mark.asyncio
        async def test_different_calls_pass_version_two(self, client):
            await client.test_different_calls(greeting_in_english="hello", greeting_in_chinese="nihao")

        @pytest.mark.parametrize('api_version', ["2.0.0"])
        @pytest.mark.asyncio
        async def test_different_calls_pass_version_two_incorrect_parameters(self, client):
            with pytest.raises(ValueError) as ex:
                await client.test_different_calls(
                    greeting_in_english="hello", greeting_in_chinese="nihao", greeting_in_french="bonjour"
                )

            expected_error_string = (
                "Passed in parameter(s) 'greeting_in_french' not valid with api version '2.0.0': "
                "'greeting_in_french' was added in api version '3.0.0'"
            )

            assert expected_error_string in str(ex.value)

        @pytest.mark.asyncio
        async def test_different_calls_pass_version_three(self, default_client):
            await default_client.test_different_calls(
                greeting_in_english="hello", greeting_in_chinese="nihao", greeting_in_french='bonjour'
            )