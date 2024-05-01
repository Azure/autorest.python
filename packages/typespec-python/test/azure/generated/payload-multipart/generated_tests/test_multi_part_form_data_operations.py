# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import MultiPartClientTestBase, MultiPartPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestMultiPartFormDataOperations(MultiPartClientTestBase):
    @MultiPartPreparer()
    @recorded_by_proxy
    def test_basic(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.basic(
            body={"id": "str", "profileImage": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_complex(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.complex(
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
    def test_json_part(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.json_part(
            body={"address": {"city": "str"}, "profileImage": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_binary_array_parts(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.binary_array_parts(
            body={"id": "str", "pictures": ["filetype"]},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_json_array_parts(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.json_array_parts(
            body={"previousAddresses": [{"city": "str"}], "profileImage": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_multi_binary_parts(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.multi_binary_parts(
            body={"profileImage": "filetype", "picture": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_check_file_name_and_content_type(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.check_file_name_and_content_type(
            body={"id": "str", "profileImage": "filetype"},
        )

        # please add some check logic here by yourself
        # ...

    @MultiPartPreparer()
    @recorded_by_proxy
    def test_anonymous_model(self, multipart_endpoint):
        client = self.create_client(endpoint=multipart_endpoint)
        response = client.form_data.anonymous_model(
            body={"profileImage": "filetype"},
            profile_image=bytes("bytes", encoding="utf-8"),
        )

        # please add some check logic here by yourself
        # ...
