# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
import re

from .python_mappings import primary_types, basic_latin_chars, reserved_words


_LOGGER = logging.getLogger(__name__)


def to_python_type(original_type):
    try:
        return primary_types[original_type]
    except KeyError as e:
        _LOGGER.critical("The type you are trying to convert to Python is not a known type")
        return "KEYERROR" # FIXME
