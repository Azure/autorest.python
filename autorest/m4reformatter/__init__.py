# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""The modelerfour reformatter autorest plugin.
"""
import re
from typing import Dict, Any, List, Optional

from .. import YamlUpdatePlugin

ORIGINAL_ID_TO_UPDATED_TYPE: Dict[int, Dict[str, Any]] = {}
def update_list(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "type": "list",
        "elementType": update_type(yaml_data["elementType"])
    }

def update_dict(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "type": "dict",
        "elementType": update_type(yaml_data["elementType"])
    }

def update_constant(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "type": "constant",
        "valueType": update_type(yaml_data["valueType"]),
        "value": yaml_data["value"]["value"]
    }

def update_enum_value(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "name": yaml_data["language"]["default"]["name"],
        "value": yaml_data["value"],
        "description": yaml_data["language"]["default"]["description"]
    }


def update_enum(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "name": yaml_data["language"]["default"]["name"],
        "type": "enum",
        "valueType": update_type(yaml_data["choiceType"]),
        "values": [update_enum_value(v) for v in yaml_data["choices"]]
    }

def update_property(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "clientName": yaml_data["language"]["default"]["name"],
        "restApiName": yaml_data["serializedName"],
        "type": update_type(yaml_data["schema"]),
        "optional": not yaml_data.get("required"),
        "description": yaml_data["language"]["default"]["description"],
        "isDiscriminator": yaml_data.get("isDiscriminator"),
        "readonly": yaml_data.get("readOnly", False)
    }

def update_discriminated_subtypes(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        obj["discriminatorValue"]: update_type(obj)
        for obj in yaml_data.get("discriminator", {}).get("immediate", {}).values()
    }

def create_model(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "type": "model",
        "name": yaml_data["language"]["default"]["name"],
        "description": yaml_data["language"]["default"]["description"],

    }

def fill_model(yaml_data: Dict[str, Any], current_model: Dict[str, Any]) -> Dict[str, Any]:
    properties = [update_property(p) for p in yaml_data.get("properties", [])]
    yaml_parents = yaml_data.get("parents", {}).get("immediate", [])
    dict_parents = [p for p in yaml_parents if p["type"] == "dict"]
    if dict_parents:
        # add additional properties property
        properties.append({
            "clientName": "additional_properties",
            "restApiName": "",
            "type": dict_parents[0],
            "optional": True,
            "description": "Unmatched properties from the message are deserialized to this collection.",
            "isDiscriminator": False,
            "readonly": False
        })
    current_model.update({
        "properties": properties,
        "parents": [update_type(yaml_data=p) for p in yaml_parents if p["type"] == "model"],
        "discriminatedSubtypes": update_discriminated_subtypes(yaml_data),
        "discriminatorValue": yaml_data.get("discriminatorValue"),
    })
    return current_model


def update_primitive(type_group: str, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    if type_group == "integer":
        return {"type": "integer"}
    if type_group == "number":
        return {"type": "float"}
    if type_group == "string":
        return {"type": "string"}
    if type_group == "byte-array":
        return {"type": "bytes"}
    if type_group == "any":
        return {"type": "any"}
    if type_group == "date-time":
        return {"type": "datetime", "format": yaml_data["format"]}
    if type_group == "duration":
        return {"type": "duration"}
    if type_group == "date":
        return {"type": "date"}
    if type_group == "base64":
        return {"type": "base64"}
    if type_group == "boolean":
        return {"type": "bool"}
    raise ValueError(f"Unknown type group {type_group}")

def update_type(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    if id(yaml_data) in ORIGINAL_ID_TO_UPDATED_TYPE:
        return ORIGINAL_ID_TO_UPDATED_TYPE[id(yaml_data)]
    type_group = yaml_data["type"]
    if type_group == "array":
        updated_type = update_list(yaml_data)
    elif type_group == "dictionary":
        updated_type = update_dict(yaml_data)
    elif type_group == "constant":
        updated_type = update_constant(yaml_data)
    elif type_group in ("choice", "sealed-choice"):
        updated_type = update_enum(yaml_data)
    elif type_group == "object":
        # avoiding infinite loop
        initial_model = create_model(yaml_data)
        ORIGINAL_ID_TO_UPDATED_TYPE[id(yaml_data)] = initial_model
        updated_type = fill_model(yaml_data, initial_model)
    else:
        updated_type = update_primitive(type_group, yaml_data)
    ORIGINAL_ID_TO_UPDATED_TYPE[id(yaml_data)] = updated_type
    return updated_type

def update_parameter_base(
    yaml_data: Dict[str, Any], *, client_name: Optional[str] = None
) -> Dict[str, Any]:
    return {
        "optional": not yaml_data["required"],
        "description": yaml_data["language"]["default"]["description"],
        "clientName": client_name or yaml_data["language"]["default"]["name"],
        "clientDefaultValue": yaml_data.get("clientDefaultValue")
    }

def update_parameter(yaml_data: Dict[str, Any], implementation: str, *, client_name: Optional[str] = None) -> Dict[str, Any]:
    param_base = update_parameter_base(yaml_data, client_name=client_name)
    location = yaml_data["protocol"]["http"]["in"]
    if location == "uri":
        location = "path"
    param_base.update({
        "restApiName": yaml_data["language"]["default"]["serializedName"],
        "location": location,
        "type": ORIGINAL_ID_TO_UPDATED_TYPE[id(yaml_data["schema"])],
        "implementation": implementation
    })
    return param_base

def update_body_parameter(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    base_body_param = next(
        p
        for sr in yaml_data.values()
        for p in sr["parameters"]
        if p["protocol"]["http"]["in"] == "body"
    )
    param_base = update_parameter_base(base_body_param)
    content_type_to_type: Dict[str, Dict[str, Any]] = {}
    for content_type, schema_request in yaml_data.items():
        curr_body_param = next(p for p in schema_request["parameters"] if p["protocol"]["http"]["in"] == "body")
        content_type_to_type[content_type] = update_type(curr_body_param["schema"])
    param_base["contentTypeToType"] = content_type_to_type
    return param_base

def update_parameters(yaml_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    retval: List[Dict[str, Any]] = []
    for param in yaml_data["parameters"]:
        if param["language"]["default"]["name"] == "$host":
            continue
        retval.append(update_parameter(param, "Method"))

    # now we handle content type and accept headers.
    # We only care about the content types on the body parameter itself,
    # so ignoring the different content types for now
    for request in yaml_data["requests"]:
        for param in request["parameters"]:
            if param["protocol"]["http"]["in"] != "body":
                param = update_parameter(param, "Method")
                # find a string type
                param["type"] = next(t for t in ORIGINAL_ID_TO_UPDATED_TYPE.values() if t["type"] == "string")  # override to string type
                retval.append(param)
    return retval

def update_response_header(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "restApiName": yaml_data["header"]["name"],
        "type": update_type(yaml_data["schema"])
    }

def update_response(
    operation_group_yaml_data: Dict[str, Any],
    yaml_data: Dict[str, Any],
) -> Dict[str, Any]:
    type = update_type(yaml_data["schema"]) if yaml_data.get("schema") else None
    return {
        "headers": [update_response_header(h) for h in yaml_data["protocol"]["http"].get("headers", [])],
        "statusCodes": [
            int(code) if code != "default" else "default"
            for code in yaml_data["protocol"]["http"]["statusCodes"]
        ],
        "isError": any(e for e in operation_group_yaml_data.get("exceptions", []) if id(e) == id(yaml_data)),
        "type": type
    }

def update_operation_group_class_name(yaml_data: Dict[str, Any], operation_group_yaml_data: Dict[str, Any]) -> str:
    name = operation_group_yaml_data["language"]["default"]["name"]
    if operation_group_yaml_data["language"] == "":
        # i'm a mixin
        return yaml_data["default"]["name"] + "OperationsMixin"
    if name == "Operations":
        return "Operations"
    return name + "Operations"

def update_operation(group_name: str, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "name": yaml_data["language"]["default"]["name"],
        "description": yaml_data["language"]["default"]["description"],
        "url": yaml_data["requests"][0]["protocol"]["http"]["path"],
        "method": yaml_data["requests"][0]["protocol"]["http"]["method"].upper(),
        "parameters": update_parameters(yaml_data),
        "bodyParameter": update_body_parameter(yaml_data["requestMediaTypes"]) if yaml_data.get("requestMediaTypes") else None,
        "responses": [update_response(yaml_data, r) for r in yaml_data["responses"]],
        "groupName": group_name,
        "operationType": "basic",
    }

def update_operation_group(yaml_data: Dict[str, Any], operation_group_yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    property_name = operation_group_yaml_data["language"]["default"]["name"]
    return {
        "propertyName": property_name,
        "className": update_operation_group_class_name(yaml_data, operation_group_yaml_data),
        "operations": [
            update_operation(property_name, o) for o in operation_group_yaml_data["operations"]
        ]
    }

def update_client_url(yaml_data: Dict[str, Any]) -> str:
    if any(p for p in yaml_data["globalParameters"] if p["language"]["default"]["name"] == "$host"):
        # this means we DO NOT have a parameterized host
        # in order to share code better, going to make it a "parameterized host" of
        # just the endpoint parameter
        return "{endpoint}"
    # we have a parameterized host. Return first url from first request, quite gross
    return yaml_data["operationGroups"][0]["operations"][0]["requests"][0]["protocol"]["http"]["uri"]

class M4Reformatter(YamlUpdatePlugin):
    """Add Python naming information."""

    def update_global_parameters(self, yaml_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        global_params: List[Dict[str, Any]] = []
        for global_parameter in yaml_data:
            client_name: Optional[str] = None
            name = global_parameter["language"]["default"]["name"]
            if name == "$host":
                # I am the non-parameterized endpoint. Modify name based off of flag
                version_tolerant = self._autorestapi.get_boolean_value("version-tolerant", False)
                low_level_client = self._autorestapi.get_boolean_value("low-level-client", False)
                client_name = "endpoint" if (version_tolerant or low_level_client) else "base_url"
            global_params.append(update_parameter(global_parameter, "Client", client_name=client_name))
        return global_params


    def update_client(self, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "name": yaml_data["language"]["default"]["name"],
            "description": yaml_data["info"]["description"],
            "parameters": self.update_global_parameters(yaml_data["globalParameters"]),
            "security": yaml_data["security"],
            "url": update_client_url(yaml_data),
            "namespace": self._autorestapi.get_value("namespace") or yaml_data["language"]["default"]["name"]
        }

    def update_yaml(self, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
        """Convert in place the YAML str."""
        # First we update the types, so we can access for when we're creating parameters etc.
        types: List[Dict[str, Any]] = [
            update_type(t)
            for types in yaml_data["schemas"].values()
            for t in types
        ]
        return {
            "client": self.update_client(yaml_data),
            "operationGroups": [
                update_operation_group(yaml_data, og)
                for og in yaml_data["operationGroups"]
            ],
            "types": types
        }
