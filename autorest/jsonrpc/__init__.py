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
from typing import List


class AutorestAPI:
    """Defines the base interface of communication to Autorest from the plugin.
    """

    def write_file(self, filename: str, file_content: str) -> None:
        """Ask autorest to write the content to the current path.

        pathlib.Path object are acceptable but must be relative.

        :param filename: A file path
        :param file_content: The content as string
        """
        pass

    def read_file(self, filename: str) -> str:
        """Ask autorest to read a file for me.

        pathlib.Path object are acceptable but must be relative.

        :param filename: A file path
        :return: The content of the file
        :rtype: str
        """
        pass

    def list_inputs(self) -> List[str]:
        pass

    def get_value(self, key: str) -> str:
        pass

    def message(self, message) -> None:
        pass

    def get_boolean_value(self, key: str) -> bool:
        """Get a value and interpret it as a boolean.

        For the JSON testserver, empty dict means "it was on the line", so we want it to true.
        """
        result = self.get_value(key)
        if result is None:
            return False
        if isinstance(result, bool):
            return result
        return result == {} or result.lower() == "true" or result == 1