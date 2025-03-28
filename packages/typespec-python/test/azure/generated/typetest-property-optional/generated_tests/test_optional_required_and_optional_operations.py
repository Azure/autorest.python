# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import OptionalClientTestBase, OptionalPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOptionalRequiredAndOptionalOperations(OptionalClientTestBase):
    @OptionalPreparer()
    @recorded_by_proxy
    def test_required_and_optional_get_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.required_and_optional.get_all()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_required_and_optional_get_required_only(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.required_and_optional.get_required_only()

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_required_and_optional_put_all(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.required_and_optional.put_all(
            body={"requiredProperty": 0, "optionalProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @OptionalPreparer()
    @recorded_by_proxy
    def test_required_and_optional_put_required_only(self, optional_endpoint):
        client = self.create_client(endpoint=optional_endpoint)
        response = client.required_and_optional.put_required_only(
            body={"requiredProperty": 0, "optionalProperty": "str"},
        )

        # please add some check logic here by yourself
        # ...
