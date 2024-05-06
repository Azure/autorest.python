# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.mgmt.core import AsyncARMPipelineClient
from azure.mgmt.core.policies import AsyncARMAutoResourceProviderRegistrationPolicy
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from .._serialization import Deserializer, Serializer
from ._configuration import MultiapiServiceClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


from .operations import (
    OperationGroupOneOperations,
    OperationGroupTwoOperations,
    MultiapiServiceClientOperationsMixin,
)
from .._validation import api_version_validation
from .. import models


class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass


class MultiapiServiceClient(MultiapiServiceClientOperationsMixin, MultiApiClientMixin, _SDKClient):
    """Service client for multiapi client testing.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = "3.0.0"
    _PROFILE_TAG = "multiapicombiner.MultiapiServiceClient"
    LATEST_PROFILE = ProfileDefinition(
        {
            _PROFILE_TAG: {
                None: DEFAULT_API_VERSION,
                "begin_test_lro": "1.0.0",
                "begin_test_lro_and_paging": "1.0.0",
                "test_one": "2.0.0",
            }
        },
        _PROFILE_TAG + " latest",
    )

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        api_version: Optional[str] = None,
        base_url: str = "http://localhost:3000",
        profile: KnownProfiles = KnownProfiles.default,
        **kwargs: Any
    ) -> None:
        if api_version:
            kwargs.setdefault("api_version", api_version)
        self._config = MultiapiServiceClientConfiguration(credential, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                AsyncARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client = AsyncARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)
        super(MultiapiServiceClient, self).__init__(api_version=api_version, profile=profile)

        self._serialize = Serializer(self._models_dict())
        self._deserialize = Deserializer(self._models_dict())
        self._serialize.client_side_validation = False

    @classmethod
    def _models_dict(cls):
        return {k: v for k, v in models.__dict__.items() if isinstance(v, type)}

    @property
    def operation_group_one(self):
        api_version = self._get_api_version("operation_group_one")
        return OperationGroupOneOperations(
            self._client,
            self._config,
            Serializer(self._models_dict()),
            Deserializer(self._models_dict()),
            api_version=api_version,
        )

    @property
    @api_version_validation(method_valid_on=["2.0.0", "3.0.0"])
    def operation_group_two(self):
        api_version = self._get_api_version("operation_group_two")
        return OperationGroupTwoOperations(
            self._client,
            self._config,
            Serializer(self._models_dict()),
            Deserializer(self._models_dict()),
            api_version=api_version,
        )

    async def close(self):
        await self._client.close()

    async def __aenter__(self):
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
