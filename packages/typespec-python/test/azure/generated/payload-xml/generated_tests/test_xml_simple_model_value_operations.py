# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import XmlClientTestBase, XmlPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestXmlSimpleModelValueOperations(XmlClientTestBase):
    @XmlPreparer()
    @recorded_by_proxy
    def test_simple_model_value_get(self, xml_endpoint):
        client = self.create_client(endpoint=xml_endpoint)
        response = client.simple_model_value.get()

        # please add some check logic here by yourself
        # ...

    @XmlPreparer()
    @recorded_by_proxy
    def test_simple_model_value_put(self, xml_endpoint):
        client = self.create_client(endpoint=xml_endpoint)
        response = client.simple_model_value.put(
            input={"age": 0, "name": "str"},
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...
