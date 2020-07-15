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

from azure.core import AsyncPipelineClient
from msrest import Serializer, Deserializer

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ._configuration_async import MultiapiServiceClientConfiguration
from ._operations_mixin_async import MultiapiServiceClientOperationsMixin
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

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param endpoint: Pass in https://localhost:3000.
    :type endpoint: str
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2.0.0'
    _PROFILE_TAG = "multiapicustombaseurl.MultiapiServiceClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "AsyncTokenCredential"
        endpoint,  # type: str
        api_version=None,
        profile=KnownProfiles.default,
        **kwargs  # type: Any
    ) -> None:
        if api_version == 'v1':
            base_url = '{Endpoint}/multiapiCustomBaseUrl/v1'
        elif api_version == 'v2':
            base_url = '{Endpoint}/multiapiCustomBaseUrl/v2'
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        self._config = MultiapiServiceClientConfiguration(credential, endpoint, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(MultiapiServiceClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 1.0.0: :mod:`v1.models<multiapicustombaseurl.v1.models>`
           * 2.0.0: :mod:`v2.models<multiapicustombaseurl.v2.models>`
        """
        if api_version == '1.0.0':
            from ..v1 import models
            return models
        elif api_version == '2.0.0':
            from ..v2 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))

    async def close(self):
        await self._client.close()
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
