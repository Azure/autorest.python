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
import logging

from jsonrpc import dispatcher, JSONRPCResponseManager

from .stdstream import read_message, write_message


_LOGGER = logging.getLogger(__name__)


@dispatcher.add_method
def GetPluginNames():
    return ["mapper"]

@dispatcher.add_method
def Process(plugin_name, session_id):
    _LOGGER.info("Process was called by Autorest")
    from ..code_generator import CodeGenerator
    from .stdstream import StdStreamAutorestAPI

    stdstream_connection = StdStreamAutorestAPI(session_id)
    code_generator = CodeGenerator(stdstream_connection)

    return code_generator.process()


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        filename="autorest_python.log"
    )

    _LOGGER.info("Starting JSON RPC server")

    while True:
        _LOGGER.info(f"Trying to read")
        message = read_message()

        response = JSONRPCResponseManager.handle(message, dispatcher).json
        _LOGGER.info(f"Produced: {response}")
        write_message(response)
        _LOGGER.info(f"Message processed")

    _LOGGER.info("Ending JSON RPC server")

if __name__ == "__main__":
    main()