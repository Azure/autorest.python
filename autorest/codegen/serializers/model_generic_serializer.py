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

        for prop in model.properties:
            if model.base_model and prop in model.base_model.properties and not prop.is_discriminator:
                continue
            if prop.constant:
                continue
            if not prop.readonly and not prop.is_discriminator:
                default_value = prop.schema.get_default_value_declaration()
                init_args.append(f"self.{prop.name} = kwargs.get('{prop.name}', {default_value})")
            else:
                if not model.discriminator_value:
                    init_args.append(f"self.{prop.name} = None")
                else:
                    init_args.append(f"self.{prop.name} = '{model.discriminator_value}'")
        return init_args
