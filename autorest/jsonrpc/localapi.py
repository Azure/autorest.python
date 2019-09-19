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
from pathlib import Path
from typing import List

from . import AutorestAPI


_LOGGER = logging.getLogger(__name__)


class LocalAutorestAPI(AutorestAPI):
    """A local API that will write on local disk.
    """
    def __init__(self, reachable_files: List[str] = None):
        if reachable_files is None:
            reachable_files = []
        self._reachable_files = reachable_files

    def write_file(self, filename: str, file_content: str) -> None:
        _LOGGER.debug("Writing file: %s", filename)
        with Path(filename).open('w') as fd:
            fd.write(file_content)
        _LOGGER.debug("Written file: %s", filename)

    def read_file(self, filename: str) -> str:
        _LOGGER.debug("Reading file: %s", filename)
        with Path(filename).open('r') as fd:
            return fd.read()

    def list_inputs(self) -> List[str]:
        return self._reachable_files

    def get_value(self, key: str) -> str:
        pass

    def message(self, message) -> None:
        pass