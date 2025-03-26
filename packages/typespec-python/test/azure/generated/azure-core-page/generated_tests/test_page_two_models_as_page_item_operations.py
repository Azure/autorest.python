# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import PageClientTestBase, PagePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestPageTwoModelsAsPageItemOperations(PageClientTestBase):
    @PagePreparer()
    @recorded_by_proxy
    def test_two_models_as_page_item_list_first_item(self, page_endpoint):
        client = self.create_client(endpoint=page_endpoint)
        response = client.two_models_as_page_item.list_first_item()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @PagePreparer()
    @recorded_by_proxy
    def test_two_models_as_page_item_list_second_item(self, page_endpoint):
        client = self.create_client(endpoint=page_endpoint)
        response = client.two_models_as_page_item.list_second_item()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...
