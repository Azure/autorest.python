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
