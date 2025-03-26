# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ClientNamespaceFirstClientTestBase, NamespaceFirstPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNamespaceFirst(ClientNamespaceFirstClientTestBase):
    @NamespaceFirstPreparer()
    @recorded_by_proxy
    def test_get_first(self, namespacefirst_endpoint):
        client = self.create_client(endpoint=namespacefirst_endpoint)
        response = client.get_first()

        # please add some check logic here by yourself
        # ...
