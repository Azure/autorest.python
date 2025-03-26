# coding=utf-8
None
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from parameters.bodyoptionality import BodyOptionalityClient


class BodyOptionalityClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(BodyOptionalityClient)
        return self.create_client_from_credential(
            BodyOptionalityClient,
            credential=credential,
            endpoint=endpoint,
        )


BodyOptionalityPreparer = functools.partial(
    PowerShellPreparer, "bodyoptionality", bodyoptionality_endpoint="https://fake_bodyoptionality_endpoint.com"
)
