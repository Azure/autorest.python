# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional
import warnings

from azure.core.exceptions import map_error
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.tracing.decorator_async import distributed_trace_async

from ... import models


class PathsOperations:
    """PathsOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~custombaseurlmoreoptions.models
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
    async def get_empty(
        self,
        vault: str,
        secret: str,
        key_name: str,
        key_version: Optional[str] = None,
        *,
        cls: Optional[Callable[[AsyncHttpResponse, None, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> None:
        """Get a 200 to test a valid base uri.

        FIXME: add operation.summary

        :param vault: The vault name, e.g. https://myvault
        :type vault: str
        :param secret: Secret value.
        :type secret: str
        :param key_name: The key name with value 'key1'.
        :type key_name: str
        :param key_version: The key version. Default value 'v1'.
        :type key_version: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~custombaseurlmoreoptions.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_empty.metadata['url']
        path_format_arguments = {
            'vault': self._serialize.url("vault", vault, 'str', skip_quote=True),
            'secret': self._serialize.url("secret", secret, 'str', skip_quote=True),
            'dnsSuffix': self._serialize.url("self._config.dns_suffix", self._config.dns_suffix, 'str', skip_quote=True),
            'keyName': self._serialize.url("key_name", key_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if key_version is not None:
            query_parameters['keyVersion'] = self._serialize.query("key_version", key_version, 'str')


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(pipeline_response, None, {})

    get_empty.metadata = {'url': '/customuri/{subscriptionId}/{keyName}'}
