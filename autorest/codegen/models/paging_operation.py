# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Dict, List, Any, Optional, Union, TYPE_CHECKING, cast, TypeVar

from .operation import Operation, OperationBase
from .response import PagingResponse, LROPagingResponse, Response
from .request_builder import (
    OverloadedRequestBuilder,
    RequestBuilder,
    get_request_builder,
)
from .imports import ImportType, FileImport, TypingSection
from .parameter_list import ParameterList
from .model_type import ModelType

if TYPE_CHECKING:
    from .code_model import CodeModel

PagingResponseType = TypeVar(
    "PagingResponseType", bound=Union[PagingResponse, LROPagingResponse]
)


class PagingOperationBase(OperationBase[PagingResponseType]):
    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        name: str,
        request_builder: RequestBuilder,
        parameters: ParameterList,
        responses: List[PagingResponseType],
        exceptions: List[Response],
        *,
        overloads: Optional[List[Operation]] = None,
        public: bool = True,
        want_tracing: bool = True,
        override_success_response_to_200: bool = False,
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
        )
        self.next_request_builder: Optional[
            Union[RequestBuilder, OverloadedRequestBuilder]
        ] = (
            get_request_builder(self.yaml_data["nextOperation"], code_model)
            if self.yaml_data.get("nextOperation")
            else None
        )
        self.override_success_response_to_200 = override_success_response_to_200
        self.pager_sync: str = yaml_data["pagerSync"]
        self.pager_async: str = yaml_data["pagerAsync"]

    def _get_attr_name(self, rest_api_name: str) -> str:
        response = self.responses[0]
        try:
            return next(
                p.client_name
                for p in cast(ModelType, response.type).properties
                if p.rest_api_name == rest_api_name
            )
        except StopIteration:
            raise ValueError(
                f"Can't find a matching property in response for {rest_api_name}"
            )

    def get_pager(self, async_mode: bool) -> str:
        return self.responses[0].get_pager(async_mode)

    @property
    def continuation_token_name(self) -> Optional[str]:
        rest_api_name = self.yaml_data["continuationTokenName"]
        if not rest_api_name:
            # That's an ok scenario, it just means no next page possible
            return None
        if self.code_model.options["models_mode"]:
            return self._get_attr_name(rest_api_name)
        return rest_api_name

    @property
    def item_name(self) -> str:
        rest_api_name = self.yaml_data["itemName"]
        if self.code_model.options["models_mode"]:
            return self._get_attr_name(rest_api_name)
        return rest_api_name

    @property
    def operation_type(self) -> str:
        return "paging"

    def cls_type_annotation(self, *, async_mode: bool) -> str:
        return f"ClsType[{Response.type_annotation(self.responses[0], async_mode=async_mode)}]"

    def _imports_shared(self, async_mode: bool, **kwargs: Any) -> FileImport:
        file_import = super()._imports_shared(async_mode, **kwargs)
        if async_mode:
            file_import.add_submodule_import(
                "typing", "AsyncIterable", ImportType.STDLIB, TypingSection.CONDITIONAL
            )
        else:
            file_import.add_submodule_import(
                "typing", "Iterable", ImportType.STDLIB, TypingSection.CONDITIONAL
            )
        if (
            self.next_request_builder
            and self.code_model.options["builders_visibility"] == "embedded"
            and not async_mode
        ):
            file_import.merge(self.next_request_builder.imports())
        return file_import

    @property
    def has_optional_return_type(self) -> bool:
        return False

    def imports(self, async_mode: bool, **kwargs: Any) -> FileImport:
        if self.abstract:
            return FileImport()
        file_import = self._imports_shared(async_mode, **kwargs)
        file_import.merge(super().imports(async_mode, **kwargs))
        if self.code_model.options["tracing"] and self.want_tracing:
            file_import.add_submodule_import(
                "azure.core.tracing.decorator",
                "distributed_trace",
                ImportType.AZURECORE,
            )
        if self.next_request_builder:
            file_import.merge(
                self.get_request_builder_import(self.next_request_builder, async_mode)
            )
        elif "api-version" in [
            p.rest_api_name for p in self.code_model.client.parameters
        ]:
            file_import.add_submodule_import(
                "urllib.parse", "urlparse", ImportType.STDLIB
            )
            file_import.add_submodule_import(
                "urllib.parse", "urljoin", ImportType.STDLIB
            )
            file_import.add_submodule_import(
                "urllib.parse", "parse_qs", ImportType.STDLIB
            )
            file_import.add_submodule_import(
                "azure.core.utils", "case_insensitive_dict", ImportType.AZURECORE
            )
        return file_import


class PagingOperation(PagingOperationBase[PagingResponse]):
    ...
