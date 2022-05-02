# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import cast, List
from jinja2 import Environment
from .model_base_serializer import ModelBaseSerializer
from ..models import ModelType, CodeModel, Property
from ..models.imports import FileImport


class ModelPython3Serializer(ModelBaseSerializer):
    def __init__(self, code_model: CodeModel, env: Environment) -> None:
        super().__init__(code_model=code_model, env=env, is_python3_file=True)

    def init_line(self, model: ModelType) -> List[str]:
        init_properties_declaration = []
        init_line_parameters = [
            p
            for p in model.properties
            if not p.readonly and not p.is_discriminator and not p.constant
        ]
        init_line_parameters.sort(key=lambda x: x.optional)
        if init_line_parameters:
            init_properties_declaration.append("*")
        for param in init_line_parameters:
            init_properties_declaration.append(self.initialize_standard_property(param))

        return init_properties_declaration

    def properties_to_pass_to_super(self, model: ModelType) -> str:
        properties_to_pass_to_super = []
        for parent in model.parents:
            for prop in model.properties:
                if (
                    prop in parent.properties
                    and not prop.is_discriminator
                    and not prop.constant
                    and not prop.readonly
                ):
                    properties_to_pass_to_super.append(f"{prop.client_name}={prop.client_name}")
        properties_to_pass_to_super.append("**kwargs")
        return ", ".join(properties_to_pass_to_super)

    def required_property_no_default_init(self, prop: Property) -> str:
        return f"{prop.client_name}: {prop.type_annotation()}"

    def optional_property_init(self, prop: Property) -> str:
        return f"{prop.client_name}: {prop.type_annotation()} = {prop.client_default_value_declaration}"

    def initialize_standard_arg(self, prop: Property) -> str:
        return f"self.{prop.client_name} = {prop.client_name}"

    def super_call_template(self, model: ModelType) -> str:
        return "super().__init__({})"

    def imports(self) -> FileImport:
        file_import = super(ModelPython3Serializer, self).imports()
        for model in self.code_model.object_types:
            init_line_parameters = [
                p for p in model.properties if not p.readonly and not p.is_discriminator
            ]
            for param in init_line_parameters:
                file_import.merge(param.imports())

        return file_import
