# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import XmlClientTestBase, XmlPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestXmlModelWithDictionaryValueOperations(XmlClientTestBase):
    @XmlPreparer()
    @recorded_by_proxy
    def test_model_with_dictionary_value_get(self, xml_endpoint):
        client = self.create_client(endpoint=xml_endpoint)
        response = client.model_with_dictionary_value.get()

        # please add some check logic here by yourself
        # ...

    @XmlPreparer()
    @recorded_by_proxy
    def test_model_with_dictionary_value_put(self, xml_endpoint):
        client = self.create_client(endpoint=xml_endpoint)
        response = client.model_with_dictionary_value.put(
            input={"metadata": {"str": "str"}},
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
