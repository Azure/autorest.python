import {
    SdkClientType,
    SdkContext,
    SdkCredentialParameter,
    SdkEndpointParameter,
    SdkMethod,
    SdkMethodParameter,
    SdkParameter,
    SdkServiceMethod,
    SdkServiceOperation,
} from "@azure-tools/typespec-client-generator-core";
import { getType } from "./types.js";
import { camelToSnakeCase, getImplementation } from "./utils.js";
import { emit } from "process";

type ParamBase = {
    optional: boolean;
    description: string;
    addedOn: string | undefined;
    clientName: string;
    inOverload: boolean;
    isApiVersion: boolean;
};

function emitParamBase(parameter: SdkParameter): ParamBase {
    return {
        optional: parameter.optional,
        description: parameter.description || "",
        addedOn: parameter.apiVersions.length > 0 ? parameter.apiVersions[0] : undefined,
        clientName: camelToSnakeCase(parameter.nameInClient),
        inOverload: false,
        isApiVersion: parameter.isApiVersionParam,
    };
}

function emitBasicOperation<TServiceOperation extends SdkServiceOperation>(
    context: SdkContext<TServiceOperation>,
    method: SdkMethod<TServiceOperation>,
    operationGroupName: string,
): Record<string, any>[] {
    
}

function emitMethodParameter(
    context: SdkContext,
    parameter: SdkEndpointParameter | SdkCredentialParameter | SdkMethodParameter,
): Record<string, any> {
    const base = {
        ...emitParamBase(parameter),
        implementation: getImplementation(parameter),
        type: getType(context, parameter.type),
        clientDefaultValue: parameter.clientDefaultValue,
    };
    if (parameter.kind === "endpoint") {
        return {
            ...base,
            skipUrlEncoding: !parameter.urlEncode,
            wireName: parameter.serializedName,
            type: "endpointPath",
        };
    }
    return base;
}

function emitOperation<TServiceOperation extends SdkServiceOperation>(
    context: SdkContext<TServiceOperation>,
    method: SdkServiceMethod<TServiceOperation>,
    operationGroupName: string,
): Record<string, any>[] {
    switch (method.kind) {
        case "basic":
            return emitBasicOperation(context, method, operationGroupName);
        case "lro":
            return emitLROOperation(context, method, operationGroupName);
        case "paging":
            return emitPagingOperation(context, method, operationGroupName);
        default:
            return emitLroPagingOperation(context, method, operationGroupName);
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
            const operations: Record<string, any>[] = [];
            for (const method of operationGroup.methods) {
                if (method.kind === "clientaccessor") continue; // skipping for now since we don't do sub-sub clients
                operations.push(emitOperation(context, method, operationGroup.name));
            }
            operationGroups.push({
                className: operationGroup.name,
                propertyName: operationGroup.name,
                operations: operations,
            });
        } else {
            const groupName = context.arm ? method.operation.__raw.operation.interface?.name ?? "" : "";
            const emittedOperation = emitOperation(context, method, groupName);
            if (!clientOperations.has(groupName)) {
                clientOperations.set(groupName, {
                    className: groupName,
                    propertyName: groupName,
                    operations: [],
                });
            }
            const og = clientOperations.get(groupName) as Record<string, any>;
            og.operations.push(emittedOperation);
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
        namespace: sdkPackage.rootNamespace,
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
