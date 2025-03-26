# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import TypeChangedFromClientTestBase, TypeChangedFromPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTypeChangedFrom(TypeChangedFromClientTestBase):
    @TypeChangedFromPreparer()
    @recorded_by_proxy
    def test_test(self, typechangedfrom_endpoint):
        client = self.create_client(endpoint=typechangedfrom_endpoint)
        response = client.test(
            body={"changedProp": "str", "prop": "str"},
            param="str",
        )

        # please add some check logic here by yourself
        # ...
