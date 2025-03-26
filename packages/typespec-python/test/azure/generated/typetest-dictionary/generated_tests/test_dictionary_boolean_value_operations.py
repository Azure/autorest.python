# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DictionaryClientTestBase, DictionaryPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDictionaryBooleanValueOperations(DictionaryClientTestBase):
    @DictionaryPreparer()
    @recorded_by_proxy
    def test_boolean_value_get(self, dictionary_endpoint):
        client = self.create_client(endpoint=dictionary_endpoint)
        response = client.boolean_value.get()

        # please add some check logic here by yourself
        # ...

    @DictionaryPreparer()
    @recorded_by_proxy
    def test_boolean_value_put(self, dictionary_endpoint):
        client = self.create_client(endpoint=dictionary_endpoint)
        response = client.boolean_value.put(
            body={"str": bool},
        )

        # please add some check logic here by yourself
        # ...
