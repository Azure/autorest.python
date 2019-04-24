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


class HeaderOperations(object):
    """HeaderOperations operations.

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

    def param_existing_key(
            self,  **kwargs):
        """Send a post request with header value "User-Agent": "overwrite".

        :param user_agent: Send a post request with header value "User-Agent":
         "overwrite"
        :type user_agent: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_existing_key.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['User-Agent'] = self._serialize.header("user_agent", user_agent, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_existing_key.metadata = {'url': '/header/param/existingkey'}

    def response_existing_key(
            self,  **kwargs):
        """Get a response with header value "User-Agent": "overwrite".

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_existing_key.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_existing_key.metadata = {'url': '/header/response/existingkey'}

    def param_protected_key(
            self,  **kwargs):
        """Send a post request with header value "Content-Type": "text/html".

        :param content_type: Send a post request with header value
         "Content-Type": "text/html"
        :type content_type: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_protected_key.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_protected_key.metadata = {'url': '/header/param/protectedkey'}

    def response_protected_key(
            self,  **kwargs):
        """Get a response with header value "Content-Type": "text/html".

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_protected_key.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_protected_key.metadata = {'url': '/header/response/protectedkey'}

    def param_integer(
            self,  **kwargs):
        """Send a post request with header values "scenario": "positive", "value":
        1 or "scenario": "negative", "value": -2 .

        :param scenario: Send a post request with header values "scenario":
         "positive" or "negative"
        :type scenario: str
        :param value: Send a post request with header values 1 or -2
        :type value: int
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_integer.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        header_parameters['value'] = self._serialize.header("value", value, 'int')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_integer.metadata = {'url': '/header/param/prim/integer'}

    def response_integer(
            self,  **kwargs):
        """Get a response with header value "value": 1 or -2.

        :param scenario: Send a post request with header values "scenario":
         "positive" or "negative"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_integer.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_integer.metadata = {'url': '/header/response/prim/integer'}

    def param_long(
            self,  **kwargs):
        """Send a post request with header values "scenario": "positive", "value":
        105 or "scenario": "negative", "value": -2 .

        :param scenario: Send a post request with header values "scenario":
         "positive" or "negative"
        :type scenario: str
        :param value: Send a post request with header values 105 or -2
        :type value: long
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_long.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        header_parameters['value'] = self._serialize.header("value", value, 'long')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_long.metadata = {'url': '/header/param/prim/long'}

    def response_long(
            self,  **kwargs):
        """Get a response with header value "value": 105 or -2.

        :param scenario: Send a post request with header values "scenario":
         "positive" or "negative"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_long.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_long.metadata = {'url': '/header/response/prim/long'}

    def param_float(
            self,  **kwargs):
        """Send a post request with header values "scenario": "positive", "value":
        0.07 or "scenario": "negative", "value": -3.0.

        :param scenario: Send a post request with header values "scenario":
         "positive" or "negative"
        :type scenario: str
        :param value: Send a post request with header values 0.07 or -3.0
        :type value: float
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_float.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        header_parameters['value'] = self._serialize.header("value", value, 'float')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_float.metadata = {'url': '/header/param/prim/float'}

    def response_float(
            self,  **kwargs):
        """Get a response with header value "value": 0.07 or -3.0.

        :param scenario: Send a post request with header values "scenario":
         "positive" or "negative"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_float.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_float.metadata = {'url': '/header/response/prim/float'}

    def param_double(
            self,  **kwargs):
        """Send a post request with header values "scenario": "positive", "value":
        7e120 or "scenario": "negative", "value": -3.0.

        :param scenario: Send a post request with header values "scenario":
         "positive" or "negative"
        :type scenario: str
        :param value: Send a post request with header values 7e120 or -3.0
        :type value: float
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_double.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        header_parameters['value'] = self._serialize.header("value", value, 'float')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_double.metadata = {'url': '/header/param/prim/double'}

    def response_double(
            self,  **kwargs):
        """Get a response with header value "value": 7e120 or -3.0.

        :param scenario: Send a post request with header values "scenario":
         "positive" or "negative"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_double.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_double.metadata = {'url': '/header/response/prim/double'}

    def param_bool(
            self,  **kwargs):
        """Send a post request with header values "scenario": "true", "value":
        true or "scenario": "false", "value": false.

        :param scenario: Send a post request with header values "scenario":
         "true" or "false"
        :type scenario: str
        :param value: Send a post request with header values true or false
        :type value: bool
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_bool.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        header_parameters['value'] = self._serialize.header("value", value, 'bool')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_bool.metadata = {'url': '/header/param/prim/bool'}

    def response_bool(
            self,  **kwargs):
        """Get a response with header value "value": true or false.

        :param scenario: Send a post request with header values "scenario":
         "true" or "false"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_bool.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_bool.metadata = {'url': '/header/response/prim/bool'}

    def param_string(
            self, scenario, value=None, **kwargs):
        """Send a post request with header values "scenario": "valid", "value":
        "The quick brown fox jumps over the lazy dog" or "scenario": "null",
        "value": null or "scenario": "empty", "value": "".

        :param scenario: Send a post request with header values "scenario":
         "valid" or "null" or "empty"
        :type scenario: str
        :param value: Send a post request with header values "The quick brown
         fox jumps over the lazy dog" or null or ""
        :type value: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_string.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        if value is not None:
            header_parameters['value'] = self._serialize.header("value", value, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_string.metadata = {'url': '/header/param/prim/string'}

    def response_string(
            self,  **kwargs):
        """Get a response with header values "The quick brown fox jumps over the
        lazy dog" or null or "".

        :param scenario: Send a post request with header values "scenario":
         "valid" or "null" or "empty"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_string.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_string.metadata = {'url': '/header/response/prim/string'}

    def param_date(
            self,  **kwargs):
        """Send a post request with header values "scenario": "valid", "value":
        "2010-01-01" or "scenario": "min", "value": "0001-01-01".

        :param scenario: Send a post request with header values "scenario":
         "valid" or "min"
        :type scenario: str
        :param value: Send a post request with header values "2010-01-01" or
         "0001-01-01"
        :type value: date
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        header_parameters['value'] = self._serialize.header("value", value, 'date')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_date.metadata = {'url': '/header/param/prim/date'}

    def response_date(
            self,  **kwargs):
        """Get a response with header values "2010-01-01" or "0001-01-01".

        :param scenario: Send a post request with header values "scenario":
         "valid" or "min"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_date.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_date.metadata = {'url': '/header/response/prim/date'}

    def param_datetime(
            self,  **kwargs):
        """Send a post request with header values "scenario": "valid", "value":
        "2010-01-01T12:34:56Z" or "scenario": "min", "value":
        "0001-01-01T00:00:00Z".

        :param scenario: Send a post request with header values "scenario":
         "valid" or "min"
        :type scenario: str
        :param value: Send a post request with header values
         "2010-01-01T12:34:56Z" or "0001-01-01T00:00:00Z"
        :type value: datetime
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_datetime.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        header_parameters['value'] = self._serialize.header("value", value, 'iso-8601')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_datetime.metadata = {'url': '/header/param/prim/datetime'}

    def response_datetime(
            self,  **kwargs):
        """Get a response with header values "2010-01-01T12:34:56Z" or
        "0001-01-01T00:00:00Z".

        :param scenario: Send a post request with header values "scenario":
         "valid" or "min"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_datetime.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_datetime.metadata = {'url': '/header/response/prim/datetime'}

    def param_datetime_rfc1123(
            self, scenario, value=None, **kwargs):
        """Send a post request with header values "scenario": "valid", "value":
        "Wed, 01 Jan 2010 12:34:56 GMT" or "scenario": "min", "value": "Mon, 01
        Jan 0001 00:00:00 GMT".

        :param scenario: Send a post request with header values "scenario":
         "valid" or "min"
        :type scenario: str
        :param value: Send a post request with header values "Wed, 01 Jan 2010
         12:34:56 GMT" or "Mon, 01 Jan 0001 00:00:00 GMT"
        :type value: datetime
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_datetime_rfc1123.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        if value is not None:
            header_parameters['value'] = self._serialize.header("value", value, 'rfc-1123')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_datetime_rfc1123.metadata = {'url': '/header/param/prim/datetimerfc1123'}

    def response_datetime_rfc1123(
            self,  **kwargs):
        """Get a response with header values "Wed, 01 Jan 2010 12:34:56 GMT" or
        "Mon, 01 Jan 0001 00:00:00 GMT".

        :param scenario: Send a post request with header values "scenario":
         "valid" or "min"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_datetime_rfc1123.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_datetime_rfc1123.metadata = {'url': '/header/response/prim/datetimerfc1123'}

    def param_duration(
            self,  **kwargs):
        """Send a post request with header values "scenario": "valid", "value":
        "P123DT22H14M12.011S".

        :param scenario: Send a post request with header values "scenario":
         "valid"
        :type scenario: str
        :param value: Send a post request with header values
         "P123DT22H14M12.011S"
        :type value: timedelta
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_duration.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        header_parameters['value'] = self._serialize.header("value", value, 'duration')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_duration.metadata = {'url': '/header/param/prim/duration'}

    def response_duration(
            self,  **kwargs):
        """Get a response with header values "P123DT22H14M12.011S".

        :param scenario: Send a post request with header values "scenario":
         "valid"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_duration.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_duration.metadata = {'url': '/header/response/prim/duration'}

    def param_byte(
            self,  **kwargs):
        """Send a post request with header values "scenario": "valid", "value":
        "啊齄丂狛狜隣郎隣兀﨩".

        :param scenario: Send a post request with header values "scenario":
         "valid"
        :type scenario: str
        :param value: Send a post request with header values "啊齄丂狛狜隣郎隣兀﨩"
        :type value: bytearray
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_byte.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        header_parameters['value'] = self._serialize.header("value", value, 'bytearray')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_byte.metadata = {'url': '/header/param/prim/byte'}

    def response_byte(
            self,  **kwargs):
        """Get a response with header values "啊齄丂狛狜隣郎隣兀﨩".

        :param scenario: Send a post request with header values "scenario":
         "valid"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_byte.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_byte.metadata = {'url': '/header/response/prim/byte'}

    def param_enum(
            self, scenario, value=None, **kwargs):
        """Send a post request with header values "scenario": "valid", "value":
        "GREY" or "scenario": "null", "value": null.

        :param scenario: Send a post request with header values "scenario":
         "valid" or "null" or "empty"
        :type scenario: str
        :param value: Send a post request with header values 'GREY'. Possible
         values include: 'White', 'black', 'GREY'
        :type value: str or ~header.models.GreyscaleColors
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.param_enum.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')
        if value is not None:
            header_parameters['value'] = self._serialize.header("value", value, 'GreyscaleColors')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    param_enum.metadata = {'url': '/header/param/prim/enum'}

    def response_enum(
            self,  **kwargs):
        """Get a response with header values "GREY" or null.

        :param scenario: Send a post request with header values "scenario":
         "valid" or "null" or "empty"
        :type scenario: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.response_enum.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)
        header_parameters['scenario'] = self._serialize.header("scenario", scenario, 'str')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    response_enum.metadata = {'url': '/header/response/prim/enum'}

    def custom_request_id(
            self,  **kwargs):
        """Send x-ms-client-request-id = 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0 in
        the header of the request.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<header.models.ErrorException>`
        """
        # Construct URL
        url = self.custom_request_id.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    custom_request_id.metadata = {'url': '/header/custom/x-ms-client-request-id/9C4D50EE-2D56-4CD3-8152-34347DC9F2B0'}
