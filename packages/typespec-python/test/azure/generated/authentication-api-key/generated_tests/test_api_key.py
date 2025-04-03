# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ApiKeyClientTestBase, ApiKeyPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestApiKey(ApiKeyClientTestBase):
    @ApiKeyPreparer()
    @recorded_by_proxy
    def test_valid(self, apikey_endpoint):
        client = self.create_client(endpoint=apikey_endpoint)
        response = client.valid()

        # please add some check logic here by yourself
        # ...

    @ApiKeyPreparer()
    @recorded_by_proxy
    def test_invalid(self, apikey_endpoint):
        client = self.create_client(endpoint=apikey_endpoint)
        response = client.invalid()

        # please add some check logic here by yourself
        # ...
