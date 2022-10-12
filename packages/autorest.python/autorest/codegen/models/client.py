# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Any, Dict, TYPE_CHECKING, TypeVar, Generic, Union, List, Optional

from .base_model import BaseModel
from .parameter_list import ClientGlobalParameterList, ConfigGlobalParameterList
from .imports import FileImport, ImportType, TypingSection, MsrestImportType
from .utils import add_to_pylint_disable
from .operation_group import OperationGroup
from .request_builder import RequestBuilder, OverloadedRequestBuilder, get_request_builder
from .parameter import Parameter

ParameterListType = TypeVar(
    "ParameterListType",
    bound=Union[ClientGlobalParameterList, ConfigGlobalParameterList],
)

if TYPE_CHECKING:
    from .code_model import CodeModel


class _ClientConfigBase(Generic[ParameterListType], BaseModel):
    """The service client base. Shared across our Client and Config type"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "CodeModel",
        parameters: ParameterListType,
    ):
        super().__init__(yaml_data, code_model)
        self.parameters = parameters
        self.url: str = self.yaml_data[
            "url"
        ]  # the base endpoint of the client. Can be parameterized or not

    @property
    def description(self) -> str:
        return self.yaml_data["description"]

    @property
    def name(self) -> str:
        return self.yaml_data["name"]


class Client(_ClientConfigBase[ClientGlobalParameterList]):
    """Model representing our service client"""

    def __init__(
        self,
        yaml_data: Dict[str, Any],
        code_model: "NamespaceCodeModel",
        parameters: ClientGlobalParameterList
    ):
        super().__init__(yaml_data, code_model, parameters)
        self.operation_groups: List[OperationGroup] = []
        self.request_builders: List[
            Union[RequestBuilder, OverloadedRequestBuilder]
        ] = []
        self._build_request_builders()
        self._build_operations()
        self.config = Config()

    def _build_request_builders(self) -> None:
        if not self.yaml_data.get("operationGroups"):
            return
        for og_group in self.yaml_data["operationGroups"]:
            for operation_yaml in og_group["operations"]:
                request_builder = get_request_builder(
                    operation_yaml, code_model=self.code_model
                )
                if request_builder.overloads:
                    self.request_builders.extend(request_builder.overloads)  # type: ignore
                self.request_builders.append(request_builder)
                if operation_yaml.get("nextOperation"):
                    # i am a paging operation and i have a next operation. Make sure to include my next operation
                    self.request_builders.append(
                        get_request_builder(
                            operation_yaml["nextOperation"], code_model=self.code_model
                        )
                    )

    def _build_operations(self) -> None:
        if self.code_model.options["show_operations"] and self.yaml_data.get("operationGroups"):
            self.operation_groups = [
                OperationGroup.from_yaml(op_group, self.code_model)
                for op_group in self.yaml_data["operationGroups"]
            ]


    def pipeline_class(self, async_mode: bool) -> str:
        if self.code_model.options["azure_arm"]:
            if async_mode:
                return "AsyncARMPipelineClient"
            return "ARMPipelineClient"
        if async_mode:
            return "AsyncPipelineClient"
        return "PipelineClient"

    @property
    def credential(self) -> Optional[Parameter]:
        """The credential param, if one exists"""
        return self.parameters.credential

    @property
    def send_request_name(self) -> str:
        """Name of the send request function"""
        return (
            "send_request"
            if self.code_model.options["show_send_request"]
            else "_send_request"
        )

    @property
    def has_parameterized_host(self) -> bool:
        """Whether the base url is parameterized or not"""
        return not any(p for p in self.parameters if p.is_host)

    @property
    def pylint_disable(self) -> str:
        retval = add_to_pylint_disable("", "client-accepts-api-version-keyword")
        if len(self.operation_groups) > 6:
            retval = add_to_pylint_disable(retval, "too-many-instance-attributes")
        return retval

    @property
    def filename(self) -> str:
        """Name of the file for the client"""
        if (
            self.code_model.options["version_tolerant"]
            or self.code_model.options["low_level_client"]
        ):
            return "_client"
        return f"_{self.code_model.module_name}"

    def lookup_request_builder(
        self, request_builder_id: int
    ) -> Union[RequestBuilder, OverloadedRequestBuilder]:
        """Find the request builder based off of id"""
        try:
            return next(
                rb
                for rb in self.request_builders
                if id(rb.yaml_data) == request_builder_id
            )
        except StopIteration:
            raise KeyError(f"No request builder with id {request_builder_id} found.")

    def _imports_shared(self, async_mode: bool) -> FileImport:
        file_import = FileImport()

        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        if self.code_model.options["azure_arm"]:
            file_import.add_submodule_import(
                "azure.mgmt.core", self.pipeline_class(async_mode), ImportType.AZURECORE
            )
        else:
            file_import.add_submodule_import(
                "azure.core", self.pipeline_class(async_mode), ImportType.AZURECORE
            )

        for gp in self.parameters:
            file_import.merge(gp.imports(async_mode))
        file_import.add_submodule_import(
            "._configuration",
            f"{self.code_model.client.name}Configuration",
            ImportType.LOCAL,
        )
        file_import.add_msrest_import(
            self.code_model,
            ".." if async_mode else ".",
            MsrestImportType.SerializerDeserializer,
            TypingSection.REGULAR,
        )

        return file_import

    @property
    def has_mixin(self) -> bool:
        """Do we want a mixin ABC class for typing purposes?"""
        return any(o for o in self.operation_groups if o.is_mixin)

    @property
    def need_format_url(self) -> bool:
        """Whether we need to format urls. If so, we need to vendor core."""
        return any(rq for rq in self.request_builders if rq.parameters.path)

    @property
    def has_lro_operations(self) -> bool:
        """Are there any LRO operations in this SDK?"""
        return any(
            [
                operation.operation_type in ("lro", "lropaging")
                for operation_group in self.operation_groups
                for operation in operation_group.operations
            ]
        )

    def format_lro_operations(self) -> None:
        """Adds operations and attributes needed for LROs.
        If there are LRO functions in here, will add initial LRO function. Will also set the return
        type of the LRO operation
        """
        for operation_group in self.operation_groups:
            i = 0
            while i < len(operation_group.operations):
                operation = operation_group.operations[i]
                if operation.operation_type in ("lro", "lropaging"):
                    operation_group.operations.insert(i, operation.initial_operation)  # type: ignore
                    i += 1
                i += 1

    @property
    def need_request_converter(self) -> bool:
        """
        Whether we need to convert our created azure.core.rest.HttpRequests to
        azure.core.pipeline.transport.HttpRequests
        """
        return (
            self.code_model.options["show_operations"]
            and bool(self.request_builders)
            and not self.code_model.options["version_tolerant"]
        )

    def need_vendored_code(self, async_mode: bool) -> bool:
        """Whether we need to vendor code in the _vendor.py file for this SDK"""
        if self.has_abstract_operations:
            return True
        if async_mode:
            return self.has_mixin
        return (
            self.need_request_converter or self.need_format_url or self.has_mixin
        )

    @property
    def has_abstract_operations(self) -> bool:
        """Whether there is abstract operation in any operation group."""
        return any(og.has_abstract_operations for og in self.operation_groups)

    def imports(self, async_mode: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)
        if async_mode:
            file_import.add_submodule_import("typing", "Awaitable", ImportType.STDLIB)
            file_import.add_submodule_import(
                "azure.core.rest",
                "AsyncHttpResponse",
                ImportType.AZURECORE,
                TypingSection.CONDITIONAL,
            )
        else:
            file_import.add_submodule_import(
                "azure.core.rest",
                "HttpResponse",
                ImportType.AZURECORE,
                TypingSection.CONDITIONAL,
            )
        file_import.add_submodule_import(
            "azure.core.rest",
            "HttpRequest",
            ImportType.AZURECORE,
            TypingSection.CONDITIONAL,
        )
        for og in self.code_model.operation_groups:
            file_import.add_submodule_import(
                f".{self.code_model.operations_folder_name}",
                og.class_name,
                ImportType.LOCAL,
            )

        if (
            self.code_model.model_types
            and self.code_model.options["models_mode"] == "msrest"
        ):
            path_to_models = ".." if async_mode else "."
            if len(self.code_model.model_types) != len(
                self.code_model.public_model_types
            ):
                # this means we have hidden models. In that case, we import directly from the models
                # file, not the module, bc we don't expose the hidden models in the models module

                # Also in this case, we're in version tolerant, so python3 only is true
                file_import.add_submodule_import(
                    f"{path_to_models}models",
                    self.code_model.models_filename,
                    ImportType.LOCAL,
                    alias="models",
                )
            else:
                file_import.add_submodule_import(
                    path_to_models, "models", ImportType.LOCAL
                )
        elif self.code_model.options["models_mode"] == "msrest":
            # in this case, we have client_models = {} in the service client, which needs a type annotation
            # this import will always be commented, so will always add it to the typing section
            file_import.add_submodule_import(
                "typing", "Dict", ImportType.STDLIB, TypingSection.TYPING
            )
        file_import.add_submodule_import("copy", "deepcopy", ImportType.STDLIB)
        return file_import

    def imports_for_multiapi(self, async_mode: bool) -> FileImport:
        file_import = self._imports_shared(async_mode)
        file_import.add_submodule_import(
            "typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        try:
            mixin_operation = next(
                og for og in self.code_model.operation_groups if og.is_mixin
            )
            file_import.add_submodule_import(
                "._operations_mixin", mixin_operation.class_name, ImportType.LOCAL
            )
        except StopIteration:
            pass
        file_import.add_submodule_import(
            "azure.profiles", "KnownProfiles", import_type=ImportType.AZURECORE
        )
        file_import.add_submodule_import(
            "azure.profiles", "ProfileDefinition", import_type=ImportType.AZURECORE
        )
        file_import.add_submodule_import(
            "azure.profiles.multiapiclient",
            "MultiApiClientMixin",
            import_type=ImportType.AZURECORE,
        )
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "Client":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            parameters=ClientGlobalParameterList.from_yaml(yaml_data, code_model),
        )


class Config(_ClientConfigBase[ConfigGlobalParameterList]):
    """Model representing our Config type."""

    @property
    def description(self) -> str:
        return (
            f"Configuration for {self.yaml_data['name']}.\n\n."
            "Note that all parameters used to create this instance are saved as instance attributes."
        )

    @property
    def name(self) -> str:
        return f"{super().name}Configuration"

    def imports(self, async_mode: bool) -> FileImport:
        file_import = FileImport()
        file_import.add_submodule_import(
            "azure.core.configuration", "Configuration", ImportType.AZURECORE
        )
        file_import.add_submodule_import(
            "azure.core.pipeline", "policies", ImportType.AZURECORE
        )
        file_import.add_submodule_import(
            "typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL
        )
        if self.code_model.options["package_version"]:
            file_import.add_submodule_import(
                ".._version" if async_mode else "._version", "VERSION", ImportType.LOCAL
            )
        for gp in self.parameters:
            file_import.merge(gp.imports(async_mode=async_mode))
        if self.code_model.options["azure_arm"]:
            policy = (
                "AsyncARMChallengeAuthenticationPolicy"
                if async_mode
                else "ARMChallengeAuthenticationPolicy"
            )
            file_import.add_submodule_import(
                "azure.mgmt.core.policies", "ARMHttpLoggingPolicy", ImportType.AZURECORE
            )
            file_import.add_submodule_import(
                "azure.mgmt.core.policies", policy, ImportType.AZURECORE
            )
        return file_import

    @classmethod
    def from_yaml(cls, yaml_data: Dict[str, Any], code_model: "CodeModel") -> "Config":
        return cls(
            yaml_data=yaml_data,
            code_model=code_model,
            parameters=ConfigGlobalParameterList.from_yaml(yaml_data, code_model),
        )
