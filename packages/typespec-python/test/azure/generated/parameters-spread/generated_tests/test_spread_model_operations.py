# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import SpreadClientTestBase, SpreadPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSpreadModelOperations(SpreadClientTestBase):
    @SpreadPreparer()
    @recorded_by_proxy
    def test_model_spread_as_request_body(self, spread_endpoint):
        client = self.create_client(endpoint=spread_endpoint)
        response = client.model.spread_as_request_body(
            body={"name": "str"},
            name="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpreadPreparer()
    @recorded_by_proxy
    def test_model_spread_composite_request_only_with_body(self, spread_endpoint):
        client = self.create_client(endpoint=spread_endpoint)
        response = client.model.spread_composite_request_only_with_body(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @SpreadPreparer()
    @recorded_by_proxy
    def test_model_spread_composite_request_without_body(self, spread_endpoint):
        client = self.create_client(endpoint=spread_endpoint)
        response = client.model.spread_composite_request_without_body(
            name="str",
            test_header="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpreadPreparer()
    @recorded_by_proxy
    def test_model_spread_composite_request(self, spread_endpoint):
        client = self.create_client(endpoint=spread_endpoint)
        response = client.model.spread_composite_request(
            name="str",
            body={"name": "str"},
            test_header="str",
        )

        # please add some check logic here by yourself
        # ...

    @SpreadPreparer()
    @recorded_by_proxy
    def test_model_spread_composite_request_mix(self, spread_endpoint):
        client = self.create_client(endpoint=spread_endpoint)
        response = client.model.spread_composite_request_mix(
            name="str",
            body={"prop": "str"},
            test_header="str",
            prop="str",
        )

        # please add some check logic here by yourself
        # ...
