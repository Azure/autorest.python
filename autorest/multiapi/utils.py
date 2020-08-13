# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict
from pathlib import Path

def _extract_version(metadata_json: Dict[str, Any], version_path: Path) -> str:
    version = metadata_json['chosen_version']
    total_api_version_list = metadata_json['total_api_version_list']
    if not version:
        if total_api_version_list:
            sys.exit(
                f"Unable to match {total_api_version_list} to label {version_path.stem}"
            )
        else:
            sys.exit(
                f"Unable to extract api version of {version_path.stem}"
            )
    return version

def _sync_or_async(async_mode: bool) -> str:
    return "async" if async_mode else "sync"