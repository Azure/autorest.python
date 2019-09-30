from .base_serializer import BaseSerializer
from jinja2 import Template, PackageLoader, Environment
from ..models import ObjectSchema
from ..common.known_primary_types_mapping import known_primary_types_mapping


class Python3Serializer(BaseSerializer):
    def __init__(self, code_model):
        super(Python3Serializer, self).__init__(code_model)


    def _build_init_args(self, model):
        init_args = []
        if model.base_model:
            properties_to_initialize = []
            properties_to_pass = []
            super_initialize = "super({}, self).__init__()".format(model.name)
            # for prop in model.properties:
            #     if prop in model.base_model.properties and not prop.readonly:
            #         properties_to_pass.append(prop)
            #     else:
            #         properties_to_initialize.append(prop)
            properties_to_pass.append("**kwargs")
            init_args.append("super({}, self).__init__({})".format(model.name, ", ".join(properties_to_pass)))
        else:
            init_args.append("super({}, self).__init__(**kwargs)".format(model.name))
            properties_to_initialize = model.properties
        for prop in properties_to_initialize:
            if prop.readonly:
                init_args.append("self.{} = None".format(prop.name))
            else:
                init_args.append("self.{} = {}".format(prop.name, prop.name))
        model.init_args = init_args

    def _build_init_line(self, model):
        init_line = "def __init__(self, )"
        init_properties_declaration = []
        init_args = []
        for prop in [p for p in model.properties if not p.readonly]:
            if isinstance(prop, ObjectSchema) and prop.schema_type in known_primary_types_mapping.values():
                if prop.required:
                    init_properties_declaration.append("{}: {}".format(prop.name, prop.schema_type))
                else:
                    init_properties_declaration.append("{}: {}=None".format(prop.name, prop.schema_type))
            else:
                if prop.required:
                    init_properties_declaration.append(prop.name)
                else:
                    init_properties_declaration.append("{}=None".format(prop.name))

        if init_properties_declaration:
            model.init_line = "def __init__(self, *, {}, **kwargs) -> None:".format(", ".join(init_properties_declaration))
        else:
            model.init_line ="def __init__(self, **kwargs) -> None:"


    def _format_model_for_file(self, model):
        for prop in model.properties:
            self._format_property_doc_string_for_file(prop)
        self._build_init_line(model)
        self._build_init_args(model)