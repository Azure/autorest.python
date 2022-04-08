# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import abc
from typing import Any, Callable, Dict, Optional, TypeVar

from msrest import Serializer

from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


@abc.abstractmethod
def build_formdataurlencoded_update_pet_with_form_request(*args, **kwargs) -> HttpRequest:
    raise NotImplementedError(
        "You need to write a custom operation for 'build_formdataurlencoded_update_pet_with_form_request'. "
        "Please refer to https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize."
    )


@abc.abstractmethod
def build_formdataurlencoded_partial_constant_body_request(*args, **kwargs) -> HttpRequest:
    raise NotImplementedError(
        "You need to write a custom operation for 'build_formdataurlencoded_partial_constant_body_request'. "
        "Please refer to https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize."
    )


class FormdataurlencodedOperations(abc.ABC):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~bodyformurlencodeddataversiontolerant.BodyFormsDataURLEncoded`'s
        :attr:`formdataurlencoded` attribute.
    """

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    @abc.abstractmethod
    def update_pet_with_form(self, *args, **kwargs) -> None:  # pylint: disable=inconsistent-return-statements
        """You need to write a custom operation for "update_pet_with_form". Please refer to
        https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize.

        """

    @distributed_trace
    @abc.abstractmethod
    def partial_constant_body(self, *args, **kwargs) -> None:  # pylint: disable=inconsistent-return-statements
        """You need to write a custom operation for "partial_constant_body". Please refer to
        https://aka.ms/azsdk/python/dpcodegen/python/customize to learn how to customize.

        """
