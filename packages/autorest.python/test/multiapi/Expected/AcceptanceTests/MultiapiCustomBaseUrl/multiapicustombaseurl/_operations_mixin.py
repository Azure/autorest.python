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
import sys
from typing import Any

from . import models as _models


class MultiapiCustomBaseUrlServiceClientOperationsMixin(object):

    def test(  # pylint: disable=inconsistent-return-statements
        self,
        id: int,
        **kwargs: Any
    ) -> None:
        """Should be a mixin operation. Put in 2 for the required parameter and have the correct api
        version of 2.0.0 to pass.

        :param id: An int parameter. Put in 2 to pass. Required.
        :type id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('test')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiCustomBaseUrlServiceClientOperationsMixin as OperationClass
        elif api_version == '2.0.0':
            from .v2.operations import MultiapiCustomBaseUrlServiceClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'test'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.test(id, **kwargs)
