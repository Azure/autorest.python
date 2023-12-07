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

function emitBasicMethod<TServiceOperation extends SdkServiceOperation>(
  context: SdkContext<TServiceOperation>,
  method: SdkBasicServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitBasicHttpMethod(context, method, operationGroupName);
    default:
      throw new Error("We only support HTTP operations right now");
  }
}

function emitLroMethod<TServiceOperation extends SdkServiceOperation>(
  context: SdkContext<TServiceOperation>,
  method: SdkLroServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitLroHttpMethod(context, method, operationGroupName);
    default:
      throw new Error("We only support HTTP operations right now");
  }
}

function emitPagingMethod<TServiceOperation extends SdkServiceOperation>(
  context: SdkContext<TServiceOperation>,
  method: SdkPagingServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitPagingHttpMethod(context, method, operationGroupName);
    default:
      throw new Error("We only support HTTP operations right now");
  }
}

function emitLroPagingMethod<TServiceOperation extends SdkServiceOperation>(
  context: SdkContext<TServiceOperation>,
  method: SdkLroPagingServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitLroPagingHttpMethod(context, method, operationGroupName);
    default:
      throw new Error("We only support HTTP operations right now");
  }
}

function emitMethodParameter(
  context: SdkContext,
  parameter: SdkEndpointParameter | SdkCredentialParameter | SdkMethodParameter,
): Record<string, any> {
  const base = {
    ...emitParamBase(context, parameter),
    implementation: getImplementation(parameter),
    type: getType(context, parameter.type),
    clientDefaultValue: parameter.clientDefaultValue,
    location: parameter.kind,
  };
  if (parameter.kind === "endpoint") {
    return {
      ...base,
      skipUrlEncoding: !parameter.urlEncode,
      wireName: parameter.serializedName,
      location: "endpointPath",
    };
  }
  return base;
}

function emitMethod<TServiceOperation extends SdkServiceOperation>(
  context: SdkContext<TServiceOperation>,
  method: SdkServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  switch (method.kind) {
    case "basic":
      return emitBasicMethod(context, method, operationGroupName);
    case "lro":
      return emitLroMethod(context, method, operationGroupName);
    case "paging":
      return emitPagingMethod(context, method, operationGroupName);
    default:
      return emitLroPagingMethod(context, method, operationGroupName);
  }
}

function emitOperationGroups<TServiceOperation extends SdkServiceOperation>(
  context: SdkContext<TServiceOperation>,
  client: SdkClientType<TServiceOperation>,
): Record<string, any>[] {
  const operationGroups: Record<string, any>[] = [];
  const clientOperations: Map<string, Record<string, any>> = new Map<string, Record<string, any>>();
  for (const method of client.methods) {
    if (method.kind === "clientaccessor") {
      // Also currently assume subclient is operationGroup to keep code changes minimal
      const operationGroup = method.response;
      let operations: Record<string, any>[] = [];
      for (const method of operationGroup.methods) { 
        if (method.kind === "clientaccessor") continue; // skipping for now since we don't do sub-sub clients
        operations = operations.concat(emitMethod(context, method, operationGroup.name));
      }
      operationGroups.push({
        className: operationGroup.name,
        propertyName: operationGroup.name,
        operations: operations,
      });
    } else {
      const groupName = context.arm ? method.operation.__raw.operation.interface?.name ?? "" : "";
      const emittedOperation = emitMethod(context, method, groupName);
      if (!clientOperations.has(groupName)) {
        clientOperations.set(groupName, {
          className: groupName,
          propertyName: groupName,
          operations: [],
        });
      }
      const og = clientOperations.get(groupName) as Record<string, any>;
      og.operations = og.operations.concat(emittedOperation);
    }
  }
  for (const value of clientOperations.values()) {
    operationGroups.push(value);
  }
  return operationGroups;
}

function emitClient<TServiceOperation extends SdkServiceOperation>(
  context: SdkContext<TServiceOperation>,
  client: SdkClientType<TServiceOperation>,
): Record<string, any> {
  return {
    name: client.name,
    description: client.description,
    parameters: client.initialization?.properties.map((x) => emitMethodParameter(context, x)),
    operationGroups: emitOperationGroups(context, client),
    url: client.endpoint,
    apiVersions: client.apiVersions,
    arm: client.arm,
  };
}

export function emitCodeModel<TServiceOperation extends SdkServiceOperation>(
  sdkContext: SdkContext<TServiceOperation>,
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
