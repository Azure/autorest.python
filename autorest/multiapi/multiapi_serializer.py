# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from jinja2 import Environment, PackageLoader


class MultiAPISerializer:
    def __init__(self, conf, path_to_package, service_client_name):
        self.conf = conf
        self.path_to_package = path_to_package
        self.service_client_name = service_client_name
        self.env = Environment(
            loader=PackageLoader("autorest.multiapi", "templates"),
            keep_trailing_newline=True,
            line_statement_prefix="##",
            line_comment_prefix="###",
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def serialize_multiapi_client(self):
        template = self.env.get_template("multiapi_service_client.py.jinja2")
        result = template.render(**self.conf)

        with (self.path_to_package / self.service_client_name).open("w") as fd:
            fd.write(result)

    def serialize_multiapi_operation_mixins(self):
        template = self.env.get_template("multiapi_operations_mixin.py.jinja2")
        result = template.render(**self.conf)

        with (self.path_to_package / "_operations_mixin.py").open("w") as fd:
            fd.write(result)
