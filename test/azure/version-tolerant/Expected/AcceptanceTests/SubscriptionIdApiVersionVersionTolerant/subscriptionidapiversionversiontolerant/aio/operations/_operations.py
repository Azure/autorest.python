# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ...operations._operations import build_group_get_sample_resource_group_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class GroupOperations:
    """GroupOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_sample_resource_group(
        self, resource_group_name: str, *, api_version: str = "2014-04-01-preview", **kwargs: Any
    ) -> Any:
        """Provides a resouce group with name 'testgroup101' and location 'West US'.

        :param resource_group_name: Resource Group name 'testgroup101'.
        :type resource_group_name: str
        :keyword api_version: Api Version.
        :paramtype api_version: str
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "location": "str",  # Optional. resource group location 'West US'.
                    "name": "str"  # Optional. resource group name 'testgroup101'.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_group_get_sample_resource_group_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            api_version=api_version,
            template_url=self.get_sample_resource_group.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_sample_resource_group.metadata = {"url": "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}"}  # type: ignore
