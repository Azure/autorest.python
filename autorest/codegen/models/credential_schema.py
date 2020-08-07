# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from .base_schema import BaseSchema
from .imports import FileImport, ImportType, TypingSection

class CredentialSchema(BaseSchema):
    def __init__(self, async_mode) -> None:  # pylint: disable=super-init-not-called
        self.async_mode = async_mode
        self.async_type = "~azure.core.credentials_async.AsyncTokenCredential"
        self.sync_type = "~azure.core.credentials.TokenCredential"
        self.default_value = None

    @property
    def serialization_type(self) -> str:
        if self.async_mode:
            return self.async_type
        return self.sync_type

    @property
    def docstring_type(self) -> str:
        return self.serialization_type

    @property
    def type_annotation(self) -> str:
        if self.async_mode:
            return '"AsyncTokenCredential"'
        return '"TokenCredential"'

    @property
    def docstring_text(self) -> str:
        return "credential"

    def imports(self) -> FileImport:
        file_import = FileImport()
        if self.async_mode:
            file_import.add_from_import(
                "azure.core.credentials_async", "AsyncTokenCredential",
                ImportType.AZURECORE,
                typing_section=TypingSection.TYPING
            )
        else:
            file_import.add_from_import(
                "azure.core.credentials", "TokenCredential",
                ImportType.AZURECORE,
                typing_section=TypingSection.TYPING
            )
        return file_import
