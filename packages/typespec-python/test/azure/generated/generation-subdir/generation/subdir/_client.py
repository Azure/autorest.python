# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any
from azure.core.tracing.decorator import distributed_trace
from ._generated import RecursiveClient as GeneratedClient, models as _models


class CustomizedClient:  # pylint: disable=client-accepts-api-version-keyword
    """Tests customization of a client that is fully wrapped.

    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        self._client = GeneratedClient(endpoint=endpoint, **kwargs)

    @distributed_trace
    def customized_get(self, **kwargs: Any) -> _models.Extension:
        """get.

        :return: Extension. The Extension is compatible with MutableMapping
        :rtype: ~generation.subdir._generated.models.Extension
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        return self._client.get(**kwargs)
,line-too-long,useless-suppression