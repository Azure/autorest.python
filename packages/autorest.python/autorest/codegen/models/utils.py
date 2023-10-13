# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import TypeVar, Dict
from .imports import FileImport, ImportType, TypingSection

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

def add_literal_import(file_import: FileImport):
    file_import.add_import("sys", ImportType.STDLIB)
    file_import.add_submodule_import(
        "typing_extensions",
        "Literal",
        ImportType.BYVERSION,
        TypingSection.REGULAR,
        None,
        (
            (
                (3, 8),
                "typing",
                "pylint: disable=no-name-in-module, ungrouped-imports",
            ),
        ),
    )
