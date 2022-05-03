# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Any, Dict, Optional, Type, List, TYPE_CHECKING
from .imports import FileImport
from .operation import Operation, OperationBase, OverloadedOperation
from .response import Response
from .imports import ImportType, TypingSection
from .base_type import BaseType
from .request_builder import RequestBuilder
from .response import Response
from .parameter_list import ParameterList

_LOGGER = logging.getLogger(__name__)

if TYPE_CHECKING:
    from .code_model import CodeModel


class _LROOperationBase(OperationBase):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        request_builder: RequestBuilder,
        parameters: ParameterList,
        responses: List[Response],
        exceptions: List[Response],
        *,
        overloads: Optional[List[Operation]] = None,
        public: bool = True,
        want_tracing: bool = True,
        abstract: bool = False,
    ) -> None:
        super().__init__(
            code_model=code_model,
            yaml_data=yaml_data,
            name=name,
            request_builder=request_builder,
            parameters=parameters,
            responses=responses,
            exceptions=exceptions,
            overloads=overloads,
            public=public,
            want_tracing=want_tracing,
            abstract=abstract,
        )
        self.name = "begin_" + self.name
        self.lro_options: Dict[str, Any] = self.yaml_data.get("lroOptions", {})

    @property
    def operation_type(self) -> str:
        return "lro"

    @property
    def has_optional_return_type(self) -> bool:
        return False

    @property
    def lro_response(self) -> Optional[Response]:
        if not self.responses:
            return None
        responses_with_bodies = [r for r in self.responses if r.type]
        num_response_schemas = {id(r.type.yaml_data) for r in responses_with_bodies}
        response = None
        if len(num_response_schemas) > 1:
            # choose the response that has a status code of 200
            try:
                response = next(
                    r for r in responses_with_bodies if 200 in r.status_codes
                )
            except StopIteration:
                raise ValueError(
                    f"Your swagger is invalid because you have multiple response schemas for LRO"
                    + f" method {self.name} and none of them have a 200 status code."
                )

        elif num_response_schemas:
            response = responses_with_bodies[0]
        return response

    def get_poller_path(self, async_mode: bool) -> str:
        return (
            self.yaml_data["pollerAsync"]
            if async_mode
            else self.yaml_data["pollerSync"]
        )

    def get_poller(self, async_mode: bool) -> str:
        return self.get_poller_path(async_mode).split(".")[-1]

    def get_polling_method_path(self, async_mode: bool) -> str:
        return (
            self.yaml_data["pollingMethodAsync"]
            if async_mode
            else self.yaml_data["pollingMethodSync"]
        )

    def get_polling_method(self, async_mode: bool) -> str:
        return self.get_polling_method_path(async_mode).split(".")[-1]

    def get_no_polling_method_path(self, async_mode: bool) -> str:
        return f"azure.core.polling.{'Async' if async_mode else ''}NoPolling"

    def get_no_polling_method(self, async_mode: bool) -> str:
        return self.get_no_polling_method_path(async_mode).split(".")[-1]

    def get_base_polling_method_path(self, async_mode: bool) -> str:
        return f"azure.core.polling.{'Async' if async_mode else ''}PollingMethod"

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

    def response_type_annotation(self, *, async_mode: bool, **kwargs) -> str:
        return f"{self.get_poller(async_mode)}[{super().response_type_annotation(async_mode=async_mode)}]"

    def response_docstring_type(self, *, async_mode: bool, **kwargs) -> str:
        return f"~{self.get_poller_path(async_mode)}[{super().response_docstring_type(async_mode=async_mode)}]"

    def cls_type_annotation(self, *, async_mode: bool) -> str:
        return f"ClsType[{super().response_type_annotation(async_mode=async_mode)}]"

    def response_docstring_text(self, *, async_mode: bool, **kwargs) -> str:
        super_text = super().response_docstring_text(async_mode=async_mode)
        base_description = f"An instance of {self.get_poller(async_mode)} that returns "
        if not self.code_model.options["version_tolerant"]:
            base_description += "either "
        return base_description + super_text

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
            self.get_polling_method_path(async_mode).split(".")[:-1]
        )
        default_polling_method = self.get_polling_method(async_mode)
        file_import.add_submodule_import(
            default_polling_method_import_path,
            default_polling_method,
            ImportType.AZURECORE,
        )

        default_no_polling_method_import_path = ".".join(
            self.get_no_polling_method_path(async_mode).split(".")[:-1]
        )
        default_no_polling_method = self.get_no_polling_method(async_mode)
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


class LROOperation(Operation, _LROOperationBase):
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
            exceptions=self.exceptions,
            public=False,
            want_tracing=False,
        )


class OverloadedLROOperation(OverloadedOperation, _LROOperationBase):
    @staticmethod
    def overload_operation_class() -> Type[Operation]:
        return LROOperation

    @property
    def initial_operation(self) -> OverloadedOperation:
        return OverloadedOperation(
            yaml_data=self.yaml_data,
            code_model=self.code_model,
            request_builder=self.code_model.lookup_request_builder(id(self.yaml_data)),
            name=self.name[5:] + "_initial",
            overloads=self.overloads,
            parameters=self.parameters,
            responses=self.responses,
            exceptions=self.exceptions,
            public=False,
            want_tracing=False,
        )
