# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, cast
from abc import ABC, abstractmethod

from jinja2 import Environment
from ..models import ModelType, CodeModel
from ..models.imports import FileImport, TypingSection, ImportType
from .import_serializer import FileImportSerializer

class TypesSerializer(ABC):
    def __init__(self, code_model: CodeModel, env: Environment) -> None:
        self.code_model = code_model
        self.env = env

    def imports(self) -> FileImport:
        file_import = FileImport()
        for nu in self.code_model.named_unions:
            if any(isinstance(t, ModelType) for t in nu.types):
                file_import.add_submodule_import(
                        ".",
                        "models",
                        ImportType.LOCAL,
                        TypingSection.TYPING,
                        alias="_models",
                    )
        return file_import

    def serialize(self) -> str:
        # Generate the models
        template = self.env.get_template("types.py.jinja2")
        return template.render(
            code_model=self.code_model,
            imports=FileImportSerializer(self.imports()),
            serializer=self,
        )

  