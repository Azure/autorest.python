# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------


from ..models import ConstantType, CodeModel


def method_signature_and_response_type_annotation_template(
    *,
    method_signature: str,
    response_type_annotation: str,
) -> str:
    return f"{method_signature} -> {response_type_annotation}:"


def need_typing_extensions(code_model: CodeModel):
    if code_model.options["models_mode"] and any(
        isinstance(p.type, ConstantType)
        and (p.optional or code_model.options["models_mode"] == "dpg")
        for namespace_model in code_model.namespace_models
        for model in namespace_model.model_types
        for p in model.properties
    ):
        return True
    if any(
        isinstance(parameter.type, ConstantType)
        for namespace_model in code_model.namespace_models
        for og in namespace_model.operation_groups
        for op in og.operations
        for parameter in op.parameters.method
    ):
        return True
    if any(
        isinstance(parameter.type, ConstantType)
        for namespace_model in code_model.namespace_models
        for client in namespace_model.clients
        for parameter in client.config.parameters.kwargs_to_pop
    ):
        return True
    return False
