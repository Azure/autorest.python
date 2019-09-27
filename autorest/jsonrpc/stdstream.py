# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import json
import logging
from pathlib import Path
import sys

from jsonrpc.jsonrpc2 import JSONRPC20Request, JSONRPC20Response

from . import AutorestAPI


_LOGGER = logging.getLogger(__name__)


def read_message(stream = sys.stdin):
    # Content-Length
    order = stream.readline().rstrip()

    if not order.startswith("Content-Length"):
        raise ValueError("I was expecting to see Content-Length")
    _LOGGER.info(f"Received: {order}")
    try:
        bytes_size = int(order.split(":")[1].strip())
    except Exception as err:
        raise ValueError(f"Was unable to read length from {order}") from err
    # Double new line, so read another emptyline and ignore it
    stream.readline()

    # Read the right number of bytes
    _LOGGER.info("Trying to read the message")
    message = stream.read(bytes_size)
    _LOGGER.info("Received a %d bytes message (push to DEBUG to see full message)", len(message))
    _LOGGER.debug("Read %s", message)

    return message


def write_message(message, stream=sys.stdout.buffer):
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
        self.session_id = session_id

    def write_file(self, filename: str, file_content: str) -> None:
        _LOGGER.debug(f"Writing a file: {filename}")
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


    def message(self, message):
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
