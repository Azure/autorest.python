# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_get_pet_by_id_request(
    pet_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/errorStatusCodes/Pets/{petId}/GetPet")
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_do_something_request(
    what_action,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/errorStatusCodes/Pets/doSomething/{whatAction}")
    path_format_arguments = {
        "whatAction": _SERIALIZER.url("what_action", what_action, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        headers=_header_parameters,
        **kwargs
    )


def build_has_models_param_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    models = kwargs.pop('models', "value1")  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/errorStatusCodes/Pets/hasModelsParam")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if models is not None:
        _query_parameters['models'] = _SERIALIZER.query("models", models, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class PetOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through :class:`~xmserrorresponse.XMSErrorResponseExtensions`'s
        :attr:`~xmserrorresponse.XMSErrorResponseExtensions.pet` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        self._client = kwargs.pop("client", args[0])
        self._config = kwargs.pop("config", args[1])
        self._serialize = kwargs.pop("serializer", args[2])
        self._deserialize = kwargs.pop("deserializer", args[3])

    @distributed_trace
    def get_pet_by_id(
        self,
        pet_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.Pet"]
        """Gets pets by id.

        :param pet_id: pet id.
        :type pet_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pet, or the result of cls(response)
        :rtype: ~xmserrorresponse.models.Pet or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Optional["_models.Pet"]]
        error_map = {
            401: ClientAuthenticationError,
            409: ResourceExistsError,
            400: HttpResponseError,
            404: lambda response: ResourceNotFoundError(
                response=response, model=self._deserialize(_models.NotFoundErrorBase, response)
            ),
            501: HttpResponseError,
        }
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_pet_by_id_request(
            pet_id=pet_id,
            template_url=self.get_pet_by_id.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("Pet", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_pet_by_id.metadata = {"url": "/errorStatusCodes/Pets/{petId}/GetPet"}  # type: ignore

    @distributed_trace
    def do_something(
        self,
        what_action,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.PetAction"
        """Asks pet to do something.

        :param what_action: what action the pet should do.
        :type what_action: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PetAction, or the result of cls(response)
        :rtype: ~xmserrorresponse.models.PetAction
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.PetAction"]
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: lambda response: HttpResponseError(
                response=response, model=self._deserialize(_models.PetActionError, response)
            ),
        }
        error_map.update(kwargs.pop("error_map", {}))

        request = build_do_something_request(
            what_action=what_action,
            template_url=self.do_something.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.PetActionError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAction", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    do_something.metadata = {"url": "/errorStatusCodes/Pets/doSomething/{whatAction}"}  # type: ignore

    @distributed_trace
    def has_models_param(  # pylint: disable=inconsistent-return-statements
        self,
        models="value1",  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Ensure you can correctly deserialize the returned PetActionError and deserialization doesn't
        conflict with the input param name 'models'.

        :param models: Make sure model deserialization doesn't conflict with this param name, which has
         input name 'models'. Use client default value in call. Default value is "value1".
        :type models: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            500: lambda response: HttpResponseError(
                response=response, model=self._deserialize(_models.PetActionError, response)
            ),
        }
        error_map.update(kwargs.pop("error_map", {}))

        request = build_has_models_param_request(
            models=models,
            template_url=self.has_models_param.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.PetActionError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    has_models_param.metadata = {"url": "/errorStatusCodes/Pets/hasModelsParam"}  # type: ignore
