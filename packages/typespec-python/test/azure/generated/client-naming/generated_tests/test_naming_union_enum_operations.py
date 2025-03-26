# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NamingClientTestBase, NamingPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNamingUnionEnumOperations(NamingClientTestBase):
    @NamingPreparer()
    @recorded_by_proxy
    def test_union_enum_union_enum_name(self, naming_endpoint):
        client = self.create_client(endpoint=naming_endpoint)
        response = client.union_enum.union_enum_name(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy
    def test_union_enum_union_enum_member_name(self, naming_endpoint):
        client = self.create_client(endpoint=naming_endpoint)
        response = client.union_enum.union_enum_member_name(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
