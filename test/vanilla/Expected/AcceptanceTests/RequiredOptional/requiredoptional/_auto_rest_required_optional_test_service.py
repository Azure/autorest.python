# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.pipeline import PipelineResponse
    from azure.core.pipeline.transport import HttpRequest

from ._configuration import AutoRestRequiredOptionalTestServiceConfiguration
from .operations import ImplicitOperations
from .operations import ExplicitOperations
from . import models


class AutoRestRequiredOptionalTestService(object):
    """Test Infrastructure for AutoRest.

    :ivar implicit: ImplicitOperations operations
    :vartype implicit: requiredoptional.operations.ImplicitOperations
    :ivar explicit: ExplicitOperations operations
    :vartype explicit: requiredoptional.operations.ExplicitOperations
    :param required_global_path: number of items to skip.
    :type required_global_path: str
    :param required_global_query: number of items to skip.
    :type required_global_query: str
    :param optional_global_query: number of items to skip.
    :type optional_global_query: int
    :param str base_url: Service URL
    """

    def __init__(
        self,
        required_global_path,  # type: str
        required_global_query,  # type: str
        optional_global_query=None,  # type: Optional[int]
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = "http://localhost:3000"
        self._config = AutoRestRequiredOptionalTestServiceConfiguration(
            required_global_path, required_global_query, optional_global_query, **kwargs
        )
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.implicit = ImplicitOperations(self._client, self._config, self._serialize, self._deserialize)
        self.explicit = ExplicitOperations(self._client, self._config, self._serialize, self._deserialize)

    def invoke(self, request, **kwargs):
        # type: (HttpRequest, Any) -> PipelineResponse
        path_format_arguments = {
            "required-global-path": self._serialize.url(
                "self._config.required_global_path", self._config.required_global_path, "str"
            ),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)
        stream = kwargs.pop("stream", False)
        return self._client._pipeline.run(request, stream=stream, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestRequiredOptionalTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
