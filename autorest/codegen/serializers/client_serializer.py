# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List
from . import utils
from ..models import CodeModel


class ClientSerializer:
    def __init__(self, code_model: CodeModel, is_python3_file: bool) -> None:
        self.code_model = code_model
        self.is_python3_file = is_python3_file

    def _init_signature(self, async_mode: bool) -> str:
        return utils.serialize_method(
            function_def="def",
            method_name="__init__",
            is_in_class=True,
            method_param_signatures=self.code_model.service_client.parameters.client_method_signature(
                async_mode or self.is_python3_file
            ),
        )

    def init_signature_and_response_type_annotation(self, async_mode: bool) -> str:
        init_signature = self._init_signature(async_mode)
        return utils.method_signature_and_response_type_annotation_template(
            is_python3_file=async_mode or self.is_python3_file,
            method_signature=init_signature,
            response_type_annotation="None",
        )

    def pop_kwargs_from_signature(self, async_mode: bool) -> List[str]:
        return utils.pop_kwargs_from_signature(
            self.code_model.service_client.parameters.kwargs_to_pop(
                async_mode or self.is_python3_file,
            ),
            check_kwarg_dict=False,
            pop_headers_kwarg=utils.PopKwargType.NO,
            pop_params_kwarg=utils.PopKwargType.NO,
        )

    def class_definition(self, async_mode) -> str:
        class_name = self.code_model.class_name
        has_mixin_og = any(og for og in self.code_model.operation_groups if og.is_empty_operation_group)
        base_class = ""
        if has_mixin_og:
            base_class = f"{class_name}OperationsMixin"
        elif not (async_mode or self.is_python3_file):
            base_class = "object"
        disable = ""
        if len(self.code_model.operation_groups) > 6:
            disable = "    # pylint: disable=too-many-instance-attributes"
        if base_class:
            return f"class {class_name}({base_class}):{disable}"
        return f"class {class_name}:{disable}"

    def property_descriptions(self, async_mode: bool) -> List[str]:
        retval: List[str] = []
        operations_folder = ".aio.operations." if async_mode else ".operations."
        for og in [og for og in self.code_model.operation_groups if not og.is_empty_operation_group]:
            retval.append(f":ivar {og.name}: {og.class_name} operations")
            retval.append(f":vartype {og.name}: {self.code_model.namespace}{operations_folder}{og.class_name}")
        for param in self.code_model.service_client.parameters.client_method:
            retval.append(f":{param.description_keyword} {param.serialized_name}: {param.description}")
            retval.append(f":{param.docstring_type_keyword} {param.serialized_name}: {param.docstring_type}")
        if self.code_model.has_lro_operations:
            retval.append(
                ":keyword int polling_interval: Default waiting time between two polls for LRO operations "
                "if no Retry-After header is present."
            )
        retval.append('"""')
        return retval

    def initialize_config(self) -> str:
        config_name = f"{self.code_model.class_name}Configuration"
        config_call = ", ".join(
            [
                f"{p.serialized_name}={p.serialized_name}"
                for p in self.code_model.service_client.parameters.config_method
                if not p.is_kwarg
            ] + [
                "**kwargs"
            ])
        return f"self._config = {config_name}({config_call})"

    def initialize_pipeline_client(self, async_mode: bool) -> str:
        host_variable_name = self.code_model.service_client.parameters.host_variable_name
        if self.code_model.service_client.has_parameterized_host:
            host_variable_name = "_" + host_variable_name # we don't want potential conflicts with input params
        pipeline_client_name = self.code_model.service_client.pipeline_class(async_mode)
        return f"self._client = {pipeline_client_name}(base_url={host_variable_name}, config=self._config, **kwargs)"

    def serializers_and_operation_groups_properties(self) -> List[str]:
        retval = []
        if self.code_model.sorted_schemas:
            client_models_value = "{k: v for k, v in models.__dict__.items() if isinstance(v, type)}"
        else:
            client_models_value = "{}  # type: Dict[str, Any]"
        if self.code_model.options["models_mode"]:
            retval.append(f"client_models = {client_models_value}")
        client_models_str = "client_models" if self.code_model.options["models_mode"] else ""
        retval.append(f"self._serialize = Serializer({client_models_str})")
        retval.append(f"self._deserialize = Deserializer({client_models_str})")
        if not self.code_model.options["client_side_validation"]:
            retval.append("self._serialize.client_side_validation = False")
        operation_groups = [og for og in self.code_model.operation_groups if not og.is_empty_operation_group]
        for og in operation_groups:
            disable_check = "  # pylint: disable=abstract-class-instantiated" if og.has_abstract_operations else ""
            retval.extend([
                f"self.{og.name} = {og.class_name}({disable_check}",
                "    self._client, self._config, self._serialize, self._deserialize",
                ")",
            ])
        return retval

    def _send_request_signature(self, async_mode: bool) -> str:
        return utils.serialize_method(
            function_def="def",
            method_name=self.code_model.send_request_name,
            is_in_class=True,
            method_param_signatures=self.code_model.service_client.send_request_signature(
                async_mode or self.is_python3_file
            ),
        )

    def send_request_signature_and_response_type_annotation(self, async_mode: bool) -> str:
        send_request_signature = self._send_request_signature(async_mode)
        return utils.method_signature_and_response_type_annotation_template(
            is_python3_file=async_mode or self.is_python3_file,
            method_signature=send_request_signature,
            response_type_annotation="Awaitable[AsyncHttpResponse]" if async_mode else "HttpResponse",
        )

    def _example_make_call(self, async_mode: bool) -> List[str]:
        http_response = "AsyncHttpResponse" if async_mode else "HttpResponse"
        retval = [
            f">>> response = {'await ' if async_mode else ''}client.{self.code_model.send_request_name}(request)"
        ]
        retval.append(f"<{http_response}: 200 OK>")
        return retval

    def _request_builder_example(self, async_mode: bool) -> List[str]:
        retval = [
            "We have helper methods to create requests specific to this service in " +
            f"`{self.code_model.namespace}.{self.code_model.rest_layer_name}`."
        ]
        retval.append("Use these helper methods to create the request you pass to this method.")
        retval.append("")

        request_builder = self.code_model.rest.request_builders[0]
        request_builder_signature = ", ".join(request_builder.parameters.call)
        if request_builder.builder_group_name:
            rest_imported = request_builder.builder_group_name
            request_builder_name = f"{request_builder.builder_group_name}.{request_builder.name}"
        else:
            rest_imported = request_builder.name
            request_builder_name = request_builder.name
        retval.append(f">>> from {self.code_model.namespace}.{self.code_model.rest_layer_name} import {rest_imported}")
        retval.append(f">>> request = {request_builder_name}({request_builder_signature})")
        retval.append(f"<HttpRequest [{request_builder.method}], url: '{request_builder.url}'>")
        retval.extend(self._example_make_call(async_mode))
        return retval

    def _rest_request_example(self, async_mode: bool) -> List[str]:
        retval = [">>> from azure.core.rest import HttpRequest"]
        retval.append('>>> request = HttpRequest("GET", "https://www.example.org/")')
        retval.append(f"<HttpRequest [GET], url: 'https://www.example.org/'>")
        retval.extend(self._example_make_call(async_mode))
        return retval

    def send_request_description(self, async_mode: bool) -> List[str]:
        retval = ['"""Runs the network request through the client\'s chained policies.']
        retval.append("")
        if self.code_model.options["builders_visibility"] != "embedded":
            retval.extend(self._request_builder_example(async_mode))
        else:
            retval.extend(self._rest_request_example(async_mode))
        retval.append("")
        retval.append("For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart")
        retval.append(f"")
        retval.append(":param request: The network request you want to make. Required.")
        retval.append(f":type request: ~azure.core.rest.HttpRequest")
        retval.append(":keyword bool stream: Whether the response payload will be streamed. Defaults to False.")
        retval.append(":return: The response of your network call. Does not do error handling on your response.")
        http_response = "AsyncHttpResponse" if async_mode else "HttpResponse"
        retval.append(f":rtype: ~azure.core.rest.{http_response}")
        retval.append('"""')
        return retval

    def serialize_path(self) -> List[str]:
        return utils.serialize_path(self.code_model.global_parameters.path, "self._serialize")

class ConfigSerializer:

    def __init__(self, code_model: CodeModel, is_python3_file: bool) -> None:
        self.code_model = code_model
        self.is_python3_file = is_python3_file

    def _init_signature(self, async_mode: bool) -> str:
        return utils.serialize_method(
            function_def="def",
            method_name="__init__",
            is_in_class=True,
            method_param_signatures=self.code_model.global_parameters.config_method_signature(
                async_mode or self.is_python3_file
            ),
        )

    def init_signature_and_response_type_annotation(self, async_mode: bool) -> str:
        init_signature = self._init_signature(async_mode)
        return utils.method_signature_and_response_type_annotation_template(
            is_python3_file=async_mode or self.is_python3_file,
            method_signature=init_signature,
            response_type_annotation="None",
        )

    def pop_kwargs_from_signature(self, async_mode: bool) -> List[str]:
        return utils.pop_kwargs_from_signature(
            self.code_model.global_parameters.config_kwargs_to_pop(
                async_mode or self.is_python3_file
            ),
            check_kwarg_dict=False,
            pop_headers_kwarg=utils.PopKwargType.NO,
            pop_params_kwarg=utils.PopKwargType.NO,
        )

    def set_constants(self) -> List[str]:
        return [
            f"self.{p.serialized_name} = {p.constant_declaration}"
            for p in self.code_model.global_parameters.constant
            if p not in self.code_model.global_parameters.method
        ]

    def check_required_parameters(self) -> List[str]:
        return [
            f'if {p.serialized_name} is None:\n'
            f'    raise ValueError("Parameter \'{p.serialized_name}\' must not be None.")'
            for p in self.code_model.global_parameters.config_method
            if p.required and not p.constant
        ]

    def property_descriptions(self) -> List[str]:
        retval: List[str] = []
        for p in self.code_model.global_parameters.config_method:
            retval.append(f":{p.description_keyword} {p.serialized_name}: {p.description}")
            retval.append(f":{p.docstring_type_keyword} {p.serialized_name}: {p.docstring_type}")
        retval.append('"""')
        return retval
