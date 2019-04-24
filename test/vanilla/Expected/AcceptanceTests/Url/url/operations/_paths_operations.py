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


class PathsOperations(object):
    """PathsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar byte_path: '' as byte array
    :ivar date_path: '2012-01-01' as date. Constant value: "2012-01-01".
    :ivar date_time_path: '2012-01-01T01:01:01Z' as date-time. Constant value: "2012-01-01T01:01:01Z".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config
        self.byte_path = bytearray("", encoding="utf-8")
        self.date_path = "2012-01-01"
        self.date_time_path = "2012-01-01T01:01:01Z"

    def get_boolean_true(
            self,  **kwargs):
        """Get true Boolean value on path.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        bool_path = True

        # Construct URL
        url = self.get_boolean_true.metadata['url']
        path_format_arguments = {
            'boolPath': self._serialize.url("bool_path", bool_path, 'bool')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_boolean_true.metadata = {'url': '/paths/bool/true/{boolPath}'}

    def get_boolean_false(
            self,  **kwargs):
        """Get false Boolean value on path.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        bool_path = False

        # Construct URL
        url = self.get_boolean_false.metadata['url']
        path_format_arguments = {
            'boolPath': self._serialize.url("bool_path", bool_path, 'bool')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_boolean_false.metadata = {'url': '/paths/bool/false/{boolPath}'}

    def get_int_one_million(
            self,  **kwargs):
        """Get '1000000' integer value.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        int_path = 1000000

        # Construct URL
        url = self.get_int_one_million.metadata['url']
        path_format_arguments = {
            'intPath': self._serialize.url("int_path", int_path, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_int_one_million.metadata = {'url': '/paths/int/1000000/{intPath}'}

    def get_int_negative_one_million(
            self,  **kwargs):
        """Get '-1000000' integer value.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        int_path = -1000000

        # Construct URL
        url = self.get_int_negative_one_million.metadata['url']
        path_format_arguments = {
            'intPath': self._serialize.url("int_path", int_path, 'int')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_int_negative_one_million.metadata = {'url': '/paths/int/-1000000/{intPath}'}

    def get_ten_billion(
            self,  **kwargs):
        """Get '10000000000' 64 bit integer value.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        long_path = 10000000000

        # Construct URL
        url = self.get_ten_billion.metadata['url']
        path_format_arguments = {
            'longPath': self._serialize.url("long_path", long_path, 'long')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_ten_billion.metadata = {'url': '/paths/long/10000000000/{longPath}'}

    def get_negative_ten_billion(
            self,  **kwargs):
        """Get '-10000000000' 64 bit integer value.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        long_path = -10000000000

        # Construct URL
        url = self.get_negative_ten_billion.metadata['url']
        path_format_arguments = {
            'longPath': self._serialize.url("long_path", long_path, 'long')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    get_negative_ten_billion.metadata = {'url': '/paths/long/-10000000000/{longPath}'}

    def float_scientific_positive(
            self,  **kwargs):
        """Get '1.034E+20' numeric value.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        float_path = 1.034E+20

        # Construct URL
        url = self.float_scientific_positive.metadata['url']
        path_format_arguments = {
            'floatPath': self._serialize.url("float_path", float_path, 'float')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    float_scientific_positive.metadata = {'url': '/paths/float/1.034E+20/{floatPath}'}

    def float_scientific_negative(
            self,  **kwargs):
        """Get '-1.034E-20' numeric value.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        float_path = -1.034E-20

        # Construct URL
        url = self.float_scientific_negative.metadata['url']
        path_format_arguments = {
            'floatPath': self._serialize.url("float_path", float_path, 'float')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    float_scientific_negative.metadata = {'url': '/paths/float/-1.034E-20/{floatPath}'}

    def double_decimal_positive(
            self,  **kwargs):
        """Get '9999999.999' numeric value.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        double_path = 9999999.999

        # Construct URL
        url = self.double_decimal_positive.metadata['url']
        path_format_arguments = {
            'doublePath': self._serialize.url("double_path", double_path, 'float')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    double_decimal_positive.metadata = {'url': '/paths/double/9999999.999/{doublePath}'}

    def double_decimal_negative(
            self,  **kwargs):
        """Get '-9999999.999' numeric value.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        double_path = -9999999.999

        # Construct URL
        url = self.double_decimal_negative.metadata['url']
        path_format_arguments = {
            'doublePath': self._serialize.url("double_path", double_path, 'float')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    double_decimal_negative.metadata = {'url': '/paths/double/-9999999.999/{doublePath}'}

    def string_unicode(
            self,  **kwargs):
        """Get '啊齄丂狛狜隣郎隣兀﨩' multi-byte string value.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        string_path = "啊齄丂狛狜隣郎隣兀﨩"

        # Construct URL
        url = self.string_unicode.metadata['url']
        path_format_arguments = {
            'stringPath': self._serialize.url("string_path", string_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    string_unicode.metadata = {'url': '/paths/string/unicode/{stringPath}'}

    def string_url_encoded(
            self,  **kwargs):
        """Get 'begin!*'();:@ &=+$,/?#[]end.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        string_path = "begin!*'();:@ &=+$,/?#[]end"

        # Construct URL
        url = self.string_url_encoded.metadata['url']
        path_format_arguments = {
            'stringPath': self._serialize.url("string_path", string_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    string_url_encoded.metadata = {'url': '/paths/string/begin%21%2A%27%28%29%3B%3A%40%20%26%3D%2B%24%2C%2F%3F%23%5B%5Dend/{stringPath}'}

    def string_empty(
            self,  **kwargs):
        """Get ''.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        string_path = ""

        # Construct URL
        url = self.string_empty.metadata['url']
        path_format_arguments = {
            'stringPath': self._serialize.url("string_path", string_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    string_empty.metadata = {'url': '/paths/string/empty/{stringPath}'}

    def string_null(
            self,  **kwargs):
        """Get null (should throw).

        :param string_path: null string value
        :type string_path: str
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.string_null.metadata['url']
        path_format_arguments = {
            'stringPath': self._serialize.url("string_path", string_path, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [400]:
            raise models.ErrorException(self._deserialize, response)

    string_null.metadata = {'url': '/paths/string/null/{stringPath}'}

    def enum_valid(
            self,  **kwargs):
        """Get using uri with 'green color' in path parameter.

        :param enum_path: send the value green. Possible values include: 'red
         color', 'green color', 'blue color'
        :type enum_path: str or ~url.models.UriColor
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.enum_valid.metadata['url']
        path_format_arguments = {
            'enumPath': self._serialize.url("enum_path", enum_path, 'UriColor')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    enum_valid.metadata = {'url': '/paths/enum/green%20color/{enumPath}'}

    def enum_null(
            self,  **kwargs):
        """Get null (should throw on the client before the request is sent on
        wire).

        :param enum_path: send null should throw. Possible values include:
         'red color', 'green color', 'blue color'
        :type enum_path: str or ~url.models.UriColor
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.enum_null.metadata['url']
        path_format_arguments = {
            'enumPath': self._serialize.url("enum_path", enum_path, 'UriColor')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [400]:
            raise models.ErrorException(self._deserialize, response)

    enum_null.metadata = {'url': '/paths/string/null/{enumPath}'}

    def byte_multi_byte(
            self,  **kwargs):
        """Get '啊齄丂狛狜隣郎隣兀﨩' multibyte value as utf-8 encoded byte array.

        :param byte_path: '啊齄丂狛狜隣郎隣兀﨩' multibyte value as utf-8 encoded byte
         array
        :type byte_path: bytearray
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.byte_multi_byte.metadata['url']
        path_format_arguments = {
            'bytePath': self._serialize.url("byte_path", byte_path, 'bytearray')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    byte_multi_byte.metadata = {'url': '/paths/byte/multibyte/{bytePath}'}

    def byte_empty(
            self,  **kwargs):
        """Get '' as byte array.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.byte_empty.metadata['url']
        path_format_arguments = {
            'bytePath': self._serialize.url("self.byte_path", self.byte_path, 'bytearray')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    byte_empty.metadata = {'url': '/paths/byte/empty/{bytePath}'}

    def byte_null(
            self,  **kwargs):
        """Get null as byte array (should throw).

        :param byte_path: null as byte array (should throw)
        :type byte_path: bytearray
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.byte_null.metadata['url']
        path_format_arguments = {
            'bytePath': self._serialize.url("byte_path", byte_path, 'bytearray')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [400]:
            raise models.ErrorException(self._deserialize, response)

    byte_null.metadata = {'url': '/paths/byte/null/{bytePath}'}

    def date_valid(
            self,  **kwargs):
        """Get '2012-01-01' as date.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.date_valid.metadata['url']
        path_format_arguments = {
            'datePath': self._serialize.url("self.date_path", self.date_path, 'date')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    date_valid.metadata = {'url': '/paths/date/2012-01-01/{datePath}'}

    def date_null(
            self,  **kwargs):
        """Get null as date - this should throw or be unusable on the client side,
        depending on date representation.

        :param date_path: null as date (should throw)
        :type date_path: date
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.date_null.metadata['url']
        path_format_arguments = {
            'datePath': self._serialize.url("date_path", date_path, 'date')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [400]:
            raise models.ErrorException(self._deserialize, response)

    date_null.metadata = {'url': '/paths/date/null/{datePath}'}

    def date_time_valid(
            self,  **kwargs):
        """Get '2012-01-01T01:01:01Z' as date-time.

        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.date_time_valid.metadata['url']
        path_format_arguments = {
            'dateTimePath': self._serialize.url("self.date_time_path", self.date_time_path, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    date_time_valid.metadata = {'url': '/paths/datetime/2012-01-01T01%3A01%3A01Z/{dateTimePath}'}

    def date_time_null(
            self,  **kwargs):
        """Get null as date-time, should be disallowed or throw depending on
        representation of date-time.

        :param date_time_path: null as date-time
        :type date_time_path: datetime
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.date_time_null.metadata['url']
        path_format_arguments = {
            'dateTimePath': self._serialize.url("date_time_path", date_time_path, 'iso-8601')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [400]:
            raise models.ErrorException(self._deserialize, response)

    date_time_null.metadata = {'url': '/paths/datetime/null/{dateTimePath}'}

    def base64_url(
            self,  **kwargs):
        """Get 'lorem' encoded value as 'bG9yZW0' (base64url).

        :param base64_url_path: base64url encoded value
        :type base64_url_path: bytes
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.base64_url.metadata['url']
        path_format_arguments = {
            'base64UrlPath': self._serialize.url("base64_url_path", base64_url_path, 'base64')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    base64_url.metadata = {'url': '/paths/string/bG9yZW0/{base64UrlPath}'}

    def array_csv_in_path(
            self,  **kwargs):
        """Get an array of string ['ArrayPath1', 'begin!*'();:@ &=+$,/?#[]end' ,
        null, ''] using the csv-array format.

        :param array_path: an array of string ['ArrayPath1', 'begin!*'();:@
         &=+$,/?#[]end' , null, ''] using the csv-array format
        :type array_path: list[str]
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.array_csv_in_path.metadata['url']
        path_format_arguments = {
            'arrayPath': self._serialize.url("array_path", array_path, '[str]', div=',')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    array_csv_in_path.metadata = {'url': '/paths/array/ArrayPath1%2cbegin%21%2A%27%28%29%3B%3A%40%20%26%3D%2B%24%2C%2F%3F%23%5B%5Dend%2c%2c/{arrayPath}'}

    def unix_time_url(
            self,  **kwargs):
        """Get the date 2016-04-13 encoded value as '1460505600' (Unix time).

        :param unix_time_url_path: Unix time encoded value
        :type unix_time_url_path: datetime
        :return: None
        :rtype: None
        :raises: :class:`ErrorException<url.models.ErrorException>`
        """
        # Construct URL
        url = self.unix_time_url.metadata['url']
        path_format_arguments = {
            'unixTimeUrlPath': self._serialize.url("unix_time_url_path", unix_time_url_path, 'unix-time')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

    unix_time_url.metadata = {'url': '/paths/int/1460505600/{unixTimeUrlPath}'}
