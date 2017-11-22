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

from msrest.pipeline import ClientRawResponse

from .. import models


class PolymorphismOperations(object):
    """PolymorphismOperations operations.

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

        self.config = config

    def get_valid(
            self, custom_headers=None, raw=False, **operation_config):
        """Get complex types that are polymorphic.

        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Fish or ClientRawResponse if raw=true
        :rtype: ~fixtures.acceptancetestsbodycomplex.models.Fish or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = '/complex/polymorphism/valid'

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('Fish', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def put_valid(
            self, complex_body, custom_headers=None, raw=False, **operation_config):
        """Put complex types that are polymorphic.

        :param complex_body: Please put a salmon that looks like this:
         {
         'fishtype':'Salmon',
         'location':'alaska',
         'iswild':true,
         'species':'king',
         'length':1.0,
         'siblings':[
         {
         'fishtype':'Shark',
         'age':6,
         'birthday': '2012-01-05T01:00:00Z',
         'length':20.0,
         'species':'predator',
         },
         {
         'fishtype':'Sawshark',
         'age':105,
         'birthday': '1900-01-05T01:00:00Z',
         'length':10.0,
         'picture': new Buffer([255, 255, 255, 255, 254]).toString('base64'),
         'species':'dangerous',
         },
         {
         'fishtype': 'goblin',
         'age': 1,
         'birthday': '2015-08-08T00:00:00Z',
         'length': 30.0,
         'species': 'scary',
         'jawsize': 5
         }
         ]
         };
        :type complex_body: ~fixtures.acceptancetestsbodycomplex.models.Fish
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = '/complex/polymorphism/valid'

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'Fish')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def put_valid_missing_required(
            self, complex_body, custom_headers=None, raw=False, **operation_config):
        """Put complex types that are polymorphic, attempting to omit required
        'birthday' field - the request should not be allowed from the client.

        :param complex_body: Please attempt put a sawshark that looks like
         this, the client should not allow this data to be sent:
         {
         "fishtype": "sawshark",
         "species": "snaggle toothed",
         "length": 18.5,
         "age": 2,
         "birthday": "2013-06-01T01:00:00Z",
         "location": "alaska",
         "picture": base64(FF FF FF FF FE),
         "siblings": [
         {
         "fishtype": "shark",
         "species": "predator",
         "birthday": "2012-01-05T01:00:00Z",
         "length": 20,
         "age": 6
         },
         {
         "fishtype": "sawshark",
         "species": "dangerous",
         "picture": base64(FF FF FF FF FE),
         "length": 10,
         "age": 105
         }
         ]
         }
        :type complex_body: ~fixtures.acceptancetestsbodycomplex.models.Fish
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorException<fixtures.acceptancetestsbodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = '/complex/polymorphism/missingrequired/invalid'

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'Fish')

        # Construct and send request
        request = self._client.put(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
