# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import BodyOptionalityClientTestBase, BodyOptionalityPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBodyOptionality(BodyOptionalityClientTestBase):
    @BodyOptionalityPreparer()
    @recorded_by_proxy
    def test_required_explicit(self, bodyoptionality_endpoint):
        client = self.create_client(endpoint=bodyoptionality_endpoint)
        response = client.required_explicit(
            body={"name": "str"},
        )

        # please add some check logic here by yourself
        # ...

    @BodyOptionalityPreparer()
    @recorded_by_proxy
    def test_required_implicit(self, bodyoptionality_endpoint):
        client = self.create_client(endpoint=bodyoptionality_endpoint)
        response = client.required_implicit(
            body={"name": "str"},
            name="str",
        )

        # please add some check logic here by yourself
        # ...
