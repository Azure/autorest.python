# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
import sys
from typing import Any, Dict, List, Optional
from pathlib import Path

_LOGGER = logging.getLogger(__name__)

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

def _get_default_api_version_from_list(
    mod_to_api_version: Dict[str, str],
    api_versions_list: List[str],
    preview_mode: bool,
    default_api: Optional[str]
) -> str:
    """Get the floating latest, from a random list of API versions.
    """

    # I need default_api to be v2019_06_07_preview shaped if it exists, let's be smart
    # and change it automatically so I can take both syntax as input
    if default_api and not default_api.startswith("v"):
        default_api_version = [
            mod_api
            for mod_api, real_api in mod_to_api_version.items()
            if real_api == default_api
        ][0]
        _LOGGER.info("Default API version will be: %s", default_api_version)
        return default_api_version

    absolute_latest = sorted(api_versions_list)[-1]
    not_preview_versions = [
        version for version in api_versions_list if "preview" not in version
    ]

    # If there is no preview, easy: the absolute latest is the only latest
    if not not_preview_versions:
        return absolute_latest

    # If preview mode, let's use the absolute latest, I don't care preview or stable
    if preview_mode:
        return absolute_latest

    # If not preview mode, and there is preview, take the latest known stable
    return sorted(not_preview_versions)[-1]
