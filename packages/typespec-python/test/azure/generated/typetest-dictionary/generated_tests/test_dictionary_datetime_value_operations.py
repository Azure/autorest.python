# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import DictionaryClientTestBase, DictionaryPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestDictionaryDatetimeValueOperations(DictionaryClientTestBase):
    @DictionaryPreparer()
    @recorded_by_proxy
    def test_datetime_value_get(self, dictionary_endpoint):
        client = self.create_client(endpoint=dictionary_endpoint)
        response = client.datetime_value.get()

        # please add some check logic here by yourself
        # ...

    @DictionaryPreparer()
    @recorded_by_proxy
    def test_datetime_value_put(self, dictionary_endpoint):
        client = self.create_client(endpoint=dictionary_endpoint)
        response = client.datetime_value.put(
            body={"str": "2020-02-20 00:00:00"},
        )

        # please add some check logic here by yourself
        # ...
