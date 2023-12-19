import {
  SdkBasicServiceMethod,
  SdkClientType,
  SdkContext,
  SdkCredentialParameter,
  SdkEndpointParameter,
  SdkLroPagingServiceMethod,
  SdkLroServiceMethod,
  SdkMethodParameter,
  SdkPagingServiceMethod,
  SdkServiceMethod,
  SdkServiceOperation,
} from "@azure-tools/typespec-client-generator-core";
import { KnownTypes, getType, simpleTypesMap, typesMap } from "./types.js";
import { emitParamBase, getImplementation, removeUnderscoresFromNamespace } from "./utils.js";
import { emitBasicHttpMethod, emitLroHttpMethod, emitLroPagingHttpMethod, emitPagingHttpMethod } from "./http.js";
import { PythonSdkContext } from "./lib.js";

function emitBasicMethod<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  client: SdkClientType<TServiceOperation>,
  method: SdkBasicServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitBasicHttpMethod(context, client, method, operationGroupName);
    default:
      throw new Error("We only support HTTP operations right now");
  }
}

function emitLroMethod<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  client: SdkClientType<TServiceOperation>,
  method: SdkLroServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitLroHttpMethod(context, client, method, operationGroupName);
    default:
      throw new Error("We only support HTTP operations right now");
  }
}

function emitPagingMethod<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  client: SdkClientType<TServiceOperation>,
  method: SdkPagingServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitPagingHttpMethod(context, client, method, operationGroupName);
    default:
      throw new Error("We only support HTTP operations right now");
  }
}

function emitLroPagingMethod<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  client: SdkClientType<TServiceOperation>,
  method: SdkLroPagingServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitLroPagingHttpMethod(context, client, method, operationGroupName);
    default:
      throw new Error("We only support HTTP operations right now");
  }
}

function emitMethodParameter<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  client: SdkClientType<TServiceOperation>,
  parameter: SdkEndpointParameter | SdkCredentialParameter | SdkMethodParameter,
): Record<string, any> {
  const base = {
    ...emitParamBase(context, parameter),
    implementation: getImplementation(parameter),
    clientDefaultValue: parameter.clientDefaultValue,
    location: parameter.kind,
  };
  if (parameter.kind === "endpoint") {
    const endpointParameter = {
      ...base,
      skipUrlEncoding: !parameter.urlEncode,
      wireName: client.hasParameterizedEndpoint ? parameter.nameInClient : "$host",
      location: client.hasParameterizedEndpoint ? "endpointPath" : "path",
    };
    if (client.hasParameterizedEndpoint) {
      if (!context.__endpointPathParameters[client.name]) {
        context.__endpointPathParameters[client.name] = [];
      }
      context.__endpointPathParameters[client.name].push(endpointParameter);
    }
    return endpointParameter;
  }
  if (parameter.isApiVersionParam) {
    return {
      ...base,
      location: "query",
      wireName: "api-version",
    };
  }
  return base;
}

function emitMethod<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  client: SdkClientType<TServiceOperation>,
  method: SdkServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  switch (method.kind) {
    case "basic":
      return emitBasicMethod(context, client, method, operationGroupName);
    case "lro":
      return emitLroMethod(context, client, method, operationGroupName);
    case "paging":
      return emitPagingMethod(context, client, method, operationGroupName);
    default:
      return emitLroPagingMethod(context, client, method, operationGroupName);
  }
}

function emitOperationGroups<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  client: SdkClientType<TServiceOperation>,
  prefix: string,
): Record<string, any>[] | undefined {
  const operationGroups: Record<string, any>[] = [];

  for (const method of client.methods) {
    if (method.kind === "clientaccessor") {
      const operationGroup = method.response;
      const name = prefix + operationGroup.name;
      let operations: Record<string, any>[] = [];
      for (const method of operationGroup.methods) {
        if (method.kind === "clientaccessor") continue;
        operations = operations.concat(emitMethod(context, client, method, operationGroup.name));
      }
      operationGroups.push({
        name: name,
        className: name,
        propertyName: operationGroup.name,
        operations: operations,
        operationGroups: emitOperationGroups(context, operationGroup, name),
      });
    }
  }

  // root client should deal with mixin operation group
  if (prefix === "") {
    let operations: Record<string, any>[] = [];
    for (const method of client.methods) {
      if (method.kind === "clientaccessor") continue;
      operations = operations.concat(emitMethod(context, client, method, ""));
    }
    if (operations.length > 0) {
      operationGroups.push({
        name: "",
        className: "",
        propertyName: "",
        operations: operations,
      });
    }
  }

  return operationGroups.length > 0 ? operationGroups : undefined;
}

function emitClient<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  client: SdkClientType<TServiceOperation>,
): Record<string, any> {
  return {
    name: client.name,
    description: client.description ?? "",
    parameters: client.initialization?.properties.map((x) => emitMethodParameter(context, client, x)),
    operationGroups: emitOperationGroups(context, client, ""),
    url: client.endpoint,
    apiVersions: client.apiVersions,
    arm: client.arm,
  };
}

export function emitCodeModel<TServiceOperation extends SdkServiceOperation>(
  sdkContext: PythonSdkContext<TServiceOperation>,
) {
  // Get types
  const sdkPackage = sdkContext.sdkPackage;
  const codeModel: Record<string, any> = {
    namespace: removeUnderscoresFromNamespace(sdkPackage.rootNamespace).toLowerCase(),
    clients: [],
    subnamespaceToClients: {},
  };
  for (const model of sdkPackage.models) {
    if (model.name !== "") {
      getType(sdkContext, model);
    }
  }
  for (const sdkEnum of sdkPackage.enums) {
    getType(sdkContext, sdkEnum);
  }
  for (const client of sdkPackage.clients) {
    if (client.initialization) {
      // right now to keep python changes minimal, we're just supporting top level clients
      codeModel["clients"].push(emitClient(sdkContext, client));
    }
    if (client.nameSpace === sdkPackage.rootNamespace) {
    } else {
      codeModel["subnamespaceToClients"][client.nameSpace] = emitClient(sdkContext, client);
    }
  }
  codeModel["types"] = [...typesMap.values(), ...Object.values(KnownTypes), ...simpleTypesMap.values()];
  return codeModel;
}
