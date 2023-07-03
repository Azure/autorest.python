# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from azure.core.pipeline import PipelineRequest

from .utils.validation import validate_format, Format


def check_header(request: PipelineRequest, header: str, checked: dict):
    validate_format(
        request.http_request.headers[header], Format.UUID
    )
    checked[header] = request.http_request.headers[header]
