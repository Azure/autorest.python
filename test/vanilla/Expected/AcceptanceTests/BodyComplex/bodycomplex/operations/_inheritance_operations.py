# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.exceptions import map_error
from azure.core.tracing.decorator import distributed_trace
from msrest.serialization import Model

from .. import models


class InheritanceOperations(object):
    """InheritanceOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodycomplex.models
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
    @distributed_trace
    def get_valid(self, cls=None, **kwargs):
        # type: (Optional[Any], **Any) -> "Siamese"
        """Get complex types that extend others.

        FIXME: add operation.summary


        :param callable cls: A custom type or function that will be passed the direct response
        :return: Siamese or the result of cls(response)
        :rtype: ~bodycomplex.models.Siamese
        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('Siamese', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_valid.metadata = {'url': '/complex/inheritance/valid'}

    @distributed_trace
    def put_valid(self, complex_body, cls=None, **kwargs):
        # type: ("Siamese", Optional[Any], **Any) -> None
        """Put complex types that extend others.

        FIXME: add operation.summary


        :param complex_body: Please put a siamese with id=2, name="Siameee", color=green, breed=persion, which hates 2 dogs, the 1st one named "Potato" with id=1 and food="tomato", and the 2nd one named "Tomato" with id=-1 and food="french fries".
        :type complex_body: ~bodycomplex.models.Siamese
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None

        :raises: ~bodycomplex.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(complex_body, 'Siamese')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_valid.metadata = {'url': '/complex/inheritance/valid'}

