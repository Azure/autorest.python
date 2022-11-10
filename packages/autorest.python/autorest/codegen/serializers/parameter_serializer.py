# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Sequence, Union
from enum import Enum, auto


from ..models import (
    Parameter,
    ParameterLocation,
    ListType,
    ParameterDelimeter,
    RequestBuilderParameter,
    ClientParameter,
    ConfigParameter,
    ParameterType,
)
from ..models.parameter import _ParameterBase


class PopKwargType(Enum):
    NO = auto()
    SIMPLE = auto()
    CASE_INSENSITIVE = auto()


class ParameterSerializer:
    @staticmethod
    def serialize_parameter(parameter: ParameterType, serializer_name: str) -> str:
        optional_parameters = []

        if parameter.skip_url_encoding:
            optional_parameters.append("skip_quote=True")

        if parameter.delimiter and not parameter.explode:
            if parameter.delimiter == ParameterDelimeter.COMMA:
                div_char = ","
            elif parameter.delimiter == ParameterDelimeter.SPACE:
                div_char = " "
            elif parameter.delimiter == ParameterDelimeter.PIPE:
                div_char = "|"
            elif parameter.delimiter == ParameterDelimeter.TAB:
                div_char = "\t"
            else:
                raise ValueError(f"We do not support {parameter.delimiter} yet")
            optional_parameters.append(f"div='{div_char}'")

        if parameter.explode:
            if not isinstance(parameter.type, ListType):
                raise ValueError("Got a explode boolean on a non-array schema")
            type = parameter.type.element_type
        else:
            type = parameter.type

        serialization_constraints = type.serialization_constraints
        if serialization_constraints:
            optional_parameters += serialization_constraints

        origin_name = parameter.full_client_name

        parameters = [
            f'"{origin_name.lstrip("_")}"',
            "q" if parameter.explode else origin_name,
            f"'{type.serialization_type}'",
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

    def serialize_path(
        self,
        parameters: Union[
            List[Parameter],
            List[RequestBuilderParameter],
            List[ClientParameter],
            List[ConfigParameter],
        ],
        serializer_name: str,
    ) -> List[str]:
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

    @staticmethod
    def pop_kwargs_from_signature(
        parameters: Sequence[_ParameterBase],
        check_kwarg_dict: bool,
        pop_headers_kwarg: PopKwargType,
        pop_params_kwarg: PopKwargType,
        check_client_input: bool = False,
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
            if kwarg.client_default_value is not None or kwarg.optional:
                if check_client_input and kwarg.check_client_input:
                    default_value = f"self._config.{kwarg.client_name}"
                else:
                    default_value = kwarg.client_default_value_declaration
                if check_kwarg_dict and (
                    kwarg.location
                    in [ParameterLocation.HEADER, ParameterLocation.QUERY]
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
                    f"{kwarg.client_name}: {kwarg.type_annotation()} = kwargs.pop('{kwarg.client_name}', "
                    + f"{default_value})"
                )
            else:
                type_annot = kwarg.type_annotation()
                retval.append(
                    f"{kwarg.client_name}: {type_annot} = kwargs.pop('{kwarg.client_name}')"
                )
        return retval

    @staticmethod
    def serialize_method(
        *,
        function_def: str,
        method_name: str,
        need_self_param: bool,
        method_param_signatures: List[str],
        pylint_disable: str = "",
    ):
        lines: List[str] = []
        first_line = f"{function_def} {method_name}({pylint_disable}"
        lines.append(first_line)
        if need_self_param:
            lines.append("    self,")
        lines.extend([("    " + line) for line in method_param_signatures])
        lines.append(")")
        return "\n".join(lines)
