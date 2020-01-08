# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import abstractmethod
from typing import List
from ..models import EnumSchema, ObjectSchema
from ..models.imports import FileImport
from .import_serializer import FileImportSerializer

class ModelBaseSerializer:
    def __init__(self, code_model, env):
        self.code_model = code_model
        self.env = env
        self._model_file = None


    def serialize(self):
        self.env.globals.update(str=str)
        self.env.globals.update(init_line=self.init_line)
        self.env.globals.update(init_args=self.init_args)
        self.env.globals.update(prop_documentation_string=ModelBaseSerializer.prop_documentation_string)

        # Generate the models
        template = self.env.get_template("model_container.py.jinja2")
        self._model_file = template.render(
            code_model=self.code_model,
            imports=FileImportSerializer(self.imports())
        )

    def imports(self):
        file_import = FileImport()
        for model in self.code_model.sorted_schemas:
            file_import.merge(model.imports())
        return file_import

    @property
    def model_file(self):
        return self._model_file

    @staticmethod
    def prop_documentation_string(prop, namespace):
        # building the param line of the property doc
        if prop.constant or prop.readonly:
            param_doc_string = ":ivar {}:".format(prop.name)
        else:
            param_doc_string = ":param {}:".format(prop.name)
        description = prop.description
        if description and description[-1] != ".":
            description += "."
        if prop.name == 'tags':
            description = "A set of tags. " + description
        if prop.required:
            if description:
                description = "Required. " + description
            else:
                description = "Required. "
        if prop.constant:
            description += " Default value: \"{}\".".format(prop.schema.value)
        if prop.is_discriminator:
            description += "Constant filled by server. "

        if isinstance(prop.schema, EnumSchema):
            values = ["\'" + v.value + "\'" for v in prop.schema.values]
            description += " Possible values include: {}.".format(", ".join(values))
            if prop.schema.default_value:
                description += " Default value: \"{}\".".format(prop.schema.default_value)
        if description:
            param_doc_string += " " + description

        # building the type line of the property doc
        if prop.constant or prop.readonly:
            type_doc_string = ":vartype {}: ".format(prop.name)
        else:
            type_doc_string = ":type {}: ".format(prop.name)
        type_doc_string += prop.schema.get_python_type(namespace)
        return param_doc_string + "\n\t" + type_doc_string

    @staticmethod
    @abstractmethod
    def init_line(model: ObjectSchema) -> str:
        ...

    @staticmethod
    @abstractmethod
    def init_args(model: ObjectSchema) -> List[str]:
        ...
