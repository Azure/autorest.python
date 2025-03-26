# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import CollectionFormatClientTestBase, CollectionFormatPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestCollectionFormatHeaderOperations(CollectionFormatClientTestBase):
    @CollectionFormatPreparer()
    @recorded_by_proxy
    def test_header_csv(self, collectionformat_endpoint):
        client = self.create_client(endpoint=collectionformat_endpoint)
        response = client.header.csv(
            colors=["str"],
        )

        # please add some check logic here by yourself
        # ...
