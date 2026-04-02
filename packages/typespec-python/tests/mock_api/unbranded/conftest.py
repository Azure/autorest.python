# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
# Unbranded-specific fixtures
# Common fixtures (testserver, core_library, key_credential, png_data, jpg_data)
# are inherited from the root tests/conftest.py

import pytest
from typing import List


SPECIAL_WORDS = [
    "and",
    "as",
    "assert",
    "async",
    "await",
    "break",
    "class",
    "constructor",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "exec",
    "finally",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "try",
    "while",
    "with",
    "yield",
]


@pytest.fixture
def special_words() -> List[str]:
    return SPECIAL_WORDS
