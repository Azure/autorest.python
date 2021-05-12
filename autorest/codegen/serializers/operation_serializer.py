# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from abc import abstractmethod, ABC
from autorest.codegen.models import parameter_list
from os import stat
from typing import List, TypeVar, Dict
from ..models import (
    Operation,
    CodeModel,
    PagingOperation,
    LROOperation,
    LROPagingOperation,
)

T = TypeVar('T')
OrderedSet = Dict[T, None]

class OperationSerializerProtocol(ABC):

    @property
    @abstractmethod
    def _function_definition(self) -> str:
        """The def keyword for the function, i.e. 'def' or 'async def'"""
        ...

    @abstractmethod
    def _method_signature(self, operation: Operation) -> str:
        """Signature of the operation. Does not include return type annotation"""
        ...

    @abstractmethod
    def _parameters_method_signature(self, operation: Operation) -> List[str]:
        """Returns the parameter's portion of the method signature"""
        ...

    @abstractmethod
    def _response_type_annotation_wrapper(self, operation: Operation) -> List[str]:
        """Wrapper for the response type mypy annotation. Used by _response_type_annotation"""
        ...

    @abstractmethod
    def _response_type_annotation(self, operation: Operation, modify_if_head_as_boolean: bool = True) -> str:
        """The mypy type annotation for the response"""
        ...

    @staticmethod
    @abstractmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str) -> str:
        """Template for how to combine the method signature + the response type annotation together. Called by
        method_signature_and_response_type_annotation"""
        ...

    @abstractmethod
    def method_signature_and_response_type_annotation(self, operation: Operation) -> str:
        """Combines the method signature + the response type annotation together"""
        ...

    @abstractmethod
    def description_and_summary(self, operation: Operation) -> List[str]:
        """Description + summary from the swagger. Will be formatted into the overall operation description"""
        ...

    @abstractmethod
    def _content_type_docstring(self, operation: Operation) -> str:
        """Docstring for content type kwarg"""

    @abstractmethod
    def _response_docstring_text_template(self, operation) -> str:
        """Formats the return docstring text"""
        ...

    @abstractmethod
    def _response_docstring_type_template(self, operation: Operation) -> str:
        """Template for how to format the response type annotation in the docstring"""
        ...

    @abstractmethod
    def _response_docstring_type_wrapper(self, operation: Operation) -> List[str]:
        """Wrapper for the response type mypy annotation. Used by _response_type_annotation"""
        ...

    @abstractmethod
    def cls_type_annotation(self, operation: Operation) -> str:
        """The type annotation for the cls param in method code"""
        ...


############################## NORMAL OPERATIONS ##############################

class OperationBaseSerializer(OperationSerializerProtocol):
    def __init__(self, code_model: CodeModel) -> None:
        self.code_model = code_model

    def _method_signature(self, operation: Operation) -> str:
        lines: List[str] = []
        lines.append(f"{self._function_definition} {operation.name}(")
        lines.append("    self,")
        lines.extend(self._parameters_method_signature(operation))
        lines.append(")")
        return "\n".join(lines)

    def _response_type_annotation(self, operation: Operation, modify_if_head_as_boolean: bool = True) -> str:
        if modify_if_head_as_boolean and operation.method == 'head' and self.code_model.options['head_as_boolean']:
            return "bool"
        response_body_annotations: OrderedSet[str] = {}
        for response in [r for r in operation.responses if r.has_body]:
            response_body_annotations[response.operation_type_annotation] = None
        response_str = ", ".join(response_body_annotations.keys()) or "None"
        if len(response_body_annotations) > 1:
            response_str = f"Union[{response_str}]"
        if operation.has_optional_return_type:
            response_str = f"Optional[{response_str}]"
        return response_str

    def cls_type_annotation(self, operation: Operation) -> str:
        return f"# type: ClsType[{self._response_type_annotation(operation, modify_if_head_as_boolean=False)}]"

    def method_signature_and_response_type_annotation(self, operation: Operation) -> str:
        method_signature = self._method_signature(operation)
        response_type_annotation = self._response_type_annotation(operation)
        for wrapper in self._response_type_annotation_wrapper(operation)[::-1]:
            response_type_annotation = f"{wrapper}[{response_type_annotation}]"
        return self._method_signature_and_response_type_annotation_template(method_signature, response_type_annotation)

    def _content_type_docstring(self, operation: Operation) -> str:
        try:
            content_type_constant = next(
                p for p in operation.parameters.constant
                if p.implementation == "Method" and
                not p.original_parameter and
                p.in_method_code and
                p.serialized_name == "content_type"
            )
        except StopIteration:
            raise ValueError("No content type parameter")
        media_types: OrderedSet[str] = {
            media_type: None
            for request in operation.requests
            for media_type in request.media_types
        }
        content_type_str = (
            f":keyword str content_type: Media type of the body sent to the API. Default value is {content_type_constant.constant_declaration}. " +
            "Allowed values are: {}.".format('", "'.join(media_types))
        )
        return content_type_str

    def description_and_summary(self, operation: Operation) -> List[str]:
        description_list: List[str] = []
        description_list.append(f'{ operation.summary.strip() if operation.summary else operation.description.strip() }')
        if operation.summary and operation.description:
            description_list.append("")
            description_list.append(operation.description.strip())
        description_list.append("")
        if operation.deprecated:
            description_list.append(".. warning::")
            description_list.append("    This method is deprecated")
            description_list.append("")
        return description_list

    def param_description(self, operation: Operation) -> List[str]:
        description_list: List[str] = []
        for parameter in operation.parameters.method:
            description_list.extend(f":param { parameter.serialized_name }: { parameter.description }".replace('\n', '\n ').split("\n"))
            description_list.append(f":type { parameter.serialized_name }: { parameter.docstring_type }")
        if len(operation.requests) > 1:
            description_list.append(self._content_type_docstring(operation))
        description_list.append(":keyword callable cls: A custom type or function that will be passed the direct response")
        return description_list

    def _response_docstring_text_template(self, operation) -> str:
        return "{}, or the result of cls(response)"

    def _response_type_annotation_wrapper(self, operation: Operation) -> List[str]:
        return []

    def _response_docstring_type_wrapper(self, operation: Operation) -> List[str]:
        return []

    def _response_docstring_type_template(self, operation: Operation) -> str:
        retval = "{}"
        for wrapper in self._response_docstring_type_wrapper(operation)[::-1]:
            retval = f"{wrapper}[{retval}]"
        return retval

    def response_docstring(self, operation: Operation) -> List[str]:
        responses_with_body = [r for r in operation.responses if r.has_body]
        if operation.method == 'head' and self.code_model.options['head_as_boolean']:
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
            if operation.has_optional_return_type:
                rtype += " or None"
        else:
            response_docstring_text = "None"
            rtype = "None"
        response_str = f":return: {self._response_docstring_text_template(operation).format(response_docstring_text)}"
        rtype_str = f":rtype: {self._response_docstring_type_template(operation).format(rtype)}"
        return [response_str, rtype_str, ":raises: ~azure.core.exceptions.HttpResponseError"]

    def param_description_and_response_docstring(self, operation: Operation) -> List[str]:
        return self.param_description(operation) + self.response_docstring(operation)

class SyncOperationSerializer(OperationBaseSerializer):

    @property
    def _function_definition(self) -> str:
        return "def"

    def _parameters_method_signature(self, operation: Operation) -> List[str]:
        params = [
            f"    {param.method_signature(async_mode=False)}"
            for param in operation.parameters.method
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

    def _parameters_method_signature(self, operation: Operation) -> List[str]:
        params = [
            f"    {param.method_signature(async_mode=True)}"
            for param in operation.parameters.method
        ]
        params.append("    **kwargs: Any")
        return params

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, _response_type_annotation: str):
        return f"{method_signature} -> {_response_type_annotation}:"

############################## PAGING OPERATIONS ##############################

class PagingOperationBaseSerializer(OperationBaseSerializer):

    def _response_docstring_text_template(self, operation) -> str:
        return "An iterator like instance of either {} or the result of cls(response)"

    def cls_type_annotation(self, operation: Operation) -> str:
        interior = super()._response_type_annotation(operation, modify_if_head_as_boolean=False)
        return f"# type: ClsType[{interior}]"


class SyncPagingOperationSerializer(PagingOperationBaseSerializer, SyncOperationSerializer):

    def _response_docstring_type_wrapper(self, operation: PagingOperation) -> List[str]:
        return [f"~{operation.get_pager_path(async_mode=False)}"]

    def _response_type_annotation_wrapper(self, operation: Operation) -> List[str]:
        return ["Iterable"]

class AsyncPagingOperationSerializer(PagingOperationBaseSerializer, AsyncOperationSerializer):

    def _response_docstring_type_wrapper(self, operation: PagingOperation) -> List[str]:
        return [f"~{operation.get_pager_path(async_mode=True)}"]

    @property
    def _function_definition(self) -> str:
        return "def"

    def _response_type_annotation_wrapper(self, operation: Operation) -> List[str]:
        return ["AsyncIterable"]


############################## LRO OPERATIONS ##############################

class LROOperationBaseSerializer(OperationBaseSerializer):

    def cls_type_annotation(self, operation: Operation) -> str:
        return f"# type: ClsType[{super()._response_type_annotation(operation, modify_if_head_as_boolean=False)}]"

    def _method_signature(self, operation: Operation) -> str:
        lines: List[str] = []
        lines.append(f"{self._function_definition} begin_{operation.name}(")
        lines.append("    self,")
        lines.extend(self._parameters_method_signature(operation))
        lines.append(")")
        return "\n".join(lines)


    @abstractmethod
    def _default_polling_method(self, operation: LROOperation) -> str:
        ...

    @property
    @abstractmethod
    def _polling_method_type(self):
        ...

    def param_description(self, operation: LROOperation) -> List[str]:
        retval = super().param_description(operation)
        retval.append(":keyword str continuation_token: A continuation token to restart a poller from a saved state.")
        retval.append(
            f":keyword polling: By default, your polling method will be {self._default_polling_method(operation)}. Pass in False for this "
            "operation to not poll, or pass in your own initialized polling object for a personal polling strategy."
        )
        retval.append(f":paramtype polling: bool or ~{self._polling_method_type}")
        retval.append(":keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.")
        return retval

class SyncLROOperationSerializer(LROOperationBaseSerializer, SyncOperationSerializer):

    def _response_docstring_text_template(self, operation) -> str:
        lro_section = f"An instance of {operation.get_poller(async_mode=False)} "
        return lro_section + "that returns either {} or the result of cls(response)"

    def _response_docstring_type_wrapper(self, operation: LROOperation) -> List[str]:
        return [f"~{operation.get_poller_path(async_mode=False)}"]

    def _response_type_annotation_wrapper(self, operation: LROOperation) -> List[str]:
        return [operation.get_poller(async_mode=False)]

    def _default_polling_method(self, operation: LROOperation) -> str:
        return operation.get_default_polling_method(
            async_mode=False, azure_arm=self.code_model.options["azure_arm"]
        )

    @property
    def _polling_method_type(self):
        return "azure.core.polling.PollingMethod"

class AsyncLROOperationSerializer(LROOperationBaseSerializer, AsyncOperationSerializer):

    def _response_docstring_text_template(self, operation) -> str:
        lro_section = f"An instance of {operation.get_poller(async_mode=True)} "
        return lro_section + "that returns either {} or the result of cls(response)"

    def _response_docstring_type_wrapper(self, operation: LROOperation) -> List[str]:
        return [f"~{operation.get_poller_path(async_mode=True)}"]

    def _response_type_annotation_wrapper(self, operation: LROOperation) -> List[str]:
        return [operation.get_poller(async_mode=True)]

    def _default_polling_method(self, operation: LROOperation) -> str:
        return operation.get_default_polling_method(
            async_mode=True, azure_arm=self.code_model.options["azure_arm"]
        )

    @property
    def _polling_method_type(self):
        return "azure.core.polling.AsyncPollingMethod"

############################## LRO PAGING OPERATIONS ##############################

class SyncLROPagingOperationSerializer(SyncLROOperationSerializer, SyncPagingOperationSerializer):

    def _response_docstring_type_wrapper(self, operation: LROPagingOperation) -> List[str]:
        return (
            SyncLROOperationSerializer._response_docstring_type_wrapper(self, operation) +
            SyncPagingOperationSerializer._response_docstring_type_wrapper(self, operation)
        )

    def _response_type_annotation_wrapper(self, operation: LROPagingOperation) -> List[str]:
        return (
            SyncLROOperationSerializer._response_type_annotation_wrapper(self, operation) +
            [operation.get_pager(async_mode=False)]
        )

    def _response_docstring_text_template(self, operation: LROPagingOperation) -> str:
        lro_doc = SyncLROOperationSerializer._response_docstring_text_template(self, operation)
        paging_doc = SyncPagingOperationSerializer._response_docstring_text_template(self, operation)
        paging_doc = paging_doc.replace(paging_doc[0], paging_doc[0].lower(), 1)
        return lro_doc.format(paging_doc).replace(" or the result of cls(response)", "", 1).replace("either ", "", 1)

    def cls_type_annotation(self, operation: LROPagingOperation) -> str:
        return f"# type: ClsType[{self._response_type_annotation(operation, modify_if_head_as_boolean=False)}]"

class AsyncLROPagingOperationSerializer(AsyncLROOperationSerializer, AsyncPagingOperationSerializer):

    def _response_docstring_type_wrapper(self, operation: LROPagingOperation) -> List[str]:
        return (
            AsyncLROOperationSerializer._response_docstring_type_wrapper(self, operation) +
            AsyncPagingOperationSerializer._response_docstring_type_wrapper(self, operation)
        )

    def _response_type_annotation_wrapper(self, operation: LROPagingOperation) -> List[str]:
        return (
            AsyncLROOperationSerializer._response_type_annotation_wrapper(self, operation) +
            [operation.get_pager(async_mode=True)]
        )

    @property
    def _function_definition(self) -> str:
        return "async def"

    def _response_docstring_text_template(self, operation: LROPagingOperation) -> str:
        lro_doc = AsyncLROOperationSerializer._response_docstring_text_template(self, operation)
        paging_doc = AsyncPagingOperationSerializer._response_docstring_text_template(self, operation)
        paging_doc = paging_doc.replace(paging_doc[0], paging_doc[0].lower(), 1)
        return lro_doc.format(paging_doc).replace(" or the result of cls(response)", "", 1).replace("either ", "", 1)

