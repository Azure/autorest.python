# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Optional
from .primitive_schemas import StringSchema
from .parameter import Parameter, ParameterLocation
from .parameter_list import GlobalParameterList
from .imports import FileImport, ImportType, TypingSection


class Client:
    """A service client.
    """

    def __init__(self, parameters: GlobalParameterList):
        self.parameters = parameters
        self.base_url: Optional[str] = None
        self.custom_base_url = None
        self._config_parameters = parameters

    @staticmethod
    def pipeline_class(code_model, async_mode: bool) -> str:
        if code_model.options["azure_arm"]:
            if async_mode:
                return "AsyncARMPipelineClient"
            return "ARMPipelineClient"
        if async_mode:
            return "AsyncPipelineClient"
        return "PipelineClient"

    def imports(self, code_model, async_mode: bool) -> FileImport:
        file_import = FileImport()

        file_import.add_from_import("msrest", "Serializer", ImportType.AZURECORE)
        file_import.add_from_import("msrest", "Deserializer", ImportType.AZURECORE)
        file_import.add_from_import("typing", "Any", ImportType.STDLIB, TypingSection.CONDITIONAL)
        core_import = (code_model.namespace if code_model.options["vendor"] else "azure") + ".core.rest"
        if async_mode:
            file_import.add_from_import(
                core_import, "AsyncHttpResponse", ImportType.AZURECORE, TypingSection.CONDITIONAL
            )
        else:
            file_import.add_from_import(
                core_import, "HttpResponse", ImportType.AZURECORE, TypingSection.CONDITIONAL
            )
        file_import.add_from_import(
            core_import, "HttpRequest", ImportType.AZURECORE, TypingSection.CONDITIONAL
        )
        any_optional_gp = any(not gp.required for gp in self.parameters)

        if any_optional_gp or code_model.service_client.base_url:
            file_import.add_from_import("typing", "Optional", ImportType.STDLIB, TypingSection.CONDITIONAL)

        if code_model.options["azure_arm"]:
            file_import.add_from_import(
                "azure.mgmt.core", Client.pipeline_class(code_model, async_mode), ImportType.AZURECORE
            )
        else:
            file_import.add_from_import(
                "azure.core", Client.pipeline_class(code_model, async_mode), ImportType.AZURECORE
            )

        if not code_model.sorted_schemas:
            # in this case, we have client_models = {} in the service client, which needs a type annotation
            # this import will always be commented, so will always add it to the typing section
            file_import.add_from_import("typing", "Dict", ImportType.STDLIB, TypingSection.TYPING)
        file_import.add_from_import("copy", "deepcopy", ImportType.STDLIB)

        return file_import

    @property
    def method_parameters(self) -> List[Parameter]:
        base_url_param = []
        if self.base_url:
            base_url_param = [Parameter(
                yaml_data={},
                schema=StringSchema(namespace="", yaml_data={"type": "str"}),
                rest_api_name="base_url",
                serialized_name="base_url",
                description="Service URL",
                implementation="Client",
                required=False,
                location=ParameterLocation.Other,
                skip_url_encoding=False,
                constraints=[],
            )]
        return self.parameters.method + base_url_param

    def method_parameters_signature(self, async_mode) -> List[str]:
        return [
            parameter.method_signature(async_mode)
            for parameter in self.method_parameters
        ] + self.parameters.method_signature_kwargs(async_mode)

    @property
    def config_initialization(self) -> str:
        method = ", ".join([p.serialized_name for p in self.parameters.method])
        if method:
            return method + ", **kwargs"
        return "**kwargs"
