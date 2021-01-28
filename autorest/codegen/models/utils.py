# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

_M4_HEADER_PARAMETERS = ["content_type", "accept"]

def _remove_multiple_m4_header_parameters(parameters):
    m4_header_params_in_schema = {
        k: [p for p in parameters if p.serialized_name == k]
        for k in _M4_HEADER_PARAMETERS
    }
    remaining_params = [p for p in parameters if p.serialized_name not in _M4_HEADER_PARAMETERS]
    json_m4_header_params = {
        k: [p for p in m4_header_params_in_schema[k] if p.yaml_data["schema"]["type"] == "constant"]
        for k in m4_header_params_in_schema
    }
    for k, v in json_m4_header_params.items():
        if v:
            remaining_params.append(v[0])
        else:
            remaining_params.append(m4_header_params_in_schema[k][0])

    return remaining_params

def get_converted_parameters(yaml_data, parameter_converter):
    multiple_requests = len(yaml_data["requests"]) > 1

    multiple_media_type_parameters = []
    parameters = [parameter_converter(yaml) for yaml in yaml_data.get("parameters", [])]

    for request in yaml_data["requests"]:
        for yaml in request.get("parameters", []):
            parameter = parameter_converter(yaml)
            if yaml["language"]["python"]["name"] in _M4_HEADER_PARAMETERS:
                parameter.is_kwarg = True
                parameters.append(parameter)
            elif multiple_requests:
                multiple_media_type_parameters.append(parameter)
            else:
                parameters.append(parameter)

    if multiple_requests:
        parameters = _remove_multiple_m4_header_parameters(parameters)
        chosen_parameter = multiple_media_type_parameters[0]

        # binary body parameters are required, while object
        # ones are not. We default to optional in this case.
        optional_parameters = [p for p in multiple_media_type_parameters if not p.required]
        if optional_parameters:
            chosen_parameter = optional_parameters[0]
        else:
            chosen_parameter = multiple_media_type_parameters[0]
        chosen_parameter.has_multiple_media_types = True
        parameters.append(chosen_parameter)

    if multiple_media_type_parameters:
        body_parameters_name_set = set(
            p.serialized_name for p in multiple_media_type_parameters
        )
        if len(body_parameters_name_set) > 1:
            raise ValueError(
            f"The body parameter with multiple media types has different names: {body_parameters_name_set}"
        )


    parameters_index = {id(parameter.yaml_data): parameter for parameter in parameters}

    # Need to connect the groupBy and originalParameter
    for parameter in parameters:
        parameter_grouped_by_id = id(parameter.grouped_by)
        if parameter_grouped_by_id in parameters_index:
            parameter.grouped_by = parameters_index[parameter_grouped_by_id]

        parameter_original_id = id(parameter.original_parameter)
        if parameter_original_id in parameters_index:
            parameter.original_parameter = parameters_index[parameter_original_id]

    return parameters, multiple_media_type_parameters
