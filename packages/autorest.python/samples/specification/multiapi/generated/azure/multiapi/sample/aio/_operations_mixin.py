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
from .._serialization import Serializer, Deserializer
from io import IOBase
from typing import Any, AsyncIterable, AsyncIterator, IO, Optional, Union

from azure.core.async_paging import AsyncItemPaged
from azure.core.polling import AsyncLROPoller

from .. import models as _models


class MultiapiServiceClientOperationsMixin(object):

    async def begin_test_lro(
        self,
        product: Optional[Union[_models.Product, IO[bytes]]] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Product]:
        """Put in whatever shape of Product you want, will return a Product with id equal to 100.

        :param product: Product to put. Is either a Product type or a IO[bytes] type. Default value is
         None.
        :type product: ~azure.multiapi.sample.v1.models.Product or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either Product or the result of
         cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.multiapi.sample.v1.models.Product]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_test_lro')
        if api_version == '1.0.0':
            from ..v1.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_test_lro'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.begin_test_lro(product, **kwargs)

    async def begin_test_lro_and_paging(
        self,
        client_request_id: Optional[str] = None,
        test_lro_and_paging_options: Optional[_models.TestLroAndPagingOptions] = None,
        **kwargs: Any
    ) -> AsyncLROPoller[AsyncIterable["_models.Product"]]:
        # pylint: disable=line-too-long
        """A long-running paging operation that includes a nextLink that has 10 pages.

        :param client_request_id: Default value is None.
        :type client_request_id: str
        :param test_lro_and_paging_options: Parameter group. Default value is None.
        :type test_lro_and_paging_options: ~azure.multiapi.sample.v1.models.TestLroAndPagingOptions
        :return: An instance of LROPoller that returns an iterator like instance of either PagingResult
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.core.async_paging.AsyncItemPaged[~azure.multiapi.sample.v1.models.Product]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_test_lro_and_paging')
        if api_version == '1.0.0':
            from ..v1.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_test_lro_and_paging'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.begin_test_lro_and_paging(client_request_id, test_lro_and_paging_options, **kwargs)

    async def test_different_calls(
        self,
        greeting_in_english: str,
        greeting_in_chinese: Optional[str] = None,
        greeting_in_french: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """Has added parameters across the API versions.

        :param greeting_in_english: pass in 'hello' to pass test. Required.
        :type greeting_in_english: str
        :param greeting_in_chinese: pass in 'nihao' to pass test. Default value is None.
        :type greeting_in_chinese: str
        :param greeting_in_french: pass in 'bonjour' to pass test. Default value is None.
        :type greeting_in_french: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('test_different_calls')
        if api_version == '1.0.0':
            from ..v1.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        elif api_version == '2.0.0':
            from ..v2.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        elif api_version == '3.0.0':
            from ..v3.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test_different_calls'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.test_different_calls(greeting_in_english, greeting_in_chinese, greeting_in_french, **kwargs)

    async def test_one(
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
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('test_one')
        if api_version == '1.0.0':
            from ..v1.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        elif api_version == '2.0.0':
            from ..v2.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test_one'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.test_one(id, message, **kwargs)

    def test_paging(
        self,
        **kwargs: Any
    ) -> AsyncIterable["_models.ModelThree"]:
        """Returns ModelThree with optionalProperty 'paged'.

        :return: An iterator like instance of either ModelThree or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.multiapi.sample.v3.models.ModelThree]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('test_paging')
        if api_version == '3.0.0':
            from ..v3.aio.operations import MultiapiServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test_paging'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test_paging(**kwargs)
