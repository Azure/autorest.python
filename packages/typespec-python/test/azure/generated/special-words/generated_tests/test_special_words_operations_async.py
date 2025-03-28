# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import SpecialWordsPreparer
from testpreparer_async import SpecialWordsClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSpecialWordsOperationsAsync(SpecialWordsClientTestBaseAsync):
    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_and_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.and_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_as_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.as_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_assert_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.assert_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_async_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.async_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_await_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.await_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_break_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.break_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_class_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.class_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_constructor(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.constructor()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_continue_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.continue_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_def_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.def_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_del_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.del_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_elif_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.elif_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_else_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.else_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_except_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.except_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_exec_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.exec_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_finally_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.finally_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_for_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.for_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_from_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.from_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_global_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.global_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_if_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.if_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_import_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.import_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_in_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.in_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_is_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.is_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_lambda_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.lambda_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_not_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.not_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_or_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.or_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_pass_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.pass_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_raise_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.raise_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_return_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.return_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_try_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.try_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_while_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.while_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_with_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.with_method()

        # please add some check logic here by yourself
        # ...

    @SpecialWordsPreparer()
    @recorded_by_proxy_async
    async def test_operations_yield_method(self, specialwords_endpoint):
        client = self.create_async_client(endpoint=specialwords_endpoint)
        response = await client.operations.yield_method()

        # please add some check logic here by yourself
        # ...
