import {
  SdkBasicServiceMethod,
  SdkBodyParameter,
  SdkContext,
  SdkHeaderParameter,
  SdkHttpOperation,
  SdkHttpResponse,
  SdkLroPagingServiceMethod,
  SdkLroServiceMethod,
  SdkPagingServiceMethod,
  SdkPathParameter,
  SdkQueryParameter,
  SdkServiceResponseHeader,
} from "@azure-tools/typespec-client-generator-core";
import {
  camelToSnakeCase,
  capitalize,
  emitParamBase,
  getDelimeterAndExplode,
  getDescriptionAndSummary,
  getImplementation,
  isAbstract,
  isAzureCoreModel,
} from "./utils.js";
import { KnownTypes, getSimpleTypeResult, getType } from "./types.js";

export function emitBasicHttpMethod(
  context: SdkContext<SdkHttpOperation>,
  method: SdkBasicServiceMethod<SdkHttpOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  return [
    {
      ...emitHttpOperation(context, method.operation, operationGroupName),
      abstract: isAbstract(method),
      internal: method.access === "internal",
      name: camelToSnakeCase(method.name),
      description: getDescriptionAndSummary(method).description,
      summary: getDescriptionAndSummary(method).summary,
    },
  ];
}

function emitInitialLroHttpMethod(
  context: SdkContext<SdkHttpOperation>,
  method: SdkLroServiceMethod<SdkHttpOperation> | SdkLroPagingServiceMethod<SdkHttpOperation>,
  operationGroupName: string,
): Record<string, any> {
  const initialOperation = emitHttpOperation(context, method.operation, operationGroupName);
  return {
    ...initialOperation,
    name: `_${camelToSnakeCase(method.name)}_intial`,
    isLroInitialOperation: true,
    wantTracing: false,
    exposeStreamKeyword: false,
    responses: initialOperation.responses.forEach((resp: Record<string, any>) => {
      if (resp.type) {
        resp.type = KnownTypes.anyObject;
      }
    }),
    description: getDescriptionAndSummary(method).description,
    summary: getDescriptionAndSummary(method).summary,
  };
}

function addLroInformation(
  context: SdkContext<SdkHttpOperation>,
  method: SdkLroServiceMethod<SdkHttpOperation> | SdkLroPagingServiceMethod<SdkHttpOperation>,
  opreationGroupName: string,
) {
  return {
    ...emitHttpOperation(context, method.operation, opreationGroupName),
    name: camelToSnakeCase(method.name),
    discriminator: "lro",
    initialOperation: emitInitialLroHttpMethod(context, method, opreationGroupName),
    exposeStreamKeyword: false,
    description: getDescriptionAndSummary(method).description,
    summary: getDescriptionAndSummary(method).summary,
  };
}

function addPagingInformation(
  context: SdkContext<SdkHttpOperation>,
  method: SdkPagingServiceMethod<SdkHttpOperation> | SdkLroPagingServiceMethod<SdkHttpOperation>,
  operationGroupName: string,
) {
  for (const response of Object.values(method.operation.responses)) {
    if (response.type && !isAzureCoreModel(response.type)) {
      getType(context, response.type)["pageResultModel"] = true;
    }
  }
  const itemType = getType(context, method.response.type!);
  const base = emitHttpOperation(context, method.operation, operationGroupName);
  base.responses.forEach((resp: Record<string, any>) => {
    resp.type = itemType;
  });
  return {
    ...base,
    name: camelToSnakeCase(method.name),
    discriminator: "paging",
    exposeStreamKeyword: false,
    itemName: method.response.responsePath,
    continuationTokenName: method.nextLinkLogicalPath?.join("."),
    itemType,
    description: getDescriptionAndSummary(method).description,
    summary: getDescriptionAndSummary(method).summary,
  };
}

export function emitLroHttpMethod(
  context: SdkContext<SdkHttpOperation>,
  method: SdkLroServiceMethod<SdkHttpOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  const lroMethod = addLroInformation(context, method, operationGroupName);
  return [lroMethod, lroMethod.initialOperation];
}

export function emitPagingHttpMethod(
  context: SdkContext<SdkHttpOperation>,
  method: SdkPagingServiceMethod<SdkHttpOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  const pagingMethod = addPagingInformation(context, method, operationGroupName);
  return [pagingMethod];
}

export function emitLroPagingHttpMethod(
  context: SdkContext<SdkHttpOperation>,
  method: SdkLroPagingServiceMethod<SdkHttpOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  const pagingMethod = addPagingInformation(context, method, operationGroupName);
  const lroMethod = addLroInformation(context, method, operationGroupName);
  return [lroMethod.initialOperation, pagingMethod, lroMethod];
}

function emitHttpOperation(
  context: SdkContext<SdkHttpOperation>,
  operation: SdkHttpOperation,
  operationGroupName: string,
): Record<string, any> {
  const responses: Record<string, any>[] = [];
  const exceptions: Record<string, any>[] = [];
  for (const [statusCodes, response] of Object.entries(operation.responses)) {
    responses.push(emitHttpResponse(context, statusCodes, response)!);
  }
  for (const [statusCodes, exception] of Object.entries(operation.exceptions)) {
    exceptions.push(emitHttpResponse(context, statusCodes, exception)!);
  }
  const result = {
    url: operation.path,
    method: operation.verb.toUpperCase(),
    parameters: emitHttpParameters(context, operation),
    bodyParameter: emitHttpBodyParameter(context, operation.bodyParams),
    responses,
    exceptions,
    groupName: operationGroupName,
    addedOn: "",
    discriminator: "basic",
    isOverload: false,
    overloads: [],
    apiVersions: [],
    wantTracing: true,
    exposeStreamKeyword: true,
  };
  if (result.bodyParameter?.type.type === "model" && result.bodyParameter?.type.name === "") {
    result.bodyParameter.type.name = capitalize(operation.__raw.operation.name) + "Request";
  }
  if (result.bodyParameter?.type.type === "model" && result.bodyParameter.type.base === "json") {
    result.bodyParameter["propertyToParameterName"] = {};
    result.bodyParameter["defaultToUnsetSentinel"] = true;
    for (const property of result.bodyParameter.type.properties) {
        result.bodyParameter["propertyToParameterName"][property["wireName"]] = property["clientName"];
        result.parameters.push(emitFlattenedParameter(result.bodyParameter, property));
    }
  }
  return result;
}

function emitFlattenedParameter(
    bodyParameter: Record<string, any>,
    property: Record<string, any>,
): Record<string, any> {
    return {
        checkClientInput: false,
        clientDefaultValue: null,
        clientName: property.clientName,
        delimiter: null,
        description: property.description,
        implementation: "Method",
        inDocstring: true,
        inFlattenedBody: true,
        inOverload: false,
        inOverriden: false,
        isApiVersion: bodyParameter["isApiVersion"],
        location: "other",
        optional: property["optional"],
        wireName: null,
        skipUrlEncoding: false,
        type: property["type"],
        defaultToUnsetSentinel: true,
    };
}

function emitHttpPathParameter(context: SdkContext<SdkHttpOperation>, parameter: SdkPathParameter) {
  const base = emitParamBase(context, parameter);
  return {
    ...base,
    wireName: parameter.serializedName,
    location: parameter.kind,
    implementation: getImplementation(parameter),
    clientDefaultValue: parameter.clientDefaultValue,
    skipUrlEncoding: parameter.urlEncode === false,
  };
}
function emitHttpHeaderParameter(
  context: SdkContext<SdkHttpOperation>,
  parameter: SdkHeaderParameter,
): Record<string, any> {
  const base = emitParamBase(context, parameter);
  const [delimiter, explode] = getDelimeterAndExplode(parameter);
  if (parameter.serializedName === "Accept") {
    base.type = getSimpleTypeResult({ type: "constant", value: parameter.clientDefaultValue, valueType: base.type });
  }
  return {
    ...base,
    wireName: parameter.serializedName,
    location: parameter.kind,
    implementation: getImplementation(parameter),
    delimiter,
    explode,
    clientDefaultValue: parameter.clientDefaultValue,
  };
}

function emitHttpQueryParameter(
  context: SdkContext<SdkHttpOperation>,
  parameter: SdkQueryParameter,
): Record<string, any> {
  const base = emitParamBase(context, parameter);
  const [delimiter, explode] = getDelimeterAndExplode(parameter);
  return {
    ...base,
    wireName: parameter.serializedName,
    location: parameter.kind,
    implementation: getImplementation(parameter),
    delimiter,
    explode,
    clientDefaultValue: parameter.clientDefaultValue,
  };
}

function emitHttpParameters(context: SdkContext<SdkHttpOperation>, operation: SdkHttpOperation): Record<string, any>[] {
  const parameters: Record<string, any>[] = [];
  for (const queryParam of operation.queryParams) {
    parameters.push(emitHttpQueryParameter(context, queryParam));
  }
  for (const headerParam of operation.headerParams) {
    parameters.push(emitHttpHeaderParameter(context, headerParam));
  }
  for (const pathParam of operation.pathParams) {
    parameters.push(emitHttpPathParameter(context, pathParam));
  }
  return parameters;
}

function emitHttpBodyParameter(
  context: SdkContext<SdkHttpOperation>,
  bodyParams: SdkBodyParameter[],
): Record<string, any> | undefined {
  if (bodyParams.length === 0) return undefined;
  const bodyParam = bodyParams[0];
  return {
    ...emitParamBase(context, bodyParam, true),
    contentTypes: bodyParam.contentTypes,
    location: bodyParam.kind,
    wireName: bodyParam.nameInClient,
    implementation: getImplementation(bodyParam),
    clientDefaultValue: bodyParam.clientDefaultValue,
    defaultContentType: bodyParam.defaultContentType,
  };
}

function emitHttpResponse(
  context: SdkContext<SdkHttpOperation>,
  statusCodes: string,
  response: SdkHttpResponse,
): Record<string, any> | undefined {
  if (!response) return undefined;
  return {
    headers: response.headers.map((x) => emitHttpResponseHeader(context, x)),
    statusCodes: statusCodes === "*" ? ["default"] : statusCodes.split(",").map((x) => parseInt(x)),
    discriminator: "basic",
    type: response.type && !isAzureCoreModel(response.type) ? getType(context, response.type) : undefined,
    contentTypes: "",
  };
}

function emitHttpResponseHeader(
  context: SdkContext<SdkHttpOperation>,
  header: SdkServiceResponseHeader,
): Record<string, any> {
  return {
    type: getType(context, header.type),
    wireName: header.serializedName,
  };
}
