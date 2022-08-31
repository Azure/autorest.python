# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Union
from pathlib import Path
import re
import argparse
import black

_BLACK_MODE = black.Mode()
_BLACK_MODE.line_length = 120


def format_file(
    file: Union[Path, str], file_content: str, enable_format: bool = True
) -> str:
    if not enable_format or Path(file).suffix != ".py":
        return file_content
    try:
        return black.format_file_contents(file_content, fast=True, mode=_BLACK_MODE)
    except black.NothingChanged:
        return file_content


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
        required=need_cadl_file,
    )
    parser.add_argument(
        "--debug",
        dest="debug",
        help="Debug mode",
        required=False,
        action="store_true",
    )
    return parser.parse_args()


def get_body_type_for_description(body_parameter: Dict[str, Any]) -> str:
    if body_parameter["type"]["type"] == "binary":
        return "binary"
    if body_parameter["type"]["type"] == "string":
        return "string"
    return "JSON"


# used if we want to get a string / binary type etc
KNOWN_TYPES: Dict[str, Dict[str, Any]] = {
    "string": {"type": "string"},
    "binary": {"type": "binary"},
    "anydict": {"type": "dict", "elementType": {"type": "any"}},
}

JSON_REGEXP = re.compile(r"^(application|text)/(.+\+)?json$")
