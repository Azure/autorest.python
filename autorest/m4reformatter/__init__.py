# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""The modelerfour reformatter autorest plugin.
"""
import re
import copy
import logging
from typing import Callable, Dict, Any, Iterable, List, Optional, Sequence, Set, Tuple

from .. import YamlUpdatePlugin
JSON_REGEXP = re.compile(r"^(application|text)/(.+\+)?json$")
ORIGINAL_ID_TO_UPDATED_TYPE: Dict[int, Dict[str, Any]] = {}

OAUTH_TYPE = "OAuth2"
KEY_TYPE = "Key"

_LOGGER = logging.getLogger(__name__)

# used if we want to get a string / binary type etc
KNOWN_TYPES = {
    "string": {"type": "string"},
    "binary": {"type": "binary"},
    "anydict": {"type": "dict", "elementType": {"type": "any"}},
}

def is_body(yaml_data: Dict[str, Any]) -> bool:
    """Return true if passed in parameter is a body param"""
    return yaml_data["protocol"]["http"]["in"] == "body"

def get_body_parameter(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    """Return a request's body parameter"""
    return next(p for p in yaml_data["parameters"] if is_body(p))

def get_azure_key_credential(key: str) -> Dict[str, Any]:
    retval = {
        "type": KEY_TYPE,
        "policy": {
            "type": "AzureKeyCredentialPolicy",
            "key": key
        }
    }
    update_type(retval)
    return retval

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
        return {"type": "integer", "clientDefaultValue": yaml_data.get("defaultValue")}
    if type_group == "number":
        return {"type": "float", "clientDefaultValue": yaml_data.get("defaultValue")}
    if type_group in ("string", "uuid"):
        return KNOWN_TYPES["string"]
    if type_group == "byte-array":
        return {"type": "base64", "clientDefaultValue": yaml_data.get("defaultValue")}
    if type_group == "binary":
        return KNOWN_TYPES["binary"]
    if type_group == "any":
        return {"type": "any", "clientDefaultValue": yaml_data.get("defaultValue")}
    if type_group == "date-time":
        return {"type": "datetime", "format": yaml_data["format"], "clientDefaultValue": yaml_data.get("defaultValue")}
    if type_group == "duration":
        return {"type": "duration", "clientDefaultValue": yaml_data.get("defaultValue")}
    if type_group == "date":
        return {"type": "date", "clientDefaultValue": yaml_data.get("defaultValue")}
    if type_group == "base64":
        return {"type": "base64", "clientDefaultValue": yaml_data.get("defaultValue")}
    if type_group == "boolean":
        return {"type": "bool", "clientDefaultValue": yaml_data.get("defaultValue")}
    raise ValueError(f"Unknown type group {type_group}")

def update_types(yaml_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    types: List[Dict[str, Any]] = []
    for type in yaml_data:
        if KNOWN_TYPES.get(type["type"]):
            types.append(KNOWN_TYPES[type["type"]])
        else:
            types.append(next(v for v in ORIGINAL_ID_TO_UPDATED_TYPE.values() if id(v) == id(type)))
    retval = {
        "type": "combined",
        "types": types
    }
    ORIGINAL_ID_TO_UPDATED_TYPE[id(retval)] = retval
    return retval

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
    elif type_group in (OAUTH_TYPE, KEY_TYPE):
        updated_type = yaml_data
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
        location = "endpointPath"

    return {
        "optional": not yaml_data.get("required", False),
        "description": yaml_data["language"]["default"]["description"],
        "clientName": client_name or yaml_data["language"]["default"]["name"],
        "clientDefaultValue": yaml_data.get("clientDefaultValue"),
        "location": location,
    }

def update_parameter(yaml_data: Dict[str, Any], *, client_name: Optional[str] = None, in_overload: bool = False, in_overriden: bool = False) -> Dict[str, Any]:
    param_base = update_parameter_base(yaml_data, client_name=client_name)
    type = get_type(yaml_data["schema"])
    if type["type"] == "constant":
        param_base["clientDefaultValue"] = type["value"]
    param_base.update({
        "restApiName": yaml_data["language"]["default"]["serializedName"],
        "type": type,
        "implementation": yaml_data["implementation"],
        "explode": yaml_data["protocol"]["http"].get("explode", False),
        "inOverload": in_overload,
        "skipUrlEncoding": yaml_data.get("extensions", {}).get("x-ms-skip-url-encoding", False),
        "inDocstring": yaml_data.get("inDocstring", True),
        "inOverriden": in_overriden,
    })
    return param_base

def get_all_body_types(yaml_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    seen_body_types = {}
    for schema_request in yaml_data.values():
        body_param = get_body_parameter(schema_request)
        seen_body_types[id(body_param["schema"])] = update_type(body_param["schema"])
    return list(seen_body_types.values())

def _update_body_parameter_helper(
    yaml_data: Dict[str, Any],
    body_param: Dict[str, Any],
    body_type: Dict[str, Any],
) -> Dict[str, Any]:
    param_base = update_parameter_base(body_param)
    body_param = copy.deepcopy(param_base)
    body_param["type"] = body_type
    body_param["contentTypes"] = [
        ct
        for ct, request in yaml_data.items()
        if id(body_type) == id(ORIGINAL_ID_TO_UPDATED_TYPE[id(get_body_parameter(request)["schema"] )])
    ]
    # get default content type
    body_param["defaultContentType"] = _get_default_content_type(body_param["contentTypes"])
    if body_param["type"]["type"] == "constant":
        body_param["clientDefaultValue"] = body_type["value"]
    return body_param

def update_multipart_body_parameter(yaml_data: Dict[str, Any], client_name: str, description: str) -> Dict[str, Any]:
    first_value = list(yaml_data.values())[0]
    entries = [
        _update_body_parameter_helper(yaml_data, p, update_type(p["schema"]))
        for p in first_value["parameters"] if is_body(p)
    ]
    return {
        "optional": not first_value.get("required", False),
        "description": description,
        "clientName": client_name,
        "clientDefaultValue": None,
        "location": "Method",
        "type": KNOWN_TYPES["anydict"],
        "contentTypes": list(yaml_data.keys()),
        "defaultContentType": list(yaml_data.keys())[0], # there should only be one content type for multpart
        "entries": entries,
    }

def update_body_parameter(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    protocol_http = list(yaml_data.values())[0].get("protocol", {}).get("http", {})
    if protocol_http.get("multipart"):
        return update_multipart_body_parameter(
            yaml_data, "files", "Multipart input for files."
        )
    if protocol_http.get("knownMediaType") == "form":
        return update_multipart_body_parameter(
            yaml_data, "data", "Multipart input for form encoded data."
        )
    body_types = get_all_body_types(yaml_data)
    if len(body_types) > 1:
        body_type = update_types(body_types)
    else:
        body_type = body_types[0]
    body_param = next(
        p
        for sr in yaml_data.values()
        for p in sr["parameters"]
        if is_body(p)
    )
    return _update_body_parameter_helper(yaml_data, body_param, body_type)


def update_body_parameter_overload(yaml_data: Dict[str, Any], body_type: Dict[str, Any]) -> Dict[str, Any]:
    """For overloads we already know what body_type we want to go with"""
    body_param = next(
        p
        for sr in yaml_data.values()
        for p in sr["parameters"]
        if is_body(p)
    )
    return _update_body_parameter_helper(yaml_data, body_param, body_type)

def get_body_type_for_description(body_parameter: Dict[str, Any]) -> str:
    if body_parameter["type"]["type"] == "binary":
        return "binary"
    if body_parameter["type"]["type"] == "string":
        return "string"
    return "JSON"

def update_parameters(yaml_data: Dict[str, Any], body_parameter: Optional[Dict[str, Any]], *, in_overload: bool = False, in_overriden: bool = False) -> List[Dict[str, Any]]:
    retval: List[Dict[str, Any]] = []
    seen_rest_api_names: Set[str] = set()
    for param in yaml_data["parameters"]:
        if param["language"]["default"]["name"] == "$host":
            continue
        if param["language"]["default"]["serializedName"] not in seen_rest_api_names:
            if param.get("origin") == "modelerfour:synthesized/api-version":
                param["inDocstring"] = False
            updated_param = update_parameter(param, in_overload=in_overload, in_overriden=in_overriden)
            retval.append(updated_param)
            seen_rest_api_names.add(updated_param["restApiName"])

    # now we handle content type and accept headers.
    # We only care about the content types on the body parameter itself,
    # so ignoring the different content types for now
    if yaml_data.get("requestMediaTypes"):
        sub_requests = yaml_data["requestMediaTypes"].values()
    else:
        sub_requests = yaml_data.get("requests", [])
    for request in sub_requests:
        for param in request.get("parameters", []):
            if not is_body(param):
                if param["language"]["default"]["serializedName"] not in seen_rest_api_names:
                    if param["language"]["default"]["serializedName"] == "Content-Type":
                        # override content type type to string
                        param = copy.deepcopy(param)
                        param["schema"] = KNOWN_TYPES["string"]  # override to string type
                        param["required"] = False
                        description = param["language"]["default"]["description"]
                        if description and description[-1] != ".":
                            description += "."
                        if not (in_overriden or in_overload):
                            param["inDocstring"] = False
                        elif in_overload:
                            description += f" Content type parameter for {get_body_type_for_description(body_parameter)} body."
                        elif not in_overload:
                            content_types = "'" + "', '".join(yaml_data["requestMediaTypes"]) + "'"
                            description += f" Known values are: {content_types}."
                        if not in_overload and not in_overriden:
                            param["clientDefaultValue"] = body_parameter["defaultContentType"]
                        param["language"]["default"]["description"] = description
                    param = update_parameter(param, in_overload=in_overload, in_overriden=in_overriden)
                    retval.append(param)
                    seen_rest_api_names.add(param["restApiName"])
    return retval

def update_response_header(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "restApiName": yaml_data["header"],
        "type": update_type(yaml_data["schema"])
    }

def update_response(
    operation_group_yaml_data: Dict[str, Any],
    yaml_data: Dict[str, Any],
) -> Dict[str, Any]:
    if yaml_data.get("binary"):
        type = KNOWN_TYPES["binary"]
    else:
        type = update_type(yaml_data["schema"]) if yaml_data.get("schema") else None
    return {
        "headers": [update_response_header(h) for h in yaml_data["protocol"]["http"].get("headers", [])],
        "statusCodes": [
            int(code) if code != "default" else "default"
            for code in yaml_data["protocol"]["http"]["statusCodes"]
        ],
        "isError": any(e for e in operation_group_yaml_data.get("exceptions", []) if id(e) == id(yaml_data)),
        "type": type,
        "nullable": yaml_data.get("nullable", False)
    }

def _get_default_content_type(content_types: Iterable[str]) -> Optional[str]:
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
    if not body_parameter:
        return overloads
    body_types = body_parameter["type"].get("types", [])
    if not body_types:
        return overloads
    for body_type in body_types:
        overload = update_overload(group_name, yaml_data, body_type)
        for parameter in overload["parameters"]:
            if parameter["restApiName"] == "Content-Type":
                parameter["clientDefaultValue"] = overload["bodyParameter"]["defaultContentType"]
        overloads.append(overload)
    return overloads

def _update_operation_helper(
    group_name: str,
    yaml_data: Dict[str, Any],
    body_parameter: Optional[Dict[str, Any]],
    *,
    is_overload: bool = False
) -> Dict[str, Any]:
    in_overriden = body_parameter["type"]["type"] == "combined" if body_parameter else False
    return {
        "name": yaml_data["language"]["default"]["name"],
        "description": yaml_data["language"]["default"]["description"],
        "url": yaml_data["requests"][0]["protocol"]["http"]["path"],
        "method": yaml_data["requests"][0]["protocol"]["http"]["method"].upper(),
        "parameters": update_parameters(yaml_data, body_parameter, in_overload=is_overload, in_overriden=in_overriden),
        "bodyParameter": body_parameter,
        "responses": [update_response(yaml_data, r) for r in yaml_data["responses"]],
        "groupName": group_name,
        "operationType": "basic",
        "discriminator": "operation",
        "isOverload": is_overload,
    }

def update_operation(group_name: str, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    body_parameter = update_body_parameter(yaml_data["requestMediaTypes"]) if yaml_data.get("requestMediaTypes") else None
    if (
        body_parameter and
        body_parameter["type"]["type"] != "combined" and
        yaml_data.get("requestMediaTypes") and
        any(ct for ct in yaml_data["requestMediaTypes"] if JSON_REGEXP.match(ct)) and
        body_parameter["type"]["type"] in ("model", "dict", "list")
    ):
        combined_type = update_types([body_parameter["type"], KNOWN_TYPES["binary"]])
        body_parameter["type"] = combined_type
        body_parameter["contentTypes"] = []
        # get default content type
        body_parameter["defaultContentType"] = None
    operation = _update_operation_helper(group_name, yaml_data, body_parameter)
    operation["overloads"] = update_overloads(group_name, yaml_data, body_parameter)
    return operation

def update_overload(group_name: str, yaml_data: Dict[str, Any], body_type: Dict[str, Any]) -> Dict[str, Any]:
    body_parameter = update_body_parameter_overload(yaml_data["requestMediaTypes"], body_type)
    return _update_operation_helper(group_name, yaml_data, body_parameter, is_overload=True)

def add_lro_information(operation: Dict[str, Any], yaml_data: Dict[str, Any]) -> None:
    operation["discriminator"] = "lro"
    extensions = yaml_data["extensions"]
    operation["lroOptions"] = extensions.get("x-ms-long-running-operation-options")
    operation["pollerSync"] = extensions.get("x-python-custom-poller-sync")
    operation["pollerAsync"] = extensions.get("x-python-custom-poller-async")
    operation["pollingMethodSync"] = extensions.get("x-python-custom-default-polling-method-sync")
    operation["pollingMethodAsync"] = extensions.get("x-python-custom-default-polling-method-async")


def update_lro_operation(group_name: str, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    base_operation = update_operation(group_name, yaml_data)
    add_lro_information(base_operation, yaml_data)
    for overload in base_operation["overloads"]:
        add_lro_information(overload, yaml_data)
    return base_operation

def add_paging_information(group_name: str, operation: Dict[str, Any], yaml_data: Dict[str, Any]) -> None:
    operation["discriminator"] = "paging"
    operation["itemName"] = yaml_data["extensions"]["x-ms-pageable"].get("itemName", "value")
    operation["continuationTokenName"] = yaml_data["extensions"]["x-ms-pageable"].get("nextLinkName")
    if yaml_data["language"]["default"]["paging"].get("nextLinkOperation"):
        operation["nextOperation"] = update_operation(
            group_name=group_name,
            yaml_data=yaml_data["language"]["default"]["paging"]["nextLinkOperation"],
        )
    extensions = yaml_data["extensions"]
    operation["pagerSync"] = extensions.get("x-python-custom-pager-sync")
    operation["pagerAsync"] = extensions.get("x-python-custom-pager-async")


def update_paging_operation(group_name: str, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    base_operation = update_operation(group_name, yaml_data)
    add_paging_information(group_name, base_operation, yaml_data)
    return base_operation

def update_lro_paging_operation(group_name: str, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    operation = update_lro_operation(group_name, yaml_data)
    add_paging_information(group_name, operation, yaml_data)
    operation["discriminator"] = "lropaging"
    return operation

def get_operation_creator(yaml_data: Dict[str, Any]) -> Callable[[str, Dict[str, Any]], Dict[str, Any]]:
    lro_operation = yaml_data.get("extensions", {}).get("x-ms-long-running-operation")
    paging_operation = yaml_data.get("extensions", {}).get("x-ms-pageable")
    if lro_operation and paging_operation:
        return update_lro_paging_operation
    if lro_operation:
        return update_lro_operation
    if paging_operation:
        return update_paging_operation
    return update_operation

def filter_out_paging_next_operation(yaml_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    next_operations: Set[str] = set()
    for operation in yaml_data:
        next_operation = operation.get("nextOperation")
        if not next_operation:
            continue
        next_operations.add(next_operation["name"])
    return [
        o for o in yaml_data
        if o["name"] not in next_operations
    ]

def update_operation_group(yaml_data: Dict[str, Any]) -> Dict[str, Any]:
    property_name = yaml_data["language"]["default"]["name"]
    return {
        "propertyName": property_name,
        "className": property_name,
        "operations": filter_out_paging_next_operation([
            get_operation_creator(o)(property_name, o) for o in yaml_data["operations"]
        ])
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

    @property
    def azure_arm(self) -> bool:
        return bool(self._autorestapi.get_boolean_value("azure-arm"))

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
            global_params.append(update_parameter(global_parameter, client_name=client_name))
        return global_params

    def get_token_credential(self, credential_scopes: List[str]) -> Dict[str, Any]:
        retval = {
            "type": OAUTH_TYPE,
            "policy": {
                "type": "ARMChallengeAuthenticationPolicy" if self.azure_arm else "BearerTokenCredentialPolicy",
                "credentialScopes": credential_scopes
            }
        }
        update_type(retval)
        return retval

    def update_credential_from_security(self, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
        retval: Dict[str, Any] = {}
        for scheme in yaml_data.get("schemes", []):
            if scheme["type"] == OAUTH_TYPE:
                # TokenCredential
                retval = self.get_token_credential(scheme["scopes"])
            elif scheme["type"] == KEY_TYPE:
                retval = get_azure_key_credential(scheme["name"])
        return retval

    def get_credential_scopes_from_flags(self, auth_policy: str) -> List[str]:
        if self.azure_arm:
            return ["https://management.azure.com/.default"]
        credential_scopes = (self._autorestapi.get_value("credential-scopes") or []).split(",")
        if (
            self._autorestapi.get_boolean_value("credential-scopes", False)
            and not credential_scopes
        ):
            raise ValueError(
                "--credential-scopes takes a list of scopes in comma separated format. "
                "For example: --credential-scopes=https://cognitiveservices.azure.com/.default"
            )
        if not credential_scopes:
            _LOGGER.warning(
                "You have default credential policy %s "
                "but not the --credential-scopes flag set while generating non-management plane code. "
                "This is not recommend because it forces the customer to pass credential scopes "
                "through kwargs if they want to authenticate.",
                auth_policy,
            )
            credential_scopes = []
        return credential_scopes

    def update_credential_from_flags(self) -> Dict[str, Any]:
        default_auth_policy = "ARMChallengeAuthenticationPolicy" if self.azure_arm else "BearerTokenCredentialPolicy"
        auth_policy = self._autorestapi.get_value("credential-default-policy-type") or default_auth_policy
        credential_scopes = self.get_credential_scopes_from_flags(auth_policy)
        key = self._autorestapi.get_value("credential-key-header-name")
        if auth_policy.lower() in ("armchallengeauthenticationpolicy", "bearertokencredentialpolicy"):
            if key:
                raise ValueError(
                    "You have passed in a credential key header name with default credential policy type "
                    f"{auth_policy}. This is not allowed, since credential key header "
                    "name is tied with AzureKeyCredentialPolicy. Instead, with this policy it is recommend you "
                    "pass in --credential-scopes."
                )
            return self.get_token_credential(credential_scopes)
        # Otherwise you have AzureKeyCredentialPolicy
        if credential_scopes:
            raise ValueError(
                "You have passed in credential scopes with default credential policy type "
                "AzureKeyCredentialPolicy. This is not allowed, since credential scopes is tied with "
                f"{default_auth_policy}. Instead, with this policy "
                "you must pass in --credential-key-header-name."
            )
        if not key:
            key = "api-key"
            _LOGGER.info(
                "Defaulting the AzureKeyCredentialPolicy header's name to 'api-key'"
            )
        return get_azure_key_credential(key)

    def update_credential(self, yaml_data: Dict[str, Any], parameters: List[Dict[str, Any]]) -> None:
        # then override with credential flags
        credential = self._autorestapi.get_boolean_value(
            "add-credentials", False
        ) or self._autorestapi.get_boolean_value("add-credential", False) or self.azure_arm
        if credential:
            credential_type = self.update_credential_from_flags()
        else:
            credential_type = self.update_credential_from_security(yaml_data)
        if not credential_type:
            return
        credential = {
            "type": credential_type,
            "optional": False,
            "description": "Credential needed for the client to connect to Azure.",
            "clientName": "credential",
            "location": "other",
            "restApiName": "credential",
            "implementation": "Client",
            "skipUrlEncoding": True,
            "inOverload": False,
        }
        if (
            self._autorestapi.get_boolean_value("version-tolerant")
            or self._autorestapi.get_boolean_value("low-level-client")
        ):
            parameters.append(credential)
        else:
            parameters.insert(0, credential)


    def update_client(self, yaml_data: Dict[str, Any]) -> Dict[str, Any]:
        parameters = self.update_global_parameters(yaml_data["globalParameters"])
        self.update_credential(yaml_data.get("security", {}), parameters)
        return {
            "name": yaml_data["language"]["default"]["name"],
            "description": yaml_data["info"]["description"],
            "parameters": parameters,
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
