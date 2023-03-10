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
from ._serialization import Serializer, Deserializer
from typing import Any, IO, Iterable, Optional, Union

from azure.core.paging import ItemPaged
from azure.core.polling import LROPoller

from . import _serialization, models as _models


class MultiapiServiceClientOperationsMixin(object):

    def begin_test_lro(
        self,
        product: Optional[Union[_models.Product, IO]] = None,
        **kwargs: Any
    ) -> LROPoller[_models.Product]:
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put. Is either a Product type or a IO type. Default value is None.
        :type product: ~multiapisecurity.v1.models.Product or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either Product or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~multiapisecurity.v1.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_test_lro')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_test_lro'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_test_lro(product, **kwargs)

    def begin_test_lro_and_paging(
        self,
        client_request_id: Optional[str] = None,
        test_lro_and_paging_options: Optional[_models.TestLroAndPagingOptions] = None,
        **kwargs: Any
    ) -> LROPoller[Iterable["_models.Product"]]:
        """A long-running paging operation that includes a nextLink that has 10 pages.

        :param client_request_id: Default value is None.
        :type client_request_id: str
        :param test_lro_and_paging_options: Parameter group. Default value is None.
        :type test_lro_and_paging_options: ~multiapisecurity.v1.models.TestLroAndPagingOptions
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be LROBasePolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns an iterator like instance of either PagingResult
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.core.paging.ItemPaged[~multiapisecurity.v1.models.Product]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_test_lro_and_paging')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_test_lro_and_paging'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_test_lro_and_paging(client_request_id, test_lro_and_paging_options, **kwargs)

    def test_different_calls(  # pylint: disable=inconsistent-return-statements
        self,
        greeting_in_english: str,
        **kwargs: Any
    ) -> None:
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test. Required.
        :type greeting_in_english: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('test_different_calls')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test_different_calls'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test_different_calls(greeting_in_english, **kwargs)

    def test_one(  # pylint: disable=inconsistent-return-statements
        self,
        id: int,
        message: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """TestOne should be in an FirstVersionOperationsMixin.

        :param id: An int parameter. Required.
        :type id: int
        :param message: An optional string parameter. Default value is None.
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('test_one')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test_one'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test_one(id, message, **kwargs)
