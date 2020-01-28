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


class StringOperations:
    """StringOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodystring.models
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
    async def get_null(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, str, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> str:
        """Get null string value value.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_null.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('str', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_null.metadata = {'url': '/string/null'}

    @distributed_trace_async
    async def put_null(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, None, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> None:
        """Set string value null.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        string_body = None

        # Construct URL
        url = self.put_null.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        if string_body is not None:
            body_content = self._serialize.body(string_body, 'str')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_null.metadata = {'url': '/string/null'}

    @distributed_trace_async
    async def get_empty(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, str, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> str:
        """Get empty string value value ''.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_empty.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('str', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_empty.metadata = {'url': '/string/empty'}

    @distributed_trace_async
    async def put_empty(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, None, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> None:
        """Set string value empty ''.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        string_body = ""

        # Construct URL
        url = self.put_empty.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(string_body, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_empty.metadata = {'url': '/string/empty'}

    @distributed_trace_async
    async def get_mbcs(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, str, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> str:
        """Get mbcs string value '啊齄丂狛狜隣郎隣兀﨩ˊ〞〡￤℡㈱‐ー﹡﹢﹫、〓ⅰⅹ⒈€㈠㈩ⅠⅫ！￣ぁんァヶΑ︴АЯаяāɡㄅㄩ─╋︵﹄︻︱︳︴ⅰⅹɑɡ〇〾⿻⺁䜣€'.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_mbcs.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('str', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_mbcs.metadata = {'url': '/string/mbcs'}

    @distributed_trace_async
    async def put_mbcs(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, None, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> None:
        """Set string value mbcs '啊齄丂狛狜隣郎隣兀﨩ˊ〞〡￤℡㈱‐ー﹡﹢﹫、〓ⅰⅹ⒈€㈠㈩ⅠⅫ！￣ぁんァヶΑ︴АЯаяāɡㄅㄩ─╋︵﹄︻︱︳︴ⅰⅹɑɡ〇〾⿻⺁䜣€'.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        string_body = "啊齄丂狛狜隣郎隣兀﨩ˊ〞〡￤℡㈱‐ー﹡﹢﹫、〓ⅰⅹ⒈€㈠㈩ⅠⅫ！￣ぁんァヶΑ︴АЯаяāɡㄅㄩ─╋︵﹄︻︱︳︴ⅰⅹɑɡ〇〾⿻⺁䜣€"

        # Construct URL
        url = self.put_mbcs.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(string_body, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_mbcs.metadata = {'url': '/string/mbcs'}

    @distributed_trace_async
    async def get_whitespace(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, str, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> str:
        """Get string value with leading and trailing whitespace ':code:`<tab>`:code:`<space>`:code:`<space>`Now is the time for all good men to come to the aid of their country:code:`<tab>`:code:`<space>`:code:`<space>`'.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_whitespace.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('str', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_whitespace.metadata = {'url': '/string/whitespace'}

    @distributed_trace_async
    async def put_whitespace(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, None, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> None:
        """Set String value with leading and trailing whitespace ':code:`<tab>`:code:`<space>`:code:`<space>`Now is the time for all good men to come to the aid of their country:code:`<tab>`:code:`<space>`:code:`<space>`'.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        string_body = "    Now is the time for all good men to come to the aid of their country    "

        # Construct URL
        url = self.put_whitespace.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(string_body, 'str')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_whitespace.metadata = {'url': '/string/whitespace'}

    @distributed_trace_async
    async def get_not_provided(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, str, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> str:
        """Get String value when no string value is sent in response payload.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: str or the result of cls(response)
        :rtype: str
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_not_provided.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('str', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_not_provided.metadata = {'url': '/string/notProvided'}

    @distributed_trace_async
    async def get_base64_encoded(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, bytes, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> bytes:
        """Get value that is base64 encoded.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: bytes or the result of cls(response)
        :rtype: bytes
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_base64_encoded.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('base64', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_base64_encoded.metadata = {'url': '/string/base64Encoding'}

    @distributed_trace_async
    async def get_base64_url_encoded(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, bytes, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> bytes:
        """Get value that is base64url encoded.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: bytes or the result of cls(response)
        :rtype: bytes
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_base64_url_encoded.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('base64', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_base64_url_encoded.metadata = {'url': '/string/base64UrlEncoding'}

    @distributed_trace_async
    async def put_base64_url_encoded(
        self,
        string_body: bytes,
        *,
        cls: Optional[Callable[[AsyncHttpResponse, None, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> None:
        """Put value that is base64url encoded.

        FIXME: add operation.summary

        :param string_body: 
        :type string_body: bytes
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.put_base64_url_encoded.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(string_body, 'base64')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    put_base64_url_encoded.metadata = {'url': '/string/base64UrlEncoding'}

    @distributed_trace_async
    async def get_null_base64_url_encoded(
        self,
        cls: Optional[Callable[[AsyncHttpResponse, bytes, Dict[str, Any]], Any]] = None,
        **kwargs: Any
    ) -> bytes:
        """Get null value that is expected to be base64url encoded.

        FIXME: add operation.summary

        :param callable cls: A custom type or function that will be passed the direct response
        :return: bytes or the result of cls(response)
        :rtype: bytes
        :raises: ~bodystring.models.ErrorException:
        """
        error_map = kwargs.pop('error_map', {})

        # Construct URL
        url = self.get_null_base64_url_encoded.metadata['url']

        # Construct parameters
        query_parameters = {}


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.ErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('base64', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_null_base64_url_encoded.metadata = {'url': '/string/nullBase64UrlEncoding'}
