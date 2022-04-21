# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""The modelerfour reformatter autorest plugin.
"""
import re
import copy
from typing import Dict, Any, List, Optional, Set, Tuple

from .. import YamlUpdatePlugin
JSON_REGEXP = re.compile(r"^(application|text)/(.+\+)?json$")
ORIGINAL_ID_TO_UPDATED_TYPE: Dict[int, Dict[str, Any]] = {}

# used if we want to get a string / binary type etc
KNOWN_TYPES = {
    "string": {"type": "string"},
    "binary": {"type": "binary"},
}

def get_type(yaml_data: Dict[str, Any]):
    if KNOWN_TYPES.get(yaml_data["type"]):
        return KNOWN_TYPES[yaml_data["type"]]
    return ORIGINAL_ID_TO_UPDATED_TYPE[id(yaml_data)]

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
        "values": [update_enum_value(v) for v in yaml_data["choices"]],
        "description": yaml_data["language"]["default"]["description"],
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
        "parents": [update_type(yaml_data=p) for p in yaml_parents if p["type"] == "object"],
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
        return KNOWN_TYPES["string"]
    if type_group == "byte-array":
        return {"type": "base64"}
    if type_group == "binary":
        return KNOWN_TYPES["binary"]
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
    location = yaml_data["protocol"]["http"]["in"]
    if location == "uri":
        location = "path"

    return {
        "optional": not yaml_data.get("required", False),
        "description": yaml_data["language"]["default"]["description"],
        "clientName": client_name or yaml_data["language"]["default"]["name"],
        "clientDefaultValue": yaml_data.get("clientDefaultValue"),
        "location": location,
    }

def update_parameter(yaml_data: Dict[str, Any], implementation: str, *, client_name: Optional[str] = None) -> Dict[str, Any]:
    param_base = update_parameter_base(yaml_data, client_name=client_name)
    type = get_type(yaml_data["schema"])
    if type["type"] == "constant":
        param_base["clientDefaultValue"] = type["value"]
    param_base.update({
        "restApiName": yaml_data["language"]["default"]["serializedName"],
        "type": type,
        "implementation": implementation,
        "explode": yaml_data["protocol"]["http"].get("explode", False)
    })
    return param_base

def get_all_body_types(yaml_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    seen_body_types = {}
    for schema_request in yaml_data.values():
        curr_body_param = next(p for p in schema_request["parameters"] if p["protocol"]["http"]["in"] == "body")
        seen_body_types[id(curr_body_param["schema"])] = update_type(curr_body_param["schema"])
    return list(seen_body_types.values())


def update_body_parameter(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    base_body_param = next(
        p
        for sr in yaml_data.values()
        for p in sr["parameters"]
        if p["protocol"]["http"]["in"] == "body"
    )
    param_base = update_parameter_base(base_body_param)
    all_body_types = get_all_body_types(yaml_data)
    if len(all_body_types) == 1:
        # single type body parameter
        param_base["discriminator"] = "single"
        param_base["type"] = all_body_types[0]
        param_base["contentTypes"] = list(yaml_data.keys())
        # get default content type
        content_type_param = next(p for p in list(yaml_data.values())[0]["parameters"] if p["language"]["default"]["name"] == "content_type")
        param_base["defaultContentType"] = content_type_param["clientDefaultValue"]
        if all_body_types[0]["type"] == "constant":
            param_base["clientDefaultValue"] = all_body_types[0]["value"]
    else:
        param_base["discriminator"] = "multiple"
        content_type_to_type: Dict[str, Dict[str, Any]] = {}
        # multiple type body parameter
        for content_type, schema_request in yaml_data.items():
            curr_body_param = next(p for p in schema_request["parameters"] if p["protocol"]["http"]["in"] == "body")
            content_type_to_type[content_type] = update_type(curr_body_param["schema"])
        param_base["contentTypeToType"] = content_type_to_type
    return param_base

def update_parameters(yaml_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    retval: List[Dict[str, Any]] = []
    seen_rest_api_names: Set[str] = set()
    for param in yaml_data["parameters"]:
        if param["language"]["default"]["name"] == "$host":
            continue
        if param["language"]["default"]["serializedName"] not in seen_rest_api_names:
            updated_param = update_parameter(param, "Method")
            retval.append(updated_param)
            seen_rest_api_names.add(updated_param["restApiName"])

    # now we handle content type and accept headers.
    # We only care about the content types on the body parameter itself,
    # so ignoring the different content types for now
    for request in yaml_data.get("requestMediaTypes", {}).values():
        for param in request["parameters"]:
            if param["protocol"]["http"]["in"] != "body":
                if param["language"]["default"]["serializedName"] not in seen_rest_api_names:
                    param = update_parameter(param, "Method")
                    if param["restApiName"] == "Content-Type":
                        # override content type type to string
                        param["type"] = get_type({"type": "string"})  # override to string type
                        param["optional"] = True
                    retval.append(param)
                    seen_rest_api_names.add(param["restApiName"])
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

def _get_default_content_type(content_types: List[str]) -> Optional[str]:
    json_values = [ct for ct in content_types if JSON_REGEXP.match(ct)]
    if json_values:
        if "application/json" in json_values:
            return "application/json"
        return json_values[0]

    xml_values = [ct for ct in content_types if "xml" in ct]
    if xml_values:
        if "application/xml" in xml_values:
            return "application/xml"
        return xml_values[0]

    if "application/octet-stream" in content_types:
        return "application/octet-stream"
    return None

def update_overloads(group_name: str, yaml_data: Dict[str, Any], body_parameter: Optional[Dict[str, Any]]) -> List[Dict[str, Any]]:
    overloads: List[Dict[str, Any]] = []
    if not body_parameter or body_parameter["discriminator"] == "single":
        return overloads

    seen_types: Set[int] = set()

    for yaml_type in body_parameter["contentTypeToType"].values():
        if id(yaml_type) in seen_types:
            continue
        chosen_content_types = [
            k for k, v in body_parameter["contentTypeToType"].items()
            if id(yaml_type) == id(v)
        ]
        new_yaml_data = copy.copy(yaml_data)
        new_yaml_data["requestMediaTypes"] = {k: v for k, v in yaml_data["requestMediaTypes"].items() if k in chosen_content_types}
        default_content_type = _get_default_content_type(chosen_content_types)
        for rmt in new_yaml_data["requestMediaTypes"].values():
            for parameter in rmt["parameters"]:
                if parameter["language"]["default"]["name"] == "content_type" and default_content_type:
                    parameter["clientDefaultValue"] = default_content_type
        seen_types.add(id(yaml_type))
        overloads.append(update_operation(group_name, new_yaml_data, is_overload=True))

    return overloads


def update_operation(group_name: str, yaml_data: Dict[str, Any], *, is_overload: bool = False) -> Dict[str, Any]:
    if not is_overload and yaml_data.get("requestMediaTypes") and any(ct for ct in yaml_data["requestMediaTypes"] if JSON_REGEXP.match(ct)):
        # we add a content overload for all JSON inputs
        # first check if we already have any body param that is a stream input. If so, we skip this step
        yaml_data["requestMediaTypes"]["UNKNOWN"] = copy.deepcopy(list(yaml_data["requestMediaTypes"].values())[0])
        body_param = next(b for b in yaml_data["requestMediaTypes"]["UNKNOWN"]["parameters"] if b["protocol"]["http"]["in"] == "body")
        body_param["schema"] = get_type({"type": "binary"})
        yaml_data["requestMediaTypes"]["UNKNOWN"]["parameters"] = [
            body_param if p["protocol"]["http"]["in"] == "body" else p
            for p in list(yaml_data["requestMediaTypes"].values())[0]["parameters"]
        ]
    body_parameter = update_body_parameter(yaml_data["requestMediaTypes"]) if yaml_data.get("requestMediaTypes") else None
    return {
        "name": yaml_data["language"]["default"]["name"],
        "description": yaml_data["language"]["default"]["description"],
        "url": yaml_data["requests"][0]["protocol"]["http"]["path"],
        "method": yaml_data["requests"][0]["protocol"]["http"]["method"].upper(),
        "parameters": update_parameters(yaml_data),
        "bodyParameter": body_parameter,
        "responses": [update_response(yaml_data, r) for r in yaml_data["responses"]],
        "groupName": group_name,
        "operationType": "basic",
        "overloads": update_overloads(group_name, yaml_data, body_parameter),
        "isOverload": is_overload,
    }

def update_operation_group(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    property_name = yaml_data["language"]["default"]["name"]
    return {
        "propertyName": property_name,
        "className": property_name,
        "operations": [
            update_operation(property_name, o) for o in yaml_data["operations"]
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
                global_parameter["language"]["default"]["description"] = "Service URL."
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
        for types in yaml_data["schemas"].values():
            for t in types:
                update_type(t)
        return {
            "client": self.update_client(yaml_data),
            "operationGroups": [
                update_operation_group(og)
                for og in yaml_data["operationGroups"]
            ],
            "types": list(ORIGINAL_ID_TO_UPDATED_TYPE.values()) + list(KNOWN_TYPES.values())
        }
