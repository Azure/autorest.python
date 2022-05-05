# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import abstractmethod
from typing import cast, List
from jinja2 import Environment
from ..models import ModelType, CodeModel, Property
from ..models.imports import FileImport, ImportType
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
        f":{docstring_type_keyword} {prop.client_name}: {prop.type.docstring_type}"
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
            serializer=self,
        )

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_import("msrest.serialization", ImportType.AZURECORE)
        for model in self.code_model.model_types:
            file_import.merge(model.imports(is_operation_file=False))
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
    def declare_model(model: ModelType) -> str:
        basename = "msrest.serialization.Model"
        if model.parents:
            basename = ", ".join([cast(ModelType, m).name for m in model.parents])
        return f"class {model.name}({basename}):"

    @staticmethod
    def input_documentation_string(prop: Property) -> List[str]:
        # building the param line of the property doc
        return _documentation_string(prop, "keyword", "paramtype")

    @staticmethod
    def variable_documentation_string(prop: Property) -> List[str]:
        return _documentation_string(prop, "ivar", "vartype")

    @abstractmethod
    def super_call_template(self, model: ModelType) -> str:
        ...

    def super_call(self, model: ModelType):
        return self.super_call_template(model).format(
            self.properties_to_pass_to_super(model)
        )

    def initialize_properties(self, model: ModelType) -> List[str]:
        init_args = []
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
                    f"self.{prop.client_name} = {discriminator_value}  # type: {typing}"
                )
            elif prop.readonly:
                init_args.append(f"self.{prop.client_name} = None")
            elif not prop.constant:
                init_args.append(self.initialize_standard_arg(prop))
        return init_args

    def initialize_standard_property(self, prop: Property):
        if not (prop.optional or prop.client_default_value is not None):
            return self.required_property_no_default_init(prop)
        return self.optional_property_init(prop)

    @abstractmethod
    def init_line(self, model: ModelType) -> List[str]:
        ...

    @abstractmethod
    def properties_to_pass_to_super(self, model: ModelType) -> str:
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
