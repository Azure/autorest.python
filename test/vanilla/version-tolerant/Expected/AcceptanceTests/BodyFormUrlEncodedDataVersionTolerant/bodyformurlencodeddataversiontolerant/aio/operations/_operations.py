# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

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

from ...operations._operations import (
    build_formdataurlencoded_partial_constant_body_request,
    build_formdataurlencoded_update_pet_with_form_request,
)

T = TypeVar("T")
JSONType = Any
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class FormdataurlencodedOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through :class:`~bodyformurlencodeddataversiontolerant.aio.BodyFormsDataURLEncoded`'s
        :attr:`~bodyformurlencodeddataversiontolerant.aio.BodyFormsDataURLEncoded.formdataurlencoded` attribute.
    """

    def __init__(self, *args, **kwargs) -> None:
        self._client = kwargs.pop("client", args[0])
        self._config = kwargs.pop("config", args[1])
        self._serialize = kwargs.pop("serializer", args[2])
        self._deserialize = kwargs.pop("deserializer", args[3])

    @distributed_trace_async
    async def update_pet_with_form(  # pylint: disable=inconsistent-return-statements
        self, pet_id: int, data: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Updates a pet in the store with form data.

        Updates a pet in the store with form data.

        :param pet_id: ID of pet that needs to be updated.
        :type pet_id: int
        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    "name": "str",  # Optional. Updated name of the pet. Default value is None.
                    "pet_age": 0,  # How many years is it old?.
                    "pet_food": "str",  # Can take a value of meat, or fish, or plant. Possible
                      values are: "meat", "fish", and "plant".
                    "pet_type": "str",  # Can take a value of dog, or cat, or fish. Possible
                      values are: "dog", "cat", and "fish".
                    "status": "str"  # Optional. Updated status of the pet. Default value is
                      None.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/x-www-form-urlencoded")  # type: Optional[str]

        request = build_formdataurlencoded_update_pet_with_form_request(
            pet_id=pet_id,
            content_type=content_type,
            data=data,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 405]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    @distributed_trace_async
    async def partial_constant_body(  # pylint: disable=inconsistent-return-statements
        self, data: Dict[str, Any], **kwargs: Any
    ) -> None:
        """Test a partially constant formdata body. Pass in { grant_type: 'access_token', access_token:
        'foo', service: 'bar' } to pass the test.

        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    "access_token": "str",  # AAD access token, mandatory when grant_type is
                      access_token_refresh_token or access_token.
                    "grant_type": "access_token",  # Default value is "access_token". Constant
                      part of a formdata body. Default value is "access_token". Note that overriding
                      this default value may result in unsupported behavior.
                    "service": "str"  # Indicates the name of your Azure container registry.
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/x-www-form-urlencoded")  # type: Optional[str]

        request = build_formdataurlencoded_partial_constant_body_request(
            content_type=content_type,
            data=data,
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})
