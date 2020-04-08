# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List
from .model_base_serializer import ModelBaseSerializer
from ..models import ObjectSchema
from .import_serializer import FileImportSerializer


class ModelGenericSerializer(ModelBaseSerializer):

    def serialize(self) -> str:
        # Generate the models
        template = self.env.get_template("model_container.py.jinja2")
        return template.render(
            code_model=self.code_model,
            imports=FileImportSerializer(self.imports(), is_python_3_file=False),
            str=str,
            init_line=self.init_line,
            init_args=self.init_args,
            prop_documentation_string=ModelBaseSerializer.prop_documentation_string,
            prop_type_documentation_string=ModelBaseSerializer.prop_type_documentation_string,
        )

    @staticmethod
    def init_line(model: ObjectSchema) -> List[str]:
        return []

    @staticmethod
    def init_args(model: ObjectSchema) -> List[str]:
        init_args = []
        init_args.append(f"super({model.name}, self).__init__(**kwargs)")

        for prop in ModelGenericSerializer.get_properties_to_initialize(model):
            if prop.readonly:
                init_args.append(f"self.{prop.name} = None")
            elif prop.is_discriminator:
                discriminator_value = f"'{model.discriminator_value}'" if model.discriminator_value else None
                init_args.append(f"self.{prop.name} = {discriminator_value}")
            elif not prop.constant:
                if prop.required and not prop.schema.default_value:
                    init_args.append(f"self.{prop.name} = kwargs['{prop.name}']")
                else:
                    default = prop.schema.default_value_declaration
                    init_args.append(f"self.{prop.name} = kwargs.get('{prop.name}', {default})")
        return init_args
