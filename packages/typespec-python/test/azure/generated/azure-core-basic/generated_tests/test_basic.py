# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import BasicClientTestBase, BasicPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBasic(BasicClientTestBase):
    @BasicPreparer()
    @recorded_by_proxy
    def test_create_or_update(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.create_or_update(
            id=0,
            resource={"etag": "str", "id": 0, "name": "str", "orders": [{"detail": "str", "id": 0, "userId": 0}]},
        )

        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_create_or_replace(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.create_or_replace(
            id=0,
            resource={"etag": "str", "id": 0, "name": "str", "orders": [{"detail": "str", "id": 0, "userId": 0}]},
        )

        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_get(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.get(
            id=0,
        )

        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_list(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.list()
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_delete(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.delete(
            id=0,
        )

        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_export(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.export(
            id=0,
            format="str",
        )

        # please add some check logic here by yourself
        # ...

    @BasicPreparer()
    @recorded_by_proxy
    def test_export_all_users(self, basic_endpoint):
        client = self.create_client(endpoint=basic_endpoint)
        response = client.export_all_users(
            format="str",
        )

        # please add some check logic here by yourself
        # ...
