# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ...operations._operations import (
    build_pets_create_ap_in_properties_request,
    build_pets_create_ap_in_properties_with_ap_string_request,
    build_pets_create_ap_object_request,
    build_pets_create_ap_string_request,
    build_pets_create_ap_true_request,
    build_pets_create_cat_ap_true_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PetsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~additionalpropertiesversiontolerant.aio.AdditionalPropertiesClient`'s
        :attr:`pets` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_ap_true(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @overload
    async def create_ap_true(
        self, create_parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @distributed_trace_async
    async def create_ap_true(self, create_parameters: Union[JSON, IO], **kwargs: Any) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        request = build_pets_create_ap_true_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def create_cat_ap_true(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "friendly": bool,  # Optional.
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "friendly": bool,  # Optional.
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @overload
    async def create_cat_ap_true(
        self, create_parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "friendly": bool,  # Optional.
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @distributed_trace_async
    async def create_cat_ap_true(self, create_parameters: Union[JSON, IO], **kwargs: Any) -> JSON:
        """Create a CatAPTrue which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "friendly": bool,  # Optional.
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        request = build_pets_create_cat_ap_true_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def create_ap_object(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @overload
    async def create_ap_object(
        self, create_parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @distributed_trace_async
    async def create_ap_object(self, create_parameters: Union[JSON, IO], **kwargs: Any) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        request = build_pets_create_ap_object_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def create_ap_string(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @overload
    async def create_ap_string(
        self, create_parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @distributed_trace_async
    async def create_ap_string(self, create_parameters: Union[JSON, IO], **kwargs: Any) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        request = build_pets_create_ap_string_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def create_ap_in_properties(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @overload
    async def create_ap_in_properties(
        self, create_parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @distributed_trace_async
    async def create_ap_in_properties(self, create_parameters: Union[JSON, IO], **kwargs: Any) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        request = build_pets_create_ap_in_properties_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)

    @overload
    async def create_ap_in_properties_with_ap_string(
        self, create_parameters: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                create_parameters = {
                    "@odata.location": "str",  # Required.
                    "additionalProperties": {
                        "str": 0.0  # Optional. Dictionary of :code:`<number>`.
                    },
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }

                # response body for status code(s): 200
                response.json() == {
                    "@odata.location": "str",  # Required.
                    "additionalProperties": {
                        "str": 0.0  # Optional. Dictionary of :code:`<number>`.
                    },
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @overload
    async def create_ap_in_properties_with_ap_string(
        self, create_parameters: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Required.
        :type create_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "@odata.location": "str",  # Required.
                    "additionalProperties": {
                        "str": 0.0  # Optional. Dictionary of :code:`<number>`.
                    },
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """

    @distributed_trace_async
    async def create_ap_in_properties_with_ap_string(self, create_parameters: Union[JSON, IO], **kwargs: Any) -> JSON:
        """Create a Pet which contains more properties than what is defined.

        :param create_parameters: Is either a model type or a IO type. Required.
        :type create_parameters: JSON or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :return: JSON object
        :rtype: JSON
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "@odata.location": "str",  # Required.
                    "additionalProperties": {
                        "str": 0.0  # Optional. Dictionary of :code:`<number>`.
                    },
                    "id": 0,  # Required.
                    "name": "str",  # Optional.
                    "status": bool  # Optional.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[JSON]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(create_parameters, (IO, bytes)):
            _content = create_parameters
        else:
            _json = create_parameters

        request = build_pets_create_ap_in_properties_with_ap_string_request(
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, cast(JSON, deserialized), {})

        return cast(JSON, deserialized)
