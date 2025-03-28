# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import SpecialWordsClientTestBase, SpecialWordsPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSpecialWordsModelsOperations(SpecialWordsClientTestBase):
    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_and(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_and(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_as(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_as(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_assert(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_assert(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_async(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_async(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_await(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_await(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_break(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_break(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_class(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_class(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_constructor(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_constructor(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_continue(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_continue(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_def(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_def(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_del(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_del(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_elif(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_elif(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_else(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_else(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_except(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_except(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_exec(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_exec(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_finally(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_finally(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_for(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_for(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_from(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_from(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_global(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_global(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_if(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_if(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_import(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_import(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_in(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_in(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_is(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_is(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_lambda(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_lambda(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_not(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_not(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_or(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_or(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_pass(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_pass(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_raise(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_raise(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_return(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_return(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_try(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_try(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_while(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_while(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_with(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_with(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_models_with_yield(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.models.with_yield(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...
