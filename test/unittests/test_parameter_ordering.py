# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import pytest
from autorest.codegen.models import Parameter, AnyObjectSchema
from autorest.codegen.models.primitive_schemas import StringSchema
from autorest.codegen.models.parameter_list import ParameterList
from autorest.codegen.models.parameter import ParameterLocation

def get_parameter(name, required, default_value=None, schema=None):
    if not schema:
        schema = AnyObjectSchema(
            namespace="parameterordering",
            yaml_data={}
        )
    return Parameter(
        schema=schema,
        yaml_data={},
        rest_api_name=name,
        serialized_name=name,
        description="Parameter to test parameter ordering",
        implementation="Method",
        required=required,
        location=ParameterLocation.Path,
        skip_url_encoding=True,
        constraints=[],
        client_default_value=default_value
    )

def test_sort_parameters_with_default_value_from_schema():
    schema = StringSchema(
        namespace="parameterordering",
        yaml_data={"defaultValue": "this_is_the_default", "type": str}
    )
    parameter_with_default_schema_value_required = get_parameter(
        name="required_param_with_schema_default",
        required=True,
        schema=schema
    )
    required_parameter = get_parameter(
        name="required_parameter",
        required=True
    )

    parameter_list = [parameter_with_default_schema_value_required, required_parameter]

    assert [required_parameter, parameter_with_default_schema_value_required] == ParameterList(parameter_list).method

def test_sort_required_parameters():
    required_default_value_parameter = get_parameter(
        name="required_default_value_parameter",
        required=True,
        default_value="hello"
    )
    required_parameter = get_parameter(
        name="required_parameter",
        required=True
    )

    parameter_list = [required_parameter, required_default_value_parameter]

    assert [required_parameter, required_default_value_parameter] == ParameterList(parameter_list).method

    # switch around ordering to confirm

    parameter_list = [required_default_value_parameter, required_parameter]

    assert [required_parameter, required_default_value_parameter] == ParameterList(parameter_list).method

def test_sort_required_and_non_required_parameters():
    required_parameter = get_parameter(
        name="required_parameter",
        required=True
    )

    optional_parameter = get_parameter(
        name="optional_parameter",
        required=False
    )

    parameter_list = [optional_parameter, required_parameter]

    assert [required_parameter, optional_parameter] == ParameterList(parameter_list).method