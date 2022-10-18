# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from jinja2 import Environment
from .import_serializer import FileImportSerializer
from ..models import NamespaceModel, FileImport, ImportType, TypingSection


class PatchSerializer:
    def __init__(self, env: Environment, namespace_model: NamespaceModel) -> None:
        self.env = env
        self.namespace_model = namespace_model

    def serialize(self) -> str:
        template = self.env.get_template("patch.py.jinja2")
        imports = FileImport()
        imports.add_submodule_import(
            "typing", "List", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        return template.render(
            namespace_model=self.namespace_model,
            imports=FileImportSerializer(imports),
        )
