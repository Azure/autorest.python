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

import sys
from typing import Any, Optional, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.pipeline import policies
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from ._configuration import MultiapiServiceClientConfiguration
from ._operations_mixin import MultiapiServiceClientOperationsMixin
from ._serialization import Deserializer, Serializer

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

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
    :type credential: ~azure.core.credentials.TokenCredential
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '3.0.0'
    _PROFILE_TAG = "multiapidataplane.MultiapiServiceClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
            'begin_test_lro': '1.0.0',
            'begin_test_lro_and_paging': '1.0.0',
            'test_one': '2.0.0',
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "TokenCredential",
        api_version: Optional[str]=None,
        base_url: str = "http://localhost:3000",
        profile: KnownProfiles=KnownProfiles.default,
        **kwargs: Any
    ):
        if api_version:
            kwargs.setdefault('api_version', api_version)
        self._config = MultiapiServiceClientConfiguration(credential, **kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client = PipelineClient(base_url=base_url, policies=_policies, **kwargs)
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

           * 1.0.0: :mod:`v1.models<multiapidataplane.v1.models>`
           * 2.0.0: :mod:`v2.models<multiapidataplane.v2.models>`
           * 3.0.0: :mod:`v3.models<multiapidataplane.v3.models>`
        """
        if api_version == '1.0.0':
            from .v1 import models
            return models
        elif api_version == '2.0.0':
            from .v2 import models
            return models
        elif api_version == '3.0.0':
            from .v3 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def operation_group_one(self):
        """Instance depends on the API version:

           * 1.0.0: :class:`OperationGroupOneOperations<multiapidataplane.v1.operations.OperationGroupOneOperations>`
           * 2.0.0: :class:`OperationGroupOneOperations<multiapidataplane.v2.operations.OperationGroupOneOperations>`
           * 3.0.0: :class:`OperationGroupOneOperations<multiapidataplane.v3.operations.OperationGroupOneOperations>`
        """
        api_version = self._get_api_version('operation_group_one')
        if api_version == '1.0.0':
            from .v1.operations import OperationGroupOneOperations as OperationClass
        elif api_version == '2.0.0':
            from .v2.operations import OperationGroupOneOperations as OperationClass
        elif api_version == '3.0.0':
            from .v3.operations import OperationGroupOneOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operation_group_one'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)), api_version)

    @property
    def operation_group_two(self):
        """Instance depends on the API version:

           * 2.0.0: :class:`OperationGroupTwoOperations<multiapidataplane.v2.operations.OperationGroupTwoOperations>`
           * 3.0.0: :class:`OperationGroupTwoOperations<multiapidataplane.v3.operations.OperationGroupTwoOperations>`
        """
        api_version = self._get_api_version('operation_group_two')
        if api_version == '2.0.0':
            from .v2.operations import OperationGroupTwoOperations as OperationClass
        elif api_version == '3.0.0':
            from .v3.operations import OperationGroupTwoOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operation_group_two'".format(api_version))
        self._config.api_version = api_version
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)), api_version)

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
