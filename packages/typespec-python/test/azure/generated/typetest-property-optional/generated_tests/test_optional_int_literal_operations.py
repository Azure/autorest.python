# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import OptionalClientTestBase, OptionalPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOptionalIntLiteralOperations(OptionalClientTestBase):
    @OptionalPreparer()
    @recorded_by_proxy
    def test_int_literal_get_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.int_literal.get_all()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_int_literal_get_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.int_literal.get_default()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_int_literal_put_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.int_literal.put_all(
            body={"property": 1},
        )

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_int_literal_put_default(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.int_literal.put_default(
            body={"property": 1},
        )

        # please add some check logic here by yourself
        # ...
