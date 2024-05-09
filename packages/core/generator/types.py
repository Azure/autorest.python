# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from __future__ import annotations

from ast import TypeVar
from typing import Any, Dict, List, Literal, Optional, TypedDict, Union, Generic

class Options(TypedDict):
    """Options for the plugin."""
    yamlFile: str
    outputDir: str
    modelsMode: Literal["msrest", "dpg", False]
    versionTolerant: bool # am I a version tolerant generation?
    lowLevelClient: bool # am I a low level client generation?


class YamlData(TypedDict):
    """YAML data. Represents the structure of the yaml input our plugin takes in as input"""
    types: List[YamlSdkType]
    namespace: str
    clients: List[YamlClient]
    subnamespaceToClients: Dict[str, List[YamlClient]]
    crossLanguagePackageId: str


class YamlType(TypedDict):
    """Represents any object in the yaml dictionary. Is the base clase for clients, types, etc."""
    ...

class YamlClient(YamlType):
    name: str

class YamlSdkType(YamlType):
    ...

class YamlBuiltInType(YamlSdkType):
    kind: Literal["int"] | Literal["float"] | Literal["str"] | Literal["bool"] | Literal["bytes"] | Literal["any"] | Literal["decimal"]
    encode: str

class YamlConstantType(YamlSdkType):
    kind: Literal["constant"]
    value: str | int | float

class YamlCredentialType(YamlSdkType):
    kind: Literal["credential"]
    scheme: YamlBearerAuth | YamlApiKeyAuth

class YamlBearerAuth(YamlSdkType):
    kind: Literal["bearer"]
    type: Literal["http"]

class YamlApiKeyAuth(YamlSdkType):
    kind: Literal["apiKey"]
    location: Literal["header"] | Literal["query"]
    name: str


class YamlDatetimeType(YamlSdkType):
    kind: Literal["utcDateTime"]
    wireType: YamlBuiltInType

class YamlDictionaryType(YamlSdkType):
    kind: Literal["dictionary"]
    valueType: YamlSdkType

class YamlDurationType(YamlSdkType):
    kind: Literal["duration"]
    encode: Literal["ISO8601"] | Literal["seconds"]
    wireType: YamlBuiltInType

class YamlEndpointType(YamlSdkType):
    kind: Literal["endpoint"]
    serverUrl: str
    templateArguments: List[YamlPathParameter]

class YamlEnumType(YamlSdkType):
    kind: Literal["enum"]
    values: List[YamlEnumValueType]
    valueType: YamlSdkType
    crossLanguageDefinitionId: str

class YamlEnumValueType(YamlSdkType):
    kind: Literal["enumValue"]
    name: str
    value: str | int | float
    enumType: YamlEnumType

class YamlListType(YamlSdkType):
    kind: Literal["list"]
    valueType: YamlSdkType

class YamlModelType(YamlSdkType):
    kind: Literal["model"]
    name: str
    properties: List[YamlPropertyType]
    crossLanguageDefinitionId: str

class YamlUnionType(YamlSdkType):
    kind: Literal["union"]
    name: str

class YamlPropertyTypeBase(YamlType):
    name: str
    type: YamlSdkType
    description: str
    clientDefaultValue: Optional[Any]
    optional: bool
    onClient: bool

class YamlBodyModelPropertyType(YamlPropertyTypeBase):
    kind: Literal["property"]

class YamlEndpointParameter(YamlPropertyTypeBase):
    kind: Literal["endpoint"]
    urlEncode: bool
    onClient: Literal[True] # type: ignore
    type: YamlEndpointType # type: ignore

class YamlCredentialParameter(YamlPropertyTypeBase):
    kind: Literal["credential"]
    type: YamlCredentialType | YamlUnionType # type: ignore
    onClient: Literal[True] # type: ignore

class YamlMethodParameter(YamlPropertyTypeBase):
    kind: Literal["method"]

CollectionFormat = Literal["csv", "ssv", "tsv", "pipes", "multi"]

class YamlBodyParameter(YamlPropertyTypeBase):
    kind: Literal["body"]
    contentTypes: List[str]
    defaultContentType: str

class YamlHeaderParameter(YamlPropertyTypeBase):
    kind: Literal["header"]
    collectionFormat: CollectionFormat
    serializedName: str

class YamlPathParameter(YamlPropertyTypeBase):
    kind: Literal["path"]
    urlEncode: bool
    serializedName: str

class YamlQueryParameter(YamlPropertyTypeBase):
    kind: Literal["query"]
    collectionFormat: CollectionFormat
    serializedName: str

YamlPropertyType = Union[
    YamlBodyModelPropertyType,
    YamlEndpointParameter,
    YamlCredentialParameter,
    YamlHeaderParameter,
    YamlPathParameter,
    YamlQueryParameter,
    YamlBodyParameter,
    YamlMethodParameter
]

class _YamlServiceMethodBase(TypedDict):
    name: str
    access: Literal["public", "internal"]
    parameters: List[YamlMethodParameter]
    description: str
    crossLanguageDefinitionId: str
    response: YamlMethodResponse
    exception: Optional[YamlMethodResponse]

class YamlMethodResponse(TypedDict):
    kind: Literal["method"]
    type: Optional[YamlSdkType]
    resultPath: Optional[str]

class YamlBasicServiceMethod(_YamlServiceMethodBase):
    kind: Literal["basic"]
    operation: YamlHttpOperation

class _YamlPagingServiceMethodOptions(TypedDict):
    nextLinkPath: Optional[str]
    nextLinkOperation: Optional[YamlHttpOperation]

class YamlPagingServiceMethod(_YamlServiceMethodBase, _YamlPagingServiceMethodOptions):
    kind: Literal["paging"]

class YamlLroServiceMethod(_YamlServiceMethodBase):
    kind: Literal["lro"]

class YamlLroPagingServiceMethod(_YamlServiceMethodBase, _YamlPagingServiceMethodOptions):
    kind: Literal["lropaging"]

class YamlHttpOperation(TypedDict):
    kind: Literal["http"]
    verb: Literal["get", "put", "post", "patch", "delete", "head"]
    path: str
    parameters: List[YamlPathParameter | YamlQueryParameter | YamlHeaderParameter]
    bodyParam: Optional[YamlBodyParameter]
    responses: Dict[Literal["*"] | int, YamlHttpResponse]
    exceptions: Dict[Literal["*"] | int, YamlHttpResponse]

class YamlHttpResponse(TypedDict):
    kind: Literal["http"]
    contentTypes: Optional[List[str]]
    defaultContentType: Optional[str]
    headers: List[YamlHttpResponseHeaders]
    apiVersions: List[str]

class YamlHttpResponseHeaders(TypedDict):
    serializedName: str
    type: YamlSdkType
    description: str
