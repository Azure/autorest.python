# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft Corporation (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import EnumDiscriminatorClientTestBase, EnumDiscriminatorPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestEnumDiscriminator(EnumDiscriminatorClientTestBase):
    @EnumDiscriminatorPreparer()
    @recorded_by_proxy
    def test_get_extensible_model(self, enumdiscriminator_endpoint):
        client = self.create_client(endpoint=enumdiscriminator_endpoint)
        response = client.get_extensible_model()

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy
    def test_put_extensible_model(self, enumdiscriminator_endpoint):
        client = self.create_client(endpoint=enumdiscriminator_endpoint)
        response = client.put_extensible_model(
            input={"kind": "golden", "weight": 0},
        )

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy
    def test_get_extensible_model_missing_discriminator(self, enumdiscriminator_endpoint):
        client = self.create_client(endpoint=enumdiscriminator_endpoint)
        response = client.get_extensible_model_missing_discriminator()

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy
    def test_get_extensible_model_wrong_discriminator(self, enumdiscriminator_endpoint):
        client = self.create_client(endpoint=enumdiscriminator_endpoint)
        response = client.get_extensible_model_wrong_discriminator()

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy
    def test_get_fixed_model(self, enumdiscriminator_endpoint):
        client = self.create_client(endpoint=enumdiscriminator_endpoint)
        response = client.get_fixed_model()

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy
    def test_put_fixed_model(self, enumdiscriminator_endpoint):
        client = self.create_client(endpoint=enumdiscriminator_endpoint)
        response = client.put_fixed_model(
            input={"kind": "cobra", "length": 0},
        )

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy
    def test_get_fixed_model_missing_discriminator(self, enumdiscriminator_endpoint):
        client = self.create_client(endpoint=enumdiscriminator_endpoint)
        response = client.get_fixed_model_missing_discriminator()

        # please add some check logic here by yourself
        # ...

    @EnumDiscriminatorPreparer()
    @recorded_by_proxy
    def test_get_fixed_model_wrong_discriminator(self, enumdiscriminator_endpoint):
        client = self.create_client(endpoint=enumdiscriminator_endpoint)
        response = client.get_fixed_model_wrong_discriminator()

        # please add some check logic here by yourself
        # ...
