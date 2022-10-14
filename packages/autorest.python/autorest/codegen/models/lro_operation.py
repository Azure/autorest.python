# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, Optional, List, TYPE_CHECKING, TypeVar, Union
from .imports import FileImport
from .operation import OperationBase, Operation
from .response import LROPagingResponse, LROResponse, Response
from .imports import ImportType, TypingSection
from .request_builder import RequestBuilder
from .parameter_list import ParameterList

if TYPE_CHECKING:
    from .code_model import NamespaceModel
    from .client import Client

LROResponseType = TypeVar(
    "LROResponseType", bound=Union[LROResponse, LROPagingResponse]
)


class LROOperationBase(OperationBase[LROResponseType]):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        namespace_model: "NamespaceModel",
        client: "Client",
        name: str,
        request_builder: RequestBuilder,
        parameters: ParameterList,
        responses: List[LROResponseType],
        exceptions: List[Response],
        *,
        overloads: Optional[List[Operation]] = None,
        public: bool = True,
        want_tracing: bool = True,
    ) -> None:
        super().__init__(
            namespace_model=namespace_model,
            client=client,
            yaml_data=yaml_data,
            name=name,
            request_builder=request_builder,
            parameters=parameters,
            responses=responses,
            exceptions=exceptions,
            overloads=overloads,
            public=public,
            want_tracing=want_tracing,
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
    def lro_response(self) -> Optional[LROResponseType]:
        responses_with_bodies = [r for r in self.responses if r.type]
        num_response_schemas = {
            id(r.type.yaml_data) for r in responses_with_bodies if r.type
        }
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

    def cls_type_annotation(self, *, async_mode: bool) -> str:
        """We don't want the poller to show up in ClsType, so we call super() on resposne type annotation"""
        return f"ClsType[{Response.type_annotation(self.responses[0], async_mode=async_mode)}]"

    @property
    def initial_operation(self) -> Operation:
        """Initial operation that creates the first call for LRO polling"""
        return Operation(
            yaml_data=self.yaml_data,
            namespace_model=self.namespace_model,
            client=self.client,
            request_builder=self.namespace_model.lookup_request_builder(
                id(self.yaml_data)
            ),
            name=self.name[5:] + "_initial",
            overloads=self.overloads,
            parameters=self.parameters,
            responses=[
                Response(
                    r.yaml_data, self.namespace_model, headers=r.headers, type=r.type
                )
                for r in self.responses
            ],
            exceptions=self.exceptions,
            public=False,
            want_tracing=False,
        )

    def get_poller(self, async_mode: bool) -> str:
        return self.responses[0].get_poller(async_mode)

    def get_polling_method(self, async_mode: bool) -> str:
        return self.responses[0].get_polling_method(async_mode)

    def get_base_polling_method(self, async_mode: bool) -> str:
        return self.responses[0].get_base_polling_method(async_mode)

    def get_base_polling_method_path(self, async_mode: bool) -> str:
        return self.responses[0].get_base_polling_method_path(async_mode)

    def get_no_polling_method(self, async_mode: bool) -> str:
        return self.responses[0].get_no_polling_method(async_mode)

    def imports(self, async_mode: bool, **kwargs: Any) -> FileImport:
        file_import = super().imports(async_mode, **kwargs)
        if self.abstract:
            return file_import
        if async_mode:
            file_import.add_submodule_import(
                f"azure.core.tracing.decorator_async",
                f"distributed_trace_async",
                ImportType.AZURECORE,
            )
        file_import.add_submodule_import(
            "typing", "Union", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        file_import.add_submodule_import("typing", "cast", ImportType.STDLIB)
        return file_import


class LROOperation(LROOperationBase[LROResponse]):
    ...
