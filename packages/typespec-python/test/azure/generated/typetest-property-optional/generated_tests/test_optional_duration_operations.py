# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import OptionalClientTestBase, OptionalPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOptionalDurationOperations(OptionalClientTestBase):
    @OptionalPreparer()
    @recorded_by_proxy
    def test_duration_get_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.duration.get_all()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_duration_get_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.duration.get_default()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_duration_put_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.duration.put_all(
            body={"property": "1 day, 0:00:00"},
        )

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_duration_put_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.duration.put_default(
            body={"property": "1 day, 0:00:00"},
        )

        # please add some check logic here by yourself
        # ...
