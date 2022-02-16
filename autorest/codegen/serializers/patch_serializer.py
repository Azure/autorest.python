# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from jinja2 import Environment

class PatchSerializer:
    def __init__(self, env: Environment) -> None:
        self.env = env

    def serialize(self) -> str:
        template = self.env.get_template("patch.py.jinja2")
        return template.render()
