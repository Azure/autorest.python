# coding=utf-8
None
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import XmsRequestIdPreparer
from testpreparer_async import XmsClientRequestIdClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestXmsRequestIdAsync(XmsClientRequestIdClientTestBaseAsync):
    @XmsRequestIdPreparer()
    @recorded_by_proxy_async
    async def test_get(self, xmsrequestid_endpoint):
        client = self.create_async_client(endpoint=xmsrequestid_endpoint)
        response = await client.get()

        # please add some check logic here by yourself
        # ...
