# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import re
from typing import Iterator

_VALID_UUID = re.compile(r"^[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}$")
_VALID_RFC7231 = re.compile(
    r"^(Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s\d{2}\s"
    r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}\s\d{2}:\d{2}:\d{2}\sGMT$"
)


class Format(str):
    UUID = "uuid"
    RFC7231 = "rfc7231"


def validate_format(value: str, format: Format):
    if format == Format.UUID:
        assert _VALID_UUID.match(value)
    elif format == Format.RFC7231:
        assert _VALID_RFC7231.match(value)
    else:
        raise ValueError("Unknown format")


async def iter_bytes_to_bytes_async(data: Iterator[bytes]) -> bytes:
    return b"".join([chunk async for chunk in data])


def iter_bytes_to_bytes(data: Iterator[bytes]) -> bytes:
    return b"".join(list(data))
