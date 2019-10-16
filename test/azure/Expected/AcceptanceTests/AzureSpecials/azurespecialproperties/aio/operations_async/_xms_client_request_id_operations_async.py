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
import uuid
from azure.core.exceptions import map_error
from azure.mgmt.core.exceptions import ARMError

from ... import models


class XMsClientRequestIdOperations:
    """XMsClientRequestIdOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config

    @distributed_trace_async
    async def get(self, *, cls=None, **kwargs):
        """Get method that overwrites x-ms-client-request header with value
        9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ARMError<azure.mgmt.core.ARMError>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())

        # Construct and send request
        error_map = kwargs.pop('error_map', None)
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    get.metadata = {'url': '/azurespecials/overwrite/x-ms-client-request-id/method/'}

    @distributed_trace_async
    async def param_get(self, x_ms_client_request_id, *, cls=None, **kwargs):
        """Get method that overwrites x-ms-client-request header with value
        9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.

        :param x_ms_client_request_id: This should appear as a method
         parameter, use value '9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'
        :type x_ms_client_request_id: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<azurespecialproperties.models.ErrorException>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.param_get.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        header_parameters['x-ms-client-request-id'] = self._serialize.header("x_ms_client_request_id", x_ms_client_request_id, 'str')

        # Construct and send request
        error_map = kwargs.pop('error_map', None)
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException(response, self._deserialize)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    param_get.metadata = {'url': '/azurespecials/overwrite/x-ms-client-request-id/via-param/method/'}
