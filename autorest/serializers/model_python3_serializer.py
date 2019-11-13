from .model_base_serializer import ModelBaseSerializer
from jinja2 import Template, PackageLoader, Environment
from ..models import PrimitiveSchema
from ..common.known_primary_types_mapping import known_primary_types_mapping
from ..models.imports import FileImport, ImportType


class ModelPython3Serializer(ModelBaseSerializer):
    def __init__(self, code_model):
        super(ModelPython3Serializer, self).__init__(code_model)


    def _build_init_args(self, model):
        init_args = []
        if model.base_model:
            properties_to_initialize = []
            properties_to_pass = []
            super_initialize = "super({}, self).__init__()".format(model.name)
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

        model.init_args = init_args

    def _build_init_line(self, model):
        init_properties_declaration = []
        init_line_parameters = [p for p in model.properties if not p.readonly and not p.is_discriminator and not p.constant]
        init_line_parameters.sort(key=lambda x: x.required, reverse=True)
        for param in init_line_parameters:
            if isinstance(param.schema, PrimitiveSchema):
                if param.required:
                    init_properties_declaration.append("{}: {}".format(param.name, param.schema.get_python_type()))
                else:
                    default_value = "\"" + param.schema.default_value + "\"" if param.schema.default_value else "None"
                    init_properties_declaration.append("{}: {}={}".format(param.name, param.schema.get_python_type(), default_value))
            else:
                if param.required:
                    init_properties_declaration.append(param.name)
                else:
                    default_value = "\"" + param.schema.default_value + "\"" if param.schema.default_value else "None"
                    init_properties_declaration.append("{}={}".format(param.name, default_value))

        if init_properties_declaration:
            model.init_line = "def __init__(self, *, {}, **kwargs) -> None:".format(", ".join(init_properties_declaration))
        else:
            model.init_line ="def __init__(self, **kwargs) -> None:"


    def _format_model_for_file(self, model):
        for prop in model.properties:
            self._format_property_doc_string_for_file(prop)
        self._build_init_line(model)
        self._build_init_args(model)

    def imports(self):
        file_import = super(ModelPython3Serializer, self).imports()
        for model in self.code_model.sorted_schemas:
            init_line_parameters = [p for p in model.properties if not p.readonly and not p.is_discriminator]
            for param in init_line_parameters:
                if isinstance(param.schema, PrimitiveSchema):
                    stdlib_type = param.schema.get_python_type("")
                    if stdlib_type.startswith("~datetime"):
                        file_import.add_import("datetime", ImportType.STDLIB)

        return file_import
