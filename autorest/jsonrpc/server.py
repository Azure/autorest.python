# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
import logging
import sys

from jsonrpc import dispatcher, JSONRPCResponseManager

from .stdstream import read_message, write_message


_LOGGER = logging.getLogger(__name__)


@dispatcher.add_method
def GetPluginNames():
    return ["mapper", "python/m2r"]

@dispatcher.add_method
def Process(plugin_name, session_id):
    _LOGGER.debug("Process was called by Autorest")
    from ..code_generator import CodeGenerator
    from .stdstream import StdStreamAutorestAPI

    stdstream_connection = StdStreamAutorestAPI(session_id)
    code_generator = CodeGenerator(stdstream_connection)

    try:
        return code_generator.process()
    except Exception as err:
        _LOGGER.exception("Python generator raised an exception")


def main():
    if os.environ.get("AUTOREST_PYTHON_ATTACH_VSCODE_DEBUG", False):
        try:
            import ptvsd
        except ImportError:
            raise SystemExit("Please pip install ptvsd in order to use VSCode debugging")

        # 5678 is the default attach port in the VS Code debug configurations
        print("Waiting for debugger attach")
        ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
        ptvsd.wait_for_attach()
        breakpoint()

    _LOGGER.debug("Starting JSON RPC server")

    while True:
        _LOGGER.debug("Trying to read")
        message = read_message()

        response = JSONRPCResponseManager.handle(message, dispatcher).json
        _LOGGER.debug("Produced: %s", response)
        write_message(response)
        _LOGGER.debug("Message processed")

    _LOGGER.debug("Ending JSON RPC server")

if __name__ == "__main__":
    main()