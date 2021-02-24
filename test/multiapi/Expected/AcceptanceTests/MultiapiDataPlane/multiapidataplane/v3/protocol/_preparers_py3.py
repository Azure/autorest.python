# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import IO, Optional, Union

from azure.core.pipeline.transport import HttpRequest


def _test_paging_request(
    self,
    **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/paging')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

    return self._client.get(url, query_parameters, header_parameters)

def _test_different_calls_request(
    self,
    greeting_in_english: str,
    greeting_in_chinese: Optional[str] = None,
    greeting_in_french: Optional[str] = None,
    **kwargs
) -> HttpRequest:
    api_version = "3.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/testDifferentCalls')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['greetingInEnglish'] = self._serialize.header("greeting_in_english", greeting_in_english, 'str')
    if greeting_in_chinese is not None:
        header_parameters['greetingInChinese'] = self._serialize.header("greeting_in_chinese", greeting_in_chinese, 'str')
    if greeting_in_french is not None:
        header_parameters['greetingInFrench'] = self._serialize.header("greeting_in_french", greeting_in_french, 'str')
    header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

    return self._client.get(url, query_parameters, header_parameters)

def _test_two_request(
    self,
    body: Optional["_models.ModelThree"] = None,
    **kwargs
) -> HttpRequest:
    api_version = "3.0.0"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/one/testTwoEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
    header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs['content'] = body
    return self._client.get(url, query_parameters, header_parameters, **body_content_kwargs)

def _test_four_request(
    self,
    body: Optional[Union[IO, "_models.SourcePath"]] = None,
    **kwargs
) -> HttpRequest:
    api_version = "3.0.0"
    content_type = kwargs.pop("content_type", "application/json")
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/two/testFourEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
    header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    if header_parameters['Content-Type'].split(";")[0] in ['application/pdf', 'image/jpeg', 'image/png', 'image/tiff']:
        body_content_kwargs['stream_content'] = body

    elif header_parameters['Content-Type'].split(";")[0] in ['application/json']:
        body_content_kwargs['content'] = body
    else:
        raise ValueError(
            "The content_type '{}' is not one of the allowed values: "
            "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(header_parameters['Content-Type'])
        )
    return self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

def _test_five_request(
    self,
    **kwargs
) -> HttpRequest:
    api_version = "3.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/two/testFiveEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

    return self._client.put(url, query_parameters, header_parameters)
