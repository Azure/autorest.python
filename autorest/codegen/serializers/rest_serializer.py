# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from autorest.codegen.models import request_builder
from autorest.codegen.models.request_builder import RequestBuilder
from typing import List
from jinja2 import Environment
from abc import abstractmethod
from .import_serializer import FileImportSerializer
from ..models import CodeModel


class RestSerializer:
    def __init__(
        self, code_model: CodeModel, env: Environment, request_builders: List[RequestBuilder]
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.request_builders = request_builders

    @abstractmethod
    def serialize_request_builders(self) -> str:
        ...

    def serialize_init(self) -> str:
        template = self.env.get_template("rest_init.py.jinja2")
        return template.render(code_model=self.code_model, request_builders=self.request_builders)

class RestPython3Serializer(RestSerializer):

    def serialize_request_builders(self) -> str:
        template = self.env.get_template("request_builders.py.jinja2")

        return template.render(
            code_model=self.code_model,
            request_builders=self.request_builders,
            imports=FileImportSerializer(
                self.code_model.rest.imports(self.code_model),
                is_python_3_file=True
            ),
            is_python_3_file=True,
        )

class RestGenericSerializer(RestSerializer):

    def serialize_request_builders(self) -> str:
        template = self.env.get_template("request_builders.py.jinja2")

        return template.render(
            code_model=self.code_model,
            request_builders=self.request_builders,
            imports=FileImportSerializer(
                self.code_model.rest.imports(self.code_model),
                is_python_3_file=False
            ),
            is_python_3_file=False,
        )