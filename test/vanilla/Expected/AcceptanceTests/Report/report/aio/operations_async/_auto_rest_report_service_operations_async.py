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

from ... import models


class AutoRestReportServiceOperationsMixin:

    async def get_report(self, qualifier=None, *, cls=None, **operation_config):
        """Get test coverage report.

        :param qualifier: If specified, qualifies the generated report further
         (e.g. '2.7' vs '3.5' in for Python). The only effect is, that
         generators that run all tests several times, can distinguish the
         generated reports.
        :type qualifier: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: dict or the result of cls(response)
        :rtype: dict[str, int]
        :raises: :class:`ErrorException<report.models.ErrorException>`
        """
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
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('{int}', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_report.metadata = {'url': '/report'}
