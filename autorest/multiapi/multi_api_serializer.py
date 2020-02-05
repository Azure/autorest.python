# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from jinja2 import Environment


class MultiAPISerializer:
    def __init__(self, output_folder: str, env: Environment):
        self.output_folder = output_folder
        self.env = env
