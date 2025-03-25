# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import ConditionalRequestClientTestBase, ConditionalRequestPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestConditionalRequest(ConditionalRequestClientTestBase):
    @ConditionalRequestPreparer()
    @recorded_by_proxy
    def test_post_if_match(self, conditionalrequest_endpoint):
        client = self.create_client(endpoint=conditionalrequest_endpoint)
        response = client.post_if_match()

        # please add some check logic here by yourself
        # ...

    @ConditionalRequestPreparer()
    @recorded_by_proxy
    def test_post_if_none_match(self, conditionalrequest_endpoint):
        client = self.create_client(endpoint=conditionalrequest_endpoint)
        response = client.post_if_none_match()

        # please add some check logic here by yourself
        # ...

    @ConditionalRequestPreparer()
    @recorded_by_proxy
    def test_head_if_modified_since(self, conditionalrequest_endpoint):
        client = self.create_client(endpoint=conditionalrequest_endpoint)
        response = client.head_if_modified_since()

        # please add some check logic here by yourself
        # ...

    @ConditionalRequestPreparer()
    @recorded_by_proxy
    def test_post_if_unmodified_since(self, conditionalrequest_endpoint):
        client = self.create_client(endpoint=conditionalrequest_endpoint)
        response = client.post_if_unmodified_since()

        # please add some check logic here by yourself
        # ...
