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
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_update_pet_with_form_request(
    pet_id,  # type: int
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    # Construct URL
    url = kwargs.pop("template_url", '/formsdataurlencoded/pet/add/{petId}')
    path_format_arguments = {
        "petId": _SERIALIZER.url("pet_id", pet_id, 'int'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class FormdataurlencodedOperations(object):
    """FormdataurlencodedOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~bodyformurlencodeddata.models
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
    def update_pet_with_form(
        self,
        pet_id,  # type: int
        pet_type,  # type: Union[str, "_models.PetType"]
        pet_food,  # type: Union[str, "_models.PetFood"]
        pet_age,  # type: int
        name=None,  # type: Optional[str]
        status=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Updates a pet in the store with form data.

        Updates a pet in the store with form data.

        :param pet_id: ID of pet that needs to be updated.
        :type pet_id: int
        :param pet_type: Can take a value of dog, or cat, or fish.
        :type pet_type: str or ~bodyformurlencodeddata.models.PetType
        :param pet_food: Can take a value of meat, or fish, or plant.
        :type pet_food: str or ~bodyformurlencodeddata.models.PetFood
        :param pet_age: How many years is it old?.
        :type pet_age: int
        :param name: Updated name of the pet.
        :type name: str
        :param status: Updated status of the pet.
        :type status: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/x-www-form-urlencoded")  # type: Optional[str]

        content = self._serialize.body(pet_type, "str")

        request = build_update_pet_with_form_request(
            pet_id=pet_id,
            content_type=content_type,
            data=data,
            template_url=self.update_pet_with_form.metadata["url"],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 405]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    update_pet_with_form.metadata = {"url": "/formsdataurlencoded/pet/add/{petId}"}  # type: ignore
