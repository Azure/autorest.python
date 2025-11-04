# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from pathlib import Path
import hashlib

_FILE_PATH = Path(__file__)


def _string_to_hash_id(input_string: str) -> str:
    """Converts a string to a SHA256 hash ID.

    Args:
        input_string (str): The string to be hashed.

    Returns:
        str: The hexadecimal representation of the SHA256 hash.
    """
    encoded_string = input_string.encode("utf-8")
    hasher = hashlib.sha256()
    hasher.update(encoded_string)
    return hasher.hexdigest()


EXPECTED_HASH = "REPLACE_ME"


def test_docstring_generation():
    target = (
        _FILE_PATH.parent.parent
        / "generated"
        / "docstring"
        / "docstring"
        / "models"
        / "_models.py"
    )
    assert target.exists(), f"Generated models file not found: {target}" 
    content = target.read_text(encoding="utf-8")
    hash_id = _string_to_hash_id(content)
    assert (
        hash_id == EXPECTED_HASH
    ), f"Docstring generation changed unexpectedly. New hash {hash_id}. Update EXPECTED_HASH if intentional."
