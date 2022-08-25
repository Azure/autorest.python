# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import AdelConfiguration
from ._serialization import Deserializer, Serializer
from .models import _models as models
from .operations import (
    AlertConfigsOperations,
    DatasetsOperations,
    EvaluationsOperations,
    HooksOperations,
    ModelsOperations,
    ReplaysOperations,
    SchedulesOperations,
)


class Adel:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Service client.

    :ivar alert_configs: AlertConfigsOperations operations
    :vartype alert_configs: adel.operations.AlertConfigsOperations
    :ivar hooks: HooksOperations operations
    :vartype hooks: adel.operations.HooksOperations
    :ivar datasets: DatasetsOperations operations
    :vartype datasets: adel.operations.DatasetsOperations
    :ivar models: ModelsOperations operations
    :vartype models: adel.operations.ModelsOperations
    :ivar evaluations: EvaluationsOperations operations
    :vartype evaluations: adel.operations.EvaluationsOperations
    :ivar schedules: SchedulesOperations operations
    :vartype schedules: adel.operations.SchedulesOperations
    :ivar replays: ReplaysOperations operations
    :vartype replays: adel.operations.ReplaysOperations
    :param resource: Resource name. Required.
    :type resource: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, resource: str, **kwargs: Any
    ) -> None:
        _endpoint = "https://{resource}.cognitiveservices.azure.com"
        self._config = AdelConfiguration(resource=resource, **kwargs)
        self._client = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.alert_configs = AlertConfigsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.hooks = HooksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.datasets = DatasetsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.models = ModelsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.evaluations = EvaluationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.schedules = SchedulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.replays = ReplaysOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "resource": self._serialize.url("self._config.resource", self._config.resource, "str"),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> Adel
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
