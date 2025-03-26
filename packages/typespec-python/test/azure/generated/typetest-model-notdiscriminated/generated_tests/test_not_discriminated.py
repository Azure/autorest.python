# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import NotDiscriminatedClientTestBase, NotDiscriminatedPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNotDiscriminated(NotDiscriminatedClientTestBase):
    @NotDiscriminatedPreparer()
    @recorded_by_proxy
    def test_post_valid(self, notdiscriminated_endpoint):
        client = self.create_client(endpoint=notdiscriminated_endpoint)
        response = client.post_valid(
            input={"age": 0, "name": "str", "smart": bool},
        )

        # please add some check logic here by yourself
        # ...

    @NotDiscriminatedPreparer()
    @recorded_by_proxy
    def test_get_valid(self, notdiscriminated_endpoint):
        client = self.create_client(endpoint=notdiscriminated_endpoint)
        response = client.get_valid()

        # please add some check logic here by yourself
        # ...

    @NotDiscriminatedPreparer()
    @recorded_by_proxy
    def test_put_valid(self, notdiscriminated_endpoint):
        client = self.create_client(endpoint=notdiscriminated_endpoint)
        response = client.put_valid(
            input={"age": 0, "name": "str", "smart": bool},
        )

        # please add some check logic here by yourself
        # ...
