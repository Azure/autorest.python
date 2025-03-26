# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import XmlPreparer
from testpreparer_async import XmlClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestXmlSimpleModelValueOperationsAsync(XmlClientTestBaseAsync):
    @XmlPreparer()
    @recorded_by_proxy_async
    async def test_simple_model_value_get(self, xml_endpoint):
        client = self.create_async_client(endpoint=xml_endpoint)
        response = await client.simple_model_value.get()

        # please add some check logic here by yourself
        # ...

    @XmlPreparer()
    @recorded_by_proxy_async
    async def test_simple_model_value_put(self, xml_endpoint):
        client = self.create_async_client(endpoint=xml_endpoint)
        response = await client.simple_model_value.put(
            input={"age": 0, "name": "str"},
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
