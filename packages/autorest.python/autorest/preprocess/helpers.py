# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from typing import Any, Dict
from .python_mappings import (
    PadType,
    RESERVED_WORDS,
    REDEFINED_BUILTINS,
    BUILTIN_PACKAGES,
)


def pad_reserved_words(name: str, pad_type: PadType):
    # we want to pad hidden variables as well
    if not name:
        # we'll pass in empty operation groups sometime etc.
        return name
    name = pad_special_chars(name)
    name_prefix = "_" if name[0] == "_" else ""
    name = name[1:] if name[0] == "_" else name
    if name.lower() in RESERVED_WORDS[pad_type]:
        return name_prefix + name + pad_type
    return name_prefix + name


def add_redefined_builtin_info(name: str, yaml_data: Dict[str, Any]) -> None:
    if name in REDEFINED_BUILTINS:
        yaml_data["pylintDisable"] = "redefined-builtin"


def pad_builtin_namespaces(namespace: str) -> str:
    items = namespace.split(".")
    if items[0] in BUILTIN_PACKAGES:
        items[0] = items[0] + "_"
    return ".".join(items)

def pad_special_chars(name: str) -> str:
    return re.sub(r"[^A-z0-9_]", "_", name)
