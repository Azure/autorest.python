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


class MultiapiTestOperationsMixin(object):

    def test_one(
        self,
        id,  # type: int
        message=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        """TestOne should be in an SecondVersionOperationsMixin. Returns ModelTwo.

        :param id:
        :type id: int
        :param message:
        :type message: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ModelTwo or the result of cls(response)
        :rtype: ~multiapi.v2.models.ModelTwo
        :raises: ~azure.core.exceptions.HttpResponseError
        """

        api_version = self._get_api_version('test_one')
        if api_version == '1.0.0':
            from .v1.operations import MultiapiTestOperationsMixin as OperationClass
        elif api_version == '2.0.0':
            from .v2.operations import MultiapiTestOperationsMixin as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        mixin_instance.api_version = api_version
        return mixin_instance.test_one(id, message, **kwargs)
