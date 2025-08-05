# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Optional
from azure.core.credentials import AzureKeyCredential
from ._generated import ApiKeyClient as GeneratedClient


class CustomizedApiKeyClient:
    """Tests customization of a client that is fully wrapped

    :param credential: Credential used to authenticate requests to the service. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(
        self,
        credential: AzureKeyCredential,
        *,
        endpoint: str = "http://localhost:3000",
        api_version: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        self._client = GeneratedClient(credential=credential, endpoint=endpoint, api_version=api_version, **kwargs)

    def custom_method(self) -> bool:
        """An example of a custom method that could be added.

        :return: True if the client is valid, False otherwise.
        :rtype: bool
        """
        self._client.valid()
        return True
