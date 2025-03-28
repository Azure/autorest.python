# coding=utf-8
import pytest
from devtools_testutils.aio import recorded_by_proxy_async
from testpreparer import RoutesPreparer
from testpreparer_async import RoutesClientTestBaseAsync


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestRoutesPathParametersOperationsAsync(RoutesClientTestBaseAsync):
    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_template_only(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.template_only(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_explicit(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.explicit(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_annotation_only(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.annotation_only(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_reserved_expansion_template(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.reserved_expansion.template(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_reserved_expansion_annotation(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.reserved_expansion.annotation(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_simple_expansion_standard_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.simple_expansion.standard.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_simple_expansion_standard_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.simple_expansion.standard.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_simple_expansion_standard_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.simple_expansion.standard.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_simple_expansion_explode_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.simple_expansion.explode.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_simple_expansion_explode_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.simple_expansion.explode.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_simple_expansion_explode_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.simple_expansion.explode.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_path_expansion_standard_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.path_expansion.standard.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_path_expansion_standard_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.path_expansion.standard.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_path_expansion_standard_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.path_expansion.standard.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_path_expansion_explode_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.path_expansion.explode.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_path_expansion_explode_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.path_expansion.explode.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_path_expansion_explode_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.path_expansion.explode.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_label_expansion_standard_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.label_expansion.standard.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_label_expansion_standard_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.label_expansion.standard.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_label_expansion_standard_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.label_expansion.standard.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_label_expansion_explode_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.label_expansion.explode.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_label_expansion_explode_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.label_expansion.explode.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_label_expansion_explode_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.label_expansion.explode.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_matrix_expansion_standard_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.matrix_expansion.standard.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_matrix_expansion_standard_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.matrix_expansion.standard.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_matrix_expansion_standard_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.matrix_expansion.standard.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_matrix_expansion_explode_primitive(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.matrix_expansion.explode.primitive(
            param="str",
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_matrix_expansion_explode_array(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.matrix_expansion.explode.array(
            param=["str"],
        )

        # please add some check logic here by yourself
        # ...

    @RoutesPreparer()
    @recorded_by_proxy_async
    async def test_path_parameters_matrix_expansion_explode_record(self, routes_endpoint):
        client = self.create_async_client(endpoint=routes_endpoint)
        response = await client.path_parameters.matrix_expansion.explode.record(
            param={"str": 0},
        )

        # please add some check logic here by yourself
        # ...
