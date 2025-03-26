# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ContentNegotiationClientTestBase, ContentNegotiationPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContentNegotiationDifferentBodyOperations(ContentNegotiationClientTestBase):
    @ContentNegotiationPreparer()
    @recorded_by_proxy
    def test_different_body_get_avatar_as_png(self, contentnegotiation_endpoint):
        client = self.create_client(endpoint=contentnegotiation_endpoint)
        response = client.different_body.get_avatar_as_png(
            accept="image/png",
        )

        # please add some check logic here by yourself
        # ...

    @ContentNegotiationPreparer()
    @recorded_by_proxy
    def test_different_body_get_avatar_as_json(self, contentnegotiation_endpoint):
        client = self.create_client(endpoint=contentnegotiation_endpoint)
        response = client.different_body.get_avatar_as_json(
            accept="application/json",
        )

        # please add some check logic here by yourself
        # ...
