# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List
from .request_parameter import RequestParameter
from .parameter_list import ParameterList
from .parameter import ParameterLocation

class RequestParameterList(ParameterList):

    @property
    def method(self) -> List[RequestParameter]:
        """The list of parameter used in method signature.
        """
        signature_parameters_no_default_value = []
        signature_parameters_default_value = []

        # Client level should not be on Method, etc.
        parameters_of_this_implementation = self.get_from_predicate(
            lambda parameter: parameter.implementation == self.implementation
        )
        seen_body = False
        for parameter in parameters_of_this_implementation:
            if parameter.in_method_signature:
                if parameter.location == ParameterLocation.Body:
                    if seen_body:
                        continue
                    seen_body = True
                if not parameter.default_value and parameter.required:
                    signature_parameters_no_default_value.append(parameter)
                else:
                    signature_parameters_default_value.append(parameter)

        signature_parameters = signature_parameters_no_default_value + signature_parameters_default_value
        return signature_parameters