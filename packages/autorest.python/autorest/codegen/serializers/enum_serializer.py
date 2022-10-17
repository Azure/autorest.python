# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from jinja2 import Environment
from ..models import NamespaceModel


class EnumSerializer:
    def __init__(self, namespace_model: NamespaceModel, env: Environment) -> None:
        self.namespace_model = namespace_model
        self.env = env

    def serialize(self) -> str:
        # Generate the enum file
        template = self.env.get_template("enum_container.py.jinja2")
        return template.render(namespace_model=self.namespace_model)
