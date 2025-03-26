# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import VersionedClientTestBase, VersionedPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestVersioned(VersionedClientTestBase):
    @VersionedPreparer()
    @recorded_by_proxy
    def test_without_api_version(self, versioned_endpoint):
        client = self.create_client(endpoint=versioned_endpoint)
        response = client.without_api_version()

        # please add some check logic here by yourself
        # ...

    @VersionedPreparer()
    @recorded_by_proxy
    def test_with_query_api_version(self, versioned_endpoint):
        client = self.create_client(endpoint=versioned_endpoint)
        response = client.with_query_api_version()

        # please add some check logic here by yourself
        # ...

    @VersionedPreparer()
    @recorded_by_proxy
    def test_with_path_api_version(self, versioned_endpoint):
        client = self.create_client(endpoint=versioned_endpoint)
        response = client.with_path_api_version()

        # please add some check logic here by yourself
        # ...

    @VersionedPreparer()
    @recorded_by_proxy
    def test_with_query_old_api_version(self, versioned_endpoint):
        client = self.create_client(endpoint=versioned_endpoint)
        response = client.with_query_old_api_version()

        # please add some check logic here by yourself
        # ...
