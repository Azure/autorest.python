# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List, Optional
from .preparer_parameter import PreparerParameter
from .parameter_list import ParameterList
from .parameter import ParameterLocation, Parameter

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

    @property
    def constant(self) -> List[Parameter]:
        """We don't do constant bodys in the preparer
        """
        all_constants = super(PreparerParameterList, self).constant
        if self.has_body:
            return [c for c in all_constants if not c.location == ParameterLocation.Body]
        return all_constants

    @property
    def method(self) -> List[Parameter]:
        """The list of parameter used in method signature. Includes both positional and kwargs
        """
        signature_parameters_no_default_value = []
        signature_parameters_default_value = []

        body_param = None

        # Want all method parameters.
        # Also allow client parameters if they're going to be used in the request body.
        # i.e., path parameter, query parameter, header.
        parameters = self.get_from_predicate(
            lambda parameter: parameter.implementation == self.implementation or parameter.in_method_code
        )

        for parameter in parameters:
            if any([g for g in self.groupers if id(g.yaml_data) == id(parameter.yaml_data)]):
                continue
            if parameter.in_method_signature:
                if parameter.location == ParameterLocation.Body:
                    if body_param:
                        continue
                    body_param = parameter
                elif not parameter.default_value and parameter.required:
                    signature_parameters_no_default_value.append(parameter)
                else:
                    signature_parameters_default_value.append(parameter)

        # put body at the end of all parameters. This way, when we generate with only path and body being positional,
        # we will make sure body is the last positional
        signature_parameters = signature_parameters_no_default_value + signature_parameters_default_value
        if body_param:
            signature_parameters.append(body_param)
        return signature_parameters

    @staticmethod
    def _wanted_path_parameter(parameter):
        return parameter.location == ParameterLocation.Path
