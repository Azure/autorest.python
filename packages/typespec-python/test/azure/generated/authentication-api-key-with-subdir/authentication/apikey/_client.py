# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from ._generated import ApiKeyClient


class CustomizedApiKeyClient(ApiKeyClient):

    def custom_method(self) -> str:
        """
        A custom method that does something specific.

        :param param1: A string parameter.
        :param param2: An integer parameter.
        :return: A string result.
        """
        # Custom logic here
        return "Hello, world!"
