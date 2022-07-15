# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
import argparse

def to_snake_case(name: str) -> str:
    def replace_upper_characters(m) -> str:
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

def parse_args(need_cadl_file: bool = True):
    parser = argparse.ArgumentParser(
        description="Run mypy against target folder. Add a local custom plugin to the path prior to execution. "
    )
    parser.add_argument(
        "--output-folder",
        dest="output_folder",
        help="Output folder for generated SDK",
        required=True,
    )
    parser.add_argument(
        "--cadl-file",
        dest="cadl_file",
        help="Serialized cadl file",
        required=need_cadl_file
    )

    return parser.parse_args()
