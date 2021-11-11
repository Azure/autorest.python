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
    BuilderType,
    ObjectSchema,
    DictionarySchema,
    ListSchema,
    BaseSchema,
    Parameter,
    RequestBuilder,
    RequestBuilderParameter,
    EnumSchema,
    SchemaResponse,
    IOSchema,
    ParameterStyle,
)
from . import utils

T = TypeVar("T")
OrderedSet = Dict[T, None]


def _improve_json_string(template_representation: str) -> Any:
    origin = template_representation.split('\n')
    final = []
    for line in origin:
        idx0 = line.find('#')
        idx1 = line.rfind('"')
        modified_line = ""
        if idx0 > -1 and idx1 > -1:
            modified_line = line[:idx0] + line[idx1:] + '  ' + line[idx0:idx1] + '\n'
        else:
            modified_line = line + '\n'
        modified_line = modified_line.replace('"', "").replace("\\", '"')
        final.append(modified_line)
    return ''.join(final)

def _json_dumps_template(template_representation: Any) -> Any:
    # only for template use, since it wraps everything in strings
    return _improve_json_string(json.dumps(template_representation, sort_keys=True, indent=4))

def _serialize_files_or_data_dict(multipart_parameters: List[Parameter]) -> str:
    # only for template use
    template = {
        f'"{param.serialized_name}"': param.schema.get_files_and_data_template_representation(
            optional=not param.required,
            description=param.description,
        )
        for param in multipart_parameters
    }
    return _json_dumps_template(template)

def _get_files_example_template(builder: BuilderType) -> List[str]:
    multipart_params = builder.parameters.multipart
    if multipart_params:
        retval = [
            "# multipart input template you can fill out and use as your `files` input.",
        ]
        retval.extend(f"files = {_serialize_files_or_data_dict(multipart_params)}".splitlines())
        return retval
    raise ValueError(
        "You're trying to get a template for your multipart params, but you don't have multipart params"
    )

def _get_data_example_template(builder: BuilderType) -> List[str]:
    data_inputs = builder.parameters.data_inputs
    if data_inputs:
        retval = [
            "# form-encoded input template you can fill out and use as your `data` input."
        ]
        retval.extend(f"data = {_serialize_files_or_data_dict(data_inputs)}".splitlines())
        return retval
    raise ValueError(
        "You're trying to get a template for your form-encoded params, but you don't have form-encoded params"
    )

def _content_type_error_check(builder: BuilderType) -> List[str]:
    retval = ["else:"]
    retval.append("    raise ValueError(")
    retval.append("        \"The content_type '{}' is not one of the allowed values: \"")
    retval.append(f'        "{builder.parameters.content_types}".format(content_type)')
    retval.append("    )")
    return retval

def _serialize_files_and_data_body(builder: BuilderType, param_name: str) -> List[str]:
    retval: List[str] = []
    # we have to construct our form data before passing to the request as well
    retval.append("# Construct form data")
    retval.append(f"{param_name} = {{")
    for param in builder.parameters.body:
        retval.append(f'    "{param.rest_api_name}": {param.serialized_name},')
    retval.append("}")
    return retval

def _pop_parameters_kwarg(
    function_name: str,
    kwarg_name: str,
) -> str:
    return f'{function_name}_parameters = kwargs.pop("{kwarg_name}", {{}})  # type: Dict[str, Any]'

def _serialize_grouped_body(builder: BuilderType) -> List[str]:
    retval: List[str] = []
    for grouped_parameter in builder.parameters.grouped:
        retval.append(f"{grouped_parameter.serialized_name} = None")
    for grouper_name, grouped_parameters in groupby(
        builder.parameters.grouped, key=lambda a: cast(Parameter, a.grouped_by).serialized_name
    ):
        retval.append(f"if {grouper_name} is not None:")
        for grouped_parameter in grouped_parameters:
            retval.append(
                f"    {grouped_parameter.serialized_name} = "
                f"{ grouper_name }.{ grouped_parameter.corresponding_grouped_property.name }"
            )
    return retval

def _serialize_flattened_body(builder: BuilderType) -> List[str]:
    retval: List[str] = []
    if not builder.parameters.is_flattened:
        raise ValueError(
            "This method can't be called if the operation doesn't need parameter flattening"
        )

    parameters = builder.parameters.get_from_predicate(
        lambda parameter: parameter.in_method_code
    )
    parameter_string = ", ".join(
        [f"{param.target_property_name}={param.serialized_name}"
        for param in parameters if param.target_property_name
        ]
    )
    object_schema = cast(ObjectSchema, builder.parameters.body[0].schema)
    retval.append(
        f"{builder.parameters.body[0].serialized_name} = _models.{object_schema.name}({parameter_string})"
    )
    return retval

def _content_type_docstring(builder: BuilderType) -> str:
    content_type_str = (
        ":keyword str content_type: Media type of the body sent to the API. " +
        f'Default value is "{builder.parameters.default_content_type}". ' +
        'Allowed values are: "{}."'.format('", "'.join(builder.parameters.content_types))
    )
    return content_type_str

class _BuilderSerializerProtocol(ABC):
    @property
    @abstractmethod
    def _is_in_class(self) -> bool:
        ...

    @property
    @abstractmethod
    def _function_definition(self) -> str:
        """The def keyword for the builder we're serializing, i.e. 'def' or 'async def'"""
        ...

    @property
    @abstractmethod
    def _def(self) -> str:
        """The general definition of a function, i.e. def or async def"""
        ...

    @property
    @abstractmethod
    def _want_inline_type_hints(self) -> bool:
        """Whether you want inline type hints. If false, your type hints will be commented'"""
        ...

    @abstractmethod
    def _method_signature(self, builder: BuilderType) -> str:
        """Signature of the builder. Does not include return type annotation"""
        ...

    @abstractmethod
    def _response_type_annotation(self, builder: BuilderType, modify_if_head_as_boolean: bool = True) -> str:
        """The mypy type annotation for the response"""
        ...

    @abstractmethod
    def _response_type_annotation_wrapper(self, builder: BuilderType) -> List[str]:
        """Any wrappers that you want to go around the response type annotation"""
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
    def method_signature_and_response_type_annotation(self, builder: BuilderType) -> str:
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
    def want_example_template(self, builder: BuilderType) -> bool:
        ...

    @abstractmethod
    def get_example_template(self, builder: BuilderType) -> List[str]:
        ...

    @abstractmethod
    def _get_json_example_template(self, builder: BuilderType) -> List[str]:
        ...

    @abstractmethod
    def _has_json_example_template(self, builder: BuilderType) -> bool:
        ...

    @abstractmethod
    def _has_files_example_template(self, builder: BuilderType) -> bool:
        ...
    @abstractmethod
    def _has_data_example_template(self, builder: BuilderType) -> bool:
        ...

    @abstractmethod
    def _json_example_param_name(self, builder: BuilderType) -> str:
        ...

    @abstractmethod
    def _get_json_response_template(self, builder: BuilderType) -> List[str]:
        ...

    @abstractmethod
    def _get_json_response_template_to_status_codes(self, builder: BuilderType) -> Dict[str, List[str]]:
        ...

    @abstractmethod
    def _get_kwargs_to_pop(self, builder: BuilderType) -> List[Parameter]:
        ...

class _BuilderBaseSerializer(_BuilderSerializerProtocol):  # pylint: disable=abstract-method
    def __init__(self, code_model: CodeModel) -> None:
        self.code_model = code_model

    @property
    def _cls_docstring_rtype(self) -> str:
        return "" if self.code_model.options["version_tolerant"] else " or the result of cls(response)"

    def _method_signature(self, builder: BuilderType) -> str:
        return utils.serialize_method(
            function_def=self._function_definition,
            method_name=builder.name,
            is_in_class=self._is_in_class,
            method_param_signatures=builder.parameters.method_signature(self._want_inline_type_hints),
        )

    def _response_type_annotation_wrapper(self, builder: BuilderType) -> List[str]:
        return []

    def method_signature_and_response_type_annotation(self, builder: BuilderType) -> str:
        method_signature = self._method_signature(builder)
        response_type_annotation = self._response_type_annotation(builder)
        for wrapper in self._response_type_annotation_wrapper(builder)[::-1]:
            response_type_annotation = f"{wrapper}[{response_type_annotation}]"
        return self._method_signature_and_response_type_annotation_template(method_signature, response_type_annotation)

    def description_and_summary(self, builder: BuilderType) -> List[str]:
        description_list: List[str] = []
        description_list.append(f"{ builder.summary.strip() if builder.summary else builder.description.strip() }")
        if builder.summary and builder.description:
            description_list.append("")
            description_list.append(builder.description.strip())
        description_list.append("")
        return description_list

    def param_description(self, builder: Union[RequestBuilder, Operation]) -> List[str]:  # pylint: disable=no-self-use
        description_list: List[str] = []
        for param in [m for m in builder.parameters.method if not m.is_hidden]:
            description_list.extend(
                f":{param.description_keyword} { param.serialized_name }: { param.description }".replace(
                    "\n", "\n "
                ).split("\n")
            )
            description_list.append(
                f":{param.docstring_type_keyword} { param.serialized_name }: { param.docstring_type }"
            )
        try:
            request_builder: RequestBuilder = cast(Operation, builder).request_builder
        except AttributeError:
            request_builder = cast(RequestBuilder, builder)

        if len(request_builder.schema_requests) > 1:
            description_list.append(_content_type_docstring(builder))
        return description_list

    def param_description_and_response_docstring(self, builder: BuilderType) -> List[str]:
        return self.param_description(builder) + self.response_docstring(builder)

    def _get_json_response_template_to_status_codes(self, builder: BuilderType) -> Dict[str, List[str]]:
        # successful status codes of responses that have bodies
        responses = [
            response
            for response in builder.responses
            if any(code in builder.success_status_code for code in response.status_codes)
            and isinstance(
                response.schema, (
                    DictionarySchema,
                    ListSchema,
                    ObjectSchema,
                    EnumSchema
                ))
        ]
        retval = defaultdict(list)
        for response in responses:
            status_codes = [str(status_code) for status_code in response.status_codes]
            response_json = _json_dumps_template(cast(BaseSchema, response.schema).get_json_template_representation())
            retval[response_json].extend(status_codes)
        return retval

    def get_example_template(self, builder: BuilderType) -> List[str]:
        template = []
        if self._has_json_example_template(builder):
            template.append("")
            template += self._get_json_example_template(builder)
        if self._has_files_example_template(builder):
            template.append("")
            template += _get_files_example_template(builder)
        if self._has_data_example_template(builder):
            template.append("")
            template += _get_data_example_template(builder)
        if self._get_json_response_template_to_status_codes(builder):
            template.append("")
            template += self._get_json_response_template(builder)
        return template

    def _get_json_example_template(self, builder: BuilderType) -> List[str]:
        template = []
        json_body = builder.parameters.json_body
        object_schema = cast(ObjectSchema, json_body)
        try:
            discriminator_name = object_schema.discriminator_name
            subtype_map = object_schema.subtype_map
        except AttributeError:
            discriminator_name = None
            subtype_map = None
        if subtype_map:
            template.append("{} = '{}'".format(discriminator_name, "' or '".join(subtype_map.values())))
            template.append("")

        try:
            property_with_discriminator = object_schema.property_with_discriminator
        except AttributeError:
            property_with_discriminator = None
        if property_with_discriminator:
            polymorphic_schemas = [
                s
                for s in self.code_model.sorted_schemas
                if s.name in property_with_discriminator.schema.subtype_map.values()
            ]
            num_schemas = min(self.code_model.options["polymorphic_examples"], len(polymorphic_schemas))
            for i in range(num_schemas):
                schema = polymorphic_schemas[i]
                polymorphic_property = _json_dumps_template(
                    schema.get_json_template_representation(),
                )
                template.extend(f"{property_with_discriminator.name} = {polymorphic_property}".splitlines())
                if i != num_schemas - 1:
                    template.append("# OR")
            template.append("")
        template.append("# JSON input template you can fill out and use as your body input.")
        json_template = _json_dumps_template(
            builder.parameters.json_body.get_json_template_representation(),
        )
        template.extend(f"{self._json_example_param_name(builder)} = {json_template}".splitlines())
        return template

    @property
    @abstractmethod
    def serializer_name(self) -> str:
        ...

    def _serialize_parameter(
        self, param: Parameter, function_name: str
    ) -> List[str]:
        set_parameter = "{}_parameters['{}'] = {}".format(
            function_name,
            param.rest_api_name,
            utils.build_serialize_data_call(param, function_name, self.serializer_name)
        )
        if param.required:
            retval = [set_parameter]
        else:
            retval = [
                f"if {param.full_serialized_name} is not None:",
                f"    {set_parameter}"
            ]
        return retval

    def _get_json_response_template(self, builder: BuilderType) -> List[str]:
        template = []
        for response_body, status_codes in self._get_json_response_template_to_status_codes(builder).items():
            template.append("# response body for status code(s): {}".format(", ".join(status_codes)))
            template.extend(f"response.json() == {response_body}".splitlines())
        return template


    def pop_kwargs_from_signature(self, builder: BuilderType) -> List[str]:
        return utils.pop_kwargs_from_signature(self._get_kwargs_to_pop(builder))

    def serialize_path(self, builder: BuilderType) -> List[str]:
        return utils.serialize_path(builder.parameters.path, self.serializer_name)

    @property
    def _function_definition(self) -> str:
        return self._def


############################## REQUEST BUILDERS ##############################


class _RequestBuilderBaseSerializer(_BuilderBaseSerializer):  # pylint: disable=abstract-method
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

    def want_example_template(self, builder: BuilderType) -> bool:
        if self.code_model.options["builders_visibility"] != "public":
            return False  # if we're not exposing rest layer, don't need to generate
        if builder.parameters.has_body:
            body_kwargs = set(builder.parameters.body_kwarg_names.keys())
            return bool(body_kwargs.intersection({"json", "files", "data"}))
        return bool(self._get_json_response_template_to_status_codes(builder))

    @property
    def _def(self) -> str:
        return "def"

    @property
    def _is_in_class(self) -> bool:
        return False

    def _response_type_annotation(self, builder: BuilderType, modify_if_head_as_boolean: bool = True) -> str:
        return "HttpRequest"

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

    def _has_json_example_template(self, builder: BuilderType) -> bool:
        return "json" in builder.parameters.body_kwarg_names

    def _has_files_example_template(self, builder: BuilderType) -> bool:
        return "files" in builder.parameters.body_kwarg_names

    def _has_data_example_template(self, builder: BuilderType) -> bool:
        return "data" in builder.parameters.body_kwarg_names

    @abstractmethod
    def _body_params_to_pass_to_request_creation(self, builder: BuilderType) -> List[str]:
        ...

    def create_http_request(self, builder: BuilderType) -> List[str]:
        retval = ["return HttpRequest("]
        retval.append(f'    method="{builder.method}",')
        retval.append("    url=url,")
        if builder.parameters.query:
            retval.append("    params=query_parameters,")
        if builder.parameters.headers:
            retval.append("    headers=header_parameters,")
        if builder.parameters.has_body:
            retval.extend([
                f"    {body_kwarg}={body_kwarg},"
                for body_kwarg in self._body_params_to_pass_to_request_creation(builder)
            ])
        retval.append("    **kwargs")
        retval.append(")")
        return retval

    def serialize_headers(self, builder: BuilderType) -> List[str]:
        retval = ["# Construct headers"]
        retval.append(_pop_parameters_kwarg("header", "headers"))
        for parameter in builder.parameters.headers:
            retval.extend(self._serialize_parameter(
                parameter,
                function_name="header",
            ))
        return retval

    def serialize_query(self, builder: BuilderType) -> List[str]:
        retval = ["# Construct parameters"]
        retval.append(_pop_parameters_kwarg("query", "params"))
        for parameter in builder.parameters.query:
            retval.extend(self._serialize_parameter(
                parameter,
                function_name="query",
            ))
        return retval

class RequestBuilderGenericSerializer(_RequestBuilderBaseSerializer):
    @property
    def _want_inline_type_hints(self) -> bool:
        return False

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, response_type_annotation: str):
        return utils.method_signature_and_response_type_annotation_template(
            is_python_3_file=False, method_signature=method_signature, response_type_annotation=response_type_annotation
        )

    def _get_kwargs_to_pop(self, builder: BuilderType):
        return builder.parameters.kwargs_to_pop(is_python_3_file=False)

    def _body_params_to_pass_to_request_creation(self, builder: BuilderType) -> List[str]:
        if builder.parameters.has_body and not builder.parameters.body_kwarg_names:
            # this means we have a constant body
            # only doing json body in this case
            return ["json"]
        return []


class RequestBuilderPython3Serializer(_RequestBuilderBaseSerializer):
    @property
    def _want_inline_type_hints(self) -> bool:
        return True

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, response_type_annotation: str):
        return utils.method_signature_and_response_type_annotation_template(
            is_python_3_file=True, method_signature=method_signature, response_type_annotation=response_type_annotation
        )

    def _get_kwargs_to_pop(self, builder: BuilderType):
        return builder.parameters.kwargs_to_pop(is_python_3_file=True)

    def _body_params_to_pass_to_request_creation(self, builder: BuilderType) -> List[str]:
        body_kwargs = list(builder.parameters.body_kwarg_names.keys())
        if body_kwargs:
            return body_kwargs
        if builder.parameters.has_body:
            # this means we have a constant body
            # only doing json body in this case
            return ["json"]
        return body_kwargs


############################## NORMAL OPERATIONS ##############################


class _OperationBaseSerializer(_BuilderBaseSerializer):  # pylint: disable=abstract-method
    def description_and_summary(self, builder: BuilderType) -> List[str]:
        retval = super().description_and_summary(builder)
        if builder.deprecated:
            retval.append(".. warning::")
            retval.append("    This method is deprecated")
            retval.append("")
        return retval

    @property
    def _is_in_class(self) -> bool:
        return True

    @property
    def serializer_name(self) -> str:
        return "self._serialize"

    def _response_docstring_type_wrapper(self, builder: BuilderType) -> List[str]:  # pylint: disable=unused-argument, no-self-use
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

    def _response_type_annotation(self, builder: BuilderType, modify_if_head_as_boolean: bool = True) -> str:
        if (
            modify_if_head_as_boolean
            and builder.request_builder.method.lower() == "head"
            and self.code_model.options["head_as_boolean"]
        ):
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

    def cls_type_annotation(self, builder: BuilderType) -> str:
        return f"# type: ClsType[{self._response_type_annotation(builder, modify_if_head_as_boolean=False)}]"

    def _response_docstring_text_template(self, builder: BuilderType) -> str:  # pylint: disable=no-self-use, unused-argument
        cls_str = f",{self._cls_docstring_rtype}" if self._cls_docstring_rtype else ""
        return "{}" + cls_str

    def response_docstring(self, builder: BuilderType) -> List[str]:
        responses_with_body = [r for r in builder.responses if r.has_body]
        if builder.request_builder.method.lower() == "head" and self.code_model.options["head_as_boolean"]:
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
        response_str = f":return: {self._response_docstring_text_template(builder).format(response_docstring_text)}"
        rtype_str = f":rtype: {self._response_docstring_type_template(builder).format(rtype)}"
        return [response_str, rtype_str, ":raises: ~azure.core.exceptions.HttpResponseError"]

    def want_example_template(self, builder: BuilderType) -> bool:
        if self.code_model.options['models_mode']:
            return False
        if builder.parameters.has_body:
            if builder.parameters.multipart or builder.parameters.data_inputs:
                return True
            body_params = builder.parameters.body
            return any([b for b in body_params if isinstance(b.schema, (DictionarySchema, ListSchema, ObjectSchema))])
        return bool(self._get_json_response_template_to_status_codes(builder))

    def _json_example_param_name(self, builder: BuilderType) -> str:
        return builder.parameters.body[0].serialized_name

    def _has_json_example_template(self, builder: BuilderType) -> bool:
        return (
            builder.parameters.has_body and
            not (builder.parameters.multipart or builder.parameters.data_inputs)
        )

    def _has_files_example_template(self, builder: BuilderType) -> bool:
        return bool(builder.parameters.multipart)

    def _has_data_example_template(self, builder: BuilderType) -> bool:
        return bool(builder.parameters.data_inputs)

    def _serialize_body_call(
        self, builder: BuilderType, body_param: Parameter, send_xml: bool, ser_ctxt: Optional[str], ser_ctxt_name: str
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

    def _serialize_body(self, builder: BuilderType, body_param: Parameter, body_kwarg: str) -> List[str]:
        retval = []
        send_xml = bool(
            builder.parameters.has_body and
            any(["xml" in ct for ct in builder.parameters.content_types]) and
            not isinstance(body_param.schema, IOSchema)
        )
        ser_ctxt_name = "serialization_ctxt"
        ser_ctxt = builder.parameters.body[0].xml_serialization_ctxt if send_xml else None
        if ser_ctxt:
            retval.append(f'{ser_ctxt_name} = {{"xml": {{{ser_ctxt}}}}}')
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

    def _set_body_content_kwarg(
        self, builder: BuilderType, body_param: Parameter, body_kwarg: Parameter
    ) -> List[str]:
        retval: List[str] = []
        if body_kwarg.serialized_name == "data" or body_kwarg.serialized_name == "files":
            return retval
        try:
            if not body_param.style == ParameterStyle.binary:
                retval.extend(self._serialize_body(builder, body_param, body_kwarg.serialized_name))
                return retval
        except AttributeError:
            pass
        retval.append(f"_{body_kwarg.serialized_name} = {body_param.serialized_name}")
        return retval


    def _serialize_body_parameters(
        self, builder: BuilderType,
    ) -> List[str]:
        retval = []
        body_kwargs = [
            p for p in builder.request_builder.parameters.body
            if p.content_types
        ]
        builder_params = []
        if builder.parameters.has_body:
            builder_params += builder.parameters.body
        if builder.multiple_content_type_parameters.has_body:
            builder_params += builder.multiple_content_type_parameters.body
        if len(body_kwargs) == 1:
            retval.extend(self._set_body_content_kwarg(builder, builder.parameters.body[0], body_kwargs[0]))
        else:
            for idx, body_kwarg in enumerate(body_kwargs):
                body_param = next(
                    b for b in builder_params
                    if body_kwarg in b.body_kwargs
                )
                if_statement = "if" if idx == 0 else "elif"
                retval.append(
                    f'{if_statement} content_type.split(";")[0] in {body_kwarg.pre_semicolon_content_types}:'
                )
                retval.extend(["    " + line for line in self._set_body_content_kwarg(builder, body_param, body_kwarg)])
            retval.extend(_content_type_error_check(builder))

        return retval

    def _call_request_builder_helper(
        self,
        builder: BuilderType,
        request_builder: RequestBuilder,
        template_url: Optional[str] = None,
    ) -> List[str]:
        retval = []
        if len(builder.body_kwargs_to_pass_to_request_builder) > 1:
            # special case for files, bc we hardcode body param to be called 'files' for multipart
            body_params_to_initialize = builder.body_kwargs_to_pass_to_request_builder
            if self.code_model.options["version_tolerant"]:
                body_params_to_initialize = [p for p in body_params_to_initialize if p != "files"]
            for k in body_params_to_initialize:
                retval.append(f"_{k} = None")
        if builder.parameters.grouped:
            # request builders don't allow grouped parameters, so we group them before making the call
            retval.extend(_serialize_grouped_body(builder))

        if builder.parameters.is_flattened:
            # unflatten before passing to request builder as well
            retval.extend(_serialize_flattened_body(builder))
        if request_builder.multipart or request_builder.parameters.data_inputs:
            if not self.code_model.options["version_tolerant"]:
                param_name = "_files" if request_builder.multipart else "_data"
                retval.extend(_serialize_files_and_data_body(builder, param_name))
        elif builder.parameters.has_body and not builder.parameters.body[0].constant:
            retval.extend(self._serialize_body_parameters(builder))

        if self.code_model.options["builders_visibility"] == "embedded":
            request_path_name = request_builder.name
        else:
            builder_group_name = request_builder.builder_group_name
            request_path_name = "rest{}.{}".format(
                ("_" + builder_group_name) if builder_group_name else "", request_builder.name
            )
        retval.append("")
        retval.append(f"request = {request_path_name}(")
        for parameter in request_builder.parameters.method:
            if (
                parameter.is_body and
                not parameter.constant and
                parameter.serialized_name not in builder.body_kwargs_to_pass_to_request_builder
            ):
                continue
            high_level_name = cast(RequestBuilderParameter, parameter).name_in_high_level_operation
            retval.append(f"    {parameter.serialized_name}={high_level_name},")
        template_url = template_url or f"self.{builder.name}.metadata['url']"
        retval.append(f"    template_url={template_url},")
        retval.append(f")")
        if not self.code_model.options["version_tolerant"]:
            pass_files = ""
            if "files" in builder.body_kwargs_to_pass_to_request_builder:
                pass_files = ", _files"
            retval.append(f"request = _convert_request(request{pass_files})")
        if builder.parameters.path:
            retval.extend(self.serialize_path(builder))
        retval.append(
            "request.url = self._client.format_url(request.url{})".format(
                ", **path_format_arguments" if builder.parameters.path else ""
            )
        )
        return retval

    def call_request_builder(self, builder: BuilderType) -> List[str]:
        return self._call_request_builder_helper(builder, builder.request_builder)

    def response_headers_and_deserialization(
        self,
        response: SchemaResponse,
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
                    "response" if self.code_model.options["version_tolerant"]
                    else "response.stream_download(self._client._pipeline)"
                )
            )
        elif response.has_body:
            if self.code_model.options["models_mode"]:
                retval.append(f"deserialized = self._deserialize('{response.serialization_type}', pipeline_response)")
            else:
                is_xml = any(["xml" in ct for ct in response.content_types])
                deserialized_value = ""
                deserialized_value = "ET.fromstring(response.text())" if is_xml else "response.json()"
                retval.append(f"if response.content:")
                retval.append(f"    deserialized = {deserialized_value}")
                retval.append("else:")
                retval.append("    deserialized = None")
        return retval

    @property
    @abstractmethod
    def _call_method(self) -> str:
        ...

    def handle_error_response(self, builder: BuilderType) -> List[str]:
        retval = [f"if response.status_code not in {str(builder.success_status_code)}:"]
        retval.append("    map_error(status_code=response.status_code, response=response, error_map=error_map)")
        error_model = ""
        if builder.default_exception and self.code_model.options["models_mode"]:
            retval.append(
                f"    error = self._deserialize.failsafe_deserialize({builder.default_exception}, pipeline_response)"
            )
            error_model = ", model=error"
        retval.append("    raise HttpResponseError(response=response{}{})".format(
            error_model,
            ", error_format=ARMErrorFormat" if self.code_model.options['azure_arm'] else ""
        ))
        return retval

    def handle_response(self, builder: BuilderType) -> List[str]:
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
                for status_code in builder.success_status_code:
                    response = builder.get_response_from_status(status_code)
                    if response.headers or response.has_body:
                        retval.append(f"if response.status_code == {status_code}:")
                        retval.extend([
                            f"    {line}"
                            for line in self.response_headers_and_deserialization(response)
                        ])
                        retval.append("")
            else:
                retval.extend(self.response_headers_and_deserialization(
                    builder.responses[0]
                ))
                retval.append("")
        retval.append("if cls:")
        retval.append("    return cls(pipeline_response, {}, {})".format(
            "deserialized" if builder.has_response_body else "None",
            "response_headers" if builder.any_response_has_headers else '{}'
        ))
        if builder.has_response_body:
            retval.append("")
            retval.append("return deserialized")
        if builder.request_builder.method == 'HEAD' and self.code_model.options['head_as_boolean']:
            retval.append("return 200 <= response.status_code <= 299")
        return retval

    def error_map(self, builder: BuilderType) -> List[str]:
        retval = ["error_map = {"]
        if builder.status_code_exceptions:
            if not 401 in builder.status_code_exceptions_status_codes:
                retval.append("    401: ClientAuthenticationError,")
            if not 404 in builder.status_code_exceptions_status_codes:
                retval.append("    404: ResourceNotFoundError,")
            if not 409 in builder.status_code_exceptions_status_codes:
                retval.append("    409: ResourceExistsError,")
            for excep in builder.status_code_exceptions:
                error_model_str = ""
                if (
                    isinstance(excep.schema, ObjectSchema)
                    and excep.is_exception
                    and self.code_model.options["models_mode"]
                ):
                    error_model_str = f", model=self._deserialize(_models.{excep.serialization_type}, response)"
                error_format_str = ", error_format=ARMErrorFormat" if self.code_model.options['azure_arm'] else ""
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
            retval.append("    401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError")
        retval.append("}")
        retval.append("error_map.update(kwargs.pop('error_map', {}))")
        return retval

    @staticmethod
    def get_metadata_url(builder: BuilderType) -> str:
        return f"{builder.python_name}.metadata = {{'url': '{ builder.request_builder.url }'}}  # type: ignore"

class _SyncOperationBaseSerializer(_OperationBaseSerializer):  # pylint: disable=abstract-method
    @property
    def _want_inline_type_hints(self) -> bool:
        return False

    @property
    def _def(self) -> str:
        return "def"

    @property
    def _call_method(self) -> str:
        return ""

class SyncOperationGenericSerializer(_SyncOperationBaseSerializer):
    @property
    def _want_inline_type_hints(self) -> bool:
        return False

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, response_type_annotation: str):
        return utils.method_signature_and_response_type_annotation_template(
            is_python_3_file=False, method_signature=method_signature, response_type_annotation=response_type_annotation
        )

    def _get_kwargs_to_pop(self, builder: BuilderType):
        return builder.parameters.kwargs_to_pop(is_python_3_file=False)


class SyncOperationPython3Serializer(_SyncOperationBaseSerializer):
    @property
    def _want_inline_type_hints(self) -> bool:
        return True

    @staticmethod
    def _method_signature_and_response_type_annotation_template(method_signature: str, response_type_annotation: str):
        return utils.method_signature_and_response_type_annotation_template(
            is_python_3_file=True, method_signature=method_signature, response_type_annotation=response_type_annotation
        )

    def _get_kwargs_to_pop(self, builder: BuilderType):
        return builder.parameters.kwargs_to_pop(is_python_3_file=True)

class AsyncOperationSerializer(SyncOperationPython3Serializer):

    @property
    def _def(self) -> str:
        return "async def"

    @property
    def _function_definition(self) -> str:
        return "async def"

    @property
    def _call_method(self) -> str:
        return "await "


############################## PAGING OPERATIONS ##############################


class _PagingOperationBaseSerializer(_OperationBaseSerializer):  # pylint: disable=abstract-method
    def _response_docstring_text_template(self, builder: BuilderType) -> str:  # pylint: disable=no-self-use, unused-argument
        if self._cls_docstring_rtype:
            return "An iterator like instance of either {}" + self._cls_docstring_rtype
        return "An iterator like instance of {}"

    def cls_type_annotation(self, builder: BuilderType) -> str:
        interior = super()._response_type_annotation(builder, modify_if_head_as_boolean=False)
        return f"# type: ClsType[{interior}]"

    def call_next_link_request_builder(self, builder: BuilderType) -> List[str]:
        if builder.next_request_builder:
            request_builder = builder.next_request_builder
            template_url = f"'{request_builder.url}'"
        else:
            request_builder = builder.request_builder
            template_url = "next_link"
        request_builder = builder.next_request_builder or builder.request_builder
        return self._call_request_builder_helper(
            builder,
            request_builder,
            template_url=template_url,
        )

    def _prepare_request_callback(self, builder: BuilderType) -> List[str]:
        retval = ["def prepare_request(next_link=None):"]
        retval.append("    if not next_link:")
        retval.extend([
            f"        {line}"
            for line in self.call_request_builder(builder)
        ])
        retval.append("")
        retval.append("    else:")
        retval.extend([
            f"        {line}"
            for line in self.call_next_link_request_builder(builder)
        ])
        if not builder.next_request_builder and builder.parameters.path:
            retval.append("")
            retval.extend([
                f"        {line}"
                for line in self.serialize_path(builder)
            ])
        if not builder.next_request_builder:
            retval.append('        request.method = "GET"')
        else:
            retval.append('')
        retval.append("    return request")
        return retval

    @property
    @abstractmethod
    def _list_type_returned_to_users(self) -> str:
        ...

    @staticmethod
    @abstractmethod
    def _pager(builder: BuilderType) -> str:
        ...

    def _extract_data_callback(self, builder: BuilderType) -> List[str]:
        retval = [f"{self._def} extract_data(pipeline_response):"]
        response = builder.responses[0]
        deserialized = (
            f'self._deserialize("{response.serialization_type}", pipeline_response)'
            if self.code_model.options["models_mode"] else
            "_loads(pipeline_response.http_response.body())"
        )
        retval.append(f"    deserialized = {deserialized}")
        item_name = builder.item_name(self.code_model)
        list_of_elem = f".{item_name}" if self.code_model.options["models_mode"] else f'["{item_name}"]'
        retval.append(f"    list_of_elem = deserialized{list_of_elem}")
        retval.append("    if cls:")
        retval.append("        list_of_elem = cls(list_of_elem)")

        next_link_name = builder.next_link_name
        if not next_link_name:
            next_link_property = "None"
        elif self.code_model.options["models_mode"]:
            next_link_property = f"deserialized.{next_link_name} or None"
        else:
            next_link_property = f'deserialized.get("{next_link_name}", None)'
        retval.append(f"    return {next_link_property}, {self._list_type_returned_to_users}(list_of_elem)")
        return retval

    def _get_next_callback(self, builder: BuilderType) -> List[str]:
        retval = [f"{self._def} get_next(next_link=None):"]
        retval.append("    request = prepare_request(next_link)")
        retval.append("")
        retval.append(
            f"    pipeline_response = {self._call_method}self._client._pipeline.run(request, "
            f"stream={builder.is_stream_response}, **kwargs)"
        )
        retval.append("    response = pipeline_response.http_response")
        retval.append("")
        retval.extend([
            f"    {line}"
            for line in self.handle_error_response(builder)
        ])
        retval.append("")
        retval.append("    return pipeline_response")
        return retval

    def set_up_params_for_pager(self, builder: BuilderType) -> List[str]:
        retval = [f"cls = kwargs.pop('cls', None)  {self.cls_type_annotation(builder)}"]
        retval.extend(self.error_map(builder))
        retval.extend(self._prepare_request_callback(builder))
        retval.append("")
        retval.extend(self._extract_data_callback(builder))
        retval.append("")
        retval.extend(self._get_next_callback(builder))
        return retval

class _SyncPagingOperationBaseSerializer(_PagingOperationBaseSerializer, _SyncOperationBaseSerializer):  # pylint: disable=abstract-method
    def _response_docstring_type_wrapper(self, builder: BuilderType) -> List[str]:  # pylint: no-self-use
        return [f"~{builder.get_pager_path(async_mode=False)}"]

    def _response_type_annotation_wrapper(self, builder: BuilderType) -> List[str]:
        return ["Iterable"]

    @property
    def _list_type_returned_to_users(self) -> str:  # pylint: disable=no-self-use
        return "iter"

    @staticmethod
    def _pager(builder: BuilderType) -> str:
        return builder.get_pager(async_mode=False)

class SyncPagingOperationGenericSerializer(_SyncPagingOperationBaseSerializer, SyncOperationGenericSerializer):
    pass

class SyncPagingOperationPython3Serializer(_SyncPagingOperationBaseSerializer, SyncOperationPython3Serializer):
    pass

class AsyncPagingOperationSerializer(_PagingOperationBaseSerializer, AsyncOperationSerializer):
    def _response_docstring_type_wrapper(self, builder: BuilderType) -> List[str]:  # pylint: no-self-use
        return [f"~{builder.get_pager_path(async_mode=True)}"]

    @property
    def _function_definition(self) -> str:
        return "def"

    def _response_type_annotation_wrapper(self, builder: BuilderType) -> List[str]:
        return ["AsyncIterable"]

    @property
    def _list_type_returned_to_users(self) -> str:  # pylint: disable=no-self-use
        return "AsyncList"

    @staticmethod
    def _pager(builder: BuilderType) -> str:
        return builder.get_pager(async_mode=True)


############################## LRO OPERATIONS ##############################


class _LROOperationBaseSerializer(_OperationBaseSerializer):  # pylint: disable=abstract-method
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
        retval.append(":keyword str continuation_token: A continuation token to restart a poller from a saved state.")
        retval.append(
            f":keyword polling: By default, your polling method will be {self._default_polling_method(builder)}. "
            "Pass in False for this operation to not poll, or pass in your own initialized polling object for a"
            " personal polling strategy."
        )
        retval.append(f":paramtype polling: bool or ~{self._polling_method_type}")
        retval.append(
            ":keyword int polling_interval: Default waiting time between two polls for LRO operations "
            "if no Retry-After header is present."
        )
        return retval

    def initial_call(self, builder: BuilderType) -> List[str]:
        retval = [f"polling = kwargs.pop('polling', True)  # type: Union[bool, {self._polling_method_type}]"]
        retval.append(f"cls = kwargs.pop('cls', None)  {self.cls_type_annotation(builder)}")
        retval.append("lro_delay = kwargs.pop(")
        retval.append("    'polling_interval',")
        retval.append("    self._config.polling_interval")
        retval.append(")")
        retval.append("cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]")
        retval.append("if cont_token is None:")
        retval.append(f"    raw_result = {self._call_method}self.{builder.initial_operation.name}(")
        retval.extend([
            f"        {parameter.serialized_name}={parameter.serialized_name},"
            for parameter in builder.parameters.method
        ])
        retval.append("        cls=lambda x,y,z: x,")
        retval.append("        **kwargs")
        retval.append("    )")
        retval.append("kwargs.pop('error_map', None)")
        return retval

    def return_lro_poller(self, builder: BuilderType) -> List[str]:
        retval = []
        lro_options_str = (
            ", lro_options={'final-state-via': '" + builder.lro_options['final-state-via'] + "'}"
            if builder.lro_options else ""
        )
        path_format_arguments_str = ""
        if builder.parameters.path:
            path_format_arguments_str = ", path_format_arguments=path_format_arguments"
            retval.extend(self.serialize_path(builder))
            retval.append("")
        retval.append(
            f"if polling is True: polling_method = {self._default_polling_method(builder)}" +
            f"(lro_delay{lro_options_str}{path_format_arguments_str}, **kwargs)"
        )
        retval.append(
            f"elif polling is False: polling_method = {self._default_no_polling_method(builder)}()"
        )
        retval.append("else: polling_method = polling")
        retval.append("if cont_token:")
        retval.append(f"    return {self._poller(builder)}.from_continuation_token(")
        retval.append("        polling_method=polling_method,")
        retval.append("        continuation_token=cont_token,")
        retval.append("        client=self._client,")
        retval.append("        deserialization_callback=get_long_running_output")
        retval.append("    )")
        retval.append("else:")
        retval.append(
            f"    return {self._poller(builder)}"
            "(self._client, raw_result, get_long_running_output, polling_method)"
        )
        return retval

    def get_long_running_output(self, builder: BuilderType) -> List[str]:
        retval = ["def get_long_running_output(pipeline_response):"]
        if builder.lro_response:
            if builder.lro_response.has_headers:
                retval.append("    response_headers = {}")
            retval.append("    response = pipeline_response.http_response")
            retval.extend([
                f"    {line}"
                for line in self.response_headers_and_deserialization(builder.lro_response)
            ])
        retval.append("    if cls:")
        retval.append("        return cls(pipeline_response, {}, {})".format(
            'deserialized' if builder.lro_response and builder.lro_response.has_body else 'None',
            'response_headers' if builder.lro_response and builder.lro_response.has_headers else '{}'
        ))
        if builder.lro_response and builder.lro_response.has_body:
            retval.append("    return deserialized")
        return retval


class _SyncLROOperationBaseSerializer(_LROOperationBaseSerializer, _SyncOperationBaseSerializer):  # pylint: disable=abstract-method
    def _response_docstring_text_template(self, builder: BuilderType) -> str:  # pylint: disable=no-self-use
        lro_section = f"An instance of {builder.get_poller(async_mode=False)} "
        if self._cls_docstring_rtype:
            return lro_section + "that returns either {}" + self._cls_docstring_rtype
        return lro_section + "that returns {}"

    def _response_docstring_type_wrapper(self, builder: BuilderType) -> List[str]:  # pylint: no-self-use
        return [f"~{builder.get_poller_path(async_mode=False)}"]

    def _response_type_annotation_wrapper(self, builder: BuilderType) -> List[str]:
        return [builder.get_poller(async_mode=False)]

    def _default_polling_method(self, builder: BuilderType) -> str:
        return builder.get_default_polling_method(async_mode=False, azure_arm=self.code_model.options["azure_arm"])

    def _default_no_polling_method(self, builder: BuilderType) -> str:
        return builder.get_default_no_polling_method(async_mode=False)

    @property
    def _polling_method_type(self):
        return "azure.core.polling.PollingMethod"

    def _poller(self, builder: BuilderType) -> str:
        return builder.get_poller(async_mode=False)

class SyncLROOperationGenericSerializer(_SyncLROOperationBaseSerializer, SyncOperationGenericSerializer):
    pass

class SyncLROOperationPython3Serializer(_SyncLROOperationBaseSerializer, SyncOperationPython3Serializer):
    pass

class AsyncLROOperationSerializer(_LROOperationBaseSerializer, AsyncOperationSerializer):

    def _response_docstring_text_template(self, builder: BuilderType) -> str:  # pylint: disable=no-self-use
        lro_section = f"An instance of {builder.get_poller(async_mode=True)} "
        if self._cls_docstring_rtype:
            return lro_section + "that returns either {}" + self._cls_docstring_rtype
        return lro_section + "that returns {}"

    def _response_docstring_type_wrapper(self, builder: BuilderType) -> List[str]:  # pylint: no-self-use
        return [f"~{builder.get_poller_path(async_mode=True)}"]

    def _response_type_annotation_wrapper(self, builder: BuilderType) -> List[str]:
        return [builder.get_poller(async_mode=True)]

    def _default_polling_method(self, builder: BuilderType) -> str:
        return builder.get_default_polling_method(async_mode=True, azure_arm=self.code_model.options["azure_arm"])

    def _default_no_polling_method(self, builder: BuilderType) -> str:
        return builder.get_default_no_polling_method(async_mode=True)

    @property
    def _polling_method_type(self):
        return "azure.core.polling.AsyncPollingMethod"

    def _poller(self, builder: BuilderType) -> str:
        return builder.get_poller(async_mode=True)


############################## LRO PAGING OPERATIONS ##############################

class _LROPagingOperationBaseSerializer(_LROOperationBaseSerializer, _PagingOperationBaseSerializer):  # pylint: disable=abstract-method

    def get_long_running_output(self, builder: BuilderType) -> List[str]:
        retval = ["def get_long_running_output(pipeline_response):"]
        retval.append(f"    {self._def} internal_get_next(next_link=None):")
        retval.append("        if next_link is None:")
        retval.append("            return pipeline_response")
        retval.append("        else:")
        retval.append(f"            return {self._call_method}get_next(next_link)")
        retval.append("")
        retval.append(f"    return {self._pager(builder)}(")
        retval.append("        internal_get_next, extract_data")
        retval.append("    )")
        return retval


class _SyncLROPagingOperationBaseSerializer(  # pylint: disable=abstract-method
    _SyncLROOperationBaseSerializer, _SyncPagingOperationBaseSerializer, _LROPagingOperationBaseSerializer
):

    def _response_docstring_type_wrapper(self, builder: BuilderType) -> List[str]:
        return _SyncLROOperationBaseSerializer._response_docstring_type_wrapper(
            self, builder
        ) + _SyncPagingOperationBaseSerializer._response_docstring_type_wrapper(self, builder)

    def _response_type_annotation_wrapper(self, builder: BuilderType) -> List[str]:
        return _SyncLROOperationBaseSerializer._response_type_annotation_wrapper(self, builder) + [
            builder.get_pager(async_mode=False)
        ]

    def _response_docstring_text_template(self, builder: BuilderType) -> str:
        lro_doc = _SyncLROOperationBaseSerializer._response_docstring_text_template(self, builder)
        paging_doc = _SyncPagingOperationBaseSerializer._response_docstring_text_template(self, builder)
        paging_doc = paging_doc.replace(paging_doc[0], paging_doc[0].lower(), 1)
        return lro_doc.format(paging_doc).replace(self._cls_docstring_rtype, "", 1).replace("either ", "", 1)

    def cls_type_annotation(self, builder: BuilderType) -> str:
        return f"# type: ClsType[{self._response_type_annotation(builder, modify_if_head_as_boolean=False)}]"

class SyncLROPagingOperationGenericSerializer(_SyncLROPagingOperationBaseSerializer, SyncOperationGenericSerializer):
    pass

class SyncLROPagingOperationPython3Serializer(_SyncLROPagingOperationBaseSerializer, SyncOperationPython3Serializer):
    pass

class AsyncLROPagingOperationSerializer(
    _LROPagingOperationBaseSerializer, AsyncLROOperationSerializer, AsyncPagingOperationSerializer
):
    @property
    def _function_definition(self) -> str:
        return "async def"

    def _response_docstring_type_wrapper(self, builder: BuilderType) -> List[str]:
        return AsyncLROOperationSerializer._response_docstring_type_wrapper(
            self, builder
        ) + AsyncPagingOperationSerializer._response_docstring_type_wrapper(self, builder)

    def _response_type_annotation_wrapper(self, builder: BuilderType) -> List[str]:
        return AsyncLROOperationSerializer._response_type_annotation_wrapper(self, builder) + [
            builder.get_pager(async_mode=True)
        ]

    def _response_docstring_text_template(self, builder: BuilderType) -> str:
        lro_doc = AsyncLROOperationSerializer._response_docstring_text_template(self, builder)
        paging_doc = AsyncPagingOperationSerializer._response_docstring_text_template(self, builder)
        paging_doc = paging_doc.replace(paging_doc[0], paging_doc[0].lower(), 1)
        return lro_doc.format(paging_doc).replace(self._cls_docstring_rtype, "", 1).replace("either ", "", 1)


def get_operation_serializer(
    builder: BuilderType,
    code_model,
    async_mode: bool,
    is_python_3_file: bool,
) -> _OperationBaseSerializer:
    retcls = _OperationBaseSerializer
    if isinstance(builder, LROPagingOperation):
        retcls = (
            AsyncLROPagingOperationSerializer if async_mode
            else (
                SyncLROPagingOperationPython3Serializer if is_python_3_file
                else SyncLROPagingOperationGenericSerializer
            )
        )
        return retcls(code_model)
    if isinstance(builder, LROOperation):
        retcls = (
            AsyncLROOperationSerializer if async_mode
            else (SyncLROOperationPython3Serializer if is_python_3_file else SyncLROOperationGenericSerializer)
        )
        return retcls(code_model)
    if isinstance(builder, PagingOperation):
        retcls = (
            AsyncPagingOperationSerializer if async_mode
            else (SyncPagingOperationPython3Serializer if is_python_3_file else SyncPagingOperationGenericSerializer)
        )
        return retcls(code_model)
    retcls = (
        AsyncOperationSerializer if async_mode
        else (SyncOperationPython3Serializer if is_python_3_file else SyncOperationGenericSerializer)
    )
    return retcls(code_model)


def get_request_builder_serializer(code_model, is_python_3_file: bool) -> _RequestBuilderBaseSerializer:
    retcls = RequestBuilderPython3Serializer if is_python_3_file else RequestBuilderGenericSerializer
    return retcls(code_model)
