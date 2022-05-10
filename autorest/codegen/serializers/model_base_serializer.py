# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import abstractmethod
from typing import cast, List
from jinja2 import Environment
from ..models import ObjectSchema, CodeModel, Property
from ..models.imports import FileImport, TypingSection, MsrestImportType
from .import_serializer import FileImportSerializer


def _documentation_string(
    prop: Property, description_keyword: str, docstring_type_keyword: str
) -> List[str]:
    retval: List[str] = []
    sphinx_prefix = f":{description_keyword} {prop.name}:"
    retval.append(
        f"{sphinx_prefix} {prop.description}" if prop.description else sphinx_prefix
    )
    retval.append(
        f":{docstring_type_keyword} {prop.name}: {prop.schema.docstring_type}"
    )
    return retval


class ModelBaseSerializer:
    def __init__(
        self, code_model: CodeModel, env: Environment, is_python3_file: bool
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.is_python3_file = is_python3_file

    def serialize(self) -> str:
        # Generate the models
        template = self.env.get_template("model_container.py.jinja2")
        return template.render(
            code_model=self.code_model,
            imports=FileImportSerializer(
                self.imports(), is_python3_file=self.is_python3_file
            ),
            str=str,
            init_line=self.init_line,
            init_args=self.init_args,
            input_documentation_string=ModelBaseSerializer.input_documentation_string,
            variable_documentation_string=ModelBaseSerializer.variable_documentation_string,
            declare_model=self.declare_model,
        )

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_msrest_import(
            self.code_model, "..", MsrestImportType.Module, TypingSection.REGULAR
        )
        for model in self.code_model.sorted_schemas:
            file_import.merge(model.imports())
        return file_import

    @staticmethod
    def get_properties_to_initialize(model: ObjectSchema) -> List[Property]:
        if model.base_models:
            properties_to_initialize = list(
                {
                    p.name: p
                    for bm in model.base_models
                    for p in model.properties
                    if p not in cast(ObjectSchema, bm).properties
                    or p.is_discriminator
                    or p.constant
                }.values()
            )
        else:
            properties_to_initialize = model.properties
        return properties_to_initialize

    def declare_model(self, model: ObjectSchema) -> str:
        basename = (
            "msrest.serialization.Model"
            if self.code_model.options["client_side_validation"]
            else "_serialization.Model"
        )
        if model.base_models:
            basename = ", ".join(
                [cast(ObjectSchema, m).name for m in model.base_models]
            )
        return f"class {model.name}({basename}):"

    @staticmethod
    def input_documentation_string(prop: Property) -> List[str]:
        # building the param line of the property doc
        return _documentation_string(prop, "keyword", "paramtype")

    @staticmethod
    def variable_documentation_string(prop: Property) -> List[str]:
        return _documentation_string(prop, "ivar", "vartype")

    def init_args(self, model: ObjectSchema) -> List[str]:
        init_args = []
        properties_to_pass_to_super = self.properties_to_pass_to_super(model)
        init_args.append(
            f"super({model.name}, self).__init__({properties_to_pass_to_super})"
        )
        for prop in ModelBaseSerializer.get_properties_to_initialize(model):
            if prop.is_discriminator:
                discriminator_value = (
                    f"'{model.discriminator_value}'"
                    if model.discriminator_value
                    else None
                )
                if not discriminator_value:
                    typing = "Optional[str]"
                else:
                    typing = "str"
                init_args.append(
                    f"self.{prop.name} = {discriminator_value}  # type: {typing}"
                )
            elif prop.readonly:
                init_args.append(f"self.{prop.name} = None")
            elif not prop.constant:
                init_args.append(self.initialize_standard_arg(prop))
        return init_args

    def initialize_standard_property(self, prop: Property):
        if prop.required and not prop.default_value:
            return self.required_property_no_default_init(prop)
        return self.optional_property_init(prop)

    @abstractmethod
    def init_line(self, model: ObjectSchema) -> List[str]:
        ...

    @abstractmethod
    def properties_to_pass_to_super(self, model: ObjectSchema) -> str:
        ...

    @abstractmethod
    def required_property_no_default_init(self, prop: Property) -> str:
        ...

    @abstractmethod
    def optional_property_init(self, prop: Property) -> str:
        ...

    @abstractmethod
    def initialize_standard_arg(self, prop: Property) -> str:
        ...
