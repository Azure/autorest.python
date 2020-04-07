# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import cast, List
from .model_base_serializer import ModelBaseSerializer
from ..models import ObjectSchema
from ..models.imports import FileImport
from .import_serializer import FileImportSerializer


class ModelPython3Serializer(ModelBaseSerializer):

    def serialize(self) -> str:
        # Generate the models
        template = self.env.get_template("model_container.py.jinja2")
        return template.render(
            code_model=self.code_model,
            imports=FileImportSerializer(self.imports(), is_python_2_file=False),
            str=str,
            init_line=self.init_line,
            init_args=self.init_args,
            prop_documentation_string=ModelBaseSerializer.prop_documentation_string,
            prop_type_documentation_string=ModelBaseSerializer.prop_type_documentation_string,
        )

    @staticmethod
    def init_line(model: ObjectSchema) -> List[str]:
        init_properties_declaration = []
        init_line_parameters = [
            p for p in model.properties if not p.readonly and not p.is_discriminator and not p.constant
        ]
        init_line_parameters.sort(key=lambda x: x.required, reverse=True)
        if init_line_parameters:
            init_properties_declaration.append("*")
        for param in init_line_parameters:
            if param.required and not param.schema.default_value:
                init_properties_declaration.append(f"{param.name}: {param.type_annotation}")
            else:
                default = param.schema.default_value_declaration
                init_properties_declaration.append(f"{param.name}: {param.type_annotation} = {default}")

        return init_properties_declaration

    @staticmethod
    def init_args(model: ObjectSchema) -> List[str]:
        init_args = []
        base_model = cast(ObjectSchema, model.base_model)
        if base_model:
            properties_to_pass = []
            for prop in model.properties:
                if (
                    prop in base_model.properties
                    and not prop.is_discriminator
                    and not prop.constant
                    and not prop.readonly
                ):
                    properties_to_pass.append(f"{prop.name}={prop.name}")
            properties_to_pass.append("**kwargs")
            init_args.append("super({}, self).__init__({})".format(model.name, ", ".join(properties_to_pass)))
        else:
            init_args.append(f"super({model.name}, self).__init__(**kwargs)")
        for prop in ModelPython3Serializer.get_properties_to_initialize(model):
            if prop.readonly:
                init_args.append(f"self.{prop.name} = None")
            elif prop.is_discriminator:
                discriminator_value = f"'{model.discriminator_value}'" if model.discriminator_value else None
                init_args.append(f"self.{prop.name} = {discriminator_value}")
            elif not prop.constant:
                init_args.append(f"self.{prop.name} = {prop.name}")

        return init_args

    def imports(self) -> FileImport:
        file_import = super(ModelPython3Serializer, self).imports()
        for model in self.code_model.sorted_schemas:
            init_line_parameters = [p for p in model.properties if not p.readonly and not p.is_discriminator]
            for param in init_line_parameters:
                file_import.merge(param.imports())

        return file_import
