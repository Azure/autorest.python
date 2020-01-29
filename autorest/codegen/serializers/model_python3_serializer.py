# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List
from .model_base_serializer import ModelBaseSerializer
from ..models import PrimitiveSchema, ListSchema, DictionarySchema, EnumSchema, ObjectSchema
from ..models.imports import FileImport, ImportType


class ModelPython3Serializer(ModelBaseSerializer):

    @staticmethod
    def init_line(model: ObjectSchema) -> List[str]:
        init_properties_declaration = []
        init_line_parameters = [
            p for p in model.properties if not p.readonly and not p.is_discriminator and not p.constant
        ]
        # init_line_parameters.sort(key=lambda x: x.required, reverse=True)
        required_parameters = [p for p in init_line_parameters if p.required]
        optional_parameters = [p for p in init_line_parameters if not p.required]
        for param in required_parameters:
            init_properties_declaration.append(
                "{}: {}".format(param.name, param.type_annotation)
            )
        if optional_parameters:
            init_properties_declaration.append("*")
        for param in optional_parameters:
            default_value = param.schema.get_default_value_declaration()
            init_properties_declaration.append(
                "{}: {} = {}".format(param.name, param.type_annotation, default_value)
            )

        return init_properties_declaration

    @staticmethod
    def init_args(model: ObjectSchema) -> List[str]:
        init_args = []
        if model.base_model:
            properties_to_initialize = []
            properties_to_pass = []
            for prop in [p for p in model.properties if not p.readonly]:
                if (prop in model.base_model.properties and not prop.is_discriminator and not prop.constant):
                    properties_to_pass.append("{}={}".format(prop.name, prop.name))
                else:
                    properties_to_initialize.append(prop)
            properties_to_pass.append("**kwargs")
            init_args.append("super({}, self).__init__({})".format(model.name, ", ".join(properties_to_pass)))
        else:
            init_args.append("super({}, self).__init__(**kwargs)".format(model.name))
            properties_to_initialize = model.properties
        for prop in properties_to_initialize:
            if prop.readonly:
                init_args.append("self.{} = None".format(prop.name))
            elif prop.is_discriminator:
                init_args.append("self.{} = '{}'".format(prop.name, model.discriminator_value))
            elif not prop.constant:
                init_args.append("self.{} = {}".format(prop.name, prop.name))

        return init_args

    def imports(self):
        file_import = super(ModelPython3Serializer, self).imports()
        for model in self.code_model.sorted_schemas:
            init_line_parameters = [p for p in model.properties if not p.readonly and not p.is_discriminator]
            for param in init_line_parameters:
                file_import.merge(param.imports())

        return file_import
