# pylint: disable=too-many-lines
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from itertools import groupby
import json
from collections import defaultdict
from abc import abstractmethod, ABC
from typing import Any, List, TypeVar, Dict, Union, Optional, cast


from ..models import (
    Operation,
    CodeModel,
    PagingOperation,
    LROOperation,
    LROPagingOperation,
    ModelType,
    DictionaryType,
    ListType,
    BaseType,
    Parameter,
    RequestBuilder,
    ParameterLocation,
    EnumType,
    Response,
    BinaryType,
    SingleTypeBodyParameter,
    ParameterMethodLocation,
    RequestBuilderSingleTypeBodyParameter,
    OverloadedRequestBuilder,
)
from .parameter_serializer import ParameterSerializer, PopKwargType
from . import utils

T = TypeVar("T")
OrderedSet = Dict[T, None]

BuilderType = Union[Operation, RequestBuilder]

def _escape_str(input_str: str) -> str:
    replace = input_str.replace("'", "\\'")
    return f'"{replace}"'

def _improve_json_string(template_representation: str) -> Any:
    origin = template_representation.split("\n")
    final = []
    for line in origin:
        idx0 = line.find("#")
        idx1 = line.rfind('"')
        modified_line = ""
        if idx0 > -1 and idx1 > -1:
            modified_line = line[:idx0] + line[idx1:] + "  " + line[idx0:idx1] + "\n"
        else:
            modified_line = line + "\n"
        modified_line = modified_line.replace('"', "").replace("\\", '"')
        final.append(modified_line)
    return "".join(final)


def _json_dumps_template(template_representation: Any) -> Any:
    # only for template use, since it wraps everything in strings
    return _improve_json_string(
        json.dumps(template_representation, sort_keys=True, indent=4)
    )

class _BuilderSerializerProtocol(ABC):
    @property
    @abstractmethod
    def _need_self_param(self) -> bool:
        ...

    @property
    @abstractmethod
    def _function_definition(self) -> str:
        """The def keyword for the builder we're serializing, i.e. 'def' or 'async def'"""
        ...

    @property
    @abstractmethod
    def _is_python3_file(self) -> bool:
        """Whether it's going to be in a python3 file"""
        ...

    @abstractmethod
    def _response_type_annotation(
        self, builder
    ) -> str:
        """The mypy type annotation for the response"""
        ...


    @staticmethod
    @abstractmethod
    def _method_signature_and_response_type_annotation_template(
        method_signature: str, response_type_annotation: str
    ) -> str:
        """Template for how to combine the method signature + the response type annotation together. Called by
        method_signature_and_response_type_annotation"""
        ...

    @abstractmethod
    def decorators(self, builder, async_mode: bool) -> List[str]:
        """Decorators for the method"""
        ...

    @abstractmethod
    def method_signature_and_response_type_annotation(
        self, builder, async_mode: bool, *, want_decorators: Optional[bool] = True
    ) -> str:
        """Combines the method signature + the response type annotation together"""
        ...

    @abstractmethod
    def description_and_summary(self, builder: BuilderType) -> List[str]:
        """Description + summary from the swagger. Will be formatted into the overall operation description"""
        ...

    @abstractmethod
    def response_docstring(self, builder: BuilderType) -> List[str]:
        """Response portion of the docstring"""
        ...

    @abstractmethod
    def example_template(self, builder: BuilderType) -> List[str]:
        ...

    @abstractmethod
    def _json_example_param_name(self, builder: BuilderType) -> str:
        ...

    @abstractmethod
    def _json_response_template(self, builder: BuilderType) -> List[str]:
        ...

    @abstractmethod
    def _get_json_response_template_to_status_codes(
        self, builder
    ) -> Dict[str, List[str]]:
        ...

    @abstractmethod
    def _kwargs_to_pop(self, builder: BuilderType) -> List[Parameter]:
        ...


class _BuilderBaseSerializer(
    _BuilderSerializerProtocol
):  # pylint: disable=abstract-method
    def __init__(self, code_model: CodeModel, async_mode: bool, is_python3_file: bool) -> None:
        self.code_model = code_model
        self.async_mode = async_mode
        self.is_python3_file = is_python3_file
        self.parameter_serializer = ParameterSerializer(code_model)

    def decorators(self, builder: BuilderType) -> List[str]:
        """Decorators for the method"""
        retval: List[str] = []
        if builder.is_overload:
            return ["@overload"]
        if self.code_model.options["tracing"] and builder.want_tracing:
            retval.append(f"@distributed_trace{'_async' if self.async_mode else ''}")
        return retval

    def _method_signature(
        self, builder: Operation, response_type_annotation: str
    ) -> str:
        return self.parameter_serializer.serialize_method(
            function_def=self._function_definition,
            method_name=builder.name,
            need_self_param=self._need_self_param,
            method_param_signatures=builder.method_signature(
                self.async_mode or self.is_python3_file
            ),
            ignore_inconsistent_return_statements=(response_type_annotation == "None"),
        )

    def _response_type_annotation_wrapper(self, builder: BuilderType) -> List[str]:
        return []

    def method_signature_and_response_type_annotation(
        self, builder: BuilderType, *, want_decorators: Optional[bool] = True
    ) -> str:
        response_type_annotation = self._response_type_annotation(builder)
        # want pre-wrapped response type. As long as it's None, pylint will get mad about inconsistent return types
        method_signature = self._method_signature(builder, response_type_annotation)
        for wrapper in self._response_type_annotation_wrapper(builder)[::-1]:
            response_type_annotation = f"{wrapper}[{response_type_annotation}]"
        decorators = self.decorators(builder)
        decorators_str = ""
        if decorators and want_decorators:
            decorators_str = "\n".join(decorators) + "\n"
        return (
            decorators_str
            + self._method_signature_and_response_type_annotation_template(
                method_signature, response_type_annotation
            )
        )

    def description_and_summary(self, builder: BuilderType) -> List[str]:
        description_list: List[str] = []
        description_list.append(
            f"{ builder.summary.strip() if builder.summary else builder.description.strip() }"
        )
        if builder.summary and builder.description:
            description_list.append("")
            description_list.append(builder.description.strip())
        description_list.append("")
        return description_list

    def want_example_template(self, builder: RequestBuilder) -> bool:
        if builder.abstract:
            return False
        if self.code_model.options["builders_visibility"] != "public":
            return False  # if we're not exposing rest layer, don't need to generate
        if builder.parameters.has_body_parameter:
            if builder.overloads:
                return any([o for o in builder.overloads if o.parameters.body_parameter.client_name == "json"])
            if builder.parameters.body_parameter and builder.parameters.body_parameter.client_name == "json":
                return True
        return bool(self._get_json_response_template_to_status_codes(builder))

    def example_template(self, builder: BuilderType) -> List[str]:
        template = []
        if builder.abstract:
            return []
        if self._json_input_example_template(builder):
            template.append("")
            template += self._json_input_example_template(builder)
        if self._json_response_template(builder):
            template.append("")
            template += self._json_response_template(builder)
        return template

    def param_description(  # pylint: disable=no-self-use
        self, builder: Union[RequestBuilder, Operation]
    ) -> List[str]:
        description_list: List[str] = []
        for param in [m for m in builder.parameters.method if not m.method_location == ParameterMethodLocation.KWARG]:
            description_list.extend(
                f":{param.description_keyword} { param.client_name }: { param.description }".replace(
                    "\n", "\n "
                ).split(
                    "\n"
                )
            )
            description_list.append(
                f":{param.docstring_type_keyword} { param.client_name }: { param.docstring_type }"
            )

        # if len(builder.parameters.content_types) > 1:
        #     description_list = [
        #         _content_type_docstring(builder: BuilderType)
        #         if l.startswith(":keyword content_type:")
        #         else l
        #         for l in description_list
        #     ]
        #     if not any(
        #         l for l in description_list if l.startswith(":keyword content_type:")
        #     ):
        #         description_list.append(_content_type_docstring(builder: BuilderType))
        return description_list

    def param_description_and_response_docstring(self, builder: BuilderType) -> List[str]:
        if builder.abstract:
            return []
        return self.param_description(builder) + self.response_docstring(builder)

    def _get_json_response_template_to_status_codes(
        self, builder: BuilderType
    ) -> Dict[str, List[str]]:
        # successful status codes of responses that have bodies
        responses = [
            response
            for response in builder.responses
            if any(
                code in builder.success_status_codes for code in response.status_codes
            )
            and isinstance(
                response.type,
                (DictionaryType, ListType, ModelType, EnumType),
            )
        ]
        retval = defaultdict(list)
        for response in responses:
            status_codes = [str(status_code) for status_code in response.status_codes]
            response_json = _json_dumps_template(
                cast(BaseType, response.type).get_json_template_representation()
            )
            retval[response_json].extend(status_codes)
        return retval

    def _json_input_example_template(self, builder: BuilderType) -> List[str]:
        template = []
        if not builder.parameters.has_body_parameter:
            # No input template if now body parameter
            return template
        if builder.overloads:
            # if there's overloads, we do the json input example template on the overload
            return template

        body_param = builder.parameters.body_parameter
        if not isinstance(body_param.type, (ListType, DictionaryType, ModelType)):
            return template

        if isinstance(body_param.type, ModelType) and body_param.type.discriminator:
            discriminator_name = body_param.type.discriminator.client_name
            discriminator_values = body_param.type.discriminated_subtypes.keys()
            template.append(
                "{} = '{}'".format(
                    discriminator_name, "' or '".join(discriminator_values)
                )
            )
            template.append("")
        template.append(
            "# JSON input template you can fill out and use as your body input."
        )
        json_template = _json_dumps_template(
            body_param.type.get_json_template_representation(),
        )
        template.extend(
            f"{self._json_example_param_name(builder)} = {json_template}".splitlines()
        )
        return template

    @property
    @abstractmethod
    def serializer_name(self) -> str:
        ...

    def _serialize_parameter(self, param: Parameter, kwarg_name: str) -> List[str]:
        set_parameter = "_{}['{}'] = {}".format(
            kwarg_name,
            param.rest_api_name,
            self.parameter_serializer.serialize_parameter(param, self.serializer_name),
        )
        if not param.optional:
            retval = [set_parameter]
        else:
            retval = [
                f"if {param.full_client_name} is not None:",
                f"    {set_parameter}",
            ]
        return retval

    def _json_response_template(self, builder: BuilderType) -> List[str]:
        template = []
        for (
            response_body,
            status_codes,
        ) in self._get_json_response_template_to_status_codes(builder).items():
            template.append(
                "# response body for status code(s): {}".format(", ".join(status_codes))
            )
            template.extend(f"response.json() == {response_body}".splitlines())
        return template

    def serialize_path(self, builder: BuilderType) -> List[str]:
        return self.parameter_serializer.serialize_path(builder.parameters.path, self.serializer_name)


############################## REQUEST BUILDERS ##############################


class _RequestBuilderBaseSerializer(
    _BuilderBaseSerializer
):  # pylint: disable=abstract-method
    def description_and_summary(self, builder: BuilderType) -> List[str]:
        retval = super().description_and_summary(builder)
        retval += [
            "See https://aka.ms/azsdk/python/protocol/quickstart for how to incorporate this "
            "request builder into your code flow.",
            "",
        ]
        return retval

    @property
    def serializer_name(self) -> str:
        return "_SERIALIZER"

    @staticmethod
    def declare_non_inputtable_constants(builder: BuilderType) -> List[str]:
        def _get_value(param: Parameter):
            if param.location in [ParameterLocation.HEADER, ParameterLocation.QUERY]:
                kwarg_dict = (
                    "headers"
                    if param.location == ParameterLocation.HEADER
                    else "params"
                )
                return f"_{kwarg_dict}.pop('{param.rest_api_name}', {param.type.get_declaration()})"
            return f"{param.type.get_declaration()}"

        return [
            f"{p.client_name} = {_get_value(p)}"
            for p in builder.parameters.constant
            if not p.in_method_signature
        ]

    @property
    def _function_def(self) -> str:
        return "def"

    @property
    def _need_self_param(self) -> bool:
        return False

    def _response_type_annotation(
        self, builder: RequestBuilder
    ) -> str:
        return builder.response_type_annotation()

    def response_docstring(self, builder: BuilderType) -> List[str]:
        response_str = (
            f":return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's "
            + "`send_request` method. See https://aka.ms/azsdk/python/protocol/quickstart for how to "
            + "incorporate this response into your code flow."
        )
        rtype_str = f":rtype: ~azure.core.rest.HttpRequest"
        return [response_str, rtype_str]

    def _json_example_param_name(self, builder: BuilderType) -> str:
        return "json"

    def pop_kwargs_from_signature(self, builder: BuilderType) -> List[str]:
        return self.parameter_serializer.pop_kwargs_from_signature(
            self._kwargs_to_pop(builder),
            check_kwarg_dict=True,
            pop_headers_kwarg=PopKwargType.CASE_INSENSITIVE
            if bool(builder.parameters.headers)
            else PopKwargType.NO,
            pop_params_kwarg=PopKwargType.CASE_INSENSITIVE
            if bool(builder.parameters.query)
            else PopKwargType.NO,
        )

    def create_http_request(self, builder: RequestBuilder) -> List[str]:
        retval = ["return HttpRequest("]
        retval.append(f'    method="{builder.method}",')
        retval.append("    url=_url,")
        if builder.parameters.query:
            retval.append("    params=_params,")
        if builder.parameters.headers:
            retval.append("    headers=_headers,")
        if builder.parameters.has_body_parameter and not builder.parameters.body_parameter:
            retval.append(f"    {builder.parameters.body_parameter.client_name}={builder.parameters.body_parameter.client_name},")
        retval.append("    **kwargs")
        retval.append(")")
        return retval

    def serialize_headers(self, builder: BuilderType) -> List[str]:
        retval = ["# Construct headers"]
        for parameter in builder.parameters.headers:
            retval.extend(
                self._serialize_parameter(
                    parameter,
                    kwarg_name="headers",
                )
            )
        return retval

    def serialize_query(self, builder: BuilderType) -> List[str]:
        retval = ["# Construct parameters"]
        for parameter in builder.parameters.query:
            retval.extend(
                self._serialize_parameter(
                    parameter,
                    kwarg_name="params",
                )
            )
        return retval

    def construct_url(self, builder: RequestBuilder) -> str:
        if any(
            o
            for o in ["low_level_client", "version_tolerant"]
            if self.code_model.options.get(o)
        ):
            url_value = _escape_str(builder.url)
        else:
            url_value = f'kwargs.pop("template_url", {_escape_str(builder.url)})'
        return f"_url = {url_value}{'  # pylint: disable=line-too-long' if len(url_value) > 114 else ''}"


class RequestBuilderGenericSerializer(_RequestBuilderBaseSerializer):
    @property
    def _is_python3_file(self) -> bool:
        return False

    @staticmethod
    def _method_signature_and_response_type_annotation_template(
        method_signature: str, response_type_annotation: str
    ):
        return utils.method_signature_and_response_type_annotation_template(
            is_python3_file=False,
            method_signature=method_signature,
            response_type_annotation=response_type_annotation,
        )

    def _kwargs_to_pop(self, builder: BuilderType):
        return builder.parameters.kwargs_to_pop(is_python3_file=False)

    def _body_params_to_pass_to_request_creation(self, builder: BuilderType) -> List[str]:
        if any(
            b
            for b in builder.parameters.body
            if b.constant  # and not (b.is_data_input or b.is_multipart)
        ):
            # this means we have a constant body
            # only doing json body in this case
            return ["json"]
        return []


class RequestBuilderPython3Serializer(_RequestBuilderBaseSerializer):
    @property
    def _is_python3_file(self) -> bool:
        return True

    @staticmethod
    def _method_signature_and_response_type_annotation_template(
        method_signature: str, response_type_annotation: str
    ):
        return utils.method_signature_and_response_type_annotation_template(
            is_python3_file=True,
            method_signature=method_signature,
            response_type_annotation=response_type_annotation,
        )

    def _kwargs_to_pop(self, builder: BuilderType):
        return builder.parameters.kwargs_to_pop(is_python3_file=True)


############################## NORMAL OPERATIONS ##############################


class _OperationBaseSerializer(
    _BuilderBaseSerializer
):  # pylint: disable=abstract-method
    def description_and_summary(self, builder: BuilderType) -> List[str]:
        retval = super().description_and_summary(builder)
        if builder.deprecated:
            retval.append(".. warning::")
            retval.append("    This method is deprecated")
            retval.append("")
        return retval

    @property
    def _need_self_param(self) -> bool:
        return True

    @property
    def serializer_name(self) -> str:
        return "self._serialize"

    def decorators(self, builder, async_mode: bool) -> List[str]:
        """Decorators for the method"""
        super_decorators = super().decorators(builder, async_mode)
        if builder.abstract:
            super_decorators.append("@abc.abstractmethod")
        return super_decorators

    def _response_docstring_type_wrapper(  # pylint: disable=unused-argument, no-self-use
        self, builder
    ) -> List[str]:
        return []

    def param_description(self, builder: BuilderType) -> List[str]:  # pylint: disable=no-self-use
        description_list = super().param_description(builder)
        if not self.code_model.options["version_tolerant"]:
            description_list.append(
                ":keyword callable cls: A custom type or function that will be passed the direct response"
            )
        return description_list

    def _response_docstring_type_template(self, builder: BuilderType) -> str:
        retval = "{}"
        for wrapper in self._response_docstring_type_wrapper(builder)[::-1]:
            retval = f"{wrapper}[{retval}]"
        return retval

    def pop_kwargs_from_signature(self, builder: Operation) -> List[str]:
        kwargs_to_pop = self._kwargs_to_pop(builder)
        kwargs = self.parameter_serializer.pop_kwargs_from_signature(
            kwargs_to_pop,
            check_kwarg_dict=True,
            pop_headers_kwarg=PopKwargType.CASE_INSENSITIVE
            if builder.has_kwargs_to_pop_with_default(
                kwargs_to_pop, ParameterLocation.HEADER
            )
            else PopKwargType.SIMPLE,
            pop_params_kwarg=PopKwargType.CASE_INSENSITIVE
            if builder.has_kwargs_to_pop_with_default(
                kwargs_to_pop, ParameterLocation.QUERY
            )
            else PopKwargType.SIMPLE,
        )
        kwargs.append(
            f"cls = kwargs.pop('cls', None)  {self.cls_type_annotation(builder)}"
        )
        return kwargs

    def cls_type_annotation(self, builder: BuilderType) -> str:
        return f"# type: ClsType[{self._response_type_annotation(builder, modify_if_head_as_boolean=False)}]"

    def response_docstring(self, builder: Operation) -> List[str]:
        responses_with_body = [r for r in builder.responses if r.type]
        if (
            builder.request_builder.method.lower() == "head"
            and self.code_model.options["head_as_boolean"]
        ):
            response_docstring_text = "bool"
            rtype = "bool"
        elif responses_with_body:
            response_body_docstring_text: OrderedSet[str] = {
                response.docstring_text: None for response in responses_with_body
            }
            response_docstring_text = " or ".join(response_body_docstring_text.keys())
            response_body_docstring_type: OrderedSet[str] = {
                response.docstring_type: None for response in responses_with_body
            }
            rtype = " or ".join(response_body_docstring_type.keys())
            if builder.has_optional_return_type:
                rtype += " or None"
        else:
            response_docstring_text = "None"
            rtype = "None"
        response_str = f":return: {self._response_docstring_text(builder).format(response_docstring_text)}"
        rtype_str = (
            f":rtype: {self._response_docstring_type_template(builder).format(rtype)}"
        )
        return [
            response_str,
            rtype_str,
            ":raises: ~azure.core.exceptions.HttpResponseError",
        ]

    def _json_example_param_name(self, builder: Operation) -> str:
        return builder.parameters.body_parameter.client_name

    def _serialize_body_call(
        self,
        builder,
        body_param: Parameter,
        send_xml: bool,
        ser_ctxt: Optional[str],
        ser_ctxt_name: str,
    ) -> str:
        body_is_xml = ", is_xml=True" if send_xml else ""
        pass_ser_ctxt = f", {ser_ctxt_name}={ser_ctxt_name}" if ser_ctxt else ""
        body_kwarg_to_pass = builder.body_kwargs_to_pass_to_request_builder[0]
        if self.code_model.options["models_mode"]:
            return (
                f"_{body_kwarg_to_pass} = self._serialize.body({body_param.serialized_name}, "
                f"'{ body_param.serialization_type }'{body_is_xml}{ pass_ser_ctxt })"
            )
        return f"_{body_kwarg_to_pass} = {body_param.serialized_name}"

    def _serialize_body(
        self, builder, body_param: Parameter, body_kwarg: str
    ) -> List[str]:
        retval = []
        serialize_body_call = self._serialize_body_call(
            builder,
            body_param,
            send_xml,
            ser_ctxt,
            ser_ctxt_name,
        )
        if body_param.required:
            retval.append(serialize_body_call)
        else:
            retval.append(f"if {body_param.serialized_name} is not None:")
            retval.append("    " + serialize_body_call)
            if len(builder.body_kwargs_to_pass_to_request_builder) == 1:
                retval.append("else:")
                retval.append(f"    _{body_kwarg} = None")
        return retval

    def _create_body_parameter(
        self,
        builder: Operation,
    ) -> List[str]:
        retval = []
        body_param = cast(SingleTypeBodyParameter, builder.parameters.body_parameter)
        if isinstance(body_param.type, BinaryType):
            retval.append(f"_content = {body_param.client_name}")
        else:
            if self.code_model.options["models_mode"]:
                retval.append(f"_json = self._serialize.body({body_param.client_name}, '{body_param.type.serialization_type}')")
            else:
                retval.append(f"_json = {body_param.client_name}")
        return retval

    def _call_request_builder_helper(  # pylint: disable=too-many-statements
        self,
        builder: Operation,
        request_builder: Union[RequestBuilder, OverloadedRequestBuilder],
        template_url: Optional[str] = None,
        is_next_request: bool = False,
    ) -> List[str]:
        retval = []
        if builder.overloads:
            # we are only dealing with two overloads. If there are three, we generate an abstract operation
            for overload in builder.overloads:
                retval.append(f"_{overload.request_builder.parameters.body_parameter.client_name} = None")
            try:
                # if there is a binary overload, we do a binary check first.
                binary_overload = next((o for o in builder.overloads if isinstance(o.parameters.body_parameter.type, BinaryType)))
                binary_body_param = binary_overload.parameters.body_parameter
                retval.append(f"if {binary_body_param.type.instance_check_template.format(binary_body_param.client_name)}:")
                if binary_body_param.default_content_type:
                    retval.append(f'    content_type = content_type or "{binary_body_param.default_content_type}"')
                retval.extend(f"    {l}" for l in self._create_body_parameter(binary_overload))
                retval.append("else:")
                other_overload = next((o for o in builder.overloads if not isinstance(o.parameters.body_parameter.type, BinaryType)))
                retval.extend(f"    {l}" for l in self._create_body_parameter(other_overload))
                if other_overload.parameters.body_parameter.default_content_type:
                    retval.append(f'    content_type = content_type or "{other_overload.parameters.body_parameter.default_content_type}"')
            except StopIteration:
                for idx, overload in enumerate(builder.overloads):
                    if_statement = "if" if idx == 0 else "elif"
                    body_param = overload.parameters.body_parameter
                    retval.append(f'{if_statement} {body_param.type.instance_check_template.format(body_param.client_name)}:')
                    if body_param.default_content_type:
                        retval.append(f'    content_type = content_type or "{body_param.default_content_type}"')
                    retval.extend(f"    {l}" for l in self._create_body_parameter(overload))
        elif builder.parameters.has_body_parameter:
            # non-overloaded body
            retval.extend(self._create_body_parameter(builder))

        if self.code_model.options["builders_visibility"] == "embedded":
            request_path_name = request_builder.name
        else:
            group_name = request_builder.group_name
            request_path_name = "rest{}.{}".format(
                ("_" + group_name) if group_name else "",
                request_builder.name,
            )
        retval.append("")
        retval.append(f"request = {request_path_name}(")
        for parameter in request_builder.parameters.method:
            if parameter.location == ParameterLocation.BODY:
                # going to pass in body later based off of overloads
                continue
            retval.append(f"    {parameter.client_name}={parameter.name_in_high_level_operation},")
        if request_builder.overloads:
            for overload in request_builder.overloads:
                body_param = cast(RequestBuilderSingleTypeBodyParameter, overload.parameters.body_parameter)
                retval.append(f"    {body_param.client_name}={body_param.name_in_high_level_operation},")
        elif request_builder.parameters.has_body_parameter:
            body_param = cast(RequestBuilderSingleTypeBodyParameter, request_builder.parameters.body_parameter)
            retval.append(f"    {body_param.client_name}={body_param.name_in_high_level_operation},")
        if not self.code_model.options["version_tolerant"]:
            template_url = template_url or f"self.{builder.name}.metadata['url']"
            retval.append(f"    template_url={template_url},")
        retval.append("    headers=_headers,")
        retval.append("    params=_params,")
        retval.append(f")")
        if not self.code_model.options["version_tolerant"]:
            pass_files = ""
            # if builder.parameters.multipart:
            #     pass_files = ", _files"
            retval.append(f"request = _convert_request(request{pass_files})")
        if builder.parameters.path:
            retval.extend(self.serialize_path(builder))
        url_to_format = "request.url"
        if self.code_model.options["version_tolerant"] and template_url:
            url_to_format = template_url
        retval.append(
            "request.url = self._client.format_url({}{})  # type: ignore".format(
                url_to_format,
                ", **path_format_arguments" if builder.parameters.path else "",
            )
        )
        return retval

    def call_request_builder(self, builder: BuilderType) -> List[str]:
        return self._call_request_builder_helper(builder, builder.request_builder)

    def response_headers_and_deserialization(
        self,
        response: Response,
    ) -> List[str]:
        retval: List[str] = [
            (
                f"response_headers['{response_header.name}']=self._deserialize('{response_header.serialization_type}', "
                f"response.headers.get('{response_header.name}'))"
            )
            for response_header in response.headers
        ]
        if response.headers:
            retval.append("")
        if response.is_stream_response:
            retval.append(
                "deserialized = {}".format(
                    "response"
                    if self.code_model.options["version_tolerant"]
                    else "response.stream_download(self._client._pipeline)"
                )
            )
        elif response.type:
            if self.code_model.options["models_mode"]:
                retval.append(
                    f"deserialized = self._deserialize('{response.serialization_type}', pipeline_response)"
                )
            else:
                is_xml = False # any(["xml" in ct for ct in response.content_types])
                deserialized_value = (
                    "ET.fromstring(response.text())" if is_xml else "response.json()"
                )
                retval.append(f"if response.content:")
                retval.append(f"    deserialized = {deserialized_value}")
                retval.append("else:")
                retval.append(f"    deserialized = None")
        return retval

    @property
    @abstractmethod
    def _call_method(self) -> str:
        ...

    def handle_error_response(self, builder: Operation) -> List[str]:
        retval = [f"if response.status_code not in {str(builder.success_status_codes)}:"]
        retval.append(
            "    map_error(status_code=response.status_code, response=response, error_map=error_map)"
        )
        error_model = ""
        if builder.default_error_deserialization and self.code_model.options["models_mode"]:
            retval.append(
                f"    error = self._deserialize.failsafe_deserialize({builder.default_error_deserialization}, pipeline_response)"
            )
            error_model = ", model=error"
        retval.append(
            "    raise HttpResponseError(response=response{}{})".format(
                error_model,
                ", error_format=ARMErrorFormat"
                if self.code_model.options["azure_arm"]
                else "",
            )
        )
        return retval

    def handle_response(self, builder: Operation) -> List[str]:
        retval: List[str] = ["response = pipeline_response.http_response"]
        retval.append("")
        retval.extend(self.handle_error_response(builder))
        retval.append("")
        if builder.has_optional_return_type:
            retval.append("deserialized = None")
        if builder.any_response_has_headers:
            retval.append("response_headers = {}")
        if builder.has_response_body or builder.any_response_has_headers:
            if len(builder.responses) > 1:
                for status_code in builder.success_status_codes:
                    response = builder.get_response_from_status(status_code)
                    if response.headers or response.type:
                        retval.append(f"if response.status_code == {status_code}:")
                        retval.extend(
                            [
                                f"    {line}"
                                for line in self.response_headers_and_deserialization(
                                    response
                                )
                            ]
                        )
                        retval.append("")
            else:
                retval.extend(
                    self.response_headers_and_deserialization(builder.responses[0])
                )
                retval.append("")
        if builder.has_optional_return_type or self.code_model.options["models_mode"]:
            deserialized = "deserialized"
        else:
            deserialized = (
                f"cast({self._response_type_annotation(builder)}, deserialized)"
            )
        retval.append("if cls:")
        retval.append(
            "    return cls(pipeline_response, {}, {})".format(
                deserialized if builder.has_response_body else "None",
                "response_headers" if builder.any_response_has_headers else "{}",
            )
        )
        if builder.has_response_body:
            retval.append("")
            retval.append(f"return {deserialized}")
        if (
            builder.request_builder.method == "HEAD"
            and self.code_model.options["head_as_boolean"]
        ):
            retval.append("return 200 <= response.status_code <= 299")
        return retval

    def error_map(self, builder: Operation) -> List[str]:
        retval = ["error_map = {"]
        if builder.non_default_errors:
            if not 401 in builder.non_default_error_status_codes:
                retval.append("    401: ClientAuthenticationError,")
            if not 404 in builder.non_default_error_status_codes:
                retval.append("    404: ResourceNotFoundError,")
            if not 409 in builder.non_default_error_status_codes:
                retval.append("    409: ResourceExistsError,")
            for excep in builder.non_default_errors:
                error_model_str = ""
                if (
                    isinstance(excep.type, ModelType)
                    and excep.is_error
                    and self.code_model.options["models_mode"]
                ):
                    error_model_str = f", model=self._deserialize(_models.{excep.type.serialization_type}, response)"
                error_format_str = (
                    ", error_format=ARMErrorFormat"
                    if self.code_model.options["azure_arm"]
                    else ""
                )
                for status_code in excep.status_codes:
                    if status_code == 401:
                        retval.append(
                            "    401: lambda response: ClientAuthenticationError(response=response"
                            f"{error_model_str}{error_format_str}),"
                        )
                    elif status_code == 404:
                        retval.append(
                            "    404: lambda response: ResourceNotFoundError(response=response"
                            f"{error_model_str}{error_format_str}),"
                        )
                    elif status_code == 409:
                        retval.append(
                            "    409: lambda response: ResourceExistsError(response=response"
                            f"{error_model_str}{error_format_str}),"
                        )
                    elif not error_model_str and not error_format_str:
                        retval.append(f"    {status_code}: HttpResponseError,")
                    else:
                        retval.append(
                            f"    {status_code}: lambda response: HttpResponseError(response=response"
                            f"{error_model_str}{error_format_str}),"
                        )
        else:
            retval.append(
                "    401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError"
            )
        retval.append("}")
        retval.append("error_map.update(kwargs.pop('error_map', {}) or {})")
        return retval

    @staticmethod
    def get_metadata_url(builder: BuilderType) -> str:
        url = _escape_str(builder.request_builder.url)
        return f"{builder.python_name}.metadata = {{'url': { url }}}  # type: ignore"


class _SyncOperationBaseSerializer(
    _OperationBaseSerializer
):  # pylint: disable=abstract-method
    @property
    def _want_inline_type_hints(self) -> bool:
        return False

    @property
    def _function_def(self) -> str:
        return "def"

    @property
    def _call_method(self) -> str:
        return ""

    def _response_type_annotation(self, builder: Operation) -> str:
        return builder.response_type_annotation(async_mode=False)


class SyncOperationGenericSerializer(_SyncOperationBaseSerializer):
    @property
    def _is_python3_only(self) -> bool:
        return False

    @staticmethod
    def _method_signature_and_response_type_annotation_template(
        method_signature: str, response_type_annotation: str
    ):
        return utils.method_signature_and_response_type_annotation_template(
            is_python3_file=False,
            method_signature=method_signature,
            response_type_annotation=response_type_annotation,
        )

    def _kwargs_to_pop(self, builder: BuilderType):
        return builder.parameters.kwargs_to_pop(is_python3_file=False)


class SyncOperationPython3Serializer(_SyncOperationBaseSerializer):
    @property
    def _is_python3_only(self) -> bool:
        return True

    @staticmethod
    def _method_signature_and_response_type_annotation_template(
        method_signature: str, response_type_annotation: str
    ):
        return utils.method_signature_and_response_type_annotation_template(
            is_python3_file=True,
            method_signature=method_signature,
            response_type_annotation=response_type_annotation,
        )

    def _kwargs_to_pop(self, builder: BuilderType):
        return builder.parameters.kwargs_to_pop(is_python3_file=True)


class AsyncOperationSerializer(SyncOperationPython3Serializer):
    @property
    def _is_python3_only(self) -> bool:
        return True

    @property
    def _function_definition(self) -> str:
        return "async def"

    @property
    def _call_method(self) -> str:
        return "await "

    def _response_type_annotation(self, builder: Operation) -> str:
        return builder.response_type_annotation(async_mode=True)


############################## PAGING OPERATIONS ##############################


class _PagingOperationBaseSerializer(
    _OperationBaseSerializer
):  # pylint: disable=abstract-method

    def decorators(self, builder: PagingOperation, async_mode: bool) -> List[str]:
        """Decorators for the method"""
        retval: List[str] = []
        if self.code_model.options["tracing"] and builder.want_tracing:
            retval.append("@distributed_trace")
        if builder.abstract:
            retval.append("@abc.abstractmethod")
        return retval

    def call_next_link_request_builder(self, builder: PagingOperation) -> List[str]:
        if builder.next_request_builder:
            request_builder = builder.next_request_builder
            template_url = (
                None
                if self.code_model.options["version_tolerant"]
                else f"'{request_builder.url}'"
            )
        else:
            request_builder = builder.request_builder
            template_url = "next_link"

        request_builder = builder.next_request_builder or builder.request_builder
        return self._call_request_builder_helper(
            builder, request_builder, template_url=template_url, is_next_request=True
        )

    def _prepare_request_callback(self, builder: PagingOperation) -> List[str]:
        retval = ["def prepare_request(next_link=None):"]
        retval.append("    if not next_link:")
        retval.extend(
            [f"        {line}" for line in self.call_request_builder(builder)]
        )
        retval.append("")
        retval.append("    else:")
        retval.extend(
            [f"        {line}" for line in self.call_next_link_request_builder(builder)]
        )
        if not builder.next_request_builder and builder.parameters.path:
            retval.append("")
            retval.extend([f"        {line}" for line in self.serialize_path(builder)])
        if not builder.next_request_builder:
            retval.append('        request.method = "GET"')
        else:
            retval.append("")
        retval.append("    return request")
        return retval

    @property
    @abstractmethod
    def _list_type_returned_to_users(self) -> str:
        ...

    @staticmethod
    @abstractmethod
    def _pager(builder: PagingOperation) -> str:
        ...

    def _extract_data_callback(self, builder: PagingOperation) -> List[str]:
        retval = [f"{self._function_definition} extract_data(pipeline_response):"]
        response = builder.responses[0]
        deserialized = (
            f'self._deserialize("{response.serialization_type}", pipeline_response)'
            if self.code_model.options["models_mode"]
            else "pipeline_response.http_response.json()"
        )
        retval.append(f"    deserialized = {deserialized}")
        item_name = builder.item_name
        list_of_elem = (
            f".{item_name}"
            if self.code_model.options["models_mode"]
            else f'["{item_name}"]'
        )
        retval.append(f"    list_of_elem = deserialized{list_of_elem}")
        retval.append("    if cls:")
        retval.append("        list_of_elem = cls(list_of_elem)")

        continuation_token_name = builder.continuation_token_name
        if not continuation_token_name:
            next_link_property = "None"
        elif self.code_model.options["models_mode"]:
            next_link_property = f"deserialized.{continuation_token_name} or None"
        else:
            next_link_property = f'deserialized.get("{continuation_token_name}", None)'
        retval.append(
            f"    return {next_link_property}, {self._list_type_returned_to_users}(list_of_elem)"
        )
        return retval

    def _get_next_callback(self, builder: PagingOperation) -> List[str]:
        retval = [f"{self._function_definition} get_next(next_link=None):"]
        retval.append("    request = prepare_request(next_link)")
        retval.append("")
        retval.append(
            f"    pipeline_response = {self._call_method}self._client._pipeline.run(  # pylint: disable=protected-access"
        )
        retval.append("        request,")
        retval.append("        **kwargs")
        retval.append("    )")
        retval.append("    response = pipeline_response.http_response")
        retval.append("")
        retval.extend([f"    {line}" for line in self.handle_error_response(builder)])
        retval.append("")
        retval.append("    return pipeline_response")
        return retval

    def set_up_params_for_pager(self, builder: PagingOperation) -> List[str]:
        retval = []
        retval.extend(self.error_map(builder))
        retval.extend(self._prepare_request_callback(builder))
        retval.append("")
        retval.extend(self._extract_data_callback(builder))
        retval.append("")
        retval.extend(self._get_next_callback(builder))
        return retval


class _SyncPagingOperationBaseSerializer(
    _PagingOperationBaseSerializer, _SyncOperationBaseSerializer
):  # pylint: disable=abstract-method

    @property
    def _list_type_returned_to_users(self) -> str:  # pylint: disable=no-self-use
        return "iter"

    @staticmethod
    def _pager(builder: PagingOperation) -> str:
        return builder.get_pager(async_mode=False)

    def _response_type_annotation(self, builder: Operation) -> str:
        return builder.response_type_annotation(async_mode=False)


class SyncPagingOperationGenericSerializer(
    _SyncPagingOperationBaseSerializer, SyncOperationGenericSerializer
):
    pass


class SyncPagingOperationPython3Serializer(
    _SyncPagingOperationBaseSerializer, SyncOperationPython3Serializer
):
    pass


class AsyncPagingOperationSerializer(
    _PagingOperationBaseSerializer, AsyncOperationSerializer
):

    @property
    def _function_definition(self) -> str:
        return "def"

    @property
    def _list_type_returned_to_users(self) -> str:  # pylint: disable=no-self-use
        return "AsyncList"

    @staticmethod
    def _pager(builder: PagingOperation) -> str:
        return builder.get_pager(async_mode=True)

    def _response_type_annotation(self, builder: Operation) -> str:
        return builder.response_type_annotation(async_mode=True)


############################## LRO OPERATIONS ##############################


class _LROOperationBaseSerializer(
    _OperationBaseSerializer
):  # pylint: disable=abstract-method
    def cls_type_annotation(self, builder: BuilderType) -> str:
        return f"# type: ClsType[{super()._response_type_annotation(builder, modify_if_head_as_boolean=False)}]"

    @abstractmethod
    def _default_polling_method(self, builder: BuilderType) -> str:
        ...

    @abstractmethod
    def _default_no_polling_method(self, builder: BuilderType) -> str:
        ...

    @abstractmethod
    def _poller(self, builder: BuilderType) -> str:
        ...

    @property
    @abstractmethod
    def _polling_method_type(self):
        ...

    def param_description(self, builder: BuilderType) -> List[str]:
        retval = super().param_description(builder)
        retval.append(
            ":keyword str continuation_token: A continuation token to restart a poller from a saved state."
        )
        retval.append(
            f":keyword polling: By default, your polling method will be {self._default_polling_method(builder)}. "
            "Pass in False for this operation to not poll, or pass in your own initialized polling object for a"
            " personal polling strategy."
        )
        retval.append(
            f":paramtype polling: bool or ~azure.core.polling.{self._polling_method_type}"
        )
        retval.append(
            ":keyword int polling_interval: Default waiting time between two polls for LRO operations "
            "if no Retry-After header is present."
        )
        return retval

    def initial_call(self, builder: BuilderType) -> List[str]:
        retval = [
            f"polling = kwargs.pop('polling', True)  # type: Union[bool, {self._polling_method_type}]"
        ]
        retval.append("lro_delay = kwargs.pop(")
        retval.append("    'polling_interval',")
        retval.append("    self._config.polling_interval")
        retval.append(")")
        retval.append(
            "cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]"
        )
        retval.append("if cont_token is None:")
        retval.append(
            f"    raw_result = {self._call_method}self.{builder.initial_operation.name}(  # type: ignore"
        )
        retval.extend(
            [
                f"        {parameter.serialized_name}={parameter.serialized_name},"
                for parameter in builder.parameters.method
            ]
        )
        retval.append("        cls=lambda x,y,z: x,")
        retval.append("        headers=_headers,")
        retval.append("        params=_params,")
        retval.append("        **kwargs")
        retval.append("    )")
        retval.append("kwargs.pop('error_map', None)")
        return retval

    def return_lro_poller(self, builder: BuilderType) -> List[str]:
        retval = []
        lro_options_str = (
            "lro_options={'final-state-via': '"
            + builder.lro_options["final-state-via"]
            + "'},"
            if builder.lro_options
            else ""
        )
        path_format_arguments_str = ""
        if builder.parameters.path:
            path_format_arguments_str = "path_format_arguments=path_format_arguments,"
            retval.extend(self.serialize_path(builder))
            retval.append("")
        retval.extend(
            [
                "if polling is True:",
                f"    polling_method = cast({self._polling_method_type}, {self._default_polling_method(builder)}(",
                "        lro_delay,",
                f"        {lro_options_str}",
                f"        {path_format_arguments_str}",
                "        **kwargs",
                f"))  # type: {self._polling_method_type}",
            ]
        )
        retval.append(
            f"elif polling is False: polling_method = cast({self._polling_method_type}, "
            f"{self._default_no_polling_method(builder)}())"
        )
        retval.append("else: polling_method = polling")
        retval.append("if cont_token:")
        retval.append(f"    return {self._poller(builder)}.from_continuation_token(")
        retval.append("        polling_method=polling_method,")
        retval.append("        continuation_token=cont_token,")
        retval.append("        client=self._client,")
        retval.append("        deserialization_callback=get_long_running_output")
        retval.append("    )")
        retval.append(
            f"return {self._poller(builder)}"
            "(self._client, raw_result, get_long_running_output, polling_method)"
        )
        return retval

    def get_long_running_output(self, builder) -> List[str]:
        retval = ["def get_long_running_output(pipeline_response):"]
        if builder.lro_response:
            if builder.lro_response.headers:
                retval.append("    response_headers = {}")
            if (
                not self.code_model.options["models_mode"]
                or builder.lro_response.headers
            ):
                retval.append("    response = pipeline_response.http_response")
            retval.extend(
                [
                    f"    {line}"
                    for line in self.response_headers_and_deserialization(
                        builder.lro_response
                    )
                ]
            )
        retval.append("    if cls:")
        retval.append(
            "        return cls(pipeline_response, {}, {})".format(
                "deserialized"
                if builder.lro_response and builder.lro_response.types
                else "None",
                "response_headers"
                if builder.lro_response and builder.lro_response.headers
                else "{}",
            )
        )
        if builder.lro_response and builder.lro_response.types:
            retval.append("    return deserialized")
        return retval


class _SyncLROOperationBaseSerializer(
    _LROOperationBaseSerializer, _SyncOperationBaseSerializer
):  # pylint: disable=abstract-method
    def _response_docstring_text_template(
        self, builder
    ) -> str:  # pylint: disable=no-self-use
        lro_section = f"An instance of {builder.get_poller(async_mode=False)} "
        if self._cls_docstring_rtype:
            return lro_section + "that returns either {}" + self._cls_docstring_rtype
        return lro_section + "that returns {}"


    def _response_type_annotation(self, builder: LROOperation) -> str:
        return builder.response_type_annotation(async_mode=False)

    def _default_polling_method(self, builder: BuilderType) -> str:
        return builder.get_default_polling_method(
            async_mode=False, azure_arm=self.code_model.options["azure_arm"]
        )

    def _default_no_polling_method(self, builder: BuilderType) -> str:
        return builder.get_default_no_polling_method(async_mode=False)

    @property
    def _polling_method_type(self):
        return "PollingMethod"

    def _poller(self, builder: BuilderType) -> str:
        return builder.get_poller(async_mode=False)



class SyncLROOperationGenericSerializer(
    _SyncLROOperationBaseSerializer, SyncOperationGenericSerializer
):
    pass


class SyncLROOperationPython3Serializer(
    _SyncLROOperationBaseSerializer, SyncOperationPython3Serializer
):
    pass


class AsyncLROOperationSerializer(
    _LROOperationBaseSerializer, AsyncOperationSerializer
):
    def _response_docstring_text_template(
        self, builder
    ) -> str:  # pylint: disable=no-self-use
        lro_section = f"An instance of {builder.get_poller(async_mode=True)} "
        if self._cls_docstring_rtype:
            return lro_section + "that returns either {}" + self._cls_docstring_rtype
        return lro_section + "that returns {}"

    def _response_docstring_type_wrapper(
        self, builder
    ) -> List[str]:  # pylint: no-self-use
        return [f"~{builder.get_poller_path(async_mode=True)}"]

    def _response_type_annotation(self, builder: LROOperation) -> str:
        return builder.response_type_annotation(async_mode=True)

    def _default_polling_method(self, builder: BuilderType) -> str:
        return builder.get_default_polling_method(
            async_mode=True, azure_arm=self.code_model.options["azure_arm"]
        )

    def _default_no_polling_method(self, builder: BuilderType) -> str:
        return builder.get_default_no_polling_method(async_mode=True)

    @property
    def _polling_method_type(self):
        return "AsyncPollingMethod"

    def _poller(self, builder: BuilderType) -> str:
        return builder.get_poller(async_mode=True)


############################## LRO PAGING OPERATIONS ##############################


class _LROPagingOperationBaseSerializer(
    _LROOperationBaseSerializer, _PagingOperationBaseSerializer
):  # pylint: disable=abstract-method
    def get_long_running_output(self, builder: BuilderType) -> List[str]:
        retval = ["def get_long_running_output(pipeline_response):"]
        retval.append(f"    {self._function_definition} internal_get_next(next_link=None):")
        retval.append("        if next_link is None:")
        retval.append("            return pipeline_response")
        retval.append(f"        return {self._call_method}get_next(next_link)")
        retval.append("")
        retval.append(f"    return {self._pager(builder)}(")
        retval.append("        internal_get_next, extract_data")
        retval.append("    )")
        return retval

    def decorators(self, builder, async_mode: bool) -> List[str]:
        """Decorators for the method"""
        return _LROOperationBaseSerializer.decorators(self, builder, async_mode)


class _SyncLROPagingOperationBaseSerializer(  # pylint: disable=abstract-method
    _SyncLROOperationBaseSerializer,
    _SyncPagingOperationBaseSerializer,
    _LROPagingOperationBaseSerializer,
):
    def _response_docstring_type_wrapper(self, builder: BuilderType) -> List[str]:
        return _SyncLROOperationBaseSerializer._response_docstring_type_wrapper(
            self, builder
        ) + _SyncPagingOperationBaseSerializer._response_docstring_type_wrapper(
            self, builder
        )

    def _response_type_annotation_wrapper(self, builder: BuilderType) -> List[str]:
        return _SyncLROOperationBaseSerializer._response_type_annotation_wrapper(
            self, builder
        ) + [builder.get_pager(async_mode=False)]

    def _response_docstring_text_template(self, builder: BuilderType) -> str:
        lro_doc = _SyncLROOperationBaseSerializer._response_docstring_text_template(
            self, builder
        )
        paging_doc = (
            _SyncPagingOperationBaseSerializer._response_docstring_text_template(
                self, builder
            )
        )
        paging_doc = paging_doc.replace(paging_doc[0], paging_doc[0].lower(), 1)
        return (
            lro_doc.format(paging_doc)
            .replace(self._cls_docstring_rtype, "", 1)
            .replace("either ", "", 1)
        )

    def cls_type_annotation(self, builder: BuilderType) -> str:
        return f"# type: ClsType[{self._response_type_annotation(builder, modify_if_head_as_boolean=False)}]"


class SyncLROPagingOperationGenericSerializer(
    _SyncLROPagingOperationBaseSerializer, SyncOperationGenericSerializer
):
    pass


class SyncLROPagingOperationPython3Serializer(
    _SyncLROPagingOperationBaseSerializer, SyncOperationPython3Serializer
):
    pass


class AsyncLROPagingOperationSerializer(
    _LROPagingOperationBaseSerializer,
    AsyncLROOperationSerializer,
    AsyncPagingOperationSerializer,
):
    @property
    def _function_definition(self) -> str:
        return "async def"

    def _response_docstring_text_template(self, builder: BuilderType) -> str:
        lro_doc = AsyncLROOperationSerializer._response_docstring_text_template(
            self, builder
        )
        paging_doc = AsyncPagingOperationSerializer._response_docstring_text_template(
            self, builder
        )
        paging_doc = paging_doc.replace(paging_doc[0], paging_doc[0].lower(), 1)
        return (
            lro_doc.format(paging_doc)
            .replace(self._cls_docstring_rtype, "", 1)
            .replace("either ", "", 1)
        )


def get_operation_serializer(
    builder,
    code_model,
    async_mode: bool,
    is_python3_file: bool,
) -> _OperationBaseSerializer:
    retcls = _OperationBaseSerializer
    if isinstance(builder, LROPagingOperation):
        return LROPagingOperationSerializer(code_model, async_mode, is_python3_file)
        retcls = (
            AsyncLROPagingOperationSerializer
            if async_mode
            else (
                SyncLROPagingOperationPython3Serializer
                if is_python3_file
                else SyncLROPagingOperationGenericSerializer
            )
        )
        return retcls(code_model)
    if isinstance(builder, LROOperation):
        retcls = (
            AsyncLROOperationSerializer
            if async_mode
            else (
                SyncLROOperationPython3Serializer
                if is_python3_file
                else SyncLROOperationGenericSerializer
            )
        )
        return retcls(code_model)
    if isinstance(builder, PagingOperation):
        retcls = (
            AsyncPagingOperationSerializer
            if async_mode
            else (
                SyncPagingOperationPython3Serializer
                if is_python3_file
                else SyncPagingOperationGenericSerializer
            )
        )
        return retcls(code_model)
    retcls = (
        AsyncOperationSerializer
        if async_mode
        else (
            SyncOperationPython3Serializer
            if is_python3_file
            else SyncOperationGenericSerializer
        )
    )
    return retcls(code_model)


def get_request_builder_serializer(
    code_model, is_python3_file: bool
) -> _RequestBuilderBaseSerializer:
    retcls = (
        RequestBuilderPython3Serializer
        if is_python3_file
        else RequestBuilderGenericSerializer
    )
    return retcls(code_model)
