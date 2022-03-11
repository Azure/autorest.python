# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_report_request(*, qualifier: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    accept = "application/json"
    # Construct URL
    _url = "/report/azure"

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if qualifier is not None:
        _query_parameters["qualifier"] = _SERIALIZER.query("qualifier", qualifier, "str")

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_query_parameters, headers=_header_parameters, **kwargs)


class AutoRestReportServiceForAzureOperationsMixin(object):
    @distributed_trace
    def get_report(self, *, qualifier: Optional[str] = None, **kwargs: Any) -> Dict[str, int]:
        """Get test coverage report.

        :keyword qualifier: If specified, qualifies the generated report further (e.g. '2.7' vs '3.5'
         in for Python). The only effect is, that generators that run all tests several times, can
         distinguish the generated reports. Default value is None.
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
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_report_request(
            qualifier=qualifier,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = response.json()

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
