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
                default_value = prop.schema.get_default_value_declaration()
                init_args.append(f"self.{prop.name} = kwargs.get('{prop.name}', {default_value})")
        return init_args
