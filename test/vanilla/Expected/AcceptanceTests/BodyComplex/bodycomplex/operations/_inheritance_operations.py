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


from .. import models


class InheritanceOperations(object):
    """InheritanceOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_valid(self, cls=None, **operation_config):
        """Get complex types that extend others.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Siamese or the result of cls(response)
        :rtype: ~bodycomplex.models.Siamese
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_valid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Siamese', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_valid.metadata = {'url': '/complex/inheritance/valid'}

    def put_valid(self, complex_body, cls=None, **operation_config):
        """Put complex types that extend others.

        :param complex_body: Please put a siamese with id=2, name="Siameee",
         color=green, breed=persion, which hates 2 dogs, the 1st one named
         "Potato" with id=1 and food="tomato", and the 2nd one named "Tomato"
         with id=-1 and food="french fries".
        :type complex_body: ~bodycomplex.models.Siamese
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        body_content = self._serialize.body(complex_body, 'Siamese')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {}
            return cls(response, None, response_headers)
    put_valid.metadata = {'url': '/complex/inheritance/valid'}
