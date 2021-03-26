# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Optional, Set, Dict
from copy import deepcopy
from .request_builder_parameter import RequestBuilderParameter
from .parameter_list import ParameterList
from .parameter import ParameterLocation, Parameter
from .primitive_schemas import AnySchema, PrimitiveSchema

def _copy_body_param(new_param_name: str, original_param: RequestBuilderParameter) -> RequestBuilderParameter:
    new_param = deepcopy(original_param)
    new_param.serialized_name = new_param_name
    new_param.schema = AnySchema(namespace="", yaml_data={})
    return new_param


class RequestBuilderParameterList(ParameterList):
    def __init__(
        self, parameters: Optional[List[RequestBuilderParameter]] = None
    ) -> None:
        # need to include init to override type failure.
        # RequestBuilderParameterList takes in a list of RequestBuilderParameter,
        # while ParameterList takes in a list of Parameter
        super(RequestBuilderParameterList, self).__init__(
            parameters  # type: ignore
        )
        self.body_kwarg_names: List[str] = []

    @property
    def constant(self) -> List[Parameter]:
        """We don't do constant bodies in the request builder
        """
        all_constants = super(RequestBuilderParameterList, self).constant
        if self.has_body:
            return [c for c in all_constants if not c.location == ParameterLocation.Body]
        return all_constants

    @property
    def kwargs_to_pop(self) -> List[Parameter]:
        # we don't want to pop the body kwargs in py2.7. We send them straight to HttpRequest
        return [k for k in self.kwargs if k.serialized_name not in self.body_kwarg_names]

    def _get_body_kwargs(self, body_kwargs: List[Parameter]) -> List[Parameter]:
        seen_bodies: Set[str] = set()
        returned_bodies = []
        if body_kwargs:
            if "application/json" in self.content_types:
                returned_bodies.append(_copy_body_param("json", body_kwargs[0]))
        for body_kwarg in body_kwargs:
            if body_kwarg.is_multipart and body_kwarg.is_partial_body and "files" not in seen_bodies:
                seen_bodies.add("files")
                body_kwarg.serialized_name = "files"
                returned_bodies.append(body_kwarg)
            elif body_kwarg.is_partial_body and "data" not in seen_bodies:
                seen_bodies.add("data")
                body_kwarg.serialized_name = "data"
                returned_bodies.append(body_kwarg)
            elif isinstance(body_kwarg.schema, PrimitiveSchema) and "content" not in seen_bodies:
                seen_bodies.add("content")
                body_kwarg.serialized_name = "content"
                returned_bodies.append(body_kwarg)

        if body_kwargs and "content" not in seen_bodies:
            returned_bodies.append(_copy_body_param("content", body_kwargs[0]))
        return returned_bodies



    @property
    def method(self) -> List[Parameter]:
        """The list of parameter used in method signature. Includes both positional and kwargs
        """
        signature_parameters_no_default_value = []
        signature_parameters_default_value = []

        # Want all method parameters.
        # Also allow client parameters if they're going to be used in the request body.
        # i.e., path parameter, query parameter, header.
        parameters = self.get_from_predicate(
            lambda parameter: parameter.implementation == self.implementation or parameter.in_method_code
        )
        body_kwargs = []
        seen_bodies: OrderedSet[str] = {}
        seen_content_type = False

        for parameter in parameters:
            if any([g for g in self.groupers if id(g.yaml_data) == id(parameter.yaml_data)]):
                continue
            if seen_content_type and parameter.serialized_name == "content_type":
                continue
            if parameter.serialized_name == "content_type":
                seen_content_type = True
            if parameter.in_method_signature:
                if parameter.location == ParameterLocation.Body:
                    body_kwargs.append(parameter)
                elif not parameter.default_value and parameter.required:
                    signature_parameters_no_default_value.append(parameter)
                else:
                    signature_parameters_default_value.append(parameter)

        body_kwargs = self._get_body_kwargs(body_kwargs)
        self.body_kwarg_names = [b.serialized_name for b in body_kwargs]
        # put body first. We want them to be the first kwargs.
        signature_parameters = body_kwargs + signature_parameters_no_default_value + signature_parameters_default_value
        signature_parameters.sort(key=lambda item: item.is_kwarg)
        return signature_parameters

    @staticmethod
    def _wanted_path_parameter(parameter):
        return parameter.location == ParameterLocation.Path
