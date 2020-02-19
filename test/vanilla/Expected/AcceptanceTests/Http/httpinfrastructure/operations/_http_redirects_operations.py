# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class HttpRedirectsOperations(object):
    """HttpRedirectsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~httpinfrastructure.models
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
    def head300(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Return 300 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})

        # Construct URL
        url = self.head300.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 300]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 300:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    head300.metadata = {'url': '/http/redirect/300'}

    @distributed_trace
    def get300(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> List[str]
        """Return 300 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return:  or list or the result of cls(response)
        :rtype: None or list[str]
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[List[str]]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})

        # Construct URL
        url = self.get300.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 300]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        deserialized = None
        if response.status_code == 300:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            deserialized = self._deserialize('[str]', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get300.metadata = {'url': '/http/redirect/300'}

    @distributed_trace
    def head301(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Return 301 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})

        # Construct URL
        url = self.head301.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 301]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 301:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    head301.metadata = {'url': '/http/redirect/301'}

    @distributed_trace
    def get301(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Return 301 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})

        # Construct URL
        url = self.get301.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 301]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 301:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    get301.metadata = {'url': '/http/redirect/301'}

    @distributed_trace
    def put301(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put true Boolean value in request returns 301.  This request should not be automatically redirected, but should return the received 301 to the caller for evaluation.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})
        boolean_value = True

        # Construct URL
        url = self.put301.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [301]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    put301.metadata = {'url': '/http/redirect/301'}

    @distributed_trace
    def head302(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Return 302 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})

        # Construct URL
        url = self.head302.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 302]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 302:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    head302.metadata = {'url': '/http/redirect/302'}

    @distributed_trace
    def get302(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Return 302 status code and redirect to /http/success/200.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})

        # Construct URL
        url = self.get302.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 302]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 302:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    get302.metadata = {'url': '/http/redirect/302'}

    @distributed_trace
    def patch302(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Patch true Boolean value in request returns 302.  This request should not be automatically redirected, but should return the received 302 to the caller for evaluation.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})
        boolean_value = True

        # Construct URL
        url = self.patch302.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [302]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    patch302.metadata = {'url': '/http/redirect/302'}

    @distributed_trace
    def post303(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Post true Boolean value in request returns 303.  This request should be automatically redirected usign a get, ultimately returning a 200 status code.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})
        boolean_value = True

        # Construct URL
        url = self.post303.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 303]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 303:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    post303.metadata = {'url': '/http/redirect/303'}

    @distributed_trace
    def head307(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Redirect with 307, resulting in a 200 success.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})

        # Construct URL
        url = self.head307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.head(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    head307.metadata = {'url': '/http/redirect/307'}

    @distributed_trace
    def get307(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Redirect get with 307, resulting in a 200 success.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})

        # Construct URL
        url = self.get307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    get307.metadata = {'url': '/http/redirect/307'}

    @distributed_trace
    def options307(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """options redirected with 307, resulting in a 200 after redirect.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})

        # Construct URL
        url = self.options307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.options(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    options307.metadata = {'url': '/http/redirect/307'}

    @distributed_trace
    def put307(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Put redirected with 307, resulting in a 200 after redirect.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})
        boolean_value = True

        # Construct URL
        url = self.put307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    put307.metadata = {'url': '/http/redirect/307'}

    @distributed_trace
    def patch307(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Patch redirected with 307, resulting in a 200 after redirect.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})
        boolean_value = True

        # Construct URL
        url = self.patch307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    patch307.metadata = {'url': '/http/redirect/307'}

    @distributed_trace
    def post307(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Post redirected with 307, resulting in a 200 after redirect.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})
        boolean_value = True

        # Construct URL
        url = self.post307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    post307.metadata = {'url': '/http/redirect/307'}

    @distributed_trace
    def delete307(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete redirected with 307, resulting in a 200 after redirect.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.HttpResponseError
        """
        cls = kwargs.pop('cls', None )  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError})
        boolean_value = True

        # Construct URL
        url = self.delete307.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        if boolean_value is not None:
            body_content = self._serialize.body(boolean_value, 'bool')
        else:
            body_content = None

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 307]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.Error, response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        if response.status_code == 307:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))

        if cls:
          return cls(pipeline_response, None, response_headers)

    delete307.metadata = {'url': '/http/redirect/307'}
