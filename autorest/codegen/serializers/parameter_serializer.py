# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Union
from enum import Enum, auto
from ..models import CodeModel, Parameter, ParameterLocation, BodyParameter

class PopKwargType(Enum):
    NO = auto()
    SIMPLE = auto()
    CASE_INSENSITIVE = auto()

class ParameterSerializer:

    def __init__(self, code_model: CodeModel):
        self.code_model = code_model

    def serialize_parameter(self, parameter: Parameter, serializer_name: str) -> str:
        optional_parameters = []

        if parameter.skip_url_encoding:
            optional_parameters.append("skip_quote=True")

        # if parameter.style and not parameter.explode:
        #     if parameter.style in [ParameterStyle.simple, ParameterStyle.form]:
        #         div_char = ","
        #     elif parameter.style in [ParameterStyle.spaceDelimited]:
        #         div_char = " "
        #     elif parameter.style in [ParameterStyle.pipeDelimited]:
        #         div_char = "|"
        #     elif parameter.style in [ParameterStyle.tabDelimited]:
        #         div_char = "\t"
        #     else:
        #         raise ValueError(f"Do not support {parameter.style} yet")
        #     optional_parameters.append(f"div='{div_char}'")

        # if parameter.explode:
        #     if not isinstance(parameter.schema, ListType):
        #         raise ValueError("Got a explode boolean on a non-array schema")
        #     serialization_schema = parameter.schema.element_type
        # else:
        #     serialization_schema = parameter.schema

        # serialization_constraints = serialization_schema.serialization_constraints
        # if serialization_constraints:
        #     optional_parameters += serialization_constraints

        origin_name = parameter.full_client_name

        parameters = [
            f'"{origin_name.lstrip("_")}"',
            "q" if parameter.explode else origin_name,
            f"'{parameter.type.serialization_type}'",
            *optional_parameters,
        ]
        parameters_line = ", ".join(parameters)

        msrest_function_name = {
            ParameterLocation.PATH: "url",
            ParameterLocation.ENDPOINT_PATH: "url",
            ParameterLocation.HEADER: "header",
            ParameterLocation.QUERY: "query",
        }[parameter.location]

        serialize_line = f"{serializer_name}.{msrest_function_name}({parameters_line})"

        if parameter.explode:
            return f"[{serialize_line} if q is not None else '' for q in {origin_name}]"
        return serialize_line

    def serialize_path(self, parameters: List[Parameter], serializer_name: str) -> List[str]:
        retval = ["path_format_arguments = {"]
        retval.extend(
            [
                '    "{}": {},'.format(
                    path_parameter.rest_api_name,
                    self.serialize_parameter(path_parameter, serializer_name),
                )
                for path_parameter in parameters
            ]
        )
        retval.append("}")
        return retval

    def pop_kwargs_from_signature(
        self,
        parameters: List[Union[Parameter, BodyParameter]],
        check_kwarg_dict: bool,
        pop_headers_kwarg: PopKwargType,
        pop_params_kwarg: PopKwargType,
    ) -> List[str]:
        retval = []

        def append_pop_kwarg(key: str, pop_type: PopKwargType) -> None:
            if PopKwargType.CASE_INSENSITIVE == pop_type:
                retval.append(
                    f'_{key} = case_insensitive_dict(kwargs.pop("{key}", {{}}) or {{}})'
                )
            elif PopKwargType.SIMPLE == pop_type:
                retval.append(f'_{key} = kwargs.pop("{key}", {{}}) or {{}}')

        append_pop_kwarg("headers", pop_headers_kwarg)
        append_pop_kwarg("params", pop_params_kwarg)
        if pop_headers_kwarg != PopKwargType.NO or pop_params_kwarg != PopKwargType.NO:
            retval.append("")
        for kwarg in parameters:
            if kwarg.client_default_value or kwarg.optional:
                default_value = kwarg.client_default_value_declaration
                if check_kwarg_dict and (
                    kwarg.location in [ParameterLocation.HEADER, ParameterLocation.QUERY]
                ):
                    kwarg_dict = (
                        "headers"
                        if kwarg.location == ParameterLocation.HEADER
                        else "params"
                    )
                    default_value = (
                        f"_{kwarg_dict}.pop('{kwarg.rest_api_name}', {default_value})"
                    )
                retval.append(
                    f"{kwarg.client_name} = kwargs.pop('{kwarg.client_name}', "
                    + f"{default_value})  # type: {kwarg.type_annotation()}"
                )
            else:
                type_annot = kwarg.type_annotation()
                retval.append(
                    f"{kwarg.client_name} = kwargs.pop('{kwarg.client_name}')  # type: {type_annot}"
                )
        return retval

    def serialize_method(
        self,
        *,
        function_def: str,
        method_name: str,
        need_self_param: bool,
        method_param_signatures: List[str],
        ignore_inconsistent_return_statements: bool = False,
    ):
        lines: List[str] = []
        first_line = f"{function_def} {method_name}("
        if ignore_inconsistent_return_statements:
            first_line += "  # pylint: disable=inconsistent-return-statements"
        lines.append(first_line)
        if need_self_param:
            lines.append("    self,")
        lines.extend([("    " + line) for line in method_param_signatures])
        lines.append(")")
        return "\n".join(lines)
