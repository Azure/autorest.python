# coding=utf-8

from copy import deepcopy
from typing import Any, TYPE_CHECKING, Union
from typing_extensions import Self

from corehttp.credentials import ServiceKeyCredential
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime import PipelineClient, policies

from ._configuration import UnionClientConfiguration
from ._operations import _UnionClientOperationsMixin
from ._utils.serialization import Deserializer, Serializer

if TYPE_CHECKING:
    from corehttp.credentials import TokenCredential


class UnionClient(_UnionClientOperationsMixin):  # pylint: disable=client-accepts-api-version-keyword
    """Illustrates clients generated with ApiKey and OAuth2 authentication.

    :param credential: Credential used to authenticate requests to the service. Is either a key
     credential type or a token credential type. Required.
    :type credential: ~corehttp.credentials.ServiceKeyCredential or
     ~corehttp.credentials.TokenCredential
    :keyword endpoint: Service host. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(
        self,
        credential: Union[ServiceKeyCredential, "TokenCredential"],
        *,
        endpoint: str = "http://localhost:3000",
        **kwargs: Any
    ) -> None:
        _endpoint = "{endpoint}"
        self._config = UnionClientConfiguration(credential=credential, endpoint=endpoint, **kwargs)

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
