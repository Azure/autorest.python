# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import TypeVar, Dict

T = TypeVar("T")
OrderedSet = Dict[T, None]

NAME_LENGTH_LIMIT = 40


def add_to_description(description: str, entry: str) -> str:
    if description:
        return f"{description} {entry}"
    return entry


def add_to_pylint_disable(curr_str: str, entry: str) -> str:
    if curr_str:
        return f"{curr_str},{entry}"
    return f"  # pylint: disable={entry}"


def typing_name(
    file_name: str, internal: bool, need_module_name: bool, type_name: str
) -> str:
    # in _operations.py, models is imported with alias "_models"
    module = "_models." if need_module_name else ""
    return module + (f"{file_name}." if internal else "") + type_name
