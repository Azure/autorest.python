# coding=utf-8

from copy import deepcopy
from typing import Any, Awaitable
from typing_extensions import Self

from corehttp.rest import AsyncHttpResponse, HttpRequest
from corehttp.runtime import AsyncPipelineClient, policies

from .._utils.serialization import Deserializer, Serializer
from ..modelproperties.aio.operations import SpecialWordsClientModelPropertiesOperations
from ..models.aio.operations import SpecialWordsClientModelsOperations
from ._configuration import SpecialWordsClientConfiguration
from .operations import SpecialWordsClientOperationsOperations, SpecialWordsClientParametersOperations


class SpecialWordsClient:  # pylint: disable=client-accepts-api-version-keyword
    """Scenarios to verify that reserved words can be used in service and generators will handle it
    appropriately.

    Current list of special words

    .. code-block:: text

       and
       as
       assert
       async
       await
       break
       class
       constructor
       continue
       def
       del
       elif
       else
       except
       exec
       finally
       for
       from
       global
       if
       import
       in
       is
       lambda
       list
       not
       or
       pass
       raise
       return
       try
       while
       with
       yield.

    :ivar special_words_client_models: SpecialWordsClientModelsOperations operations
    :vartype special_words_client_models:
     specialwords.aio.operations.SpecialWordsClientModelsOperations
    :ivar special_words_client_model_properties: SpecialWordsClientModelPropertiesOperations
     operations
    :vartype special_words_client_model_properties:
     specialwords.aio.operations.SpecialWordsClientModelPropertiesOperations
    :ivar special_words_client_operations: SpecialWordsClientOperationsOperations operations
    :vartype special_words_client_operations:
     specialwords.aio.operations.SpecialWordsClientOperationsOperations
    :ivar special_words_client_parameters: SpecialWordsClientParametersOperations operations
    :vartype special_words_client_parameters:
     specialwords.aio.operations.SpecialWordsClientParametersOperations
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self, *, endpoint: str = "http://localhost:3000", **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = SpecialWordsClientConfiguration(endpoint=endpoint, **kwargs)

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
        self._client: AsyncPipelineClient = AsyncPipelineClient(endpoint=_endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.special_words_client_models = SpecialWordsClientModelsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.special_words_client_model_properties = SpecialWordsClientModelPropertiesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.special_words_client_operations = SpecialWordsClientOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.special_words_client_parameters = SpecialWordsClientParametersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from corehttp.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client.send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~corehttp.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~corehttp.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> Self:
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
