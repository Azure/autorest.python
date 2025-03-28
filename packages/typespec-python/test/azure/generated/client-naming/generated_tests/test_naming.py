# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NamingClientTestBase, NamingPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNaming(NamingClientTestBase):
    @NamingPreparer()
    @recorded_by_proxy
    def test_client_name(self, naming_endpoint):
        client = self.create_client(endpoint=naming_endpoint)
        response = client.client_name()

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy
    def test_parameter(self, naming_endpoint):
        client = self.create_client(endpoint=naming_endpoint)
        response = client.parameter(
            client_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy
    def test_client(self, naming_endpoint):
        client = self.create_client(endpoint=naming_endpoint)
        response = client.client(
            body={"defaultName": bool},
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy
    def test_language(self, naming_endpoint):
        client = self.create_client(endpoint=naming_endpoint)
        response = client.language(
            body={"defaultName": bool},
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy
    def test_compatible_with_encoded_name(self, naming_endpoint):
        client = self.create_client(endpoint=naming_endpoint)
        response = client.compatible_with_encoded_name(
            body={"wireName": bool},
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy
    def test_request(self, naming_endpoint):
        client = self.create_client(endpoint=naming_endpoint)
        response = client.request(
            client_name="str",
        )

        # please add some check logic here by yourself
        # ...

    @NamingPreparer()
    @recorded_by_proxy
    def test_response(self, naming_endpoint):
        client = self.create_client(endpoint=naming_endpoint)
        response = client.response()

        # please add some check logic here by yourself
        # ...
