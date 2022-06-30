# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
import re

_LOGGER = logging.getLogger(__name__)


def method_signature_and_response_type_annotation_template(
    *,
    method_signature: str,
    response_type_annotation: str,
) -> str:
    return f"{method_signature} -> {response_type_annotation}:"


def to_snake_case(name: str) -> str:
    return re.sub(
        "((?!^)(?<!_)[A-Z][a-z]+|(?<=[a-z0-9])[A-Z])",
        r"_\1",
        name.replace("-", "").replace(" ", "_"),
    ).lower()
