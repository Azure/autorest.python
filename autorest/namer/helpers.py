# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from .python_mappings import PadType, RESERVED_WORDS

def to_snake_case(name: str) -> str:
    def replace_upper_characters(m: re.Match[str]) -> str:
        match_str = m.group().lower()
        if m.start() > 0 and name[m.start() - 1] == "_":
            # we are good if a '_' already exists
            return match_str
        # the first letter should not have _
        prefix = "_" if m.start() > 0 else ""

        # we will add an extra _ if there are multiple upper case chars together
        next_non_upper_case_char_location = m.start() + len(match_str)
        if (
            len(match_str) > 2
            and len(name) - next_non_upper_case_char_location > 1
            and name[next_non_upper_case_char_location].isalpha()
        ):

            return (
                prefix
                + match_str[: len(match_str) - 1]
                + "_"
                + match_str[len(match_str) - 1]
            )

        return prefix + match_str

    return re.sub("[A-Z]+", replace_upper_characters, name)


def pad_reserved_words(name: str, pad_type: PadType):
    # we want to pad hidden variables as well
    if not name:
        # we'll pass in empty operation groups sometime etc.
        return name
    name_prefix = "_" if name[0] == "_" else ""
    name = name[1:] if name[0] == "_" else name
    if name.lower() in RESERVED_WORDS[pad_type]:
        return name_prefix + name + pad_type
    return name_prefix + name
