# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from .model_base_serializer import ModelBaseSerializer


class ModelGenericSerializer(ModelBaseSerializer):

    def _format_model_for_file(self, model):
        # only adding the warnings in the generic serializer because the function changes the model description
        # on the object, so the python3 model serializer will also have access to it
        self._format_model_parameter_warnings(model)
        for prop in model.properties:
            self._format_property_doc_string_for_file(prop)
        model.init_line = "def __init__(self, **kwargs):"
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
        model.init_args = init_args

    def imports(self):
        file_import = super(ModelGenericSerializer, self).imports()
        for model in self.code_model.sorted_schemas:
            init_line_parameters = [p for p in model.properties if not p.readonly and not p.is_discriminator]
            for param in init_line_parameters:
                file_import.merge(param.imports(async_mode=False))

        return file_import