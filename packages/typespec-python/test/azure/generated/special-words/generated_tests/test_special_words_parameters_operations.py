# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import SpecialWordsClientTestBase, SpecialWordsPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSpecialWordsParametersOperations(SpecialWordsClientTestBase):
    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_and(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_and(
            and_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_as(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_as(
            as_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_assert(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_assert(
            assert_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_async(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_async(
            async_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_await(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_await(
            await_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_break(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_break(
            break_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_class(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_class(
            class_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_constructor(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_constructor(
            constructor="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_continue(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_continue(
            continue_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_def(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_def(
            def_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_del(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_del(
            del_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_elif(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_elif(
            elif_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_else(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_else(
            else_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_except(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_except(
            except_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_exec(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_exec(
            exec_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_finally(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_finally(
            finally_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_for(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_for(
            for_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_from(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_from(
            from_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_global(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_global(
            global_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_if(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_if(
            if_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_import(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_import(
            import_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_in(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_in(
            in_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_is(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_is(
            is_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_lambda(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_lambda(
            lambda_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_not(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_not(
            not_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_or(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_or(
            or_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_pass(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_pass(
            pass_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_raise(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_raise(
            raise_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_return(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_return(
            return_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_try(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_try(
            try_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_while(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_while(
            while_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_with(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_with(
            with_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_yield(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_yield(
            yield_parameter="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_parameters_with_cancellation_token(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.parameters.with_cancellation_token(
            cancellation_token="str",
        )

        # please add some check logic here by yourself
        # ...
