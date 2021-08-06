# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.pipeline.transport._base import _format_url_section
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_get_pet_by_id_request(
    pet_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/errorStatusCodes/Pets/{petId}/GetPet')
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_do_something_request(
    what_action,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/errorStatusCodes/Pets/doSomething/{whatAction}')
    path_format_arguments = {
        "whatAction": _SERIALIZER.url("what_action", what_action, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )


def build_has_models_param_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    models = kwargs.pop('models', "value1")  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/errorStatusCodes/Pets/hasModelsParam')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if models is not None:
        query_parameters['models'] = _SERIALIZER.query("models", models, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class PetOperations(object):
    """PetOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~xmserrorresponse.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

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
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
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
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.PetActionError, response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("PetAction", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    do_something.metadata = {"url": "/errorStatusCodes/Pets/doSomething/{whatAction}"}  # type: ignore

    @distributed_trace
    def has_models_param(
        self,
        models="value1",  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Ensure you can correctly deserialize the returned PetActionError and deserialization doesn't
        conflict with the input param name 'models'.

        :param models: Make sure model deserialization doesn't conflict with this param name, which has
         input name 'models'. Use client default value in call.
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
        )._to_pipeline_transport_request()
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.PetActionError, response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    has_models_param.metadata = {"url": "/errorStatusCodes/Pets/hasModelsParam"}  # type: ignore
