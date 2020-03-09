# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict
from jinja2 import Environment, PackageLoader


class MultiAPISerializer:
    def __init__(self, conf: Dict[str, Any]) -> None:
        self.conf = conf
        self.env = Environment(
            loader=PackageLoader("autorest.multiapi", "templates"),
            keep_trailing_newline=True,
            line_statement_prefix="##",
            line_comment_prefix="###",
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def serialize_multiapi_client(self) -> str:
        template = self.env.get_template("multiapi_service_client.py.jinja2")
        return template.render(**self.conf)

    def serialize_multiapi_config(self) -> str:
        template = self.env.get_template("multiapi_config.py.jinja2")
        return template.render(
            client_name=self.conf["client_name"],
            package_name=self.conf["package_name"],
            **self.conf["config"]
        )

    def serialize_multiapi_models(self) -> str:
        template = self.env.get_template("multiapi_models.py.jinja2")
        return template.render(**self.conf)

    def serialize_multiapi_version(self) -> str:
        template = self.env.get_template("multiapi_version.py.jinja2")
        return template.render()

    def serialize_multiapi_operation_mixins(self) -> str:
        template = self.env.get_template("multiapi_operations_mixin.py.jinja2")
        return template.render(**self.conf)
