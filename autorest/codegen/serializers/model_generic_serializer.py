# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List
from .model_base_serializer import ModelBaseSerializer
from ..models import ObjectSchema


class ModelGenericSerializer(ModelBaseSerializer):

    @staticmethod
    def init_line(model: ObjectSchema) -> str:
        return "def __init__(self, **kwargs):"

    @staticmethod
    def init_args(model: ObjectSchema) -> List[str]:
        init_args = []
        init_args.append("super({}, self).__init__(**kwargs)".format(model.name))

        for prop in model.properties:
            if model.base_model and prop in model.base_model.properties and not prop.is_discriminator:
                continue
            if prop.constant:
                continue
            if not prop.readonly and not prop.is_discriminator:
                default_value = "\"" + prop.schema.default_value + "\"" if prop.schema.default_value else "None"
                init_args.append("self.{} = kwargs.get('{}', {})".format(prop.name, prop.name, default_value))
            else:
                if not model.discriminator_value:
                    init_args.append("self.{} = None".format(prop.name))
                else:
                    init_args.append("self.{} = '{}'".format(prop.name, model.discriminator_value))
        return init_args

    def imports(self):
        file_import = super(ModelGenericSerializer, self).imports()
        for model in self.code_model.sorted_schemas:
            init_line_parameters = [p for p in model.properties if not p.readonly and not p.is_discriminator]
            for param in init_line_parameters:
                file_import.merge(param.imports())

        return file_import
