# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional

from azure.core.pipeline.transport import HttpRequest


def _get_pet_by_id_request(pet_id: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/errorStatusCodes/Pets/{petId}/GetPet")
    path_format_arguments = {
        "petId": self._serialize.url("pet_id", pet_id, "str"),
    }
    url = self._client.format_url(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.get(url, query_parameters, header_parameters)


def _do_something_request(what_action: str, **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/errorStatusCodes/Pets/doSomething/{whatAction}")
    path_format_arguments = {
        "whatAction": self._serialize.url("what_action", what_action, "str"),
    }
    url = self._client.format_url(url, **path_format_arguments)

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)


def _has_models_param_request(models: Optional[str] = "value1", **kwargs) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/errorStatusCodes/Pets/hasModelsParam")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    if models is not None:
        query_parameters["models"] = self._serialize.query("models", models, "str")

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    return self._client.post(url, query_parameters, header_parameters)
