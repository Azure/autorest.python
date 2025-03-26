# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import SpecialWordsClientTestBase, SpecialWordsPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSpecialWordsModelPropertiesOperations(SpecialWordsClientTestBase):
    @SpecialWordsPreparer()
    @recorded_by_proxy
    def test_model_properties_same_as_model(self, specialwords_endpoint):
        client = self.create_client(endpoint=specialwords_endpoint)
        response = client.model_properties.same_as_model(
            body={"SameAsModel": "str"},
        )

        # please add some check logic here by yourself
        # ...
