import {
    SdkBodyParameter,
    SdkClientType,
    SdkContext,
    SdkCredentialParameter,
    SdkEndpointParameter,
    SdkHeaderParameter,
    SdkHttpOperation,
    SdkHttpParameter,
    SdkHttpResponse,
    SdkMethod,
    SdkMethodParameter,
    SdkParameter,
    SdkPathParameter,
    SdkQueryParameter,
    SdkServiceMethod,
    SdkServiceOperation,
    SdkServiceParameter,
} from "@azure-tools/typespec-client-generator-core";
import { getType } from "./types.js";
import { camelToSnakeCase, getDelimeterAndExplode, getImplementation, isAbstract } from "./utils.js";
import { emit } from "process";

type ParamBase = {
    optional: boolean;
    description: string;
    addedOn: string | undefined;
    clientName: string;
    inOverload: boolean;
    isApiVersion: boolean;
    type: Record<string, any>;
};

function emitParamBase<TServiceOperation extends SdkServiceOperation>(context: SdkContext<TServiceOperation>, parameter: SdkParameter | SdkHttpParameter): ParamBase {
    return {
        optional: parameter.optional,
        description: parameter.description || "",
        addedOn: parameter.apiVersions.length > 0 ? parameter.apiVersions[0] : undefined,
        clientName: camelToSnakeCase(parameter.nameInClient),
        inOverload: false,
        isApiVersion: parameter.isApiVersionParam,
        type: getType(context, parameter.type),
    };
}

function emitHttpPathParameter<TServiceOperation extends SdkServiceOperation>(context: SdkContext<TServiceOperation>, parameter: SdkPathParameter){
    const base = emitParamBase(context, parameter);
    return {
        ...base,
        wireName: parameter.serializedName,
        location: parameter.kind,
        implementation: getImplementation(parameter),
        clientDefaultValue: parameter.clientDefaultValue,
        skipUrlEncoding: parameter.urlEncode === false,
    }
}
function emitHttpHeaderParameter<TServiceOperation extends SdkServiceOperation>(context: SdkContext<TServiceOperation>, parameter: SdkHeaderParameter): Record<string, any> {
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
    }

} 

function emitHttpQueryParameter<TServiceOperation extends SdkServiceOperation>(context: SdkContext<TServiceOperation>, parameter: SdkQueryParameter): Record<string, any> {
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
    }
}

function emitHttpParameters<TServiceOperation extends SdkServiceOperation>(context: SdkContext<TServiceOperation>, operation: SdkHttpOperation): Record<string, any>[] {
    const parameters: Record<string, any>[] = [];
    for (const queryParam of operation.queryParams) {
        parameters.push(emitHttpQueryParameter(context, queryParam))
    }
    for (const headerParam of operation.headerParams) {
        parameters.push(emitHttpHeaderParameter(context, headerParam))
    }
    for (const pathParam of operation.pathParams) {
        parameters.push(emitHttpPathParameter(context, pathParam))
    }
    return parameters;
}

function emitHttpBodyParameter<TServiceOperation extends SdkServiceOperation>(context: SdkContext<TServiceOperation>, bodyParams: SdkBodyParameter[]): Record<string, any> | undefined {
    if (bodyParams.length === 0) return undefined;
    const bodyParam = bodyParams[0];
    return {
        ...emitParamBase(context, bodyParam),
        contentTypes: bodyParam.contentTypes,
        location: bodyParam.kind,
        wireName: bodyParam.nameInClient,
        type: getType(context, bodyParam.type),
        implementation: getImplementation(bodyParam),
        clientDefaultValue: bodyParam.clientDefaultValue,
        defaultContentType: bodyParam.defaultContentType,
    }

}

function emitHttpResponse<TServiceOperation extends SdkServiceOperation>(context: SdkContext<TServiceOperation>, statusCodes: string, response?: SdkHttpResponse): Record<string, any> | undefined {
    if (!response) return undefined;
    return {
        headers: response.headers.map(x => emitResponseHeader(context, x)),
        statusCodes: statusCodes,
        addedOn: "",
        discriminator: "basic",
        type: response.type ? getType(context, response.type) : undefined,
        contentTypes: "",
        
    }
}


function emitBasicOperation<TServiceOperation extends SdkServiceOperation>(
    context: SdkContext<TServiceOperation>,
    method: SdkServiceMethod<TServiceOperation>,
    operationGroupName: string,
): Record<string, any>[] {
    const responses: Record<string, any>[] = [];
    for (const [statusCodes, response] of Object.entries(method.operation.responses)) {
        responses.push(emitHttpResponse(context, statusCodes, response));
    }
    return [{
        name: camelToSnakeCase(method.name),
        description: method.details ?? method.description,
        summary: method.details ? method.description : undefined,
        url: method.operation.path,
        method: method.operation.verb.toUpperCase(),
        parameters: emitHttpParameters(context, method.operation),
        bodyParameter: emitHttpBodyParameter(context, method.operation.bodyParams),
        responses,
        exception: emitHttpResponse(context, "*", method.operation.exception),
        groupName: operationGroupName,
        addedOn: "",
        discriminator: "basic",
        isOverload: false,
        overloads: [],
        apiVersions: [],
        wantTracing: true,
        exposeStreamKeyword: true,
        abstract: isAbstract(method),
        internal: method.access === "internal",
    }]
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
