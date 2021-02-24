# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Optional

from azure.core.pipeline.transport import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()

def _test_one_request(
    id: int,
    message: Optional[str] = None,
    **kwargs
) -> HttpRequest:
    api_version = "2.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testOneEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['id'] = _SERIALIZER.query("id", id, 'int')
    if message is not None:
        query_parameters['message'] = _SERIALIZER.query("message", message, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return self._client.put(url, query_parameters, header_parameters)

def _test_different_calls_request(
    greeting_in_english: str,
    greeting_in_chinese: Optional[str] = None,
    **kwargs
) -> HttpRequest:
    api_version = "2.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testDifferentCalls')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['greetingInEnglish'] = _SERIALIZER.header("greeting_in_english", greeting_in_english, 'str')
    if greeting_in_chinese is not None:
        header_parameters['greetingInChinese'] = _SERIALIZER.header("greeting_in_chinese", greeting_in_chinese, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return self._client.get(url, query_parameters, header_parameters)

def _test_two_request(
    body: Optional["_models.ModelTwo"] = None,
    **kwargs
) -> HttpRequest:
    api_version = "2.0.0"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/one/testTwoEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs['content'] = body
    return self._client.get(url, query_parameters, header_parameters, **body_content_kwargs)

def _test_three_request(
    **kwargs
) -> HttpRequest:
    api_version = "2.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/one/testThreeEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return self._client.put(url, query_parameters, header_parameters)

def _test_four_request(
    parameter_one: bool,
    **kwargs
) -> HttpRequest:
    api_version = "2.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/two/testFourEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['parameterOne'] = _SERIALIZER.query("parameter_one", parameter_one, 'bool')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return self._client.post(url, query_parameters, header_parameters)
