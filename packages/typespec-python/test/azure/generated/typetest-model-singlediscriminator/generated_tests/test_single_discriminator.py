# coding=utf-8
None
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import SingleDiscriminatorClientTestBase, SingleDiscriminatorPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestSingleDiscriminator(SingleDiscriminatorClientTestBase):
    @SingleDiscriminatorPreparer()
    @recorded_by_proxy
    def test_get_model(self, singlediscriminator_endpoint):
        client = self.create_client(endpoint=singlediscriminator_endpoint)
        response = client.get_model()

        # please add some check logic here by yourself
        # ...

    @SingleDiscriminatorPreparer()
    @recorded_by_proxy
    def test_put_model(self, singlediscriminator_endpoint):
        client = self.create_client(endpoint=singlediscriminator_endpoint)
        response = client.put_model(
            input={"kind": "eagle", "wingspan": 0, "friends": ["bird"], "hate": {"str": "bird"}, "partner": "bird"},
        )

        # please add some check logic here by yourself
        # ...

    @SingleDiscriminatorPreparer()
    @recorded_by_proxy
    def test_get_recursive_model(self, singlediscriminator_endpoint):
        client = self.create_client(endpoint=singlediscriminator_endpoint)
        response = client.get_recursive_model()

        # please add some check logic here by yourself
        # ...

    @SingleDiscriminatorPreparer()
    @recorded_by_proxy
    def test_put_recursive_model(self, singlediscriminator_endpoint):
        client = self.create_client(endpoint=singlediscriminator_endpoint)
        response = client.put_recursive_model(
            input={"kind": "eagle", "wingspan": 0, "friends": ["bird"], "hate": {"str": "bird"}, "partner": "bird"},
        )

        # please add some check logic here by yourself
        # ...

    @SingleDiscriminatorPreparer()
    @recorded_by_proxy
    def test_get_missing_discriminator(self, singlediscriminator_endpoint):
        client = self.create_client(endpoint=singlediscriminator_endpoint)
        response = client.get_missing_discriminator()

        # please add some check logic here by yourself
        # ...

    @SingleDiscriminatorPreparer()
    @recorded_by_proxy
    def test_get_wrong_discriminator(self, singlediscriminator_endpoint):
        client = self.create_client(endpoint=singlediscriminator_endpoint)
        response = client.get_wrong_discriminator()

        # please add some check logic here by yourself
        # ...

    @SingleDiscriminatorPreparer()
    @recorded_by_proxy
    def test_get_legacy_model(self, singlediscriminator_endpoint):
        client = self.create_client(endpoint=singlediscriminator_endpoint)
        response = client.get_legacy_model()

        # please add some check logic here by yourself
        # ...
