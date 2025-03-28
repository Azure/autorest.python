# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import OAuth2ClientTestBase, OAuth2Preparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestOAuth2(OAuth2ClientTestBase):
    @OAuth2Preparer()
    @recorded_by_proxy
    def test_valid(self, oauth2_endpoint):
        client = self.create_client(endpoint=oauth2_endpoint)
        response = client.valid()

        # please add some check logic here by yourself
        # ...

    @OAuth2Preparer()
    @recorded_by_proxy
    def test_invalid(self, oauth2_endpoint):
        client = self.create_client(endpoint=oauth2_endpoint)
        response = client.invalid()

        # please add some check logic here by yourself
        # ...
