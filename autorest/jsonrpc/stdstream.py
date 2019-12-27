# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import io
import json
import os
import logging
from pathlib import Path
import sys
from typing import BinaryIO

from jsonrpc.jsonrpc2 import JSONRPC20Request, JSONRPC20Response

from . import AutorestAPI, Channel


# Being we use "Message" as default logger, we can't propate this particular
# file or we'll get an infite loop
# If Logging at this deep level is expected, go with a config file
# https://docs.python.org/3.8/library/logging.config.html
_LOGGER = logging.getLogger(__name__)
_LOGGER.propagate = False


def read_message(stream: BinaryIO = sys.stdin.buffer) -> str:
    # Content-Length
    order = stream.readline().rstrip()

    if not order.startswith(b"Content-Length"):
        raise ValueError("I was expecting to see Content-Length")
    _LOGGER.info(f"Received: {order}")
    try:
        bytes_size = int(order.split(b":")[1].strip())
    except Exception as err:
        raise ValueError(f"Was unable to read length from {order}") from err
    # Double new line, so read another emptyline and ignore it
    stream.readline()

    # Read the right number of bytes
    _LOGGER.info("Trying to read the message")
    message = stream.read(bytes_size)
    assert isinstance(message, bytes)
    message = message.decode('utf-8')
    _LOGGER.info("Received a %d bytes message (push to DEBUG to see full message)", len(message))
    _LOGGER.debug("Read %s", message)

    return message


def write_message(message: str, stream: BinaryIO = sys.stdout.buffer) -> None:
    bytes_message = message.encode("utf-8")
    stream.write(b"Content-Length: ")
    stream.write(str(len(bytes_message)).encode("ascii"))
    stream.write(b"\r\n\r\n")
    stream.write(bytes_message)
    stream.flush()


class StdStreamAutorestAPI(AutorestAPI):
    """The stream API with Autorest
    """
    def __init__(self, session_id: str):
        super().__init__()
        self.session_id = session_id

    def write_file(self, filename: str, file_content: str) -> None:
        _LOGGER.debug(f"Writing a file: {filename}")
        filename = os.fspath(filename)
        request = JSONRPC20Request(
            method="WriteFile",
            params=[
                self.session_id,
                filename,
                file_content,
                None  # sourceMap ?
            ],
            is_notification=True
        )
        write_message(request.json)

    def read_file(self, filename: str) -> str:
        _LOGGER.debug(f"Asking content for file {filename}")
        filename = os.fspath(filename)
        request = JSONRPC20Request(
            method="ReadFile",
            params=[
                self.session_id,
                filename
            ],
            _id=42
        )
        write_message(request.json)
        return json.loads(read_message())["result"]

    def list_inputs(self):
        _LOGGER.debug("Calling list inputs to Autorest")
        request = JSONRPC20Request(
            method="ListInputs",
            params=[
                self.session_id,
                None
            ],
            _id=42
        )
        write_message(request.json)
        return json.loads(read_message())["result"]

    def get_value(self, key):
        _LOGGER.debug(f"Calling get value to Autorest: {key}")
        request = JSONRPC20Request(
            method="GetValue",
            params=[
                self.session_id,
                key
            ],
            _id=42
        )
        write_message(request.json)
        return json.loads(read_message())["result"]


    def message(self, channel: Channel, text: str) -> None:
        # https://github.com/Azure/autorest/blob/ad7f01ffe17aa74ad0075d6b1562a3fa78fd2e96/src/autorest-core/lib/message.ts#L53
        message = {
            'Channel': channel.value,
            'Text': text,
        }
        _LOGGER.debug(f"Sending a message to Autorest: {message}")
        request = JSONRPC20Request(
            method="Message",
            params=[
                self.session_id,
                message
            ],
            is_notification=True
        )
        write_message(request.json)
