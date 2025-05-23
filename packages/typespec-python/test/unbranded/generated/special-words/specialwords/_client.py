# coding=utf-8

from copy import deepcopy
from typing import Any
from typing_extensions import Self

from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import SpecialWordsClientConfiguration
from ._utils.serialization import Deserializer, Serializer
from .modelproperties.operations import ModelPropertiesOperations
from .models.operations import ModelsOperations
from .operations import Operations, ParametersOperations


class SpecialWordsClient:  # pylint: disable=client-accepts-api-version-keyword
    """Scenarios to verify that reserved words can be used in service and generators will handle it
    appropriately.

    Current list of special words

    .. code-block:: txt

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
       not
       or
       pass
       raise
       return
       try
       while
       with
       yield.

    :ivar models: ModelsOperations operations
    :vartype models: specialwords.operations.ModelsOperations
    :ivar model_properties: ModelPropertiesOperations operations
    :vartype model_properties: specialwords.operations.ModelPropertiesOperations
    :ivar operations: Operations operations
    :vartype operations: specialwords.operations.Operations
    :ivar parameters: ParametersOperations operations
    :vartype parameters: specialwords.operations.ParametersOperations
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
        self._client: PipelineClient = PipelineClient(endpoint=_endpoint, policies=_policies, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.models = ModelsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.model_properties = ModelPropertiesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.parameters = ParametersOperations(self._client, self._config, self._serialize, self._deserialize)

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
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
