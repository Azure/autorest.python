# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._model_base import AzureJSONEncoder, _deserialize
from ..._operations._operations import build_templated_create_or_update_user_request
from .._vendor import TemplatedClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class TemplatedClientOperationsMixin(TemplatedClientMixinABC):
    @overload
    async def create_or_update_user(
        self,
        id: int,
        body: Union[_models.TemplatedCreateOrUpdateUserRequest, JSON],
        *,
        api_version: str,
        content_type: str = "application/merge-patch+json",
        **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param body: Required.
        :type body: ~bodies.templated.models.TemplatedCreateOrUpdateUserRequest or JSON
        :keyword api_version: The API version to use for this operation. Required.
        :paramtype api_version: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~bodies.templated.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update_user(
        self, id: int, body: IO, *, api_version: str, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param body: Required.
        :type body: IO
        :keyword api_version: The API version to use for this operation. Required.
        :paramtype api_version: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~bodies.templated.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update_user(
        self,
        id: int,
        body: Union[_models.TemplatedCreateOrUpdateUserRequest, JSON, IO],
        *,
        api_version: str,
        **kwargs: Any
    ) -> _models.User:
        """Adds a user or updates a user's fields.

        Creates or updates a User.

        :param id: The user's id. Required.
        :type id: int
        :param body: Is either a model type or a IO type. Required.
        :type body: ~bodies.templated.models.TemplatedCreateOrUpdateUserRequest or JSON or IO
        :keyword api_version: The API version to use for this operation. Required.
        :paramtype api_version: str
        :keyword content_type: This request has a JSON Merge Patch body. Default value is None.
        :paramtype content_type: str
        :return: User. The User is compatible with MutableMapping
        :rtype: ~bodies.templated.models.User
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type = kwargs.pop("content_type", _headers.pop("content-type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.User]

        content_type = content_type or "application/merge-patch+json"
        _content = None
        if isinstance(body, (IO, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=AzureJSONEncoder)

        request = build_templated_create_or_update_user_request(
            id=id,
            api_version=api_version,
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = _deserialize(_models.ErrorResponse, response.json())
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = _deserialize(_models.User, response.json())

        if response.status_code == 201:
            deserialized = _deserialize(_models.User, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
