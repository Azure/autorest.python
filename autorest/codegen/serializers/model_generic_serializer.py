# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List
from jinja2 import Environment
from .model_base_serializer import ModelBaseSerializer
from ..models import ModelType, CodeModel, Property


class ModelGenericSerializer(ModelBaseSerializer):
    def __init__(self, code_model: CodeModel, env: Environment) -> None:
        super().__init__(code_model=code_model, env=env, is_python3_file=False)

    def init_line(self, model: ModelType) -> List[str]:
        return []

    def properties_to_pass_to_super(self, model: ModelType) -> str:
        return "**kwargs"

    def required_property_no_default_init(self, prop: Property) -> str:
        return f"self.{prop.client_name} = kwargs['{prop.client_name}']"

    def optional_property_init(self, prop: Property) -> str:
        default = prop.type.get_declaration(prop.client_default_value)
        return f"self.{prop.client_name} = kwargs.get('{prop.client_name}', {default})"

    def initialize_standard_arg(self, prop: Property) -> str:
        return self.initialize_standard_property(prop)

    def super_call_template(self, model: ModelType) -> str:
        return "super({}, self).__init__({})".format(model.name)
