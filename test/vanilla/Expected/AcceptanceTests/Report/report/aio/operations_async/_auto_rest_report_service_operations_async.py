# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.exceptions import map_error
from ... import models


class AutoRestReportServiceOperationsMixin:

    @distributed_trace_async
    async def get_report(self, qualifier=None, *, cls=None, **kwargs):
        """Get test coverage report.

        :param qualifier: If specified, qualifies the generated report further
         (e.g. '2.7' vs '3.5' in for Python). The only effect is, that
         generators that run all tests several times, can distinguish the
         generated reports.
        :type qualifier: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: dict or the result of cls(response)
        :rtype: dict[str, int]
        :raises: :class:`ErrorException<report.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_report.metadata['url']

        # Construct parameters
        query_parameters = {}
        if qualifier is not None:
            query_parameters['qualifier'] = self._serialize.query("qualifier", qualifier, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('{int}', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_report.metadata = {'url': '/report'}
