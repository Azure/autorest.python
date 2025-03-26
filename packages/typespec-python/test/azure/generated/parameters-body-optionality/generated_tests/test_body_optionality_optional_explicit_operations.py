# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import BodyOptionalityClientTestBase, BodyOptionalityPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestBodyOptionalityOptionalExplicitOperations(BodyOptionalityClientTestBase):
    @BodyOptionalityPreparer()
    @recorded_by_proxy
    def test_optional_explicit_set(self, bodyoptionality_endpoint):
        client = self.create_client(endpoint=bodyoptionality_endpoint)
        response = client.optional_explicit.set()

        # please add some check logic here by yourself
        # ...

    @BodyOptionalityPreparer()
    @recorded_by_proxy
    def test_optional_explicit_omit(self, bodyoptionality_endpoint):
        client = self.create_client(endpoint=bodyoptionality_endpoint)
        response = client.optional_explicit.omit()

        # please add some check logic here by yourself
        # ...
