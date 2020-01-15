# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from collections.abc import MutableSequence
import logging
from typing import List, Callable

from .parameter import Parameter, ParameterLocation
from .constant_schema import ConstantSchema


_LOGGER = logging.getLogger(__name__)


class ParameterList(MutableSequence):

    def __init__(self, parameters: List[Parameter] = None, implementation: str = "Method"):
        self.parameters = parameters or []
        self.implementation = implementation

    # MutableSequence

    def __getitem__(self, index):
        if isinstance(index, str):
            raise TypeError(f"{index} is invalid type")
        return self.parameters[index]

    def __len__(self):
        return len(self.parameters)

    def __setitem__(self, index, parameter):
        self.parameters[index] = parameter

    def __delitem__(self, index):
        del self.parameters[index]

    def insert(self, index, value):
        self.parameters.insert(index, value)

    # Parameter helpers

    def has_any_location(self, location: ParameterLocation) -> bool:
        return bool([
            parameter for parameter in self.parameters if parameter.location == location
        ])

    def get_from_predicate(self, predicate: Callable[[Parameter], bool]):
        return [
            parameter for parameter in self.parameters if predicate(parameter)
        ]

    def get_from_location(self, location: ParameterLocation) -> List[Parameter]:
        return self.get_from_predicate(lambda parameter: parameter.location == location)

    @property
    def has_body(self):
        return self.has_any_location(ParameterLocation.Body)

    @property
    def body(self) -> Parameter:
        if not self.has_body:
            raise ValueError(f"Can't get body parameter")
        # Should we check if there is two body? Modeler role right?
        return self.get_from_location(ParameterLocation.Body)[0]

    @property
    def path(self) -> List[Parameter]:
        return [
            parameter for parameter in self.parameters
            if parameter.location in [ParameterLocation.Uri, ParameterLocation.Path] and
            parameter.rest_api_name != "$host"
        ]

    @property
    def query(self) -> List[Parameter]:
        return self.get_from_location(ParameterLocation.Query)

    @property
    def headers(self) -> List[Parameter]:
        return self.get_from_location(ParameterLocation.Header)

    @property
    def constant(self) -> List[Parameter]:
        return self.get_from_predicate(lambda parameter: isinstance(parameter.schema, ConstantSchema))

    @property
    def method(self) -> List[Parameter]:
        """The list of parameter used in method signature.
        """
        def is_parameter_in_signature(parameter):
            """A predicate to tell if this parmater deserves to be in the signature.
            """
            return not (isinstance(parameter.schema, ConstantSchema) or parameter.implementation != self.implementation)

        signature_parameters_required = []
        signature_parameters_optional = []
        for parameter in self.parameters:
            if is_parameter_in_signature(parameter):
                if parameter.is_required:
                    signature_parameters_required.append(parameter)
                else:
                    signature_parameters_optional.append(parameter)

        signature_parameters = signature_parameters_required + signature_parameters_optional
        if self.is_flattened:
            signature_parameters.remove(self.body)
        return signature_parameters

    @property
    def method_signature(self):
        signature = ", ".join([
            parameter.for_method_signature for parameter in self.method
        ])
        if signature:
            signature = ", "+signature
        return signature

    @property
    def is_flattened(self):
        return self.has_any_location(ParameterLocation.Flattened)

    def build_flattened_object(self):
        if not self.is_flattened:
            raise ValueError("This method can't be called if the operation doesn't need parameter flattening")

        parameters = self.get_from_location(ParameterLocation.Flattened)
        parameter_string = ",".join([f"{param.serialized_name}={param.serialized_name}" for param in parameters])

        return f"{self.body.serialized_name} = models.{self.body.schema.name}({parameter_string})"
