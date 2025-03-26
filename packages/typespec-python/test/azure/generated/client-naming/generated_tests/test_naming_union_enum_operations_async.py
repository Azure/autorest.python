# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import NamingPreparer
from testpreparer_async import NamingClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNamingUnionEnumOperationsAsync(NamingClientTestBaseAsync):
    @NamingPreparer()
    @recorded_by_proxy_async
    async def test_union_enum_union_enum_name(self, naming_endpoint):
        client = self.create_async_client(endpoint=naming_endpoint)
        response = await client.union_enum.union_enum_name(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy_async
    async def test_union_enum_union_enum_member_name(self, naming_endpoint):
        client = self.create_async_client(endpoint=naming_endpoint)
        response = await client.union_enum.union_enum_member_name(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
