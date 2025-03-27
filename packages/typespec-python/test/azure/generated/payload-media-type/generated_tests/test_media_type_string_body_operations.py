# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import MediaTypeClientTestBase, MediaTypePreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMediaTypeStringBodyOperations(MediaTypeClientTestBase):
    @MediaTypePreparer()
    @recorded_by_proxy
    def test_string_body_send_as_text(self, mediatype_endpoint):
        client = self.create_client(endpoint=mediatype_endpoint)
        response = client.string_body.send_as_text(
            text="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @MediaTypePreparer()
    @recorded_by_proxy
    def test_string_body_get_as_text(self, mediatype_endpoint):
        client = self.create_client(endpoint=mediatype_endpoint)
        response = client.string_body.get_as_text()

        # please add some check logic here by yourself
        # ...

    @MediaTypePreparer()
    @recorded_by_proxy
    def test_string_body_send_as_json(self, mediatype_endpoint):
        client = self.create_client(endpoint=mediatype_endpoint)
        response = client.string_body.send_as_json(
            text="str",
            content_type="str",
        )

        # please add some check logic here by yourself
        # ...

    @MediaTypePreparer()
    @recorded_by_proxy
    def test_string_body_get_as_json(self, mediatype_endpoint):
        client = self.create_client(endpoint=mediatype_endpoint)
        response = client.string_body.get_as_json()

        # please add some check logic here by yourself
        # ...
