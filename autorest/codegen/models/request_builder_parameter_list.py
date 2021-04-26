# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import json
from autorest.codegen.models.base_schema import BaseSchema
from copy import deepcopy
from typing import List, Optional, Set
from .request_builder_parameter import RequestBuilderParameter
from .parameter_list import ParameterList
from .parameter import ParameterLocation, Parameter
from .primitive_schemas import IOSchema, AnySchema
from .dictionary_schema import DictionarySchema

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
        self.body_kwarg_names: Set[str] = set()
        self._json_body: Optional[BaseSchema] = None
        self._multipart_parameters: Optional[Set[RequestBuilderParameter]] = set()

    @property
    def constant(self) -> List[Parameter]:
        """We don't do constant bodies in the request builder
        """
        return [
            c for c in super(RequestBuilderParameterList, self).constant
            if c.location != ParameterLocation.Body
        ]

    @property
    def kwargs_to_pop(self) -> List[Parameter]:
        # we don't want to pop the body kwargs in py2.7. We send them straight to HttpRequest
        return [k for k in self.kwargs if k.serialized_name not in self.body_kwarg_names]

    def get_files_template_representation(self) -> str:
        template = {
            param.serialized_name: param.schema.get_files_template_representation(
                optional=not param.required,
                description=param.description,
            )
            for param in self._multipart_parameters
        }
        return json.dumps(template, sort_keys=True, indent=4)

    def get_json_template_representation(self) -> str:
        return json.dumps(self._json_body.get_json_template_representation(), sort_keys=True, indent=4)

    def _change_body_param_name(self, parameter: RequestBuilderParameter, name: str) -> None:
        self.body_kwarg_names.add(name)
        parameter.serialized_name = name

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
        seen_content_type = False
        body_kwargs = []
        multipart_parameters = set()

        for parameter in parameters:
            if any([g for g in self.groupers if id(g.yaml_data) == id(parameter.yaml_data)]):
                # we don't allow a grouped parameter for the body param
                continue
            if seen_content_type and parameter.serialized_name == "content_type":
                # we ony want one content type
                # there can be multiple content types in the case of multiple media types
                continue
            if parameter.serialized_name == "content_type":
                seen_content_type = True
            if parameter.in_method_signature:
                if parameter.location == ParameterLocation.Body:
                    if parameter.is_multipart:
                        multipart_parameters.add(deepcopy(parameter))
                        if not any(p for p in body_kwargs if p.serialized_name == "files"):
                            parameter.serialized_name = "files"
                            parameter.schema = DictionarySchema(
                                namespace="",
                                yaml_data={},
                                element_type=AnySchema(namespace="", yaml_data={}),
                            )
                            parameter.description = "Multipart input for files. See the template in our example to find the input shape."
                            self.body_kwarg_names.add("files")
                        else:
                            continue
                    elif parameter.is_partial_body:
                        self._change_body_param_name(parameter, "data")
                    elif isinstance(parameter.schema, IOSchema) or not any([ct for ct in self.content_types if "json" in ct]):
                        self._change_body_param_name(parameter, "content")
                    else:
                        self._change_body_param_name(parameter, "json")
                        if not self._json_body:
                            self._json_body = deepcopy(parameter.schema)
                        parameter.schema = AnySchema(namespace="", yaml_data={})
                    body_kwargs.append(parameter)
                elif not parameter.default_value and parameter.required:
                    signature_parameters_no_default_value.append(parameter)
                else:
                    signature_parameters_default_value.append(parameter)
        if not self._multipart_parameters:
            self._multipart_parameters = multipart_parameters
        if body_kwargs and not any(p for p in body_kwargs if p.serialized_name == "content"):
            # we always want to have content so users can pass their info through a stream
            # in this case, we also know there will be at least 2 ways to input your body,
            # so we don't make each body kwarg required
            body_kwargs = [p for p in body_kwargs if p.location == ParameterLocation.Body]
            self.body_kwarg_names.add("content")
            content_param = deepcopy(body_kwargs[0])
            content_param.serialized_name = "content"
            content_param.schema = AnySchema(namespace="", yaml_data={})
            for body_kwarg in body_kwargs:
                body_kwarg.required = False
            body_kwargs.append(content_param)

        signature_parameters = body_kwargs + signature_parameters_no_default_value + signature_parameters_default_value
        signature_parameters.sort(key=lambda item: item.is_kwarg)
        return signature_parameters

    @staticmethod
    def _wanted_path_parameter(parameter):
        return parameter.location == ParameterLocation.Path
