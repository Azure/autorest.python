# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import EmptyClientTestBase, EmptyPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestEmpty(EmptyClientTestBase):
    @EmptyPreparer()
    @recorded_by_proxy
    def test_put_empty(self, empty_endpoint):
        client = self.create_client(endpoint=empty_endpoint)
        response = client.put_empty(
            input={},
        )

        # please add some check logic here by yourself
        # ...

    @EmptyPreparer()
    @recorded_by_proxy
    def test_get_empty(self, empty_endpoint):
        client = self.create_client(endpoint=empty_endpoint)
        response = client.get_empty()

        # please add some check logic here by yourself
        # ...

    @EmptyPreparer()
    @recorded_by_proxy
    def test_post_round_trip_empty(self, empty_endpoint):
        client = self.create_client(endpoint=empty_endpoint)
        response = client.post_round_trip_empty(
            body={},
        )

        # please add some check logic here by yourself
        # ...
