# coding=utf-8
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from routes import RoutesClient


class RoutesClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(RoutesClient)
        return self.create_client_from_credential(
            RoutesClient,
            credential=credential,
            endpoint=endpoint,
        )


RoutesPreparer = functools.partial(PowerShellPreparer, "routes", routes_endpoint="https://fake_routes_endpoint.com")
