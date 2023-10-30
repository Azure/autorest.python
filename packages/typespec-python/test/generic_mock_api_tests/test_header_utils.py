# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

def check_repeatability_header(request, validate_format):
    validate_format(
        request.http_request.headers["Repeatability-Request-ID"], "uuid"
    )
    validate_format(
        request.http_request.headers["Repeatability-First-Sent"], "rfc7231"
    )


def check_client_request_id_header(request, header: str, checked: dict):
    validate_format(request.http_request.headers[header], Format.UUID)
    checked[header] = request.http_request.headers[header]
