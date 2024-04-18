import {
    SdkBasicServiceMethod,
    SdkBodyParameter,
    SdkClientType,
    SdkHeaderParameter,
    SdkHttpOperation,
    SdkHttpResponse,
    SdkLroPagingServiceMethod,
    SdkLroServiceMethod,
    SdkPagingServiceMethod,
    SdkPathParameter,
    SdkQueryParameter,
    SdkServiceMethod,
    SdkServiceResponseHeader,
    getCrossLanguageDefinitionId,
} from "@azure-tools/typespec-client-generator-core";
import {
    camelToSnakeCase,
    emitParamBase,
    getAddedOn,
    getDelimeterAndExplode,
    getDescriptionAndSummary,
    getImplementation,
    isAbstract,
    isAzureCoreModel
} from "./utils.js";
import { KnownTypes, getType } from "./types.js";
import { PythonSdkContext } from "./lib.js";
import { HttpStatusCodeRange } from "@typespec/http";

function isContentTypeParameter(parameter: SdkHeaderParameter) {
    return parameter.serializedName.toLowerCase() === "content-type";
}

export function emitBasicHttpMethod(
    context: PythonSdkContext<SdkHttpOperation>,
    rootClient: SdkClientType<SdkHttpOperation>,
    method: SdkBasicServiceMethod<SdkHttpOperation>,
    operationGroupName: string,
): Record<string, any>[] {
    return [
        {
            ...emitHttpOperation(context, rootClient, operationGroupName, method.operation, method),
            abstract: isAbstract(method),
            internal: method.access === "internal",
            name: camelToSnakeCase(method.name),
            description: getDescriptionAndSummary(method).description,
            summary: getDescriptionAndSummary(method).summary,
        },
    ];
}

function emitInitialLroHttpMethod(
    context: PythonSdkContext<SdkHttpOperation>,
    rootClient: SdkClientType<SdkHttpOperation>,
    method: SdkLroServiceMethod<SdkHttpOperation> | SdkLroPagingServiceMethod<SdkHttpOperation>,
    operationGroupName: string,
): Record<string, any> {
    const initialOperation = emitHttpOperation(context, rootClient, operationGroupName, method.operation);
    initialOperation.responses.forEach((resp: Record<string, any>) => {
        if (method.operation.responses.get(resp.statusCodes[0])?.type) {
            resp["type"] = KnownTypes.anyObject;
        }
    });
    return {
        ...initialOperation,
        name: `_${camelToSnakeCase(method.name)}_initial`,
        isLroInitialOperation: true,
        wantTracing: false,
        exposeStreamKeyword: false,
        description: getDescriptionAndSummary(method).description,
        summary: getDescriptionAndSummary(method).summary,
    };
}

function addLroInformation(
    context: PythonSdkContext<SdkHttpOperation>,
    rootClient: SdkClientType<SdkHttpOperation>,
    method: SdkLroServiceMethod<SdkHttpOperation> | SdkLroPagingServiceMethod<SdkHttpOperation>,
    operationGroupName: string,
) {
    return {
        ...emitHttpOperation(context, rootClient, operationGroupName, method.operation, method),
        name: camelToSnakeCase(method.name),
        discriminator: "lro",
        initialOperation: emitInitialLroHttpMethod(context, rootClient, method, operationGroupName),
        exposeStreamKeyword: false,
        description: getDescriptionAndSummary(method).description,
        summary: getDescriptionAndSummary(method).summary,
    };
}

function addPagingInformation(
    context: PythonSdkContext<SdkHttpOperation>,
    rootClient: SdkClientType<SdkHttpOperation>,
    method: SdkPagingServiceMethod<SdkHttpOperation> | SdkLroPagingServiceMethod<SdkHttpOperation>,
    operationGroupName: string,
) {
    for (const response of Object.values(method.operation.responses)) {
        if (response.type && !isAzureCoreModel(response.type)) {
            getType(context, response.type)["pageResultModel"] = true;
        }
    }
    const itemType = getType(context, method.response.type!);
    const base = emitHttpOperation(context, rootClient, operationGroupName, method.operation, method);
    base.responses.forEach((resp: Record<string, any>) => {
        resp.type = itemType;
    });
    return {
        ...base,
        name: camelToSnakeCase(method.name),
        discriminator: "paging",
        exposeStreamKeyword: false,
        itemName: method.response.resultPath,
        continuationTokenName: method.nextLinkPath,
        itemType,
        description: getDescriptionAndSummary(method).description,
        summary: getDescriptionAndSummary(method).summary,
    };
}

export function emitLroHttpMethod(
    context: PythonSdkContext<SdkHttpOperation>,
    rootClient: SdkClientType<SdkHttpOperation>,
    method: SdkLroServiceMethod<SdkHttpOperation>,
    operationGroupName: string,
): Record<string, any>[] {
    const lroMethod = addLroInformation(context, rootClient, method, operationGroupName);
    return [lroMethod.initialOperation, lroMethod];
}

export function emitPagingHttpMethod(
    context: PythonSdkContext<SdkHttpOperation>,
    rootClient: SdkClientType<SdkHttpOperation>,
    method: SdkPagingServiceMethod<SdkHttpOperation>,
    operationGroupName: string,
): Record<string, any>[] {
    const pagingMethod = addPagingInformation(context, rootClient, method, operationGroupName);
    return [pagingMethod];
}

export function emitLroPagingHttpMethod(
    context: PythonSdkContext<SdkHttpOperation>,
    rootClient: SdkClientType<SdkHttpOperation>,
    method: SdkLroPagingServiceMethod<SdkHttpOperation>,
    operationGroupName: string,
): Record<string, any>[] {
    const pagingMethod = addPagingInformation(context, rootClient, method, operationGroupName);
    const lroMethod = addLroInformation(context, rootClient, method, operationGroupName);
    return [lroMethod.initialOperation, pagingMethod, lroMethod];
}

function emitHttpOperation(
    context: PythonSdkContext<SdkHttpOperation>,
    rootClient: SdkClientType<SdkHttpOperation>,
    operationGroupName: string,
    operation: SdkHttpOperation,
    method?: SdkServiceMethod<SdkHttpOperation>,
): Record<string, any> {
    const responses: Record<string, any>[] = [];
    const exceptions: Record<string, any>[] = [];
    for (const [statusCodes, response] of operation.responses) {
        responses.push(emitHttpResponse(context, statusCodes, response, method)!);
    }
    for (const [statusCodes, exception] of operation.exceptions) {
        exceptions.push(emitHttpResponse(context, statusCodes, exception)!);
    }
    const result = {
        url: operation.path,
        method: operation.verb.toUpperCase(),
        parameters: emitHttpParameters(context, rootClient, operation),
        bodyParameter: emitHttpBodyParameter(context, operation.bodyParam),
        responses,
        exceptions,
        groupName: operationGroupName,
        addedOn: method ? getAddedOn(context, method) : "",
        discriminator: "basic",
        isOverload: false,
        overloads: [],
        apiVersions: [],
        wantTracing: true,
        exposeStreamKeyword: true,
        crossLanguageDefinitionId: method ? getCrossLanguageDefinitionId(method) : undefined,
    };
    if (
        result.bodyParameter &&
        operation.bodyParam?.type.kind === "model" &&
        operation.bodyParam?.type.isGeneratedName
    ) {
        result.bodyParameter["propertyToParameterName"] = {};
        result.bodyParameter["defaultToUnsetSentinel"] = true;
        result.bodyParameter.type.base = "json";
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

function emitHttpPathParameter(context: PythonSdkContext<SdkHttpOperation>, parameter: SdkPathParameter) {
    const base = emitParamBase(context, parameter);
    return {
        ...base,
        wireName: parameter.serializedName,
        location: parameter.kind,
        implementation: getImplementation(context, parameter),
        clientDefaultValue: parameter.clientDefaultValue,
        skipUrlEncoding: parameter.urlEncode === false,
    };
}
function emitHttpHeaderParameter(
    context: PythonSdkContext<SdkHttpOperation>,
    parameter: SdkHeaderParameter,
): Record<string, any> {
    const base = emitParamBase(context, parameter);
    const [delimiter, explode] = getDelimeterAndExplode(parameter);
    let clientDefaultValue = parameter.clientDefaultValue;
    if (isContentTypeParameter(parameter)) {
        // we switch to string type for content-type header
        if (!clientDefaultValue && parameter.type.kind === "constant") {
            clientDefaultValue = parameter.type.value;
        }
        base.type = KnownTypes.string;
    }
    return {
        ...base,
        wireName: parameter.serializedName,
        location: parameter.kind,
        implementation: getImplementation(context, parameter),
        delimiter,
        explode,
        clientDefaultValue,
    };
}

function emitHttpQueryParameter(
    context: PythonSdkContext<SdkHttpOperation>,
    parameter: SdkQueryParameter,
): Record<string, any> {
    const base = emitParamBase(context, parameter);
    const [delimiter, explode] = getDelimeterAndExplode(parameter);
    return {
        ...base,
        wireName: parameter.serializedName,
        location: parameter.kind,
        implementation: getImplementation(context, parameter),
        delimiter,
        explode,
        clientDefaultValue: parameter.clientDefaultValue,
    };
}

function emitHttpParameters(
    context: PythonSdkContext<SdkHttpOperation>,
    rootClient: SdkClientType<SdkHttpOperation>,
    operation: SdkHttpOperation,
): Record<string, any>[] {
    const parameters: Record<string, any>[] = [...context.__endpointPathParameters];
    for (const parameter of operation.parameters) {
        switch (parameter.kind) {
            case "header":
                parameters.push(emitHttpHeaderParameter(context, parameter));
                break;
            case "query":
                parameters.push(emitHttpQueryParameter(context, parameter));
                break;
            case "path":
                parameters.push(emitHttpPathParameter(context, parameter));
                break;
        }
    }
    return parameters;
}

function emitHttpBodyParameter(
    context: PythonSdkContext<SdkHttpOperation>,
    bodyParam?: SdkBodyParameter,
): Record<string, any> | undefined {
    if (bodyParam === undefined) return undefined;
    return {
        ...emitParamBase(context, bodyParam, true),
        contentTypes: bodyParam.contentTypes,
        location: bodyParam.kind,
        clientName: bodyParam.isGeneratedName ? "body" : camelToSnakeCase(bodyParam.name),
        wireName: bodyParam.isGeneratedName ? "body" : bodyParam.name,
        implementation: getImplementation(context, bodyParam),
        clientDefaultValue: bodyParam.clientDefaultValue,
        defaultContentType: bodyParam.defaultContentType,
    };
}

function emitHttpResponse(
    context: PythonSdkContext<SdkHttpOperation>,
    statusCodes: HttpStatusCodeRange | number | "*",
    response: SdkHttpResponse,
    method?: SdkServiceMethod<SdkHttpOperation>,
): Record<string, any> | undefined {
    if (!response) return undefined;
    let type = undefined;
    if (response.type && !isAzureCoreModel(response.type)) {
        type = getType(context, response.type);
    } else if (method && method.response.type && !isAzureCoreModel(method.response.type)) {
        type = getType(context, method.response.type);
    }
    return {
        headers: response.headers.map((x) => emitHttpResponseHeader(context, x)),
        statusCodes:
            typeof statusCodes === "object"
                ? [(statusCodes as HttpStatusCodeRange).start]
                : statusCodes === "*"
                ? ["default"]
                : [statusCodes],
        discriminator: "basic",
        type,
        contentTypes: response.contentTypes,
        defaultContentType: response.defaultContentType ?? "application/json",
        resultProperty: method?.response.resultPath,
    };
}

function emitHttpResponseHeader(
    context: PythonSdkContext<SdkHttpOperation>,
    header: SdkServiceResponseHeader,
): Record<string, any> {
    return {
        type: getType(context, header.type),
        wireName: header.serializedName,
    };
}
