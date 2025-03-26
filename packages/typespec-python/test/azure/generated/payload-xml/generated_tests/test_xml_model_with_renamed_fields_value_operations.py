# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import XmlClientTestBase, XmlPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestXmlModelWithRenamedFieldsValueOperations(XmlClientTestBase):
    @XmlPreparer()
    @recorded_by_proxy
    def test_model_with_renamed_fields_value_get(self, xml_endpoint):
        client = self.create_client(endpoint=xml_endpoint)
        response = client.model_with_renamed_fields_value.get()

        # please add some check logic here by yourself
        # ...

    @XmlPreparer()
    @recorded_by_proxy
    def test_model_with_renamed_fields_value_put(self, xml_endpoint):
        client = self.create_client(endpoint=xml_endpoint)
        response = client.model_with_renamed_fields_value.put(
            input={"inputData": {"age": 0, "name": "str"}, "outputData": {"age": 0, "name": "str"}},
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
