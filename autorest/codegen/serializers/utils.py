# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
def method_signature_and_response_type_annotation_template(
    *,
    is_python3_file: bool,
    method_signature: str,
    response_type_annotation: str,
) -> str:
    if is_python3_file:
        return f"{method_signature} -> {response_type_annotation}:"
    return f"{method_signature}:\n    # type: (...) -> {response_type_annotation}"


SAMPLE_AAD_ANNOTATION = """
    Please set the values of the client ID, tenant ID and client secret of the AAD application as environment variables:
    AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET.
    For more info about how to get the value, please see https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal"""

SAMPLE_KEY_ANNOTATION = """
    Please set environment variables "AZURE_KEY" with real value which can access your service"""
