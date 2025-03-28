# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import RoutesPreparer
from testpreparer_async import RoutesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRoutesQueryParametersOperationsAsync(RoutesClientTestBaseAsync):
    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_template_only(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.template_only(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_explicit(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.explicit(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_annotation_only(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.annotation_only(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_expansion_standard_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_expansion.standard.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_expansion_standard_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_expansion.standard.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_expansion_standard_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_expansion.standard.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_expansion_explode_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_expansion.explode.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_expansion_explode_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_expansion.explode.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_expansion_explode_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_expansion.explode.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_continuation_standard_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_continuation.standard.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_continuation_standard_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_continuation.standard.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_continuation_standard_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_continuation.standard.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_continuation_explode_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_continuation.explode.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_continuation_explode_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_continuation.explode.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_query_parameters_query_continuation_explode_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.query_parameters.query_continuation.explode.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...
