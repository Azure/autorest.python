# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List
from jinja2 import Environment

from ..models import RequestBuilder, FileImport
from .import_serializer import FileImportSerializer
from ..models import CodeModel
from .builder_serializer import (
    RequestBuilderGenericSerializer,
    RequestBuilderPython3Serializer,
)


class RequestBuildersSerializer:
    def __init__(
        self,
        code_model: CodeModel,
        env: Environment,
        request_builders: List[RequestBuilder],
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.request_builders = request_builders
        self.group_name = request_builders[0].group_name

    @property
    def imports(self) -> FileImport:
        file_import = FileImport()
        for request_builder in self.request_builders:
            if request_builder.group_name == self.group_name:
                file_import.merge(request_builder.imports())
        return file_import

    def serialize_init(self) -> str:
        template = self.env.get_template("rest_init.py.jinja2")
        return template.render(
            code_model=self.code_model, request_builders=self.request_builders
        )


class RequestBuildersPython3Serializer(RequestBuildersSerializer):
    def serialize_request_builders(self) -> str:
        template = self.env.get_template("request_builders.py.jinja2")

        return template.render(
            code_model=self.code_model,
            request_builders=self.request_builders,
            imports=FileImportSerializer(
                self.imports,
                is_python3_file=True,
            ),
            is_python3_file=True,
            request_builder_serializer=RequestBuilderPython3Serializer(self.code_model),
        )


class RequestBuildersGenericSerializer(RequestBuildersSerializer):
    def serialize_request_builders(self) -> str:
        template = self.env.get_template("request_builders.py.jinja2")

        return template.render(
            code_model=self.code_model,
            request_builders=self.request_builders,
            imports=FileImportSerializer(
                self.imports,
                is_python3_file=False,
            ),
            is_python3_file=False,
            request_builder_serializer=RequestBuilderGenericSerializer(self.code_model),
        )
