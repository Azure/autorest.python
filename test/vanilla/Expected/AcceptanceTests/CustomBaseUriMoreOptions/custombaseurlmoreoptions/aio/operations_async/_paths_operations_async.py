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


class PathsOperations:
    """PathsOperations async operations.

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

    async def get_empty(
            self, vault, secret, key_name, key_version="v1", **kwargs):
        """Get a 200 to test a valid base uri.

        :param vault: The vault name, e.g. https://myvault
        :type vault: str
        :param secret: Secret value.
        :type secret: str
        :param key_name: The key name with value 'key1'.
        :type key_name: str
        :param key_version: The key version. Default value 'v1'.
        :type key_version: str
        :return: None
        :rtype: None
        :raises:
         :class:`ErrorException<custombaseurlmoreoptions.models.ErrorException>`
        """
        # Construct URL
        url = self.get_empty.metadata['url']
        path_format_arguments = {
            'vault': self._serialize.url("vault", vault, 'str', skip_quote=True),
            'secret': self._serialize.url("secret", secret, 'str', skip_quote=True),
            'dnsSuffix': self._serialize.url("self._config.dns_suffix", self._config.dns_suffix, 'str', skip_quote=True),
            'keyName': self._serialize.url("key_name", key_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if key_version is not None:
            query_parameters['keyVersion'] = self._serialize.query("key_version", key_version, 'str')

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_empty.metadata = {'url': '/customuri/{subscriptionId}/{keyName}'}
