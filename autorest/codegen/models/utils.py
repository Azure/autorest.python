# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from typing import Any, TypeVar, Dict, TYPE_CHECKING, List, Set
import logging


_LOGGER = logging.getLogger(__name__)

JSON_REGEXP = re.compile(r"^(application|text)/(.+\+)?json$")

T = TypeVar("T")
OrderedSet = Dict[T, None]

def add_to_description(description: str, entry: str) -> str:
    if description:
        return f"{description} {entry}"
    return entry

