# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NotDefinedClientTestBase, NotDefinedPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNotDefined(NotDefinedClientTestBase):
    @NotDefinedPreparer()
    @recorded_by_proxy
    def test_valid(self, notdefined_endpoint):
        client = self.create_client(endpoint=notdefined_endpoint)
        response = client.valid()

        # please add some check logic here by yourself
        # ...
