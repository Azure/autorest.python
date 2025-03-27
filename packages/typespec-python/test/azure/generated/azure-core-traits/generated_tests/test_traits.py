# coding=utf-8
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import TraitsClientTestBase, TraitsPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTraits(TraitsClientTestBase):
    @TraitsPreparer()
    @recorded_by_proxy
    def test_smoke_test(self, traits_endpoint):
        client = self.create_client(endpoint=traits_endpoint)
        response = client.smoke_test(
            id=0,
            foo="str",
        )

        # please add some check logic here by yourself
        # ...

    @TraitsPreparer()
    @recorded_by_proxy
    def test_repeatable_action(self, traits_endpoint):
        client = self.create_client(endpoint=traits_endpoint)
        response = client.repeatable_action(
            id=0,
            body={"userActionValue": "str"},
        )

        # please add some check logic here by yourself
        # ...
