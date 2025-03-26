# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DictionaryClientTestBase, DictionaryPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDictionaryUnknownValueOperations(DictionaryClientTestBase):
    @DictionaryPreparer()
    @recorded_by_proxy
    def test_unknown_value_get(self, dictionary_endpoint):
        client = self.create_client(endpoint=dictionary_endpoint)
        response = client.unknown_value.get()

        # please add some check logic here by yourself
        # ...

    @DictionaryPreparer()
    @recorded_by_proxy
    def test_unknown_value_put(self, dictionary_endpoint):
        client = self.create_client(endpoint=dictionary_endpoint)
        response = client.unknown_value.put(
            body={"str": {}},
        )

        # please add some check logic here by yourself
        # ...
