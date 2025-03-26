# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ClientNamespaceSecondClientTestBase, NamespaceSecondPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNamespaceSecond(ClientNamespaceSecondClientTestBase):
    @NamespaceSecondPreparer()
    @recorded_by_proxy
    def test_get_second(self, namespacesecond_endpoint):
        client = self.create_client(endpoint=namespacesecond_endpoint)
        response = client.get_second()

        # please add some check logic here by yourself
        # ...
