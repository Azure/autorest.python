# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from abc import abstractmethod, ABC
from autorest.codegen.models import code_model
from autorest.codegen.models.request_builder import RequestBuilder
from autorest.codegen.models.base_builder import BaseBuilder
from typing import Any, List, TypeVar, Dict
from ..models import (
    Operation,
    CodeModel,
    PagingOperation,
    LROOperation,
    LROPagingOperation,
    BaseBuilder,
    ObjectSchema,
)

T = TypeVar('T')
OrderedSet = Dict[T, None]

def _serialize_json_dict(template_representation: str) -> Any:
    return json.dumps(template_representation, sort_keys=True, indent=4)

class BuilderSerializerProtocol(ABC):

    @property
    @abstractmethod
    def _is_in_class(self) -> bool:
        ...

    @property
    @abstractmethod
    def _function_definition(self) -> str:
        """The def keyword for the function, i.e. 'def' or 'async def'"""
        ...

    @abstractmethod
    def _method_signature(self, builder: BaseBuilder) -> str:
        """Signature of the builder. Does not include return type annotation"""
        ...

    @abstractmethod
    def _parameters_method_signature(self, builder: BaseBuilder) -> List[str]:
        """Returns the parameter's portion of the method signature"""
        ...

    @abstractmethod
    def _response_type_annotation(self, builder: BaseBuilder, modify_if_head_as_boolean: bool = True) -> str:
        """The mypy type annotation for the response"""
        ...

    @abstractmethod
    def _response_type_annotation_wrapper(self, builder: BaseBuilder) -> List[str]:
        """Any wrappers that you want to go around the response type annotation"""
        ...

    @staticmethod
    @abstractmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str) -> str:
        """Template for how to combine the method signature + the response type annotation together. Called by
        method_signature_and_response_type_annotation"""
        ...

    @abstractmethod
    def method_signature_and_response_type_annotation(self, builder: BaseBuilder) -> str:
        """Combines the method signature + the response type annotation together"""
        ...

    @abstractmethod
    def description_and_summary(self, builder: BaseBuilder) -> List[str]:
        """Description + summary from the swagger. Will be formatted into the overall operation description"""
        ...

    @abstractmethod
    def response_docstring(self, builder: BaseBuilder) -> List[str]:
        """Response portion of the docstring"""
        ...

    @abstractmethod
    def _content_type_docstring(self, builder: BaseBuilder) -> str:
        """Docstring for content type kwarg"""

    @abstractmethod
    def get_example_template(self, builder: BaseBuilder) -> List[str]:
        ...

    @abstractmethod
    def _get_json_example_template(self, builder: BaseBuilder) -> List[str]:
        ...

    @abstractmethod
    def _has_json_example_template(self, builder: BaseBuilder) -> bool:
        ...

    @abstractmethod
    def _has_files_example_template(self, builder: BaseBuilder) -> bool:
        ...

    @abstractmethod
    def _json_example_param_name(self, builder: BaseBuilder) -> str:
        ...

    @abstractmethod
    def _get_files_example_template(self, builder: BaseBuilder) -> List[str]:
        ...

    @abstractmethod
    def _get_json_response_template(self, builder: BaseBuilder) -> List[str]:
        ...

class BuilderBaseSerializer(BuilderSerializerProtocol):
    def __init__(self, code_model: CodeModel) -> None:
        self.code_model = code_model

    def _method_signature(self, builder: BaseBuilder) -> str:
        lines: List[str] = []
        lines.append(f"{self._function_definition} {builder.name}(")
        if self._is_in_class:
            lines.append("    self,")
        lines.extend(self._parameters_method_signature(builder))
        lines.append(")")
        return "\n".join(lines)

    def _response_type_annotation_wrapper(self, builder: BaseBuilder) -> List[str]:
        return []

    def method_signature_and_response_type_annotation(self, builder: BaseBuilder) -> str:
        method_signature = self._method_signature(builder)
        response_type_annotation = self._response_type_annotation(builder)
        for wrapper in self._response_type_annotation_wrapper(builder)[::-1]:
            response_type_annotation = f"{wrapper}[{response_type_annotation}]"
        return self._method_signature_and_response_type_annotation_template(method_signature, response_type_annotation)

    def description_and_summary(self, builder: BaseBuilder) -> List[str]:
        description_list: List[str] = []
        description_list.append(f'{ builder.summary.strip() if builder.summary else builder.description.strip() }')
        if builder.summary and builder.description:
            description_list.append("")
            description_list.append(builder.description.strip())
        description_list.append("")
        return description_list

    def param_description(self, builder: BaseBuilder) -> List[str]:
        description_list: List[str] = []
        for parameter in builder.parameters.method:
            description_list.extend(f":param { parameter.serialized_name }: { parameter.description }".replace('\n', '\n ').split("\n"))
            description_list.append(f":type { parameter.serialized_name }: { parameter.docstring_type }")
        try:
            request_builder: RequestBuilder = builder.request_builder
        except AttributeError:
            request_builder: RequestBuilder = builder

        if len(request_builder.schema_requests) > 1:
            description_list.append(self._content_type_docstring(builder))
        return description_list

    def param_description_and_response_docstring(self, builder: Operation) -> List[str]:
        return self.param_description(builder) + self.response_docstring(builder)

    def _content_type_docstring(self, builder: Operation) -> str:
        try:
            content_type_constant = next(
                p for p in builder.parameters.constant
                if p.implementation == "Method" and
                not p.original_parameter and
                p.in_method_code and
                p.serialized_name == "content_type"
            )
        except StopIteration:
            raise ValueError("No content type parameter")
        media_types: OrderedSet[str] = {
            media_type: None
            for request in builder.requests
            for media_type in request.media_types
        }
        content_type_str = (
            f":keyword str content_type: Media type of the body sent to the API. Default value is {content_type_constant.constant_declaration}. " +
            "Allowed values are: {}.".format('", "'.join(media_types))
        )
        return content_type_str

    def get_example_template(self, builder: BaseBuilder) -> List[str]:
        if not builder.has_example_template or not self.code_model.no_models:
            return []
        template = ["Example:\n    .. code-block:: python"]
        if self._has_json_example_template:
            template.append("")
            template += self._get_json_example_template(builder)
        if self._has_files_example_template:
            template.append("")
            template += self._get_files_example_template(builder)
        if builder.get_json_response_template_to_status_codes():
            template.append("")
            template += self._get_json_response_template(builder)
        return template

    def _get_json_example_template(self, builder: BaseBuilder) -> List[str]:
        template = []
        json_body = builder.parameters.json_body

        if isinstance(json_body, ObjectSchema):
            discriminator_name = json_body.discriminator_name
            if discriminator_name:
                template.append(
                    "{} = '{}'".format(
                        discriminator_name,
                        "' or '".join(json_body.subtype_map.values())
                    )
                )
                template.append([""])
            property_with_discriminator = json_body.property_with_discriminator
            if property_with_discriminator:
                polymorphic_schemas = [
                    s for s in self.code_model.sorted_schemas
                    if s.name in property_with_discriminator.schema.subtype_map.values()
                ]
                num_schemas = min(
                    self.code_model.options['polymorphic_examples'],
                    len(polymorphic_schemas)
                )
                for i in range(num_schemas):
                    schema = polymorphic_schemas[i]
                    template.append(
                        f"{property_with_discriminator.name} = {_serialize_json_dict(schema.get_json_template_representation())}"
                    )
                    if i != num_schemas - 1:
                        template.append("# OR")
                template.append("")
        template.append("# JSON input template you can fill out and use as your `json` input.")
        template.append(
            f"{self._json_example_param_name(builder)} = {builder.parameters.get_json_template_representation()}"
        )
        return template

    def _get_files_example_template(self, builder: BaseBuilder) -> List[str]:
        return [
            "# multipart input template you can fill out and use as your `files` input.",
            f"files = {builder.parameters.get_files_template_representation()}"
        ]

    def _get_json_response_template(self, builder: BaseBuilder) -> List[str]:
        template = []
        for response_body, status_codes in builder._get_json_response_template_to_status_codes().items():
            template.append("# response body for status code(s): {}".format(', '.join(status_codes)))
            template.append(f"response_body == {response_body}")
        return template

############################## REQUEST BUILDERS ##############################

class RequestBuilderBaseSerializer(BuilderBaseSerializer):

    @property
    def _function_definition(self) -> str:
        return "def"

    @property
    def _is_in_class(self) -> bool:
        return False

    def _response_type_annotation(self, builder: RequestBuilder, modify_if_head_as_boolean: bool = True) -> str:
        return "HttpRequest"

    def response_docstring(self, builder: RequestBuilder) -> List[str]:
        core_import = "{}.core.rest".format(
            self.code_model.namespace if self.code_model.options["vendor"] else "azure"
        )
        response_str = (
            f":return: Returns an :class:`~{ core_import }.HttpRequest` that you will pass to the client's " +
            "`send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to " +
            "incorporate this response into your code flow."
        )
        rtype_str = f":rtype: ~{ core_import }.HttpRequest"
        return [response_str, rtype_str]

    def _json_example_param_name(self, builder: RequestBuilder) -> str:
        return "json"

    def _has_json_example_template(self, builder: RequestBuilder) -> bool:
        return "json" in builder.parameters.body_kwarg_names

    def _has_files_example_template(self, builder: RequestBuilder) -> bool:
        return "files" in builder.parameters.body_kwarg_names

class RequestBuilderGenericSerializer(RequestBuilderBaseSerializer):
    def _parameters_method_signature(self, builder: RequestBuilder) -> List[str]:
        params = [
            f"{param.method_signature(async_mode=False)}"
            for param in builder.parameters.method
        ]
        params.append("**kwargs  # type: Any")
        return params

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str):
        return f"{method_signature}:\n    # type: (...) -> {_response_type_annotation}"

class RequestBuilderPython3Serializer(RequestBuilderBaseSerializer):

    def _parameters_method_signature(self, builder: RequestBuilder) -> List[str]:
        params = [
            f"{param.method_signature(async_mode=True)}"
            for param in builder.parameters.method
        ]
        params.append("**kwargs: Any")
        return params

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str):
        return f"{method_signature} -> {_response_type_annotation}:"

############################## NORMAL OPERATIONS ##############################

class OperationBaseSerializer(BuilderBaseSerializer):

    def description_and_summary(self, builder: Operation) -> List[str]:
        retval = super().description_and_summary(builder)
        if builder.deprecated:
            retval.append(".. warning::")
            retval.append("    This method is deprecated")
            retval.append("")
        return retval

    @property
    def _is_in_class(self) -> bool:
        return True

    def _response_docstring_type_wrapper(self, builder: BaseBuilder) -> List[str]:
        return []

    def param_description(self, builder: Operation) -> List[str]:
        description_list = super().param_description(builder)
        description_list.append(":keyword callable cls: A custom type or function that will be passed the direct response")
        return description_list

    def _response_docstring_type_template(self, builder: BaseBuilder) -> str:
        retval = "{}"
        for wrapper in self._response_docstring_type_wrapper(builder)[::-1]:
            retval = f"{wrapper}[{retval}]"
        return retval

    def _response_type_annotation(self, builder: Operation, modify_if_head_as_boolean: bool = True) -> str:
        if modify_if_head_as_boolean and builder.request_builder.method == 'head' and self.code_model.options['head_as_boolean']:
            return "bool"
        response_body_annotations: OrderedSet[str] = {}
        for response in [r for r in builder.responses if r.has_body]:
            response_body_annotations[response.operation_type_annotation] = None
        response_str = ", ".join(response_body_annotations.keys()) or "None"
        if len(response_body_annotations) > 1:
            response_str = f"Union[{response_str}]"
        if builder.has_optional_return_type:
            response_str = f"Optional[{response_str}]"
        return response_str

    def cls_type_annotation(self, builder: Operation) -> str:
        return f"# type: ClsType[{self._response_type_annotation(builder, modify_if_head_as_boolean=False)}]"

    def _response_docstring_text_template(self, builder: Operation) -> str:
        return "{}, or the result of cls(response)"

    def response_docstring(self, builder: Operation) -> List[str]:
        responses_with_body = [r for r in builder.responses if r.has_body]
        if builder.request_builder.method == 'head' and self.code_model.options['head_as_boolean']:
            response_docstring_text = "bool"
            rtype = "bool"
        elif responses_with_body:
            response_body_docstring_text: OrderedSet[str] = {
                response.docstring_text: None
                for response in responses_with_body
            }
            response_docstring_text = " or ".join(response_body_docstring_text.keys())
            response_body_docstring_type: OrderedSet[str] = {
                response.docstring_type: None
                for response in responses_with_body
            }
            rtype = ' or '.join(response_body_docstring_type.keys())
            if builder.has_optional_return_type:
                rtype += " or None"
        else:
            response_docstring_text = "None"
            rtype = "None"
        response_str = f":return: {self._response_docstring_text_template(builder).format(response_docstring_text)}"
        rtype_str = f":rtype: {self._response_docstring_type_template(builder).format(rtype)}"
        return [response_str, rtype_str, ":raises: ~azure.core.exceptions.HttpResponseError"]

    def _json_example_param_name(self, builder: Operation) -> str:
        return builder.parameters.body[0].serialized_name

    def _has_json_example_template(self, builder: BaseBuilder) -> bool:
        return builder.parameters.has_body

    def _has_files_example_template(self, builder: RequestBuilder) -> bool:
        return False

class SyncOperationSerializer(OperationBaseSerializer):

    @property
    def _function_definition(self) -> str:
        return "def"

    def _parameters_method_signature(self, builder: Operation) -> List[str]:
        params = [
            f"    {param.method_signature(async_mode=False)}"
            for param in builder.parameters.method
        ]
        params.append("    **kwargs  # type: Any")
        return params

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str):
        return f"{method_signature}:\n    # type: (...) -> {_response_type_annotation}"

class AsyncOperationSerializer(OperationBaseSerializer):

    @property
    def _function_definition(self) -> str:
        return "async def"

    def _parameters_method_signature(self, builder: Operation) -> List[str]:
        params = [
            f"    {param.method_signature(async_mode=True)}"
            for param in builder.parameters.method
        ]
        params.append("    **kwargs: Any")
        return params

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str):
        return f"{method_signature} -> {_response_type_annotation}:"

############################## PAGING OPERATIONS ##############################

class PagingOperationBaseSerializer(OperationBaseSerializer):

    def _response_docstring_text_template(self, builder: PagingOperation) -> str:
        return "An iterator like instance of either {} or the result of cls(response)"

    def cls_type_annotation(self, builder: PagingOperation) -> str:
        interior = super()._response_type_annotation(builder, modify_if_head_as_boolean=False)
        return f"# type: ClsType[{interior}]"


class SyncPagingOperationSerializer(PagingOperationBaseSerializer, SyncOperationSerializer):

    def _response_docstring_type_wrapper(self, builder: PagingOperation) -> List[str]:
        return [f"~{builder.get_pager_path(async_mode=False)}"]

    def _response_type_annotation_wrapper(self, builder: BaseBuilder) -> List[str]:
        return ["Iterable"]

class AsyncPagingOperationSerializer(PagingOperationBaseSerializer, AsyncOperationSerializer):

    def _response_docstring_type_wrapper(self, builder: PagingOperation) -> List[str]:
        return [f"~{builder.get_pager_path(async_mode=True)}"]

    @property
    def _function_definition(self) -> str:
        return "def"

    def _response_type_annotation_wrapper(self, builder: PagingOperation) -> List[str]:
        return ["AsyncIterable"]


############################## LRO OPERATIONS ##############################

class LROOperationBaseSerializer(OperationBaseSerializer):

    def cls_type_annotation(self, builder: LROOperation) -> str:
        return f"# type: ClsType[{super()._response_type_annotation(builder, modify_if_head_as_boolean=False)}]"

    def _method_signature(self, builder: LROOperation) -> str:
        lines: List[str] = []
        lines.append(f"{self._function_definition} begin_{builder.name}(")
        lines.append("    self,")
        lines.extend(self._parameters_method_signature(builder))
        lines.append(")")
        return "\n".join(lines)


    @abstractmethod
    def _default_polling_method(self, builder: LROOperation) -> str:
        ...

    @property
    @abstractmethod
    def _polling_method_type(self):
        ...

    def param_description(self, builder: LROOperation) -> List[str]:
        retval = super().param_description(builder)
        retval.append(":keyword str continuation_token: A continuation token to restart a poller from a saved state.")
        retval.append(
            f":keyword polling: By default, your polling method will be {self._default_polling_method(builder)}. Pass in False for this "
            "operation to not poll, or pass in your own initialized polling object for a personal polling strategy."
        )
        retval.append(f":paramtype polling: bool or ~{self._polling_method_type}")
        retval.append(":keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.")
        return retval

class SyncLROOperationSerializer(LROOperationBaseSerializer, SyncOperationSerializer):

    def _response_docstring_text_template(self, builder: LROOperation) -> str:
        lro_section = f"An instance of {builder.get_poller(async_mode=False)} "
        return lro_section + "that returns either {} or the result of cls(response)"

    def _response_docstring_type_wrapper(self, builder: LROOperation) -> List[str]:
        return [f"~{builder.get_poller_path(async_mode=False)}"]

    def _response_type_annotation_wrapper(self, builder: LROOperation) -> List[str]:
        return [builder.get_poller(async_mode=False)]

    def _default_polling_method(self, builder: LROOperation) -> str:
        return builder.get_default_polling_method(
            async_mode=False, azure_arm=self.code_model.options["azure_arm"]
        )

    @property
    def _polling_method_type(self):
        return "azure.core.polling.PollingMethod"

class AsyncLROOperationSerializer(LROOperationBaseSerializer, AsyncOperationSerializer):

    def _response_docstring_text_template(self, builder: LROOperation) -> str:
        lro_section = f"An instance of {builder.get_poller(async_mode=True)} "
        return lro_section + "that returns either {} or the result of cls(response)"

    def _response_docstring_type_wrapper(self, builder: LROOperation) -> List[str]:
        return [f"~{builder.get_poller_path(async_mode=True)}"]

    def _response_type_annotation_wrapper(self, builder: LROOperation) -> List[str]:
        return [builder.get_poller(async_mode=True)]

    def _default_polling_method(self, builder: LROOperation) -> str:
        return builder.get_default_polling_method(
            async_mode=True, azure_arm=self.code_model.options["azure_arm"]
        )

    @property
    def _polling_method_type(self):
        return "azure.core.polling.AsyncPollingMethod"

############################## LRO PAGING OPERATIONS ##############################

class SyncLROPagingOperationSerializer(SyncLROOperationSerializer, SyncPagingOperationSerializer):

    def _response_docstring_type_wrapper(self, builder: LROPagingOperation) -> List[str]:
        return (
            SyncLROOperationSerializer._response_docstring_type_wrapper(self, builder) +
            SyncPagingOperationSerializer._response_docstring_type_wrapper(self, builder)
        )

    def _response_type_annotation_wrapper(self, builder: LROPagingOperation) -> List[str]:
        return (
            SyncLROOperationSerializer._response_type_annotation_wrapper(self, builder) +
            [builder.get_pager(async_mode=False)]
        )

    def _response_docstring_text_template(self, builder: LROPagingOperation) -> str:
        lro_doc = SyncLROOperationSerializer._response_docstring_text_template(self, builder)
        paging_doc = SyncPagingOperationSerializer._response_docstring_text_template(self, builder)
        paging_doc = paging_doc.replace(paging_doc[0], paging_doc[0].lower(), 1)
        return lro_doc.format(paging_doc).replace(" or the result of cls(response)", "", 1).replace("either ", "", 1)

    def cls_type_annotation(self, builder: LROPagingOperation) -> str:
        return f"# type: ClsType[{self._response_type_annotation(builder, modify_if_head_as_boolean=False)}]"

class AsyncLROPagingOperationSerializer(AsyncLROOperationSerializer, AsyncPagingOperationSerializer):

    def _response_docstring_type_wrapper(self, builder: LROPagingOperation) -> List[str]:
        return (
            AsyncLROOperationSerializer._response_docstring_type_wrapper(self, builder) +
            AsyncPagingOperationSerializer._response_docstring_type_wrapper(self, builder)
        )

    def _response_type_annotation_wrapper(self, builder: LROPagingOperation) -> List[str]:
        return (
            AsyncLROOperationSerializer._response_type_annotation_wrapper(self, builder) +
            [builder.get_pager(async_mode=True)]
        )

    def _response_docstring_text_template(self, builder: LROPagingOperation) -> str:
        lro_doc = AsyncLROOperationSerializer._response_docstring_text_template(self, builder)
        paging_doc = AsyncPagingOperationSerializer._response_docstring_text_template(self, builder)
        paging_doc = paging_doc.replace(paging_doc[0], paging_doc[0].lower(), 1)
        return lro_doc.format(paging_doc).replace(" or the result of cls(response)", "", 1).replace("either ", "", 1)

