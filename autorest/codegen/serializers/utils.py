# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from typing import Any
from pathlib import Path
from autorest.codegen.models.operation import OperationBase


def method_signature_and_response_type_annotation_template(
    *,
    method_signature: str,
    response_type_annotation: str,
) -> str:
    return f"{method_signature} -> {response_type_annotation}:"


def operation_additional(operation: OperationBase[Any]) -> str:
    lro = ".result()"
    paging = "\n    response = [item for item in response]"
    if operation.operation_type == "paging":
        return "\n    response = [item for item in response]"
    if operation.operation_type == "lro":
        return ".result()"
    if operation.operation_type == "lropaging":
        return lro + paging
    return ""


def to_lower_camel_case(name: str) -> str:
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), name)


def to_snake_case(name: str) -> str:
    return re.sub(
        "((?!^)(?<!_)[A-Z][a-z]+|(?<=[a-z0-9])[A-Z])",
        r"_\1",
        name.replace("-", "").replace(" ", "_"),
    ).lower()


# find root folder where "setup.py" is
def package_root_folder(namespace: str, namespace_path: Path) -> Path:
    return namespace_path / Path("../" * (namespace.count(".") + 1))
