# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NotVersionedClientTestBase, NotVersionedPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNotVersioned(NotVersionedClientTestBase):
    @NotVersionedPreparer()
    @recorded_by_proxy
    def test_without_api_version(self, notversioned_endpoint):
        client = self.create_client(endpoint=notversioned_endpoint)
        response = client.without_api_version()

        # please add some check logic here by yourself
        # ...

    @NotVersionedPreparer()
    @recorded_by_proxy
    def test_with_query_api_version(self, notversioned_endpoint):
        client = self.create_client(endpoint=notversioned_endpoint)
        response = client.with_query_api_version(
            api_version="str",
        )

        # please add some check logic here by yourself
        # ...

    @NotVersionedPreparer()
    @recorded_by_proxy
    def test_with_path_api_version(self, notversioned_endpoint):
        client = self.create_client(endpoint=notversioned_endpoint)
        response = client.with_path_api_version(
            api_version="str",
        )

        # please add some check logic here by yourself
        # ...
