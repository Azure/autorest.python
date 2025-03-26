# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ReturnTypeChangedFromClientTestBase, ReturnTypeChangedFromPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestReturnTypeChangedFrom(ReturnTypeChangedFromClientTestBase):
    @ReturnTypeChangedFromPreparer()
    @recorded_by_proxy
    def test_test(self, returntypechangedfrom_endpoint):
        client = self.create_client(endpoint=returntypechangedfrom_endpoint)
        response = client.test(
            body="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
