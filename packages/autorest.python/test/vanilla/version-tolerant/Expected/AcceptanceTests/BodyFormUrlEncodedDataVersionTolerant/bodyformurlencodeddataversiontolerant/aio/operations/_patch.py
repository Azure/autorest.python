# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import Any, Dict, List

from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.rest import HttpRequest
from azure.core.pipeline import PipelineResponse

from ._operations import FormdataurlencodedOperations as _FormdataurlencodedOperations
from ...operations._patch import Helpers


class FormdataurlencodedOperations(_FormdataurlencodedOperations, Helpers):
    async def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> PipelineResponse:
        return await self._client._pipeline.run(request, stream=stream, **kwargs)  # pylint: disable=protected-access

    @distributed_trace_async
    async def update_pet_with_form(self, pet_id: int, data: Dict[str, Any], **kwargs: Any) -> None:
        """Updates a pet in the store with form data.

        Updates a pet in the store with form data.

        :param pet_id: ID of pet that needs to be updated.
        :type pet_id: int
        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python
                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    "name": "str",  # Optional. Updated name of the pet. Default value is None.
                    "pet_age": 0,  # How many years is it old?.
                    "pet_food": "str",  # Can take a value of meat, or fish, or plant. Known
                      values are: "meat", "fish", and "plant".
                    "pet_type": "str",  # Can take a value of dog, or cat, or fish. Known values
                      are: "dog", "cat", and "fish".
                    "status": "str"  # Optional. Updated status of the pet. Default value is
                      None.
                }
        """
        request = self._update_pet_with_form_request(pet_id=pet_id, data=data, **kwargs)
        request.url = self._client.format_url(request.url)
        return self._update_pet_with_form_deserialize(await self._send_request(request, **kwargs))

    @distributed_trace_async
    async def partial_constant_body(self, data: Dict[str, Any], **kwargs: Any) -> None:
        """Test a partially constant formdata body. Pass in { grant_type: 'access_token', access_token:
        'foo', service: 'bar' } to pass the test.

        :param data: Form-encoded input for data. See the template in our example to find the input
         shape.
        :type data: dict[str, any]
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python
                # form-encoded input template you can fill out and use as your `data` input.
                data = {
                    "access_token": "str",  # AAD access token, mandatory when grant_type is
                      access_token_refresh_token or access_token.
                    "grant_type": "access_token",  # Default value is "access_token". Constant
                      part of a formdata body. Default value is "access_token". Note that overriding
                      this default value may result in unsupported behavior.
                    "service": "str"  # Indicates the name of your Azure container registry.
                }
        """
        request = self._partial_constant_body_request(data=data, **kwargs)
        request.url = self._client.format_url(request.url)
        return self._partial_constant_body_deserialize(await self._send_request(request, **kwargs))


__all__: List[str] = [
    "FormdataurlencodedOperations"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
