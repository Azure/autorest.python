# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import cast, List
from jinja2 import Environment
from ..models import ModelType, CodeModel, Property
from ..models.imports import FileImport, TypingSection, MsrestImportType, ImportType
from .import_serializer import FileImportSerializer


def _documentation_string(
    prop: Property, description_keyword: str, docstring_type_keyword: str
) -> List[str]:
    retval: List[str] = []
    sphinx_prefix = f":{description_keyword} {prop.client_name}:"
    retval.append(
        f"{sphinx_prefix} {prop.description(is_operation_file=False)}"
        if prop.description(is_operation_file=False)
        else sphinx_prefix
    )
    retval.append(
        f":{docstring_type_keyword} {prop.client_name}: {prop.type.docstring_type()}"
    )
    return retval


class ModelSerializer:
    def __init__(self, code_model: CodeModel, env: Environment) -> None:
        self.code_model = code_model
        self.env = env

    def serialize(self) -> str:
        # Generate the models
        template = self.env.get_template("model_container.py.jinja2")
        return template.render(
            code_model=self.code_model,
            imports=FileImportSerializer(self.imports()),
            str=str,
            serializer=self,
        )

    def imports(self) -> FileImport:
        file_import = FileImport()
        if self.code_model.options["models_mode"] == "json":
            file_import.add_submodule_import(
                "..",
                "_model_base",
                ImportType.LOCAL,
                TypingSection.REGULAR,
            )
            file_import.add_submodule_import("typing", "overload", ImportType.STDLIB)
            file_import.add_submodule_import("typing", "Mapping", ImportType.STDLIB)
            file_import.add_submodule_import("typing", "Any", ImportType.STDLIB)
        else:
            file_import.add_msrest_import(
                self.code_model, "..", MsrestImportType.Module, TypingSection.REGULAR
            )
        for model in self.code_model.model_types:
            file_import.merge(model.imports(is_operation_file=False))
            if self.code_model.options["models_mode"] == "json":
                for param in model.properties:
                    file_import.merge(param.imports())
            else:
                init_line_parameters = [
                    p
                    for p in model.properties
                    if not p.readonly and not p.is_discriminator
                ]
                for param in init_line_parameters:
                    file_import.merge(param.imports())
        return file_import

    @staticmethod
    def get_properties_to_initialize(model: ModelType) -> List[Property]:
        if model.parents:
            properties_to_initialize = list(
                {
                    p.client_name: p
                    for bm in model.parents
                    for p in model.properties
                    if p not in cast(ModelType, bm).properties
                    or p.is_discriminator
                    or p.constant
                }.values()
            )
        else:
            properties_to_initialize = model.properties
        return properties_to_initialize

    @staticmethod
    def get_properties_to_declare(model: ModelType) -> List[Property]:
        if model.parents:
            properties_to_declare = list(
                {
                    p.client_name: p
                    for bm in model.parents
                    for p in model.properties
                    if p not in cast(ModelType, bm).properties
                }.values()
            )
        else:
            properties_to_declare = model.properties
        return properties_to_declare

    def declare_model(self, model: ModelType) -> str:
        basename = (
            "msrest.serialization.Model"
            if self.code_model.options["client_side_validation"]
            else "_model_base.Model"
            if self.code_model.options["models_mode"] == "json"
            else "_serialization.Model"
        )
        if model.parents:
            basename = ", ".join([cast(ModelType, m).name for m in model.parents])
        if (
            self.code_model.options["models_mode"] == "json"
            and model.discriminator_value
        ):
            basename += f", discriminator='{model.discriminator_value}'"
        return f"class {model.name}({basename}):{model.pylint_disable}"

    @staticmethod
    def declare_property(prop: Property) -> List[str]:
        attribute_key = prop.rest_api_name.replace(".", "\\\\.")
        args = [f'name="{attribute_key}"']
        if prop.readonly:
            args.append("readonly=True")
        if prop.client_default_value is not None:
            args.append(f"default={prop.client_default_value_declaration}")

        field = "rest_discriminator" if prop.is_discriminator else "rest_field"
        ret = [
            f'{prop.client_name}: {prop.type_annotation().replace("_models.", "")} ='
            f' {field}({", ".join(args)})'
        ]
        comment = prop.description(is_operation_file=False).replace('"', '\\"')
        if comment:
            ret.append(f'"""{comment}"""')
        return ret

    @staticmethod
    def input_documentation_string(prop: Property) -> List[str]:
        # building the param line of the property doc
        return _documentation_string(prop, "keyword", "paramtype")

    @staticmethod
    def variable_documentation_string(prop: Property) -> List[str]:
        return _documentation_string(prop, "ivar", "vartype")

    def super_call(self, model: ModelType):
        return f"super().__init__({self.properties_to_pass_to_super(model)})"

    def initialize_properties(self, model: ModelType) -> List[str]:
        init_args = []
        for prop in self.get_properties_to_initialize(model):
            if prop.is_discriminator:
                init_args.append(self.initialize_discriminator_property(model, prop))
            elif prop.readonly:
                init_args.append(f"self.{prop.client_name} = None")
            elif not prop.constant:
                init_args.append(f"self.{prop.client_name} = {prop.client_name}")
        return init_args

    @staticmethod
    def initialize_discriminator_property(model: ModelType, prop: Property) -> str:
        discriminator_value = (
            f"'{model.discriminator_value}'" if model.discriminator_value else None
        )
        if not discriminator_value:
            typing = "Optional[str]"
        else:
            typing = "str"
        return f"self.{prop.client_name} = {discriminator_value}  # type: {typing}"

    @staticmethod
    def initialize_standard_property(prop: Property):
        if not (prop.optional or prop.client_default_value is not None):
            return f"{prop.client_name}: {prop.type_annotation()},{prop.pylint_disable}"
        return (
            f"{prop.client_name}: {prop.type_annotation()} = "
            f"{prop.client_default_value_declaration},{prop.pylint_disable}"
        )

    @staticmethod
    def discriminator_docstring(model: ModelType) -> str:
        return (
            "You probably want to use the sub-classes and not this class directly. "
            f"Known sub-classes are: {', '.join(v.name for v in model.discriminated_subtypes.values())}"
        )

    def init_line(self, model: ModelType) -> List[str]:
        init_properties_declaration = []
        init_line_parameters = [
            p
            for p in model.properties
            if not p.readonly and not p.is_discriminator and not p.constant
        ]
        init_line_parameters.sort(key=lambda x: x.optional)
        if init_line_parameters:
            init_properties_declaration.append("*,")
        for param in init_line_parameters:
            init_properties_declaration.append(self.initialize_standard_property(param))

        return init_properties_declaration

    @staticmethod
    def properties_to_pass_to_super(model: ModelType) -> str:
        properties_to_pass_to_super = []
        for parent in model.parents:
            for prop in model.properties:
                if (
                    prop in parent.properties
                    and not prop.is_discriminator
                    and not prop.constant
                    and not prop.readonly
                ):
                    properties_to_pass_to_super.append(
                        f"{prop.client_name}={prop.client_name}"
                    )
        properties_to_pass_to_super.append("**kwargs")
        return ", ".join(properties_to_pass_to_super)
