# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Optional, Set
from copy import deepcopy
from .preparer_parameter import PreparerParameter
from .parameter_list import ParameterList
from .parameter import ParameterLocation, Parameter
from .object_schema import ObjectSchema

def _get_body_param(body_param_name: str, body_param: PreparerParameter):
    copied_param = deepcopy(body_param)
    copied_param.serialized_name = body_param_name
    return copied_param

class PreparerParameterList(ParameterList):
    def __init__(
        self, parameters: Optional[List[PreparerParameter]] = None
    ) -> None:
        # need to include init to override type failure.
        # PreparerParameterList takes in a list of PreparerParameter,
        # while ParameterList takes in a list of Parameter
        super(PreparerParameterList, self).__init__(
            parameters  # type: ignore
        )
        self.body_kwarg_names: Set[str] = set()

    @property
    def constant(self) -> List[Parameter]:
        """We don't do constant bodies in the preparer
        """
        all_constants = super(PreparerParameterList, self).constant
        if self.has_body:
            return [c for c in all_constants if not c.location == ParameterLocation.Body]
        return all_constants

    def _get_body_params(self, body_param: PreparerParameter) -> List[PreparerParameter]:
        body_params = [_get_body_param("content", body_param)]  # we always include content for streams
        if "json" in self.content_type:
            body_params.append(_get_body_param("json", body_param))
        if self.has_multipart:
            body_params.append(_get_body_param("files", body_param))
        if self.has_partial_body:
            body_params.append(_get_body_param("data", body_param))
        return body_params

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
        body_params = []
        seen_bodies: Set[str] = set()

        for parameter in parameters:
            if any([g for g in self.groupers if id(g.yaml_data) == id(parameter.yaml_data)]):
                continue
            if parameter.in_method_signature:
                if parameter.location == ParameterLocation.Body:
                    if isinstance(parameter.schema, ObjectSchema) and "json" not in seen_bodies:
                        seen_bodies.add("json")
                        parameter.serialized_name = "json"
                        body_params.append(parameter)
                    elif parameter.is_multipart and parameter.is_partial_body and "files" not in seen_bodies:
                        seen_bodies.add("files")
                        parameter.serialized_name = "files"
                        body_params.append(parameter)
                    elif parameter.is_partial_body and "data" not in seen_bodies:
                        seen_bodies.add("data")
                        parameter.serialized_name = "data"
                        body_params.append(parameter)
                    elif "content" not in seen_bodies:
                        seen_bodies.add("content")
                        parameter.serialized_name = "content"
                        body_params.append(parameter)
                elif not parameter.default_value and parameter.required:
                    signature_parameters_no_default_value.append(parameter)
                else:
                    signature_parameters_default_value.append(parameter)
        self.body_kwarg_names = seen_bodies

        if body_params:
            if "content" not in seen_bodies:
                content_param = deepcopy(body_params[0])
                content_param.serialized_name = "content"
                body_params.append(content_param)

        # put body first. We want them to be the first kwargs.
        signature_parameters = body_params + signature_parameters_no_default_value + signature_parameters_default_value
        # if body_param:
        #     signature_parameters = self._get_body_params(body_param) + signature_parameters
        return signature_parameters

    @staticmethod
    def _wanted_path_parameter(parameter):
        return parameter.location == ParameterLocation.Path
