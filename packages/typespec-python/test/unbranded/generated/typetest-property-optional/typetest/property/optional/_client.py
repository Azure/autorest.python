# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
import sys
from typing import Any

from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import OptionalClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    BooleanLiteralOperations,
    BytesOperations,
    CollectionsByteOperations,
    CollectionsModelOperations,
    DatetimeOperations,
    DurationOperations,
    FloatLiteralOperations,
    IntLiteralOperations,
    RequiredAndOptionalOperations,
    StringLiteralOperations,
    StringOperations,
    UnionFloatLiteralOperations,
    UnionIntLiteralOperations,
    UnionStringLiteralOperations,
)

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self  # type: ignore  # pylint: disable=ungrouped-imports


class OptionalClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Illustrates models with optional properties.

    :ivar string: StringOperations operations
    :vartype string: typetest.property.optional.operations.StringOperations
    :ivar bytes: BytesOperations operations
    :vartype bytes: typetest.property.optional.operations.BytesOperations
    :ivar datetime: DatetimeOperations operations
    :vartype datetime: typetest.property.optional.operations.DatetimeOperations
    :ivar duration: DurationOperations operations
    :vartype duration: typetest.property.optional.operations.DurationOperations
    :ivar collections_byte: CollectionsByteOperations operations
    :vartype collections_byte: typetest.property.optional.operations.CollectionsByteOperations
    :ivar collections_model: CollectionsModelOperations operations
    :vartype collections_model: typetest.property.optional.operations.CollectionsModelOperations
    :ivar string_literal: StringLiteralOperations operations
    :vartype string_literal: typetest.property.optional.operations.StringLiteralOperations
    :ivar int_literal: IntLiteralOperations operations
    :vartype int_literal: typetest.property.optional.operations.IntLiteralOperations
    :ivar float_literal: FloatLiteralOperations operations
    :vartype float_literal: typetest.property.optional.operations.FloatLiteralOperations
    :ivar boolean_literal: BooleanLiteralOperations operations
    :vartype boolean_literal: typetest.property.optional.operations.BooleanLiteralOperations
    :ivar union_string_literal: UnionStringLiteralOperations operations
    :vartype union_string_literal:
     typetest.property.optional.operations.UnionStringLiteralOperations
    :ivar union_int_literal: UnionIntLiteralOperations operations
    :vartype union_int_literal: typetest.property.optional.operations.UnionIntLiteralOperations
    :ivar union_float_literal: UnionFloatLiteralOperations operations
    :vartype union_float_literal: typetest.property.optional.operations.UnionFloatLiteralOperations
    :ivar required_and_optional: RequiredAndOptionalOperations operations
    :vartype required_and_optional:
     typetest.property.optional.operations.RequiredAndOptionalOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        self._config = OptionalClientConfiguration(**kwargs)
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.logging_policy,
            ]
        self._client: PipelineClient = PipelineClient(endpoint=endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.string = StringOperations(self._client, self._config, self._serialize, self._deserialize)
        self.bytes = BytesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.datetime = DatetimeOperations(self._client, self._config, self._serialize, self._deserialize)
        self.duration = DurationOperations(self._client, self._config, self._serialize, self._deserialize)
        self.collections_byte = CollectionsByteOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.collections_model = CollectionsModelOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.string_literal = StringLiteralOperations(self._client, self._config, self._serialize, self._deserialize)
        self.int_literal = IntLiteralOperations(self._client, self._config, self._serialize, self._deserialize)
        self.float_literal = FloatLiteralOperations(self._client, self._config, self._serialize, self._deserialize)
        self.boolean_literal = BooleanLiteralOperations(self._client, self._config, self._serialize, self._deserialize)
        self.union_string_literal = UnionStringLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.union_int_literal = UnionIntLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.union_float_literal = UnionFloatLiteralOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.required_and_optional = RequiredAndOptionalOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from corehttp.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~corehttp.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~corehttp.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
