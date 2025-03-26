# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ContentNegotiationClientTestBase, ContentNegotiationPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestContentNegotiationSameBodyOperations(ContentNegotiationClientTestBase):
    @ContentNegotiationPreparer()
    @recorded_by_proxy
    def test_same_body_get_avatar_as_png(self, contentnegotiation_endpoint):
        client = self.create_client(endpoint=contentnegotiation_endpoint)
        response = client.same_body.get_avatar_as_png(
            accept="image/png",
        )

        # please add some check logic here by yourself
        # ...

    @ContentNegotiationPreparer()
    @recorded_by_proxy
    def test_same_body_get_avatar_as_jpeg(self, contentnegotiation_endpoint):
        client = self.create_client(endpoint=contentnegotiation_endpoint)
        response = client.same_body.get_avatar_as_jpeg(
            accept="image/jpeg",
        )

        # please add some check logic here by yourself
        # ...
