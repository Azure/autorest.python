# pylint: disable=too-many-lines
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from abc import abstractmethod
from collections import defaultdict
from typing import Any, Generic, List, Type, TypeVar, Dict, Union, Optional, cast


from ..models import (
    Operation,
    CodeModel,
    PagingOperation,
    LROOperation,
    LROPagingOperation,
    ModelType,
    DictionaryType,
    ListType,
    Parameter,
    RequestBuilder,
    ParameterLocation,
    Response,
    BinaryType,
    BodyParameter,
    ParameterMethodLocation,
    RequestBuilderBodyParameter,
    OverloadedRequestBuilder,
    ConstantType,
    MultipartBodyParameter,
    Property,
    RequestBuilderType,
)
from .parameter_serializer import ParameterSerializer, PopKwargType
from . import utils

T = TypeVar("T")
OrderedSet = Dict[T, None]

BuilderType = TypeVar(
    "BuilderType",
    bound=Union[
        RequestBuilder,
        Operation,
        PagingOperation,
        LROOperation,
        LROPagingOperation,
        OverloadedRequestBuilder,
    ],
)
OperationType = TypeVar(
    "OperationType",
    bound=Union[Operation, PagingOperation, LROOperation, LROPagingOperation],
)


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


def _get_polymorphic_subtype_template(polymorphic_subtype: ModelType) -> List[str]:
    retval: List[str] = []
    retval.append("")
    retval.append(
        f'# JSON input template for discriminator value "{polymorphic_subtype.discriminator_value}":'
    )
    subtype_template = _json_dumps_template(
        polymorphic_subtype.get_json_template_representation(),
    )

    def _get_polymorphic_parent(
        polymorphic_subtype: Optional[ModelType],
    ) -> Optional[ModelType]:
        if not polymorphic_subtype:
            return None
        try:
            return next(
                p for p in polymorphic_subtype.parents if p.discriminated_subtypes
            )
        except StopIteration:
            return None

    polymorphic_parent = _get_polymorphic_parent(polymorphic_subtype)
    while _get_polymorphic_parent(polymorphic_parent):
        polymorphic_parent = _get_polymorphic_parent(polymorphic_parent)
    retval.extend(
        f"{cast(ModelType, polymorphic_parent).snake_case_name} = {subtype_template}".splitlines()
    )
    return retval


def _serialize_grouped_body(builder: BuilderType) -> List[str]:
    retval: List[str] = []
    for grouped_parameter in builder.parameters.grouped:
        retval.append(f"{grouped_parameter.client_name} = None")
    groupers = [p for p in builder.parameters if p.grouper]
    for grouper in groupers:
        retval.append(f"if {grouper.client_name} is not None:")
        retval.extend(
            [
                f"    {parameter} = {grouper.client_name}.{property}"
                for property, parameter in grouper.property_to_parameter_name.items()
            ]
        )
    return retval


def _serialize_flattened_body(body_parameter: BodyParameter) -> List[str]:
    retval: List[str] = []
    if not body_parameter.property_to_parameter_name:
        raise ValueError(
            "This method can't be called if the operation doesn't need parameter flattening"
        )

    parameter_string = ", ".join(
        f"{property_name}={parameter_name}"
        for property_name, parameter_name in body_parameter.property_to_parameter_name.items()
    )
    model_type = cast(ModelType, body_parameter.type)
    retval.append(
        f"{body_parameter.client_name} = _models.{model_type.name}({parameter_string})"
    )
    return retval


def _serialize_multipart_body(builder: BuilderType) -> List[str]:
    retval: List[str] = []
    body_param = cast(MultipartBodyParameter, builder.parameters.body_parameter)
    # we have to construct our form data before passing to the request as well
    retval.append("# Construct form data")
    retval.append(f"_{body_param.client_name} = {{")
    for param in body_param.entries:
        retval.append(f'    "{param.rest_api_name}": {param.client_name},')
    retval.append("}")
    return retval


def _get_json_response_template_to_status_codes(
    builder: OperationType,
) -> Dict[str, List[str]]:
    retval = defaultdict(list)
    for response in builder.responses:
        json_template = response.get_json_template_representation()
        if not json_template:
            continue
        status_codes = [str(status_code) for status_code in response.status_codes]
        response_json = _json_dumps_template(json_template)
        retval[response_json].extend(status_codes)
    return retval


class _BuilderBaseSerializer(Generic[BuilderType]):  # pylint: disable=abstract-method
    def __init__(
        self, code_model: CodeModel, async_mode: bool, is_python3_file: bool
    ) -> None:
        self.code_model = code_model
        self.async_mode = async_mode
        self.is_python3_file = is_python3_file
        self.parameter_serializer = ParameterSerializer()

    @property
    @abstractmethod
    def _need_self_param(self) -> bool:
        ...

    @property
    @abstractmethod
    def _function_def(self) -> str:
        """The def keyword for the builder we're serializing, i.e. 'def' or 'async def'"""
        ...

    @property
    @abstractmethod
    def _call_method(self) -> str:
        """How to call network calls. Await if we have to await network calls"""
        ...

    @property
    @abstractmethod
    def serializer_name(self) -> str:
        ...

    @abstractmethod
    def response_docstring(self, builder: BuilderType) -> List[str]:
        """Response portion of the docstring"""
        ...

    def decorators(self, builder: BuilderType) -> List[str]:
        """Decorators for the method"""
        retval: List[str] = []
        if builder.is_overload:
            return ["@overload"]
        if self.code_model.options["tracing"] and builder.want_tracing:
            retval.append(f"@distributed_trace{'_async' if self.async_mode else ''}")
        return retval

    def _method_signature(self, builder: BuilderType) -> str:
        return self.parameter_serializer.serialize_method(
            function_def=self._function_def,
            method_name=builder.name,
            need_self_param=self._need_self_param,
            method_param_signatures=builder.method_signature(
                self.async_mode or self.is_python3_file, self.async_mode
            ),
            pylint_disable=builder.pylint_disable,
        )

    def method_signature_and_response_type_annotation(
        self, builder: BuilderType, *, want_decorators: Optional[bool] = True
    ) -> str:
        response_type_annotation = builder.response_type_annotation(
            async_mode=self.async_mode
        )
        method_signature = self._method_signature(builder)
        decorators = self.decorators(builder)
        decorators_str = ""
        if decorators and want_decorators:
            decorators_str = "\n".join(decorators) + "\n"
        return (
            decorators_str
            + utils.method_signature_and_response_type_annotation_template(
                is_python3_file=self.is_python3_file,
                method_signature=method_signature,
                response_type_annotation=response_type_annotation,
            )
        )

    def description_and_summary(  # pylint: disable=no-self-use
        self, builder: BuilderType
    ) -> List[str]:
        description_list: List[str] = []
        description_list.append(
            f"{ builder.summary.strip() if builder.summary else builder.description.strip() }"
        )
        if builder.summary and builder.description:
            description_list.append("")
            description_list.append(builder.description.strip())
        description_list.append("")
        return description_list

    def example_template(self, builder: BuilderType) -> List[str]:
        template = []
        if builder.abstract:
            return []
        if self._json_input_example_template(builder):
            template.append("")
            template += self._json_input_example_template(builder)
        return template

    def param_description(  # pylint: disable=no-self-use
        self, builder: BuilderType
    ) -> List[str]:
        description_list: List[str] = []
        for param in builder.parameters.method:
            if not param.in_docstring:
                continue
            description_list.extend(
                f":{param.description_keyword} { param.client_name }: { param.description }".replace(
                    "\n", "\n "
                ).split(
                    "\n"
                )
            )
            docstring_type = param.docstring_type(async_mode=self.async_mode)
            description_list.append(
                f":{param.docstring_type_keyword} {param.client_name}: {docstring_type}"
            )
        return description_list

    def param_description_and_response_docstring(
        self, builder: BuilderType
    ) -> List[str]:
        if builder.abstract:
            return []
        return self.param_description(builder) + self.response_docstring(builder)

    @property
    @abstractmethod
    def _json_response_template_name(self) -> str:
        ...

    def _json_input_example_template(self, builder: BuilderType) -> List[str]:
        template: List[str] = []
        if self.code_model.options["models_mode"]:
            # No input template if we have models
            return template
        if (
            not builder.parameters.has_body
            or builder.parameters.body_parameter.flattened
        ):
            # No input template if now body parameter
            return template
        if builder.overloads:
            # if there's overloads, we do the json input example template on the overload
            return template

        body_param = builder.parameters.body_parameter
        if not isinstance(body_param.type, (ListType, DictionaryType, ModelType)):
            return template

        polymorphic_subtypes: List[ModelType] = []
        body_param.type.get_polymorphic_subtypes(polymorphic_subtypes)
        if polymorphic_subtypes:
            # we just assume one kind of polymorphic body for input
            discriminator_name = cast(
                Property, polymorphic_subtypes[0].discriminator
            ).rest_api_name
            template.append(
                "# The input is polymorphic. The following are possible polymorphic "
                f'inputs based off discriminator "{discriminator_name}":'
            )
            for idx in range(
                min(
                    self.code_model.options["polymorphic_examples"],
                    len(polymorphic_subtypes),
                )
            ):
                template.extend(
                    _get_polymorphic_subtype_template(polymorphic_subtypes[idx])
                )
            template.append("")
        template.append(
            "# JSON input template you can fill out and use as your body input."
        )
        json_template = _json_dumps_template(
            body_param.type.get_json_template_representation(),
        )
        template.extend(
            f"{builder.parameters.body_parameter.client_name} = {json_template}".splitlines()
        )
        return template

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

    def serialize_path(self, builder: BuilderType) -> List[str]:
        return self.parameter_serializer.serialize_path(
            builder.parameters.path, self.serializer_name
        )


############################## REQUEST BUILDERS ##############################


class RequestBuilderSerializer(
    _BuilderBaseSerializer[RequestBuilderType]
):  # pylint: disable=abstract-method
    def description_and_summary(self, builder: RequestBuilderType) -> List[str]:
        retval = super().description_and_summary(builder)
        retval += [
            "See https://aka.ms/azsdk/dpcodegen/python/send_request for how to incorporate this "
            "request builder into your code flow.",
            "",
        ]
        return retval

    @property
    def _call_method(self) -> str:
        return ""

    @property
    def serializer_name(self) -> str:
        return "_SERIALIZER"

    @property
    def _json_response_template_name(self) -> str:
        return "response.json()"

    @staticmethod
    def declare_non_inputtable_constants(builder: RequestBuilderType) -> List[str]:
        def _get_value(param):
            param_type = cast(ConstantType, param.type)
            if param.location in [ParameterLocation.HEADER, ParameterLocation.QUERY]:
                kwarg_dict = (
                    "headers"
                    if param.location == ParameterLocation.HEADER
                    else "params"
                )
                return f"_{kwarg_dict}.pop('{param.rest_api_name}', {param_type.get_declaration()})"
            return f"{param_type.get_declaration()}"

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

    def response_docstring(self, builder: RequestBuilderType) -> List[str]:
        response_str = (
            f":return: Returns an :class:`~azure.core.rest.HttpRequest` that you will pass to the client's "
            + "`send_request` method. See https://aka.ms/azsdk/dpcodegen/python/send_request for how to "
            + "incorporate this response into your code flow."
        )
        rtype_str = f":rtype: ~azure.core.rest.HttpRequest"
        return [response_str, rtype_str]

    def pop_kwargs_from_signature(self, builder: RequestBuilderType) -> List[str]:
        return self.parameter_serializer.pop_kwargs_from_signature(
            builder.parameters.kwargs_to_pop(is_python3_file=self.is_python3_file),
            check_kwarg_dict=True,
            pop_headers_kwarg=PopKwargType.CASE_INSENSITIVE
            if bool(builder.parameters.headers)
            else PopKwargType.NO,
            pop_params_kwarg=PopKwargType.CASE_INSENSITIVE
            if bool(builder.parameters.query)
            else PopKwargType.NO,
        )

    def create_http_request(self, builder: RequestBuilderType) -> List[str]:
        retval = ["return HttpRequest("]
        retval.append(f'    method="{builder.method}",')
        retval.append("    url=_url,")
        if builder.parameters.query:
            retval.append("    params=_params,")
        if builder.parameters.headers:
            retval.append("    headers=_headers,")
        if (
            builder.parameters.has_body
            and builder.parameters.body_parameter.in_method_signature
        ):
            body_param = builder.parameters.body_parameter
            if body_param.constant or (
                self.is_python3_file
                and body_param.method_location != ParameterMethodLocation.KWARG
            ):
                # we only need to pass it through if it's not a kwarg or it's a popped kwarg
                retval.append(
                    f"    {builder.parameters.body_parameter.client_name}="
                    f"{builder.parameters.body_parameter.client_name},"
                )
        retval.append("    **kwargs")
        retval.append(")")
        return retval

    def serialize_headers(self, builder: RequestBuilderType) -> List[str]:
        retval = ["# Construct headers"]
        for parameter in builder.parameters.headers:
            retval.extend(
                self._serialize_parameter(
                    parameter,
                    kwarg_name="headers",
                )
            )
        return retval

    def serialize_query(self, builder: RequestBuilderType) -> List[str]:
        retval = ["# Construct parameters"]
        for parameter in builder.parameters.query:
            retval.extend(
                self._serialize_parameter(
                    parameter,
                    kwarg_name="params",
                )
            )
        return retval

    def construct_url(self, builder: RequestBuilderType) -> str:
        if any(
            o
            for o in ["low_level_client", "version_tolerant"]
            if self.code_model.options.get(o)
        ):
            url_value = _escape_str(builder.url)
        else:
            url_value = f'kwargs.pop("template_url", {_escape_str(builder.url)})'
        return f"_url = {url_value}{'  # pylint: disable=line-too-long' if len(url_value) > 114 else ''}"


############################## NORMAL OPERATIONS ##############################


class _OperationSerializer(
    _BuilderBaseSerializer[OperationType]
):  # pylint: disable=abstract-method
    def description_and_summary(self, builder: OperationType) -> List[str]:
        retval = super().description_and_summary(builder)
        if builder.deprecated:
            retval.append(".. warning::")
            retval.append("    This method is deprecated")
            retval.append("")
        return retval

    @property
    def _json_response_template_name(self) -> str:
        return "response"

    def example_template(self, builder: OperationType) -> List[str]:
        retval = super().example_template(builder)
        if self.code_model.options["models_mode"]:
            return retval
        for response in builder.responses:
            polymorphic_subtypes: List[ModelType] = []
            if not response.type:
                continue
            response.type.get_polymorphic_subtypes(polymorphic_subtypes)
            if polymorphic_subtypes:
                # we just assume one kind of polymorphic body for input
                discriminator_name = cast(
                    Property, polymorphic_subtypes[0].discriminator
                ).rest_api_name
                retval.append(
                    "# The response is polymorphic. The following are possible polymorphic "
                    f'responses based off discriminator "{discriminator_name}":'
                )
                for idx in range(
                    min(
                        self.code_model.options["polymorphic_examples"],
                        len(polymorphic_subtypes),
                    )
                ):
                    retval.extend(
                        _get_polymorphic_subtype_template(polymorphic_subtypes[idx])
                    )

        if _get_json_response_template_to_status_codes(builder):
            retval.append("")
            for (
                response_body,
                status_codes,
            ) in _get_json_response_template_to_status_codes(builder).items():
                retval.append(
                    "# response body for status code(s): {}".format(
                        ", ".join(status_codes)
                    )
                )
                retval.extend(
                    f"{self._json_response_template_name} == {response_body}".splitlines()
                )
        return retval

    def make_pipeline_call(self, builder: OperationType) -> List[str]:
        return [
            f"pipeline_response = {self._call_method}self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access",
            "    request,",
            f"    stream={builder.has_stream_response},",
            "    **kwargs",
            ")",
        ]

    @property
    def _function_def(self) -> str:
        return "async def" if self.async_mode else "def"

    @property
    def _need_self_param(self) -> bool:
        return True

    @property
    def serializer_name(self) -> str:
        return "self._serialize"

    def decorators(self, builder: OperationType) -> List[str]:
        """Decorators for the method"""
        super_decorators = super().decorators(builder)
        if builder.abstract:
            super_decorators.append("@abc.abstractmethod")
        return super_decorators

    def param_description(
        self, builder: OperationType
    ) -> List[str]:  # pylint: disable=no-self-use
        description_list = super().param_description(builder)
        if not self.code_model.options["version_tolerant"]:
            description_list.append(
                ":keyword callable cls: A custom type or function that will be passed the direct response"
            )
        return description_list

    def pop_kwargs_from_signature(self, builder: OperationType) -> List[str]:
        kwargs_to_pop = builder.parameters.kwargs_to_pop(
            is_python3_file=self.is_python3_file
        )
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
            check_client_input=not self.code_model.options["multiapi"],
        )
        kwargs.append(
            f"cls = kwargs.pop('cls', None)  {self.cls_type_annotation(builder)}"
        )
        return kwargs

    def cls_type_annotation(self, builder: OperationType) -> str:
        return f"# type: {builder.cls_type_annotation(async_mode=self.async_mode)}"

    def response_docstring(self, builder: OperationType) -> List[str]:
        response_str = (
            f":return: {builder.response_docstring_text(async_mode=self.async_mode)}"
        )
        rtype_str = (
            f":rtype: {builder.response_docstring_type(async_mode=self.async_mode)}"
        )
        return [
            response_str,
            rtype_str,
            ":raises ~azure.core.exceptions.HttpResponseError:",
        ]

    def _serialize_body_parameter(self, builder: OperationType) -> List[str]:
        """We need to serialize params if they're not meant to be streamed in.

        This function serializes the body params that need to be serialized.
        """
        retval: List[str] = []
        body_param = cast(BodyParameter, builder.parameters.body_parameter)
        body_kwarg_name = builder.request_builder.parameters.body_parameter.client_name
        send_xml = builder.parameters.body_parameter.type.is_xml
        xml_serialization_ctxt = (
            body_param.type.xml_serialization_ctxt if send_xml else None
        )
        ser_ctxt_name = "serialization_ctxt"
        if xml_serialization_ctxt and self.code_model.options["models_mode"]:
            retval.append(f'{ser_ctxt_name} = {{"xml": {{{xml_serialization_ctxt}}}}}')
        if self.code_model.options["models_mode"]:
            is_xml_cmd = ", is_xml=True" if send_xml else ""
            serialization_ctxt_cmd = (
                f", {ser_ctxt_name}={ser_ctxt_name}" if xml_serialization_ctxt else ""
            )
            create_body_call = (
                f"_{body_kwarg_name} = self._serialize.body({body_param.client_name}, "
                f"'{body_param.type.serialization_type}'{is_xml_cmd}{serialization_ctxt_cmd})"
            )
        else:
            create_body_call = f"_{body_kwarg_name} = {body_param.client_name}"
        if body_param.optional:
            retval.append(f"if {body_param.client_name} is not None:")
            retval.append("    " + create_body_call)
            retval.append("else:")
            retval.append(f"    _{body_kwarg_name} = None")
        else:
            retval.append(create_body_call)
        return retval

    def _create_body_parameter(
        self,
        builder: OperationType,
    ) -> List[str]:
        """Create the body parameter before we pass it as either json or content to the request builder"""
        retval = []
        body_param = cast(BodyParameter, builder.parameters.body_parameter)
        if hasattr(body_param, "entries"):
            return _serialize_multipart_body(builder)
        body_kwarg_name = builder.request_builder.parameters.body_parameter.client_name
        if isinstance(body_param.type, BinaryType):
            retval.append(f"_{body_kwarg_name} = {body_param.client_name}")
            if not body_param.default_content_type:
                content_types = "'" + "', '".join(body_param.content_types) + "'"
                retval.extend(
                    [
                        "if not content_type:",
                        f'    raise TypeError("Missing required keyword-only argument: content_type. '
                        f'Known values are:" + "{content_types}")',
                    ]
                )
        else:
            retval.extend(self._serialize_body_parameter(builder))
        return retval

    def _initialize_overloads(self, builder: OperationType) -> List[str]:
        retval: List[str] = []
        same_content_type = (
            len(
                set(
                    o.parameters.body_parameter.default_content_type
                    for o in builder.overloads
                )
            )
            == 1
        )
        if same_content_type:
            default_content_type = builder.overloads[
                0
            ].parameters.body_parameter.default_content_type
            retval.append(f'content_type = content_type or "{default_content_type}"')
        for overload in builder.overloads:
            retval.append(
                f"_{overload.request_builder.parameters.body_parameter.client_name} = None"
            )
        try:
            # if there is a binary overload, we do a binary check first.
            binary_overload = cast(
                OperationType,
                next(
                    (
                        o
                        for o in builder.overloads
                        if isinstance(o.parameters.body_parameter.type, BinaryType)
                    )
                ),
            )
            binary_body_param = binary_overload.parameters.body_parameter
            retval.append(
                f"if {binary_body_param.type.instance_check_template.format(binary_body_param.client_name)}:"
            )
            if binary_body_param.default_content_type and not same_content_type:
                retval.append(
                    f'    content_type = content_type or "{binary_body_param.default_content_type}"'
                )
            retval.extend(
                f"    {l}" for l in self._create_body_parameter(binary_overload)
            )
            retval.append("else:")
            other_overload = cast(
                OperationType,
                next(
                    (
                        o
                        for o in builder.overloads
                        if not isinstance(o.parameters.body_parameter.type, BinaryType)
                    )
                ),
            )
            retval.extend(
                f"    {l}" for l in self._create_body_parameter(other_overload)
            )
            if (
                other_overload.parameters.body_parameter.default_content_type
                and not same_content_type
            ):
                retval.append(
                    "    content_type = content_type or "
                    f'"{other_overload.parameters.body_parameter.default_content_type}"'
                )
        except StopIteration:
            for idx, overload in enumerate(builder.overloads):
                if_statement = "if" if idx == 0 else "elif"
                body_param = overload.parameters.body_parameter
                retval.append(
                    f"{if_statement} {body_param.type.instance_check_template.format(body_param.client_name)}:"
                )
                if body_param.default_content_type and not same_content_type:
                    retval.append(
                        f'    content_type = content_type or "{body_param.default_content_type}"'
                    )
                retval.extend(
                    f"    {l}"
                    for l in self._create_body_parameter(cast(OperationType, overload))
                )
        return retval

    def _create_request_builder_call(
        self,
        builder: OperationType,
        request_builder: RequestBuilderType,
        template_url: Optional[str] = None,
        is_next_request: bool = False,
    ) -> List[str]:
        retval: List[str] = []
        if self.code_model.options["builders_visibility"] == "embedded":
            request_path_name = request_builder.name
        else:
            group_name = request_builder.group_name
            request_path_name = "rest{}.{}".format(
                ("_" + group_name) if group_name else "",
                request_builder.name,
            )
        retval.append(f"request = {request_path_name}(")
        for parameter in request_builder.parameters.method:
            if parameter.location == ParameterLocation.BODY:
                # going to pass in body later based off of overloads
                continue
            if (
                is_next_request
                and builder.operation_type == "paging"
                and not bool(builder.next_request_builder)  # type: ignore
                and not self.code_model.options["reformat_next_link"]
                and parameter.location == ParameterLocation.QUERY
            ):
                # if we don't want to reformat query parameters for next link calls
                # in paging operations with a single swagger operation defintion,
                # we skip passing query params when building the next request
                continue
            retval.append(
                f"    {parameter.client_name}={parameter.name_in_high_level_operation},"
            )
        if request_builder.overloads:
            for overload in request_builder.overloads:
                body_param = cast(
                    RequestBuilderBodyParameter, overload.parameters.body_parameter
                )
                retval.append(
                    f"    {body_param.client_name}={body_param.name_in_high_level_operation},"
                )
        elif request_builder.parameters.has_body:
            body_param = cast(
                RequestBuilderBodyParameter, request_builder.parameters.body_parameter
            )
            retval.append(
                f"    {body_param.client_name}={body_param.name_in_high_level_operation},"
            )
        if not self.code_model.options["version_tolerant"]:
            template_url = template_url or f"self.{builder.name}.metadata['url']"
            retval.append(f"    template_url={template_url},")
        retval.append("    headers=_headers,")
        retval.append("    params=_params,")
        retval.append(f")")
        return retval

    def _postprocess_http_request(
        self, builder: OperationType, template_url: Optional[str] = None
    ) -> List[str]:
        retval: List[str] = []
        if not self.code_model.options["version_tolerant"]:
            pass_files = ""
            if (
                builder.parameters.has_body
                and builder.parameters.body_parameter.client_name == "files"
            ):
                pass_files = ", _files"
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

    def _call_request_builder_helper(  # pylint: disable=too-many-statements
        self,
        builder: OperationType,
        request_builder: RequestBuilderType,
        template_url: Optional[str] = None,
        is_next_request: bool = False,
    ) -> List[str]:
        retval = []
        if builder.parameters.grouped:
            # request builders don't allow grouped parameters, so we group them before making the call
            retval.extend(_serialize_grouped_body(builder))
        if builder.parameters.has_body and builder.parameters.body_parameter.flattened:
            # unflatten before passing to request builder as well
            retval.extend(_serialize_flattened_body(builder.parameters.body_parameter))
        if builder.overloads:
            # we are only dealing with two overloads. If there are three, we generate an abstract operation
            retval.extend(self._initialize_overloads(builder))
        elif builder.parameters.has_body:
            # non-overloaded body
            retval.extend(self._create_body_parameter(builder))
        retval.append("")
        retval.extend(
            self._create_request_builder_call(
                builder, request_builder, template_url, is_next_request
            )
        )
        retval.extend(self._postprocess_http_request(builder, template_url))
        return retval

    def call_request_builder(self, builder: OperationType) -> List[str]:
        return self._call_request_builder_helper(builder, builder.request_builder)

    def response_headers_and_deserialization(
        self,
        response: Response,
    ) -> List[str]:
        retval: List[str] = [
            (
                f"response_headers['{response_header.rest_api_name}']=self._deserialize("
                f"'{response_header.serialization_type}', response.headers.get('{response_header.rest_api_name}'))"
            )
            for response_header in response.headers
        ]
        if response.headers:
            retval.append("")
        if response.is_stream_response:
            retval.append(
                "deserialized = {}".format(
                    "response.iter_bytes()"
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
                deserialized_value = (
                    "ET.fromstring(response.text())"
                    if response.type.is_xml
                    else "response.json()"
                )
                retval.append(f"if response.content:")
                retval.append(f"    deserialized = {deserialized_value}")
                retval.append("else:")
                retval.append(f"    deserialized = None")
        return retval

    def handle_error_response(self, builder: OperationType) -> List[str]:
        retval = [
            f"if response.status_code not in {str(builder.success_status_codes)}:"
        ]
        retval.append(
            "    map_error(status_code=response.status_code, response=response, error_map=error_map)"
        )
        error_model = ""
        if (
            builder.default_error_deserialization
            and self.code_model.options["models_mode"]
        ):
            retval.append(
                f"    error = self._deserialize.failsafe_deserialize({builder.default_error_deserialization}, "
                "pipeline_response)"
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

    def handle_response(self, builder: OperationType) -> List[str]:
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
            deserialized = f"cast({builder.response_type_annotation(async_mode=self.async_mode)}, deserialized)"
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

    def error_map(self, builder: OperationType) -> List[str]:
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
    def get_metadata_url(builder: OperationType) -> str:
        url = _escape_str(builder.request_builder.url)
        return f"{builder.name}.metadata = {{'url': { url }}}  # type: ignore"

    @property
    def _call_method(self) -> str:
        return "await " if self.async_mode else ""


class OperationSerializer(_OperationSerializer[Operation]):
    ...


############################## PAGING OPERATIONS ##############################

PagingOperationType = TypeVar(
    "PagingOperationType", bound=Union[PagingOperation, LROPagingOperation]
)


class _PagingOperationSerializer(
    _OperationSerializer[PagingOperationType]
):  # pylint: disable=abstract-method
    def __init__(
        self, code_model: CodeModel, async_mode: bool, is_python3_file: bool
    ) -> None:
        # for pylint reasons need to redefine init
        # probably because inheritance is going too deep
        super().__init__(code_model, async_mode, is_python3_file)
        self.code_model = code_model
        self.async_mode = async_mode
        self.is_python3_file = is_python3_file
        self.parameter_serializer = ParameterSerializer()

    def serialize_path(self, builder: PagingOperationType) -> List[str]:
        return self.parameter_serializer.serialize_path(
            builder.parameters.path, self.serializer_name
        )

    def decorators(self, builder: PagingOperationType) -> List[str]:
        """Decorators for the method"""
        retval: List[str] = []
        if self.code_model.options["tracing"] and builder.want_tracing:
            retval.append("@distributed_trace")
        if builder.abstract:
            retval.append("@abc.abstractmethod")
        return retval

    def call_next_link_request_builder(self, builder: PagingOperationType) -> List[str]:
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

    def _prepare_request_callback(self, builder: PagingOperationType) -> List[str]:
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
    def _function_def(self) -> str:
        return "def"

    def _extract_data_callback(self, builder: PagingOperationType) -> List[str]:
        retval = [
            f"{'async ' if self.async_mode else ''}def extract_data(pipeline_response):"
        ]
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
            cont_token_property = "None"
        elif self.code_model.options["models_mode"]:
            cont_token_property = f"deserialized.{continuation_token_name} or None"
        else:
            cont_token_property = f'deserialized.get("{continuation_token_name}", None)'
        list_type = "AsyncList" if self.async_mode else "iter"
        retval.append(f"    return {cont_token_property}, {list_type}(list_of_elem)")
        return retval

    def _get_next_callback(self, builder: PagingOperationType) -> List[str]:
        retval = [f"{'async ' if self.async_mode else ''}def get_next(next_link=None):"]
        retval.append("    request = prepare_request(next_link)")
        retval.append("")
        retval.extend([f"    {l}" for l in self.make_pipeline_call(builder)])
        retval.append("    response = pipeline_response.http_response")
        retval.append("")
        retval.extend([f"    {line}" for line in self.handle_error_response(builder)])
        retval.append("")
        retval.append("    return pipeline_response")
        return retval

    def set_up_params_for_pager(self, builder: PagingOperationType) -> List[str]:
        retval = []
        retval.extend(self.error_map(builder))
        retval.extend(self._prepare_request_callback(builder))
        retval.append("")
        retval.extend(self._extract_data_callback(builder))
        retval.append("")
        retval.extend(self._get_next_callback(builder))
        return retval


class PagingOperationSerializer(_PagingOperationSerializer[PagingOperation]):
    ...


############################## LRO OPERATIONS ##############################

LROOperationType = TypeVar(
    "LROOperationType", bound=Union[LROOperation, LROPagingOperation]
)


class _LROOperationSerializer(_OperationSerializer[LROOperationType]):
    def __init__(
        self, code_model: CodeModel, async_mode: bool, is_python3_file: bool
    ) -> None:
        # for pylint reasons need to redefine init
        # probably because inheritance is going too deep
        super().__init__(code_model, async_mode, is_python3_file)
        self.code_model = code_model
        self.async_mode = async_mode
        self.is_python3_file = is_python3_file
        self.parameter_serializer = ParameterSerializer()

    def param_description(self, builder: LROOperationType) -> List[str]:
        retval = super().param_description(builder)
        retval.append(
            ":keyword str continuation_token: A continuation token to restart a poller from a saved state."
        )
        retval.append(
            f":keyword polling: By default, your polling method will be {builder.get_polling_method(self.async_mode)}. "
            "Pass in False for this operation to not poll, or pass in your own initialized polling object for a"
            " personal polling strategy."
        )
        retval.append(
            f":paramtype polling: bool or ~{builder.get_base_polling_method_path(self.async_mode)}"
        )
        retval.append(
            ":keyword int polling_interval: Default waiting time between two polls for LRO operations "
            "if no Retry-After header is present."
        )
        return retval

    def serialize_path(self, builder: LROOperationType) -> List[str]:
        return self.parameter_serializer.serialize_path(
            builder.parameters.path, self.serializer_name
        )

    def initial_call(self, builder: LROOperationType) -> List[str]:
        retval = [
            "polling = kwargs.pop('polling', True)  # type: Union[bool, "
            f"{builder.get_base_polling_method(self.async_mode)}]"
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
                f"        {parameter.client_name}={parameter.client_name},"
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

    def return_lro_poller(self, builder: LROOperationType) -> List[str]:
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
                f"    polling_method = cast({builder.get_base_polling_method(self.async_mode)}, "
                f"{builder.get_polling_method(self.async_mode)}(",
                "        lro_delay,",
                f"        {lro_options_str}",
                f"        {path_format_arguments_str}",
                "        **kwargs",
                f"))  # type: {builder.get_base_polling_method(self.async_mode)}",
            ]
        )
        retval.append(
            f"elif polling is False: polling_method = cast({builder.get_base_polling_method(self.async_mode)}, "
            f"{builder.get_no_polling_method(self.async_mode)}())"
        )
        retval.append("else: polling_method = polling")
        retval.append("if cont_token:")
        retval.append(
            f"    return {builder.get_poller(self.async_mode)}.from_continuation_token("
        )
        retval.append("        polling_method=polling_method,")
        retval.append("        continuation_token=cont_token,")
        retval.append("        client=self._client,")
        retval.append("        deserialization_callback=get_long_running_output")
        retval.append("    )")
        retval.append(
            f"return {builder.get_poller(self.async_mode)}"
            "(self._client, raw_result, get_long_running_output, polling_method)"
        )
        return retval

    def get_long_running_output(self, builder: LROOperationType) -> List[str]:
        pylint_disable = ""
        if not builder.lro_response:
            pylint_disable = "  # pylint: disable=inconsistent-return-statements"
        retval = [f"def get_long_running_output(pipeline_response):{pylint_disable}"]
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
                if builder.lro_response and builder.lro_response.type
                else "None",
                "response_headers"
                if builder.lro_response and builder.lro_response.headers
                else "{}",
            )
        )
        if builder.lro_response and builder.lro_response.type:
            retval.append("    return deserialized")
        return retval


class LROOperationSerializer(_LROOperationSerializer[LROOperation]):
    ...


############################## LRO PAGING OPERATIONS ##############################


class LROPagingOperationSerializer(
    _LROOperationSerializer[LROPagingOperation],
    _PagingOperationSerializer[LROPagingOperation],
):  # pylint: disable=abstract-method
    @property
    def _call_method(self) -> str:
        return "await " if self.async_mode else ""

    @property
    def _function_def(self) -> str:
        return "async def" if self.async_mode else "def"

    def get_long_running_output(self, builder: LROPagingOperation) -> List[str]:
        retval = ["def get_long_running_output(pipeline_response):"]
        retval.append(f"    {self._function_def} internal_get_next(next_link=None):")
        retval.append("        if next_link is None:")
        retval.append("            return pipeline_response")
        retval.append(f"        return {self._call_method}get_next(next_link)")
        retval.append("")
        retval.append(f"    return {builder.get_pager(self.async_mode)}(")
        retval.append("        internal_get_next, extract_data")
        retval.append("    )")
        return retval

    def decorators(self, builder: LROPagingOperation) -> List[str]:  # type: ignore
        """Decorators for the method"""
        return _LROOperationSerializer.decorators(self, builder)  # type: ignore


def get_operation_serializer(
    builder: Operation,
    code_model,
    async_mode: bool,
    is_python3_file: bool,
) -> Union[
    OperationSerializer,
    PagingOperationSerializer,
    LROOperationSerializer,
    LROPagingOperationSerializer,
]:
    retcls: Union[
        Type[OperationSerializer],
        Type[PagingOperationSerializer],
        Type[LROOperationSerializer],
        Type[LROPagingOperationSerializer],
    ] = OperationSerializer
    if builder.operation_type == "lropaging":
        retcls = LROPagingOperationSerializer
    elif builder.operation_type == "lro":
        retcls = LROOperationSerializer
    elif builder.operation_type == "paging":
        retcls = PagingOperationSerializer
    return retcls(code_model, async_mode, is_python3_file)
