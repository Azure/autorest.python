# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import IO, Optional, Union

from azure.core.pipeline.transport import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()

def _prepare_test_paging_request(
    **kwargs
) -> HttpRequest:
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/paging')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request

def _prepare_test_different_calls_request(
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
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['greetingInEnglish'] = _SERIALIZER.header("greeting_in_english", greeting_in_english, 'str')
    if greeting_in_chinese is not None:
        header_parameters['greetingInChinese'] = _SERIALIZER.header("greeting_in_chinese", greeting_in_chinese, 'str')
    if greeting_in_french is not None:
        header_parameters['greetingInFrench'] = _SERIALIZER.header("greeting_in_french", greeting_in_french, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request

def _prepare_operationgroupone_test_two_request(
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
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    content = body

    request = HttpRequest(
        method="GET",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request

def _prepare_operationgrouptwo_test_four_request(
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
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    body_content_kwargs = {}  # type: Dict[str, Any]
    if header_parameters['Content-Type'].split(";")[0] in ['application/pdf', 'image/jpeg', 'image/png', 'image/tiff']:
        content = body

    elif header_parameters['Content-Type'].split(";")[0] in ['application/json']:
        content = body
    else:
        raise ValueError(
            "The content_type '{}' is not one of the allowed values: "
            "['application/pdf', 'image/jpeg', 'image/png', 'image/tiff', 'application/json']".format(header_parameters['Content-Type'])
        )

    request = HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        json=content,
        query=query_parameters,
    )
    return request

def _prepare_operationgrouptwo_test_five_request(
    **kwargs
) -> HttpRequest:
    api_version = "3.0.0"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/multiapi/two/testFiveEndpoint')

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    
    request = HttpRequest(
        method="PUT",
        url=url,
        headers=header_parameters,
        query=query_parameters,
    )
    return request
