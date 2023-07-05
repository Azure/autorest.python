# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from azure.core.pipeline import PipelineRequest

from .utils.validation import validate_format, Format


def check_repeatability_header(request: PipelineRequest):
    validate_format(
        request.http_request.headers["Repeatability-Request-ID"], Format.UUID
    )
    validate_format(
        request.http_request.headers["Repeatability-First-Sent"], Format.RFC7231
    )


def check_request_id_header(request: PipelineRequest, header: str, checked: dict):
    validate_format(request.http_request.headers[header], Format.UUID)
    checked[header] = request.http_request.headers[header]
