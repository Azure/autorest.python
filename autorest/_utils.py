# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
from pathlib import Path


def get_output_folder(output_folder_uri: str) -> Path:
    if output_folder_uri.startswith("file:"):
        output_folder_uri = output_folder_uri[5:]
    if os.name == "nt" and output_folder_uri.startswith("///"):
        output_folder_uri = output_folder_uri[3:]
    return Path(output_folder_uri)
