# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ..._operations._operations import (
    build_json_merge_patch_create_resource_request,
    build_json_merge_patch_update_optional_resource_request,
    build_json_merge_patch_update_resource_request,
)
from ...models._model_base import SdkJSONEncoder, _deserialize
from .._vendor import JsonMergePatchClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class JsonMergePatchClientOperationsMixin(JsonMergePatchClientMixinABC):

    @overload
    async def create_resource(
        self, body: _models.Resource, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: ~payload.jsonmergepatch.models.Resource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """

    @overload
    async def create_resource(
        self, body: JSON, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """

    @overload
    async def create_resource(
        self, body: IO[bytes], *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """

    @distributed_trace_async
    async def create_resource(self, body: Union[_models.Resource, JSON, IO[bytes]], **kwargs: Any) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Is one of the following types: Resource, JSON, IO[bytes] Required.
        :type body: ~payload.jsonmergepatch.models.Resource or JSON or IO[bytes]
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Resource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_json_merge_patch_create_resource_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Resource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update_resource(
        self, body: _models.ResourcePatch, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: ~payload.jsonmergepatch.models.ResourcePatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """

    @overload
    async def update_resource(
        self, body: JSON, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """

    @overload
    async def update_resource(
        self, body: IO[bytes], *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Required.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """

    @distributed_trace_async
    async def update_resource(
        self, body: Union[_models.ResourcePatch, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with required body.

        :param body: Is one of the following types: ResourcePatch, JSON, IO[bytes] Required.
        :type body: ~payload.jsonmergepatch.models.ResourcePatch or JSON or IO[bytes]
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[_models.Resource] = kwargs.pop("cls", None)

        content_type = content_type or "application/merge-patch+json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_json_merge_patch_update_resource_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Resource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update_optional_resource(
        self,
        body: Optional[_models.ResourcePatch] = None,
        *,
        content_type: str = "application/merge-patch+json",
        **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with optional body.

        :param body: Default value is None.
        :type body: ~payload.jsonmergepatch.models.ResourcePatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """

    @overload
    async def update_optional_resource(
        self, body: Optional[JSON] = None, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with optional body.

        :param body: Default value is None.
        :type body: JSON
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """

    @overload
    async def update_optional_resource(
        self, body: Optional[IO[bytes]] = None, *, content_type: str = "application/merge-patch+json", **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with optional body.

        :param body: Default value is None.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/merge-patch+json".
        :paramtype content_type: str
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """

    @distributed_trace_async
    async def update_optional_resource(
        self, body: Optional[Union[_models.ResourcePatch, JSON, IO[bytes]]] = None, **kwargs: Any
    ) -> _models.Resource:
        """Test content-type: application/merge-patch+json with optional body.

        :param body: Is one of the following types: ResourcePatch, JSON, IO[bytes] Default value is
         None.
        :type body: ~payload.jsonmergepatch.models.ResourcePatch or JSON or IO[bytes]
        :return: Resource. The Resource is compatible with MutableMapping
        :rtype: ~payload.jsonmergepatch.models.Resource
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }

                # response body for status code(s): 200
                response == {
                    "name": "str",  # Required.
                    "array": [
                        {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    ],
                    "description": "str",  # Optional.
                    "floatValue": 0.0,  # Optional.
                    "innerModel": {
                        "description": "str",  # Optional.
                        "name": "str"  # Optional.
                    },
                    "intArray": [
                        0  # Optional.
                    ],
                    "intValue": 0,  # Optional.
                    "map": {
                        "str": {
                            "description": "str",  # Optional.
                            "name": "str"  # Optional.
                        }
                    }
                }
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[_models.Resource] = kwargs.pop("cls", None)

        content_type = content_type or "application/merge-patch+json"
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            if body is not None:
                _content = json.dumps(body, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore
            else:
                _content = None

        _request = build_json_merge_patch_update_optional_resource_request(
            content_type=content_type,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                await response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.Resource, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
