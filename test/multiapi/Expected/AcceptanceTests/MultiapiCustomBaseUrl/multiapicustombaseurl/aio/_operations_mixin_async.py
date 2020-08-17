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
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest


class MultiapiCustomBaseUrlServiceClientOperationsMixin(object):

    async def test(
        self,
        id: int,
        **kwargs
    ) -> None:
        """Should be a mixin operation. Put in 2 for the required parameter and have the correct api
        version of 2.0.0 to pass.

        :param id: An int parameter. Put in 2 to pass.
        :type id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('test')
        if api_version == '1.0.0':
            from ..v1.aio.operations_async import MultiapiCustomBaseUrlServiceClientOperationsMixin as OperationClass
        elif api_version == '2.0.0':
            from ..v2.aio.operations_async import MultiapiCustomBaseUrlServiceClientOperationsMixin as OperationClass
        else:
            raise NotImplementedError("API version {} does not have operation 'test'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.test(id, **kwargs)
