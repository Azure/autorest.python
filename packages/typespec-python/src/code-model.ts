import {
  SdkBasicServiceMethod,
  SdkClientType,
  SdkCredentialParameter,
  SdkEndpointParameter,
  SdkLroPagingServiceMethod,
  SdkLroServiceMethod,
  SdkMethodParameter,
  SdkPagingServiceMethod,
  SdkServiceMethod,
  SdkServiceOperation,
  UsageFlags,
} from "@azure-tools/typespec-client-generator-core";
import { KnownTypes, getType, simpleTypesMap, typesMap } from "./types.js";
import { emitParamBase, getImplementation, removeUnderscoresFromNamespace } from "./utils.js";
import { emitBasicHttpMethod, emitLroHttpMethod, emitLroPagingHttpMethod, emitPagingHttpMethod } from "./http.js";
import { PythonSdkContext } from "./lib.js";

function emitBasicMethod<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  rootClient: SdkClientType<TServiceOperation>,
  method: SdkBasicServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitBasicHttpMethod(context, rootClient, method, operationGroupName);
    default:
      throw new Error("We only support HTTP operations right now");
  }
}

function emitLroMethod<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  rootClient: SdkClientType<TServiceOperation>,
  method: SdkLroServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitLroHttpMethod(context, rootClient, method, operationGroupName);
    default:
      throw new Error("We only support HTTP operations right now");
  }
}

function emitPagingMethod<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  rootClient: SdkClientType<TServiceOperation>,
  method: SdkPagingServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitPagingHttpMethod(context, rootClient, method, operationGroupName);
    default:
      throw new Error("We only support HTTP operations right now");
  }
}

function emitLroPagingMethod<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  rootClient: SdkClientType<TServiceOperation>,
  method: SdkLroPagingServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  if (method.operation.kind !== "http") throw new Error("We only support HTTP operations right now");
  switch (method.operation.kind) {
    case "http":
      return emitLroPagingHttpMethod(context, rootClient, method, operationGroupName);
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
    implementation: getImplementation(context, parameter),
    clientDefaultValue: parameter.clientDefaultValue,
    location: parameter.kind,
  };
  if (parameter.kind === "endpoint") {
    const endpointParameter = {
      ...base,
      clientDefaultValue: base.type.value,
      type: client.hasParameterizedEndpoint ? base.type : KnownTypes.string,
      skipUrlEncoding: !parameter.urlEncode,
      wireName: client.hasParameterizedEndpoint ? parameter.nameInClient : "$host",
      location: client.hasParameterizedEndpoint ? "endpointPath" : "path",
      clientName: context.arm ? "base_url" : base.clientName,
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
      in_docstring: false,
    };
  }
  return base;
}

function emitMethod<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  rootClient: SdkClientType<TServiceOperation>,
  method: SdkServiceMethod<TServiceOperation>,
  operationGroupName: string,
): Record<string, any>[] {
  switch (method.kind) {
    case "basic":
      return emitBasicMethod(context, rootClient, method, operationGroupName);
    case "lro":
      return emitLroMethod(context, rootClient, method, operationGroupName);
    case "paging":
      return emitPagingMethod(context, rootClient, method, operationGroupName);
    default:
      return emitLroPagingMethod(context, rootClient, method, operationGroupName);
  }
}

function emitOperationGroups<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  client: SdkClientType<TServiceOperation>,
  rootClient: SdkClientType<TServiceOperation>,
  prefix: string,
): Record<string, any>[] | undefined {
  const operationGroups: Record<string, any>[] = [];

  for (const method of client.methods) {
    if (method.kind === "clientaccessor") {
      const operationGroup = method.response;
      const name = `${prefix}${operationGroup.name}`;
      let operations: Record<string, any>[] = [];
      for (const method of operationGroup.methods) {
        if (method.kind === "clientaccessor") continue;
        operations = operations.concat(emitMethod(context, rootClient, method, name));
      }
      operationGroups.push({
        name: name,
        className: name,
        propertyName: operationGroup.name,
        operations: operations,
        operationGroups: emitOperationGroups(context, operationGroup, rootClient, name),
      });
    }
  }

  // root client should deal with mixin operation group
  if (prefix === "") {
    let operations: Record<string, any>[] = [];
    for (const method of client.methods) {
      if (method.kind === "clientaccessor") continue;
      operations = operations.concat(emitMethod(context, rootClient, method, ""));
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
  const operationGroups = emitOperationGroups(context, client, client, "");
  const parameters = client.initialization?.properties.map((x) => emitMethodParameter(context, client, x)) ?? [];
  if(context.__subscriptionIdPathParameter) {
    parameters.push(context.__subscriptionIdPathParameter);
  }
  return {
    name: client.name,
    description: client.description ?? "",
    parameters,
    operationGroups,
    url: client.endpoint,
    apiVersions: client.apiVersions,
    arm: client.arm,
  };
}

export function emitCodeModel<TServiceOperation extends SdkServiceOperation>(
  sdkContext: PythonSdkContext<TServiceOperation>,
) {
  // Get types
  const sdkPackage = sdkContext.experimental_sdkPackage;
  const codeModel: Record<string, any> = {
    namespace: removeUnderscoresFromNamespace(sdkPackage.rootNamespace).toLowerCase(),
    clients: [],
    subnamespaceToClients: {},
  };
  for (const model of sdkPackage.models) {
    if (model.name === "") {
        continue;
    }
    getType(sdkContext, model);
  }
  for (const sdkEnum of sdkPackage.enums) {
    if(sdkEnum.usage === UsageFlags.Versioning) {
        continue;
    }
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
