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
from msrest import Serializer, Deserializer
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union


class MultiapiServiceClientOperationsMixin(object):

    def begin_test_lro(
        self,
        product=None,  # type: Optional["models.Product"]
        **kwargs  # type: Any
    ):
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put.
        :type product: ~multiapinoasync.v1.models.Product
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either Product or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~multiapinoasync.v1.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_test_lro')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_test_lro(product, **kwargs)

    def begin_test_lro_and_paging(
        self,
        client_request_id=None,  # type: Optional[str]
        test_lro_and_paging_options=None,  # type: Optional["models.TestLroAndPagingOptions"]
        **kwargs  # type: Any
    ):
        """A long-running paging operation that includes a nextLink that has 10 pages.

        :param client_request_id:
        :type client_request_id: str
        :param test_lro_and_paging_options: Parameter group.
        :type test_lro_and_paging_options: ~multiapinoasync.v1.models.TestLroAndPagingOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns an iterator like instance of either PagingResult or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.core.paging.ItemPaged[~multiapinoasync.v1.models.PagingResult]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_test_lro_and_paging')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_test_lro_and_paging(client_request_id, test_lro_and_paging_options, **kwargs)

    def test_one(
        self,
        id,  # type: int
        message=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        """TestOne should be in an SecondVersionOperationsMixin. Returns ModelTwo.

        :param id: An int parameter.
        :type id: int
        :param message: An optional string parameter.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelTwo, or the result of cls(response)
        :rtype: ~multiapinoasync.v2.models.ModelTwo
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('test_one')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        elif api_version == '2.0.0':
            from .v2.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test_one(id, message, **kwargs)

    def test_paging(
        self,
        **kwargs  # type: Any
    ):
        """Returns ModelThree with optionalProperty 'paged'.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PagingResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~multiapinoasync.v3.models.PagingResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('test_paging')
        if api_version == '3.0.0':
            from .v3.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test_paging(**kwargs)
