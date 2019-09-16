import json
import logging
import sys

from jsonrpc import dispatcher, JSONRPCResponseManager
from jsonrpc.jsonrpc2 import JSONRPC20Request, JSONRPC20Response

_LOGGER = logging.getLogger()


@dispatcher.add_method
def GetPluginNames():
    return ["mapper"]

@dispatcher.add_method
def Process(plugin_name, session_id):
    _LOGGER.info("Process was called by Autorest")
    inputs = list_inputs(session_id)
    _LOGGER.info(f"Inputs: {inputs}")
    filename = inputs[0]
    file_content = read_file(session_id, filename)
    write_file(session_id, filename, file_content)

    from .code_generator import generate
    generate(file_content, session_id)

    return True

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
    _LOGGER.info(f"Read {message}")

    return message


def write_message(message, stream=sys.stdout.buffer):
    bytes_message = message.encode("utf-8")
    stream.write(b"Content-Length: ")
    stream.write(str(len(bytes_message)).encode("ascii"))
    stream.write(b"\r\n\r\n")
    stream.write(bytes_message)
    stream.flush()

def list_inputs(session_id):
    _LOGGER.info("Calling list inputs to Autorest")
    request = JSONRPC20Request(
        method="ListInputs",
        params=[
            session_id,
            None
        ],
        _id=42
    )
    write_message(request.json)
    return json.loads(read_message())["result"]

def get_value(session_id, key):
    _LOGGER.info(f"Calling get value to Autorest: {key}")
    request = JSONRPC20Request(
        method="GetValue",
        params=[
            session_id,
            key
        ],
        _id=42
    )
    write_message(request.json)
    return json.loads(read_message())["result"]


def message(session_id, message):
    _LOGGER.info(f"Sending a message to Autorest: {message}")
    request = JSONRPC20Request(
        method="Message",
        params=[
            session_id,
            message
        ],
        is_notification=True
    )
    write_message(request.json)

def write_file(session_id, filename, file_content):
    _LOGGER.info(f"Writing a file: {filename}")
    request = JSONRPC20Request(
        method="WriteFile",
        params=[
            session_id,
            filename,
            file_content,
            None  # sourceMap ?
        ],
        is_notification=True
    )
    write_message(request.json)


def read_file(session_id, filename):
    _LOGGER.info(f"Asking content for file {filename}")
    request = JSONRPC20Request(
        method="ReadFile",
        params=[
            session_id,
            filename
        ],
        _id=42
    )
    write_message(request.json)
    return json.loads(read_message())["result"]


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        filename="autorest_python.log"
    )

    _LOGGER.info("Starting JSON RPC server")

    while True:
        _LOGGER.info(f"Trying to read")
        # order = sys.stdin.readline().rstrip()
        # _LOGGER.info(f"Received: {order!a}")

        # if order.startswith("Content-Length") or not order:
        #     _LOGGER.info(f"Skipping: {order}")
        #     continue
        message = read_message()

        response = JSONRPCResponseManager.handle(message, dispatcher).json
        _LOGGER.info(f"Produced: {response}")
        write_message(response)
        _LOGGER.info(f"Message processed")

    _LOGGER.info("Ending JSON RPC server")

if __name__ == "__main__":
    main()