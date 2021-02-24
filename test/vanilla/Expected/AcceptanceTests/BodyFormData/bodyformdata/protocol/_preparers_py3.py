# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import IO, List

from azure.core.pipeline.transport import HttpRequest


def _upload_file_request(body: IO, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "multipart/form-data")
    accept = "application/octet-stream, application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfile")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["form_content"] = body

    return self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)


def _upload_file_via_body_request(body: IO, **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "application/octet-stream")
    accept = "application/octet-stream, application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfile")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["stream_content"] = body

    return self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)


def _upload_files_request(body: List[IO], **kwargs) -> HttpRequest:
    content_type = kwargs.pop("content_type", "multipart/form-data")
    accept = "application/octet-stream, application/json"

    # Construct URL
    url = kwargs.pop("template_url", "/formdata/stream/uploadfiles")

    # Construct parameters
    query_parameters = {}  # type: Dict[str, Any]

    # Construct headers
    header_parameters = {}  # type: Dict[str, Any]
    header_parameters["Content-Type"] = self._serialize.header("content_type", content_type, "str")
    header_parameters["Accept"] = self._serialize.header("accept", accept, "str")

    body_content_kwargs = {}  # type: Dict[str, Any]
    body_content_kwargs["form_content"] = body

    return self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
