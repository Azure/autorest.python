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
    from typing import Any

    from azure.core.credentials import TokenCredential

from ._configuration import MultiapiCustomBaseUrlServiceClientConfiguration
from .operations import MultiapiCustomBaseUrlServiceClientOperationsMixin
from . import models


class MultiapiCustomBaseUrlServiceClient(MultiapiCustomBaseUrlServiceClientOperationsMixin):
    """Service client for multiapi custom base url testing.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param endpoint: Pass in https://localhost:3000.
    :type endpoint: str
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        endpoint,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = '{Endpoint}/multiapiCustomBaseUrl/v2'
        self._config = MultiapiCustomBaseUrlServiceClientConfiguration(credential, endpoint, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MultiapiCustomBaseUrlServiceClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
