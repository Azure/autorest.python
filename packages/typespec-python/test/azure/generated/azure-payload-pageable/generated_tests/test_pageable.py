# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import PageableClientTestBase, PageablePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestPageable(PageableClientTestBase):
    @PageablePreparer()
    @recorded_by_proxy
    def test_list(self, pageable_endpoint):
        client = self.create_client(endpoint=pageable_endpoint)
        response = client.list()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
