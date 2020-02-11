# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from jinja2 import Environment, PackageLoader
from typing import Dict, List, Union


class MultiAPISerializer:
    def __init__(self, conf, output_filename):
        self.conf = conf
        self.output_filename = output_filename
        self.env = Environment(
            loader=PackageLoader("autorest.multiapi", "templates"),
            keep_trailing_newline=True,
            line_statement_prefix="##",
            line_comment_prefix="###",
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def serialize(self) -> str:
        template = self.env.get_template("multiapi_service_client.py.jinja2")
        result = template.render(**self.conf)

        with self.output_filename.open("w") as fd:
            fd.write(result)
