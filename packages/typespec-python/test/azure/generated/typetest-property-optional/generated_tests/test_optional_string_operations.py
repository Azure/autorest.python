# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import OptionalClientTestBase, OptionalPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOptionalStringOperations(OptionalClientTestBase):
    @OptionalPreparer()
    @recorded_by_proxy
    def test_string_get_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.string.get_all()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_string_get_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.string.get_default()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_string_put_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.string.put_all(
            body={"property": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_string_put_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.string.put_default(
            body={"property": "str"},
        )

        # please add some check logic here by yourself
        # ...
