# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Optional, cast
from .imports import FileImport
from .operation import Operation
from .response import Response
from .imports import ImportType, TypingSection
from .base_schema import BaseSchema
_LOGGER = logging.getLogger(__name__)


class LROOperation(Operation):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.lro_options = self.yaml_data.get("extensions", {}).get(
            "x-ms-long-running-operation-options", {}
        )
        self.name = "begin_" + self.name

    @property
    def lro_response(self) -> Optional[Response]:
        if not self.responses:
            return None
        responses_with_bodies = [r for r in self.responses if r.types]
        num_response_schemas = {t for r in responses_with_bodies for t in r.types}
        response = None
        if len(num_response_schemas) > 1:
            # choose the response that has a status code of 200
            responses_with_200_status_codes = [
                r for r in responses_with_bodies if 200 in r.status_codes
            ]
            try:
                response = responses_with_200_status_codes[0]
                schema_types = {t for r in responses_with_bodies for t in r.types}
                response_schema = cast(BaseSchema, response.types[0]).serialization_type
                _LOGGER.warning(
                    "Multiple schema types in responses: %s. Choosing: %s",
                    schema_types,
                    response_schema,
                )
            except IndexError:
                raise ValueError(
                    f"Your swagger is invalid because you have multiple response schemas for LRO"
                    + f" method {self.name} and none of them have a 200 status code."
                )

        elif num_response_schemas:
            response = responses_with_bodies[0]
        return response

    @property
    def initial_operation(self) -> Operation:
        return Operation(
            yaml_data=self.yaml_data,
            code_model=self.code_model,
            request_builder=self.code_model.lookup_request_builder(id(self.yaml_data)),
            name=self.name[5:] + "_initial",
            overloads=self.overloads,
            parameters=self.parameters,
            responses=self.responses,
            want_description_docstring=False,
            want_tracing=False,
        )

    @property
    def has_optional_return_type(self) -> bool:
        """An LROOperation will never have an optional return type, we will always return a poller"""
        return False

    def _get_lro_extension(self, extension_base, async_mode, *, azure_arm=None):
        extension_name = extension_base + ("-async" if async_mode else "-sync")
        extension = self.yaml_data["extensions"][extension_name]
        arm_extension = None
        if azure_arm is not None:
            arm_extension = "azure-arm" if azure_arm else "data-plane"
        return extension[arm_extension] if arm_extension else extension

    def get_poller_path(self, async_mode: bool) -> str:
        return self._get_lro_extension("poller", async_mode)

    def get_poller(self, async_mode: bool) -> str:
        return self.get_poller_path(async_mode).split(".")[-1]

    def get_default_polling_method_path(self, async_mode: bool, azure_arm: bool) -> str:
        return self._get_lro_extension(
            "default-polling-method", async_mode, azure_arm=azure_arm
        )

    def get_default_polling_method(self, async_mode: bool, azure_arm: bool) -> str:
        return self.get_default_polling_method_path(async_mode, azure_arm).split(".")[
            -1
        ]

    def get_default_no_polling_method_path(self, async_mode: bool) -> str:
        return self._get_lro_extension("default-no-polling-method", async_mode)

    def get_default_no_polling_method(self, async_mode: bool) -> str:
        return self.get_default_no_polling_method_path(async_mode).split(".")[-1]

    def get_base_polling_method_path(self, async_mode: bool) -> str:
        return self._get_lro_extension("base-polling-method", async_mode)

    def get_base_polling_method(self, async_mode: bool) -> str:
        return self.get_base_polling_method_path(async_mode).split(".")[-1]

    def imports_for_multiapi(self, async_mode: bool) -> FileImport:
        file_import = super().imports_for_multiapi(async_mode)
        poller_import_path = ".".join(self.get_poller_path(async_mode).split(".")[:-1])
        poller = self.get_poller(async_mode)
        file_import.add_submodule_import(
            poller_import_path, poller, ImportType.AZURECORE, TypingSection.CONDITIONAL
        )
        return file_import

    def imports(self, async_mode: bool, is_python3_file: bool) -> FileImport:
        file_import = self._imports_base(async_mode, is_python3_file)
        file_import.add_submodule_import(
            "typing", "Union", ImportType.STDLIB, TypingSection.CONDITIONAL
        )

        poller_import_path = ".".join(self.get_poller_path(async_mode).split(".")[:-1])
        poller = self.get_poller(async_mode)
        file_import.add_submodule_import(
            poller_import_path, poller, ImportType.AZURECORE
        )

        default_polling_method_import_path = ".".join(
            self.get_default_polling_method_path(
                async_mode, self.code_model.options["azure_arm"]
            ).split(".")[:-1]
        )
        default_polling_method = self.get_default_polling_method(
            async_mode, self.code_model.options["azure_arm"]
        )
        file_import.add_submodule_import(
            default_polling_method_import_path,
            default_polling_method,
            ImportType.AZURECORE,
        )

        default_no_polling_method_import_path = ".".join(
            self.get_default_no_polling_method_path(async_mode).split(".")[:-1]
        )
        default_no_polling_method = self.get_default_no_polling_method(async_mode)
        file_import.add_submodule_import(
            default_no_polling_method_import_path,
            default_no_polling_method,
            ImportType.AZURECORE,
        )

        base_polling_method_import_path = ".".join(
            self.get_base_polling_method_path(async_mode).split(".")[:-1]
        )
        base_polling_method = self.get_base_polling_method(async_mode)
        file_import.add_submodule_import(
            base_polling_method_import_path, base_polling_method, ImportType.AZURECORE
        )
        file_import.add_submodule_import("typing", "cast", ImportType.STDLIB)
        if async_mode:
            file_import.add_submodule_import(
                "typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL
            )
        if self.code_model.options["tracing"] and self.want_tracing:
            file_import.add_submodule_import(
                f"azure.core.tracing.decorator{'_async' if async_mode else ''}",
                f"distributed_trace{'_async' if async_mode else ''}",
                ImportType.AZURECORE,
            )
        return file_import
