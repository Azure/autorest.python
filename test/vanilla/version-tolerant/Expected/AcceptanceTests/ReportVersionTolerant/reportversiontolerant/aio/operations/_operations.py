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

from ...operations._operations import build_get_optional_report_request, build_get_report_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AutoRestReportServiceOperationsMixin:
    @distributed_trace_async
    async def get_report(self, *, qualifier: Optional[str] = None, **kwargs: Any) -> Dict[str, int]:
        """Get test coverage report.

        :keyword qualifier: If specified, qualifies the generated report further (e.g. '2.7' vs '3.5'
         in for Python). The only effect is, that generators that run all tests several times, can
         distinguish the generated reports.
        :paramtype qualifier: str
        :return: dict mapping str to int
        :rtype: dict[str, int]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "str": 0  # Optional.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, int]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_get_report_request(
            qualifier=qualifier,
            template_url=self.get_report.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_report.metadata = {"url": "/report"}  # type: ignore

    @distributed_trace_async
    async def get_optional_report(self, *, qualifier: Optional[str] = None, **kwargs: Any) -> Dict[str, int]:
        """Get optional test coverage report.

        :keyword qualifier: If specified, qualifies the generated report further (e.g. '2.7' vs '3.5'
         in for Python). The only effect is, that generators that run all tests several times, can
         distinguish the generated reports.
        :paramtype qualifier: str
        :return: dict mapping str to int
        :rtype: dict[str, int]
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "str": 0  # Optional.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Dict[str, int]]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        request = build_get_optional_report_request(
            qualifier=qualifier,
            template_url=self.get_optional_report.metadata["url"],
            headers=kwargs.pop("headers", {}),
            params=kwargs.pop("params", {}),
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_optional_report.metadata = {"url": "/report/optional"}  # type: ignore
