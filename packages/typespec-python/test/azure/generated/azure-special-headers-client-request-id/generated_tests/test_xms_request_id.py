# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import XmsClientRequestIdClientTestBase, XmsRequestIdPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestXmsRequestId(XmsClientRequestIdClientTestBase):
    @XmsRequestIdPreparer()
    @recorded_by_proxy
    def test_get(self, xmsrequestid_endpoint):
        client = self.create_client(endpoint=xmsrequestid_endpoint)
        response = client.get()

        # please add some check logic here by yourself
        # ...
