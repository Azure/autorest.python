# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from typing import Any, TypeVar, Dict, TYPE_CHECKING, List, Set
import logging

from .imports import FileImport, ImportModel, ImportType, TypingSection


_LOGGER = logging.getLogger(__name__)

JSON_REGEXP = re.compile(r"^(application|text)/(.+\+)?json$")

T = TypeVar("T")
OrderedSet = Dict[T, None]

def add_to_description(description: str, entry: str) -> str:
    if description:
        return f"{description} {entry}"
    return entry

def define_mutable_mapping_type(file_import: FileImport) -> FileImport:
    file_import.define_mypy_type(
        "JSON",
        "MutableMapping[str, Any] # pylint: disable=unsubscriptable-object",
        None,
        {
            (3, 9): ImportModel(
                TypingSection.CONDITIONAL,
                ImportType.STDLIB,
                "collections.abc",
                submodule_name="MutableMapping",
            ),
            None: ImportModel(
                TypingSection.CONDITIONAL,
                ImportType.STDLIB,
                "typing",
                submodule_name="MutableMapping",
            ),
        },
    )
    return file_import
