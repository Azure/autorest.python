# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar, cast

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

from ..._operations._operations import (
    build_get_cat_request,
    build_get_feline_request,
    build_get_horse_request,
    build_get_kitten_request,
    build_get_pet_request,
    build_put_cat_request,
    build_put_feline_request,
    build_put_horse_request,
    build_put_kitten_request,
    build_put_pet_request,
)
from .._vendor import MixinABC

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class MultipleInheritanceServiceClientOperationsMixin(MixinABC):
    @distributed_trace_async
    async def get_horse(self, **kwargs: Any) -> JSONType:
        """Get a horse with name 'Fred' and isAShowHorse true.

        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "isAShowHorse": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]

        request = build_get_horse_request()
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
            return cls(pipeline_response, cast(JSONType, deserialized), {})

        return cast(JSONType, deserialized)

    @distributed_trace_async
    async def put_horse(self, horse: JSONType, **kwargs: Any) -> str:
        """Put a horse with name 'General' and isAShowHorse false.

        :param horse: Put a horse with name 'General' and isAShowHorse false.
        :type horse: JSONType
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                horse = {
                    "isAShowHorse": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = horse

        request = build_put_horse_request(
            content_type=content_type,
            json=_json,
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @distributed_trace_async
    async def get_pet(self, **kwargs: Any) -> JSONType:
        """Get a pet with name 'Peanut'.

        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]

        request = build_get_pet_request()
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
            return cls(pipeline_response, cast(JSONType, deserialized), {})

        return cast(JSONType, deserialized)

    @distributed_trace_async
    async def put_pet(self, pet: JSONType, **kwargs: Any) -> str:
        """Put a pet with name 'Butter'.

        :param pet: Put a pet with name 'Butter'.
        :type pet: JSONType
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                pet = {
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = pet

        request = build_put_pet_request(
            content_type=content_type,
            json=_json,
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @distributed_trace_async
    async def get_feline(self, **kwargs: Any) -> JSONType:
        """Get a feline where meows and hisses are true.

        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "hisses": bool,  # Optional.
                    "meows": bool  # Optional.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]

        request = build_get_feline_request()
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
            return cls(pipeline_response, cast(JSONType, deserialized), {})

        return cast(JSONType, deserialized)

    @distributed_trace_async
    async def put_feline(self, feline: JSONType, **kwargs: Any) -> str:
        """Put a feline who hisses and doesn't meow.

        :param feline: Put a feline who hisses and doesn't meow.
        :type feline: JSONType
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                feline = {
                    "hisses": bool,  # Optional.
                    "meows": bool  # Optional.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = feline

        request = build_put_feline_request(
            content_type=content_type,
            json=_json,
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @distributed_trace_async
    async def get_cat(self, **kwargs: Any) -> JSONType:
        """Get a cat with name 'Whiskers' where likesMilk, meows, and hisses is true.

        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "hisses": bool,  # Optional.
                    "likesMilk": bool,  # Optional.
                    "meows": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]

        request = build_get_cat_request()
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
            return cls(pipeline_response, cast(JSONType, deserialized), {})

        return cast(JSONType, deserialized)

    @distributed_trace_async
    async def put_cat(self, cat: JSONType, **kwargs: Any) -> str:
        """Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.

        :param cat: Put a cat with name 'Boots' where likesMilk and hisses is false, meows is true.
        :type cat: JSONType
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                cat = {
                    "hisses": bool,  # Optional.
                    "likesMilk": bool,  # Optional.
                    "meows": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = cat

        request = build_put_cat_request(
            content_type=content_type,
            json=_json,
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)

    @distributed_trace_async
    async def get_kitten(self, **kwargs: Any) -> JSONType:
        """Get a kitten with name 'Gatito' where likesMilk and meows is true, and hisses and eatsMiceYet
        is false.

        :return: JSON object
        :rtype: JSONType
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "eatsMiceYet": bool,  # Optional.
                    "hisses": bool,  # Optional.
                    "likesMilk": bool,  # Optional.
                    "meows": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        cls = kwargs.pop("cls", None)  # type: ClsType[JSONType]

        request = build_get_kitten_request()
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
            return cls(pipeline_response, cast(JSONType, deserialized), {})

        return cast(JSONType, deserialized)

    @distributed_trace_async
    async def put_kitten(self, kitten: JSONType, **kwargs: Any) -> str:
        """Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and eatsMiceYet is
        true.

        :param kitten: Put a kitten with name 'Kitty' where likesMilk and hisses is false, meows and
         eatsMiceYet is true.
        :type kitten: JSONType
        :return: str
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                kitten = {
                    "eatsMiceYet": bool,  # Optional.
                    "hisses": bool,  # Optional.
                    "likesMilk": bool,  # Optional.
                    "meows": bool,  # Optional.
                    "name": "str"  # Required.
                }
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[str]

        _json = kitten

        request = build_put_kitten_request(
            content_type=content_type,
            json=_json,
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
            return cls(pipeline_response, cast(str, deserialized), {})

        return cast(str, deserialized)
