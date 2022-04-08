# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any
from .base_schema import BaseSchema
from .imports import FileImport, ImportType, TypingSection

class CredentialSchema(BaseSchema):
    def __init__(self) -> None:  # pylint: disable=super-init-not-called
        self.default_value = None

    def type_annotation(self, *, is_operation_file: bool = False) -> str:
        raise ValueError("Children classes should set their own type annotation")

    @property
    def docstring_type(self) -> str:
        return self.serialization_type

    @property
    def docstring_text(self) -> str:
        return "credential"

    @property
    def serialization_type(self) -> str:
        # this property is added, because otherwise pylint says that
        # abstract serialization_type in BaseSchema is not overridden
        pass

    def get_json_template_representation(self, **kwargs: Any) -> Any:
        raise TypeError("You should not try to get a JSON template representation of a CredentialSchema")

class AzureKeyCredentialSchema(CredentialSchema):

    @property
    def serialization_type(self) -> str:
        return "~azure.core.credentials.AzureKeyCredential"

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
        return "AzureKeyCredential"

    def imports(self) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import(
            "azure.core.credentials",
            "AzureKeyCredential",
            ImportType.AZURECORE,
            typing_section=TypingSection.CONDITIONAL
        )
        return file_import


class TokenCredentialSchema(CredentialSchema):
    def __init__(self, async_mode) -> None:
        super(TokenCredentialSchema, self).__init__()
        self.async_mode = async_mode
        self.async_type = "~azure.core.credentials_async.AsyncTokenCredential"
        self.sync_type = "~azure.core.credentials.TokenCredential"

    @property
    def serialization_type(self) -> str:
        if self.async_mode:
            return self.async_type
        return self.sync_type

    def type_annotation(self, *, is_operation_file: bool = False) -> str:  # pylint: disable=unused-argument
        if self.async_mode:
            return '"AsyncTokenCredential"'
        return '"TokenCredential"'


    def imports(self) -> FileImport:
        file_import = FileImport()
        if self.async_mode:
            file_import.add_submodule_import(
                "azure.core.credentials_async", "AsyncTokenCredential",
                ImportType.AZURECORE,
                typing_section=TypingSection.TYPING
            )
        else:
            file_import.add_submodule_import(
                "azure.core.credentials", "TokenCredential",
                ImportType.AZURECORE,
                typing_section=TypingSection.TYPING
            )
        return file_import
