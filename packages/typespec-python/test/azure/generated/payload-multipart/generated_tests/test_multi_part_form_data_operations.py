# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import MultiPartClientTestBase, MultiPartPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMultiPartFormDataOperations(MultiPartClientTestBase):
    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_basic(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.basic(
            body={"id": "str", "profileImage": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_file_array_and_basic(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.file_array_and_basic(
            body={"address": {"city": "str"}, "id": "str", "pictures": ["filetype"], "profileImage": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_json_part(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.json_part(
            body={"address": {"city": "str"}, "profileImage": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_binary_array_parts(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.binary_array_parts(
            body={"id": "str", "pictures": ["filetype"]},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_multi_binary_parts(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.multi_binary_parts(
            body={"profileImage": "filetype", "picture": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_check_file_name_and_content_type(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.check_file_name_and_content_type(
            body={"id": "str", "profileImage": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_anonymous_model(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.anonymous_model(
            body={"profileImage": "filetype"},
            profile_image="filetype",
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_http_parts_json_array_and_file_array(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.http_parts.json_array_and_file_array(
            body={
                "address": {"city": "str"},
                "id": "str",
                "pictures": ["filetype"],
                "previousAddresses": [{"city": "str"}],
                "profileImage": "filetype",
            },
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_http_parts_content_type_image_jpeg_content_type(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.http_parts.content_type.image_jpeg_content_type(
            body={"profileImage": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_http_parts_content_type_required_content_type(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.http_parts.content_type.required_content_type(
            body={"profileImage": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_http_parts_content_type_optional_content_type(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.http_parts.content_type.optional_content_type(
            body={"profileImage": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_form_data_http_parts_non_string_float(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.http_parts.non_string.float(
            body={"temperature": 0.0},
        )

        # please add some check logic here by yourself
        # ...
