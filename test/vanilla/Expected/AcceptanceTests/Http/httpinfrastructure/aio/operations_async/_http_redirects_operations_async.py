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


class HttpRedirectsOperations:
    """HttpRedirectsOperations async operations.

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

    async def head300(self, *, cls=None, **operation_config):
        """Return 300 status code and redirect to /http/success/200.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head300.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 300]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    head300.metadata = {'url': '/http/redirect/300'}

    async def get300(self, *, cls=None, **operation_config):
        """Return 300 status code and redirect to /http/success/200.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or the result of cls(response)
        :rtype: list[str]
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get300.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 300]:
            raise models.ErrorException(self._deserialize, response)

        header_dict = {}
        deserialized = None
        if response.status_code == 300:
            deserialized = self._deserialize('[str]', response)
            header_dict = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }

        if cls:
            return cls(response, deserialized, header_dict)

        return deserialized
    get300.metadata = {'url': '/http/redirect/300'}

    async def head301(self, *, cls=None, **operation_config):
        """Return 301 status code and redirect to /http/success/200.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head301.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 301]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    head301.metadata = {'url': '/http/redirect/301'}

    async def get301(self, *, cls=None, **operation_config):
        """Return 301 status code and redirect to /http/success/200.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get301.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 301]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    get301.metadata = {'url': '/http/redirect/301'}

    async def put301(self, boolean_value=None, *, cls=None, **operation_config):
        """Put true Boolean value in request returns 301.  This request should not
        be automatically redirected, but should return the received 301 to the
        caller for evaluation.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put301.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [301]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    put301.metadata = {'url': '/http/redirect/301'}

    async def head302(self, *, cls=None, **operation_config):
        """Return 302 status code and redirect to /http/success/200.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head302.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 302]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    head302.metadata = {'url': '/http/redirect/302'}

    async def get302(self, *, cls=None, **operation_config):
        """Return 302 status code and redirect to /http/success/200.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get302.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 302]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    get302.metadata = {'url': '/http/redirect/302'}

    async def patch302(self, boolean_value=None, *, cls=None, **operation_config):
        """Patch true Boolean value in request returns 302.  This request should
        not be automatically redirected, but should return the received 302 to
        the caller for evaluation.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch302.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [302]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    patch302.metadata = {'url': '/http/redirect/302'}

    async def post303(self, boolean_value=None, *, cls=None, **operation_config):
        """Post true Boolean value in request returns 303.  This request should be
        automatically redirected usign a get, ultimately returning a 200 status
        code.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post303.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 303]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    post303.metadata = {'url': '/http/redirect/303'}

    async def head307(self, *, cls=None, **operation_config):
        """Redirect with 307, resulting in a 200 success.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.head307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    head307.metadata = {'url': '/http/redirect/307'}

    async def get307(self, *, cls=None, **operation_config):
        """Redirect get with 307, resulting in a 200 success.

        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.get307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    get307.metadata = {'url': '/http/redirect/307'}

    async def put307(self, boolean_value=None, *, cls=None, **operation_config):
        """Put redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.put307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    put307.metadata = {'url': '/http/redirect/307'}

    async def patch307(self, boolean_value=None, *, cls=None, **operation_config):
        """Patch redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.patch307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    patch307.metadata = {'url': '/http/redirect/307'}

    async def post307(self, boolean_value=None, *, cls=None, **operation_config):
        """Post redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.post307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    post307.metadata = {'url': '/http/redirect/307'}

    async def delete307(self, boolean_value=None, *, cls=None, **operation_config):
        """Delete redirected with 307, resulting in a 200 after redirect.

        :param boolean_value: Simple boolean value true
        :type boolean_value: bool
        :param callable cls: A custom type or function that will be passed the
         direct response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or the result of cls(response)
        :rtype: None
        :raises:
         :class:`ErrorException<httpinfrastructure.models.ErrorException>`
        """
        # Construct URL
        url = self.delete307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters, body_content)
        pipeline_output = await self._client.pipeline.run(request, stream=False, **operation_config)
        response = pipeline_output.http_response

        if response.status_code not in [200, 307]:
            raise models.ErrorException(self._deserialize, response)

        if cls:
            response_headers = {
                'Location': self._deserialize('str', response.headers.get('Location')),
            }
            return cls(response, None, response_headers)
    delete307.metadata = {'url': '/http/redirect/307'}
