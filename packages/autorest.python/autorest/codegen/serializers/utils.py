# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from pathlib import Path
from typing import Dict, Any


def method_signature_and_response_type_annotation_template(
    *,
    method_signature: str,
    response_type_annotation: str,
) -> str:
    return f"{method_signature} -> {response_type_annotation}:"


def extract_sample_name(sample: Dict[str, Any]) -> str:
    file = sample.get("x-ms-original-file", "sample.json").split("specification")[-1]
    return Path(file).parts[-1].replace(".json", "")


def invalid_file_name(name: str) -> bool:
    return bool(len(name) > 80 or re.compile("[^a-z0-9_]+").findall(name))
