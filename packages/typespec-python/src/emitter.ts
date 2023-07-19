import { getPagedResult, getLroMetadata } from "@azure-tools/typespec-azure-core";
import {
    getDoc,
    getEncode,
    getSummary,
    ignoreDiagnostics,
    isErrorModel,
    Model,
    ModelProperty,
    Namespace,
    getEffectiveModelType,
    Operation,
    Scalar,
    EmitContext,
    listServices,
    Type,
    getNamespaceFullName,
    BooleanLiteral,
    StringLiteral,
    NumericLiteral,
    Union,
    isNeverType,
} from "@typespec/compiler";
import {
    getAuthentication,
    getHeaderFieldName,
    getHttpOperation,
    getPathParamName,
    getQueryParamName,
    getServers,
    HttpAuth,
    HttpOperationParameter,
    HttpOperationResponse,
    HttpServer,
    isStatusCode,
    HttpOperation,
    isHeader,
    Visibility,
} from "@typespec/http";
import { getAddedOnVersions } from "@typespec/versioning";
import {
    SdkClient,
    listClients,
    listOperationGroups,
    listOperationsInOperationGroup,
    isApiVersion,
    getDefaultApiVersion,
    getClientNamespaceString,
    createSdkContext,
    SdkContext,
    getLibraryName,
    getAllModels,
    isInternal,
    SdkEnumValueType,
    getSdkModel,
    getSdkConstant,
    SdkType,
    SdkModelType,
    SdkBodyModelPropertyType,
    SdkUnionType,
    SdkEnumType,
    SdkBuiltInType,
    SdkArrayType,
    SdkDictionaryType,
    getSdkArrayOrDict,
    SdkConstantType,
    getSdkBuiltInType,
    getSdkDatetimeType,
    getSdkDurationType,
    SdkDatetimeType,
    SdkDurationType,
    getSdkUnion,
} from "@azure-tools/typespec-client-generator-core";
import { getResourceOperation } from "@typespec/rest";
import { resolveModuleRoot, saveCodeModelAsYaml } from "./external-process.js";
import { dirname } from "path";
import { fileURLToPath } from "url";
import { dump } from "js-yaml";
import { execFileSync } from "child_process";
import { PythonEmitterOptions } from "./lib.js";

interface HttpServerParameter {
    type: "endpointPath";
    name: string;
    param: ModelProperty;
}

interface CredentialType {
    kind: "Credential";
    scheme: HttpAuth;
}

interface CredentialTypeUnion {
    kind: "CredentialTypeUnion";
    types: CredentialType[];
}

type EmitterType = CredentialType | CredentialTypeUnion | Type;

const defaultOptions = {
    "basic-setup-py": true,
    "package-version": "1.0.0b1",
};

const sdkScalarKindToPythonKind: Record<string, string> = {
    int32: "integer",
    int64: "integer",
    float32: "float",
    float64: "float",
};

export async function $onEmit(context: EmitContext<PythonEmitterOptions>) {
    const program = context.program;
    const resolvedOptions = { ...defaultOptions, ...context.options };

    const root = await resolveModuleRoot(program, "@autorest/python", dirname(fileURLToPath(import.meta.url)));
    const outputDir = context.emitterOutputDir;
    const yamlMap = emitCodeModel(context);
    const yamlPath = await saveCodeModelAsYaml("typespec-python-yaml-map", yamlMap);
    const commandArgs = [
        `${root}/run-python3.js`,
        `${root}/run_cadl.py`,
        `--output-folder=${outputDir}`,
        `--cadl-file=${yamlPath}`,
    ];
    for (const [key, value] of Object.entries(resolvedOptions)) {
        commandArgs.push(`--${key}=${value}`);
    }
    if (resolvedOptions.debug) {
        commandArgs.push("--debug");
    }
    if (!program.compilerOptions.noEmit && !program.hasError()) {
        execFileSync(process.execPath, commandArgs);
    }
}

function camelToSnakeCase(name: string): string {
    if (!name) return name;
    const camelToSnakeCaseRe = (str: string) =>
        str
            .replace("/", "_")
            .replace(/\s+/g, "_")
            .replace(/\$/g, "")
            .replace(/-/g, "_")
            .replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`);

    return camelToSnakeCaseRe(name[0].toLowerCase() + name.slice(1));
}

const typesMap = new Map<string, Record<string, any>>();
const simpleTypesMap = new Map<string, Record<string, any>>();
const endpointPathParameters: Record<string, any>[] = [];
let apiVersionParam: Record<string, any> | undefined = undefined;

function getDocStr(context: SdkContext, target: Type): string {
    return getDoc(context.program, target) ?? "";
}

function getEffectiveSchemaType(context: SdkContext, type: Model): Model {
    const program = context.program;
    function isSchemaProperty(property: ModelProperty) {
        const headerInfo = getHeaderFieldName(program, property);
        const queryInfo = getQueryParamName(program, property);
        const pathInfo = getPathParamName(program, property);
        const statusCodeinfo = isStatusCode(program, property);
        return !(headerInfo || queryInfo || pathInfo || statusCodeinfo);
    }

    const effective = getEffectiveModelType(program, type, isSchemaProperty);
    if (effective.name) {
        return effective;
    }
    return type;
}

function isEmptyModel(type: EmitterType | SdkType): boolean {
    // object, {} will be treated as empty model, user defined empty model will not
    return (
        type.kind === "model" &&
        type.properties.length === 0 &&
        !type.baseModel &&
        !type.discriminatedSubtypes &&
        !type.discriminatorValue &&
        (type.name === "" || type.name === "object")
    );
}

export function getType(context: SdkContext, type: EmitterType | SdkType): Record<string, any> {
    let oriType;
    if (type.kind === "ModelProperty") {
        oriType = type;
        type = type.type;
    }
    const isArrayDict = type.kind === "Model" && type.indexer;
    const enableCache = !isEmptyModel(type) && (type.kind === "model" || type.kind === "enum" || type.kind === "Model" || type.kind === "Enum") && !isArrayDict;
    if (type.kind === "Model") {
        type = getEffectiveSchemaType(context, type);
    }
    // using name to cache will have some problem for template
    if (enableCache && typesMap.has((type as any).name)) {
        return typesMap.get((type as any).name)!;
    }
    let newValue;
    if (isEmptyModel(type)) {
        newValue = { type: "any" };
    } else {
        newValue = emitType(context, type);
    }
    if (oriType?.kind === "ModelProperty") {
        updateWithEncode(context, oriType, newValue);
    }
    if (enableCache) {
        typesMap.set((type as SdkModelType | SdkEnumType).name, newValue);
        if (type.kind === "model") {
            for (const property of type.properties.values()) {
                if (property.kind === "property") {
                    newValue.properties.push(emitProperty(context, property));
                }
            }
            if (type.discriminatedSubtypes) {
                for (const key in type.discriminatedSubtypes) {
                    newValue.discriminatedSubtypes[key] = getType(context, type.discriminatedSubtypes[key]);
                }
            }
        }
    } else {
        const key = dump(newValue, { sortKeys: true });
        const value = simpleTypesMap.get(key);
        if (value) {
            newValue = value;
        } else {
            simpleTypesMap.set(key, newValue);
        }
    }
    return newValue;
}

// To pass the yaml dump
function getAddedOnVersion(context: SdkContext, t: Type): string | undefined {
    const versions = getAddedOnVersions(context.program as any, t as any);
    if (versions !== undefined && versions.length > 0) {
        return versions[0].value;
    }
    return undefined;
}

type ParamBase = {
    optional: boolean;
    description: string;
    addedOn: string | undefined;
    clientName: string;
    inOverload: boolean;
};
function emitParamBase(context: SdkContext, parameter: ModelProperty | Type): ParamBase {
    let optional: boolean;
    let name: string;
    let description: string = "";
    let addedOn: string | undefined;

    if (parameter.kind === "ModelProperty") {
        optional = parameter.optional;
        name = parameter.name;
        description = getDocStr(context, parameter);
        addedOn = getAddedOnVersion(context, parameter);
    } else {
        optional = false;
        name = "body";
    }

    return {
        optional,
        description,
        addedOn,
        clientName: camelToSnakeCase(name),
        inOverload: false,
    };
}

type BodyParameter = ParamBase & {
    contentTypes: string[];
    type: any;
    wireName: string;
    location: "body";
    defaultContentType: string;
};

function getBodyType(context: SdkContext, route: HttpOperation): Type {
    let bodyModel = route.parameters.body?.type;
    if (bodyModel && bodyModel.kind === "Model" && route.operation) {
        const resourceType = getResourceOperation(context.program, route.operation)?.resourceType;
        if (resourceType && route.responses && route.responses.length > 0) {
            const resp = route.responses[0];
            if (resp && resp.responses && resp.responses.length > 0) {
                const responseBody = resp.responses[0]?.body;
                if (responseBody?.type?.kind === "Model") {
                    const bodyTypeInResponse = getEffectiveSchemaType(context, responseBody.type);
                    // response body type is reosurce type, and request body type (if templated) contains resource type
                    if (
                        bodyTypeInResponse === resourceType &&
                        bodyModel.templateMapper &&
                        bodyModel.templateMapper.args.some((it) => {
                            return it.kind === "Model" || it.kind === "Union" ? it === bodyTypeInResponse : false;
                        })
                    ) {
                        bodyModel = resourceType;
                    }
                }
            }
        }
        if (resourceType && bodyModel.name === "") {
            bodyModel = resourceType;
        }
    }
    return bodyModel!;
}

function emitBodyParameter(context: SdkContext, httpOperation: HttpOperation): BodyParameter {
    const params = httpOperation.parameters;
    const body = params.body!;
    const base = emitParamBase(context, body.parameter ?? body.type);
    let contentTypes = body.contentTypes;
    if (contentTypes.length === 0) {
        contentTypes = ["application/json"];
    }
    const type = getType(context, getBodyType(context, httpOperation));

    if (type.type === "model" && type.name === "") {
        type.name = capitalize(httpOperation.operation.name) + "Request";
    }

    return {
        contentTypes,
        type,
        wireName: body.parameter?.name ?? "body",
        location: "body",
        ...base,
        defaultContentType:
            body.parameter?.default ?? contentTypes.includes("application/json") ? "application/json" : contentTypes[0],
    };
}

function emitParameter(
    context: SdkContext,
    parameter: HttpOperationParameter | HttpServerParameter,
    implementation: string,
): Record<string, any> {
    const base = emitParamBase(context, parameter.param);
    let type = getType(context, parameter.param);
    let clientDefaultValue = undefined;
    if (parameter.name.toLowerCase() === "content-type" && type["type"] === "constant") {
        /// We don't want constant types for content types, so we make sure if it's
        /// a constant, we make it not constant
        clientDefaultValue = type["value"];
        type = type["valueType"];
    }
    const paramMap: Record<string, any> = {
        wireName: parameter.type === "path" ? parameter.param.name : parameter.name,
        location: parameter.type,
        type: type,
        implementation: implementation,
        skipUrlEncoding: parameter.type === "endpointPath",
    };
    if (type.type === "list" && (parameter.type === "query" || parameter.type === "header")) {
        if (parameter.format === "csv") {
            paramMap["delimiter"] = "comma";
        } else if ((parameter.format as string) === "ssv") {
            paramMap["delimiter"] = "space";
        } else if ((parameter.format as string) === "tsv") {
            paramMap["delimiter"] = "tab";
        } else if ((parameter.format as string) === "pipes") {
            paramMap["delimiter"] = "pipe";
        } else {
            paramMap["explode"] = true;
        }
    }

    if (paramMap.type.type === "constant") {
        clientDefaultValue = paramMap.type.value;
    }

    if (isApiVersion(context, parameter as HttpOperationParameter)) {
        const defaultApiVersion = getDefaultApiVersion(context, getServiceNamespace(context));
        paramMap.type = defaultApiVersion ? getConstantType(defaultApiVersion.value) : KnownTypes.string;
        paramMap.implementation = "Client";
        paramMap.in_docstring = false;
        paramMap.isApiVersion = true;
        if (defaultApiVersion) {
            clientDefaultValue = defaultApiVersion.value;
        }
    }
    return { clientDefaultValue, ...base, ...paramMap };
}

function emitContentTypeParameter(
    bodyParameter: Record<string, any>,
    inOverload: boolean,
    inOverriden: boolean,
): Record<string, any> {
    return {
        checkClientInput: false,
        clientDefaultValue: bodyParameter.defaultContentType,
        clientName: "content_type",
        delimiter: null,
        description: `Body parameter Content-Type. Known values are: ${bodyParameter.contentTypes}.`,
        implementation: "Method",
        inDocstring: true,
        inOverload: inOverload,
        inOverriden: inOverriden,
        location: "header",
        optional: true,
        wireName: "Content-Type",
        type: KnownTypes.string,
    };
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

function getConstantType(key: string): Record<string, any> {
    const cache = simpleTypesMap.get(key);
    if (cache) {
        return cache;
    }
    const type = {
        apiVersions: [],
        clientDefaultValue: null,
        type: "constant",
        value: key,
        valueType: KnownTypes.string,
        xmlMetadata: {},
    };
    simpleTypesMap.set(key, type);
    return type;
}

function emitAcceptParameter(inOverload: boolean, inOverriden: boolean): Record<string, any> {
    return {
        checkClientInput: false,
        clientDefaultValue: "application/json",
        clientName: "accept",
        delimiter: null,
        description: "Accept header.",
        explode: false,
        groupedBy: null,
        implementation: "Method",
        inDocstring: true,
        inOverload: inOverload,
        inOverriden: inOverriden,
        location: "header",
        optional: false,
        wireName: "Accept",
        skipUrlEncoding: false,
        type: getConstantType("application/json"),
    };
}

function emitResponseHeaders(context: SdkContext, response: HttpOperationResponse): Record<string, any>[] {
    const headers: Record<string, any>[] = [];
    for (const innerResponse of response.responses) {
        if (innerResponse.headers && Object.keys(innerResponse.headers).length > 0) {
            for (const [key, value] of Object.entries(innerResponse.headers)) {
                headers.push({
                    type: getType(context, value.type),
                    wireName: key,
                });
            }
        }
    }
    return headers;
}

function isAzureCoreModel(t: Type): boolean {
    return (
        t.kind === "Model" &&
        t.namespace !== undefined &&
        ["Azure.Core", "Azure.Core.Foundations"].includes(getNamespaceFullName(t.namespace))
    );
}

function hasDefaultStatusCode(response: HttpOperationResponse): boolean {
    return response.statusCode === "*";
}

function getBodyFromResponse(context: SdkContext, response: HttpOperationResponse): Type | undefined {
    let body: Type | undefined = undefined;
    for (const innerResponse of response.responses) {
        if (!body && innerResponse.body) {
            body = innerResponse.body.type;
        }
    }
    if (body && body.kind === "Model") {
        body = getEffectiveSchemaType(context, body);
    }
    return body;
}

function emitResponse(context: SdkContext, response: HttpOperationResponse): Record<string, any> {
    let type = undefined;
    const body = getBodyFromResponse(context, response);
    if (body) {
        if (body.kind === "Model") {
            if (body && body.decorators.find((d) => d.decorator.name === "$pagedResult")) {
                type = getType(context, Array.from(body.properties.values())[0]);
            } else if (body && !isAzureCoreModel(body)) {
                type = getType(context, body);
            }
        } else {
            type = getType(context, body);
        }
    }
    const statusCodes = [];
    if (hasDefaultStatusCode(response)) {
        statusCodes.push("default");
    } else {
        statusCodes.push(parseInt(response.statusCode));
    }
    return {
        headers: emitResponseHeaders(context, response),
        statusCodes: statusCodes,
        addedOn: getAddedOnVersion(context, response.type),
        discriminator: "basic",
        type: type,
    };
}

function emitOperation(context: SdkContext, operation: Operation, operationGroupName: string): Record<string, any>[] {
    const lro = getLroMetadata(context.program, operation);
    const paging = getPagedResult(context.program, operation);
    if (lro && paging) {
        return emitLroPagingOperation(context, operation, operationGroupName);
    } else if (paging) {
        return emitPagingOperation(context, operation, operationGroupName);
    } else if (lro) {
        return emitLroOperation(context, operation, operationGroupName);
    }
    return emitBasicOperation(context, operation, operationGroupName);
}

function addLroInformation(
    context: SdkContext,
    tspOperation: Operation,
    emittedOperation: Record<string, any>,
    initialOperation: Record<string, any>,
) {
    emittedOperation["discriminator"] = "lro";
    emittedOperation["initialOperation"] = initialOperation;
    emittedOperation["exposeStreamKeyword"] = false;
    const lroMeta = getLroMetadata(context.program, tspOperation);
    if (!isAzureCoreModel(lroMeta!.logicalResult)) {
        emittedOperation["responses"][0]["type"] = getType(context, lroMeta!.logicalResult);
        if (lroMeta!.finalStep?.target.kind === "ModelProperty") {
            emittedOperation["responses"][0]["resultProperty"] = lroMeta!.finalStep.target.name;
        }
        addAcceptParameter(context, tspOperation, emittedOperation["parameters"]);
        addAcceptParameter(context, lroMeta!.operation, emittedOperation["initialOperation"]["parameters"]);
    }
}
function addPagingInformation(context: SdkContext, operation: Operation, emittedOperation: Record<string, any>) {
    emittedOperation["discriminator"] = "paging";
    const pagedResult = getPagedResult(context.program, operation);
    if (pagedResult === undefined) {
        throw Error("Trying to add paging information, but not paging metadata for this operation");
    }
    if (!isAzureCoreModel(pagedResult.modelType)) {
        getType(context, pagedResult.modelType)["pageResultModel"] = true;
    }
    emittedOperation["itemName"] = pagedResult.itemsPath;
    emittedOperation["itemType"] = getType(context, pagedResult.itemsProperty!.type);
    emittedOperation["continuationTokenName"] = pagedResult.nextLinkPath;
    emittedOperation["exposeStreamKeyword"] = false;
}

function getLroInitialOperation(
    context: SdkContext,
    operation: Operation,
    operationGroupName: string,
): Record<string, any> {
    const initialTspOperation = getLroMetadata(context.program, operation)!.operation;
    const initialOperation = emitBasicOperation(context, initialTspOperation, operationGroupName)[0];
    initialOperation["name"] = `_${initialOperation["name"]}_initial`;
    initialOperation["isLroInitialOperation"] = true;
    initialOperation["wantTracing"] = false;
    initialOperation["exposeStreamKeyword"] = false;
    initialOperation["responses"].forEach((resp: Record<string, any>, index: number) => {
        if (
            getBodyFromResponse(
                context,
                ignoreDiagnostics(getHttpOperation(context.program, initialTspOperation)).responses[index],
            )
        ) {
            // if there's a body, even if it's an Azure.Core model, we want to use anyObject
            resp["type"] = KnownTypes.anyObject;
        }
    });
    return initialOperation;
}

function emitLroPagingOperation(
    context: SdkContext,
    operation: Operation,
    operationGroupName: string,
): Record<string, any>[] {
    const retval: Record<string, any>[] = [];
    for (const emittedOperation of emitBasicOperation(context, operation, operationGroupName)) {
        const initialOperation = getLroInitialOperation(context, operation, operationGroupName);
        addLroInformation(context, operation, emittedOperation, initialOperation);
        addPagingInformation(context, operation, emittedOperation);
        emittedOperation["discriminator"] = "lropaging";
        retval.push(emittedOperation);
    }
    return retval;
}

function emitLroOperation(
    context: SdkContext,
    operation: Operation,
    operationGroupName: string,
): Record<string, any>[] {
    const retval = [];
    for (const emittedOperation of emitBasicOperation(context, operation, operationGroupName)) {
        const initialOperation = getLroInitialOperation(context, operation, operationGroupName);
        addLroInformation(context, operation, emittedOperation, initialOperation);
        retval.push(initialOperation);
        retval.push(emittedOperation);
    }
    return retval;
}

function emitPagingOperation(
    context: SdkContext,
    operation: Operation,
    operationGroupName: string,
): Record<string, any>[] {
    const retval = [];
    for (const emittedOperation of emitBasicOperation(context, operation, operationGroupName)) {
        addPagingInformation(context, operation, emittedOperation);
        retval.push(emittedOperation);
    }
    return retval;
}

function isAbstract(operation: HttpOperation): boolean {
    const body = operation.parameters.body;
    return body !== undefined && body.contentTypes.length > 1;
}

function addAcceptParameter(context: SdkContext, operation: Operation, parameters: Record<string, any>[]) {
    const httpOperation = ignoreDiagnostics(getHttpOperation(context.program, operation));
    if (
        getBodyFromResponse(context, httpOperation.responses[0]) &&
        parameters.filter((e) => e.wireName.toLowerCase() === "accept").length === 0
    ) {
        parameters.push(emitAcceptParameter(false, false));
    }
}

function emitBasicOperation(
    context: SdkContext,
    operation: Operation,
    operationGroupName: string,
): Record<string, any>[] {
    // Set up parameters for operation
    const parameters: Record<string, any>[] = [];
    if (endpointPathParameters) {
        for (const param of endpointPathParameters) {
            parameters.push(param);
        }
    }
    const httpOperation = ignoreDiagnostics(getHttpOperation(context.program, operation));
    for (const param of httpOperation.parameters.parameters) {
        const emittedParam = emitParameter(context, param, "Method");
        if (isApiVersion(context, param) && apiVersionParam === undefined) {
            apiVersionParam = emittedParam;
        }
        parameters.push(emittedParam);
    }

    // Set up responses for operation
    const responses: Record<string, any>[] = [];
    const exceptions: Record<string, any>[] = [];
    const isOverload: boolean = false;
    const isOverriden: boolean = false;
    for (const response of httpOperation.responses) {
        const emittedResponse = emitResponse(context, response);
        addAcceptParameter(context, operation, parameters);
        if (isErrorModel(context.program, response.type)) {
            // * is valid status code in cadl but invalid for autorest.python
            if (response.statusCode === "*") {
                exceptions.push(emittedResponse);
            }
        } else {
            responses.push(emittedResponse);
        }
    }

    let bodyParameter: Record<string, any> | undefined;
    if (httpOperation.parameters.body === undefined) {
        bodyParameter = undefined;
    } else {
        bodyParameter = emitBodyParameter(context, httpOperation);
        if (parameters.filter((e) => e.wireName.toLowerCase() === "content-type").length === 0) {
            parameters.push(emitContentTypeParameter(bodyParameter, isOverload, isOverriden));
        }
        if (bodyParameter.type.type === "model" && bodyParameter.type.base === "json") {
            bodyParameter["propertyToParameterName"] = {};
            if (!isOverload) {
                bodyParameter.defaultToUnsetSentinel = true;
            }
            for (const property of bodyParameter.type.properties) {
                bodyParameter["propertyToParameterName"][property["wireName"]] = property["clientName"];
                parameters.push(emitFlattenedParameter(bodyParameter, property));
            }
        }
    }
    const name = camelToSnakeCase(getLibraryName(context, operation));
    return [
        {
            name: name,
            description: getDocStr(context, operation),
            summary: getSummary(context.program, operation),
            url: httpOperation.path,
            method: httpOperation.verb.toUpperCase(),
            parameters: parameters,
            bodyParameter: bodyParameter,
            responses: responses,
            exceptions: exceptions,
            groupName: operationGroupName,
            addedOn: getAddedOnVersion(context, operation),
            discriminator: "basic",
            isOverload: false,
            overloads: [],
            apiVersions: [getAddedOnVersion(context, operation)],
            wantTracing: true,
            exposeStreamKeyword: true,
            abstract: isAbstract(httpOperation),
            internal: isInternal(context, operation),
        },
    ];
}

function visibilityMapping(visibility?: Visibility[]): string[] | undefined {
    if (visibility === undefined) {
        return undefined;
    }
    const result = [];
    for (const v of visibility) {
        if (v === Visibility.Read) {
            result.push("read");
        } else if (v === Visibility.Create) {
            result.push("create");
        } else if (v === Visibility.Update) {
            result.push("update");
        } else if (v === Visibility.Delete) {
            result.push("delete");
        } else if (v === Visibility.Query) {
            result.push("query");
        }
    }
    return result;
}

function emitProperty(context: SdkContext, type: SdkBodyModelPropertyType): Record<string, any> {
    return {
        clientName: camelToSnakeCase(type.nameInClient),
        wireName: type.serializedName,
        type: getType(context, type.type),
        optional: type.optional,
        description: type.doc,
        addedOn: type.apiVersions[0],
        visibility: visibilityMapping(type.visibility),
        isDiscriminator: type.discriminator,
    };
}

function emitModel(context: SdkContext, type: SdkModelType): Record<string, any> {
    return {
        type: type.kind,
        name: type.name,
        description: type.doc,
        parents: type.baseModel ? [getType(context, type.baseModel)] : [],
        discriminatedSubtypes: {},
        properties: [],
        snakeCaseName: type.name ? camelToSnakeCase(type.name) : type.name,
        base: "dpg",
        internal: type.internal,
    };
}

function enumName(name: string): string {
    if (name.toUpperCase() === name) {
        return name;
    }
    return camelToSnakeCase(name).toUpperCase();
}

function emitEnumMember(type: SdkEnumValueType): Record<string, any> {
    return {
        name: enumName(type.name),
        value: type.value,
        description: type.doc,
    };
}

function emitEnum(context: SdkContext, type: SdkEnumType): Record<string, any> {
    return {
        type: type.kind,
        name: type.name,
        description: type.doc,
        valueType: emitBuiltInType(context, type.valueType),
        values: type.values.map((x) => emitEnumMember(x)),
    };
}

function emitCredential(auth: HttpAuth): Record<string, any> {
    let credential_type: Record<string, any> = {};
    if (auth.type === "oauth2") {
        credential_type = {
            type: "OAuth2",
            policy: {
                type: "BearerTokenCredentialPolicy",
                credentialScopes: [],
            },
        };
        for (const flow of auth.flows) {
            for (const scope of flow.scopes) {
                credential_type.policy.credentialScopes.push(scope.value);
            }
            credential_type.policy.credentialScopes.push();
        }
    } else if (auth.type === "apiKey") {
        credential_type = {
            type: "Key",
            policy: {
                type: "AzureKeyCredentialPolicy",
                key: auth.name,
            },
        };
    } else if (auth.type === "http") {
        credential_type = {
            type: "Key",
            policy: {
                type: "AzureKeyCredentialPolicy",
                key: "Authorization",
                scheme: auth.scheme,
            },
        };
    }
    return credential_type;
}

function emitCredentialUnion(cred_types: CredentialTypeUnion): Record<string, any> {
    const result: Record<string, any> = {};
    // Export as CombinedType, which is already a Union Type in autorest codegen
    result.type = "combined";
    result.types = [];
    for (const cred_type of cred_types.types) {
        result.types.push(emitCredential(cred_type.scheme));
    }

    return result;
}

function emitBuiltInType(
    context: SdkContext,
    type: Scalar | SdkBuiltInType | SdkDurationType | SdkDatetimeType,
): Record<string, any> {
    if (type.kind === "Scalar") {
        while (type.baseScalar) {
            type = type.baseScalar;
        }
        if (type.name === "utcDateTime" || type.name === "offsetDateTime") {
            type = getSdkDatetimeType(type);
        } else if (type.name === "duration") {
            type = getSdkDurationType(type);
        } else {
            type = getSdkBuiltInType(context, type);
        }
    }
    if (type.kind === "duration" && type.encode === "seconds") {
        return {
            type: sdkScalarKindToPythonKind[type.wireType.kind],
            format: type.encode
        }
    }
    if (type.encode === "unixTimestamp") {
        return {
            type: "unixtime",
            format: type.encode,
        }
    }
    return {
        type: sdkScalarKindToPythonKind[type.kind] || type.kind, // TODO: switch to kind
        format: type.encode,
    };
}

function emitDurationOrDateType(context: SdkContext, type: SdkDurationType | SdkDatetimeType): Record<string, any> {
    return {
        ...emitBuiltInType(context, type),
        wireType: emitBuiltInType(context, type.wireType),
    };
}

function emitArrayOrDict(context: SdkContext, type: SdkArrayType | SdkDictionaryType): Record<string, any> {
    const kind = type.kind === "array" ? "list" : type.kind;
    return {
        type: kind,
        elementType: getType(context, type.valueType),
    };
}

function emitConstant(context: SdkContext, type: StringLiteral | NumericLiteral | BooleanLiteral | SdkConstantType) {
    if (type.kind !== "constant") {
        const convertedType = getSdkConstant(context, type);
        type = convertedType!;
    }
    return {
        type: type.kind,
        value: type.value,
        valueType: emitBuiltInType(context, type.valueType),
    };
}

function capitalize(name: string): string {
    return name[0].toUpperCase() + name.slice(1);
}

function emitUnion(context: SdkContext, type: SdkUnionType | SdkEnumType | Union): Record<string, any> {
    if (type.kind === "union") {
        return {
            name: type.name,
            snakeCaseName: camelToSnakeCase(type.name || ""),
            description: `Type of ${type.name}`,
            internal: true,
            type: "combined",
            types: type.values.map((x) => getType(context, x)),
            xmlMetadata: {},
        };
    } else if (type.kind === "enum") {
        return {
            name: type.name,
            snakeCaseName: camelToSnakeCase(type.name),
            description: type.doc || `Type of ${type.name}`,
            internal: true,
            type: type.kind,
            valueType: emitBuiltInType(context, type.valueType),
            values: type.values.map((x) => emitEnumMember(x)),
            xmlMetadata: {},
        };
    } else {
        return emitUnion(context, getSdkUnion(context, type)! as SdkUnionType);
    }
}

function emitType(context: SdkContext, type: EmitterType | SdkType): Record<string, any> {
    if (type.kind === "Credential") {
        return emitCredential(type.scheme);
    }
    if (type.kind === "CredentialTypeUnion") {
        return emitCredentialUnion(type);
    }

    switch (type.kind) {
        case "model":
            return emitModel(context, type);
        case "union":
            return emitUnion(context, type);
        case "enum":
            return emitEnum(context, type);
        case "constant":
            return emitConstant(context, type)!;
        case "array":
        case "dict":
            return emitArrayOrDict(context, type)!;
        case "datetime":
        case "duration":
            return emitDurationOrDateType(context, type);
        case "bytes":
        case "boolean":
        case "date":
        case "time":
        case "any":
        case "int32":
        case "int64":
        case "float32":
        case "float64":
        case "string":
        case "guid":
        case "url":
        case "uuid":
        case "password":
        case "armId":
        case "ipAddress":
        case "azureLocation":
        case "etag":
            return emitBuiltInType(context, type);
        case "Intrinsic":
            return { type: "any" };
        case "Scalar":
            const result = emitBuiltInType(context, type);
            updateWithEncode(context, type, result);
            return result;
        case "Number":
        case "String":
        case "Boolean":
            return emitConstant(context, type);
        case "Union":
            return emitUnion(context, type);
        case "UnionVariant":
            return {};
        case "Model":
            // only any/dict param Model and lro logical result Model will be left
            return emitArrayOrDict(context, getSdkArrayOrDict(context, type)!);
        default:
            throw Error(`Not supported ${type.kind}`);
    }
}

function updateWithEncode(context: SdkContext, entity: ModelProperty | Scalar, result: Record<string, any>) {
    const encode = getEncode(context.program, entity);
    if (encode) {
        if (encode.encoding === "seconds") {
            result["type"] = encode.type.name.includes("float") ? "float" : "integer";
        } else if (encode.encoding === "rfc7231") {
            result["format"] = "date-time-rfc1123";
        } else if (encode.encoding === "unixTimestamp") {
            result["type"] = "unixtime";
        } else if (encode.encoding === "base64url") {
            result["format"] = "base64url";
        }
    } else if (
        entity.kind === "ModelProperty" &&
        entity.type.kind === "Scalar" &&
        isHeader(context.program, entity) &&
        (entity.type.name === "utcDateTime" || entity.type.name === "offsetDateTime")
    ) {
        result["format"] = "date-time-rfc1123";
    }
}

function emitOperationGroups(context: SdkContext, client: SdkClient): Record<string, any>[] {
    const operationGroups: Record<string, any>[] = [];
    for (const operationGroup of listOperationGroups(context, client)) {
        let operations: Record<string, any>[] = [];
        const name = operationGroup.type.name;
        for (const operation of listOperationsInOperationGroup(context, operationGroup)) {
            operations = operations.concat(emitOperation(context, operation, name));
        }
        operationGroups.push({
            className: name,
            propertyName: name,
            operations: operations,
        });
    }
    let clientOperations: Record<string, any>[] = [];
    for (const operation of listOperationsInOperationGroup(context, client)) {
        clientOperations = clientOperations.concat(emitOperation(context, operation, ""));
    }
    if (clientOperations.length > 0) {
        operationGroups.push({
            className: "",
            propertyName: "",
            operations: clientOperations,
        });
    }
    return operationGroups;
}

function getServerHelper(context: SdkContext, namespace: Namespace): HttpServer | undefined {
    const servers = getServers(context.program, namespace);
    if (servers === undefined) {
        return undefined;
    }
    return servers[0];
}

function emitServerParams(context: SdkContext, namespace: Namespace): Record<string, any>[] {
    const server = getServerHelper(context, namespace);
    if (server === undefined) {
        return [
            {
                optional: false,
                description: "Service host",
                clientName: "endpoint",
                clientDefaultValue: null,
                wireName: "$host",
                location: "path",
                type: KnownTypes.string,
                implementation: "Client",
                inOverload: false,
            },
        ];
    }
    if (server.parameters) {
        const params: Record<string, any>[] = [];
        for (const param of server.parameters.values()) {
            const serverParameter: HttpServerParameter = {
                type: "endpointPath",
                name: param.name,
                param: param,
            };
            const emittedParameter = emitParameter(context, serverParameter, "Client");
            endpointPathParameters.push(emittedParameter);
            if (isApiVersion(context, serverParameter as any) && apiVersionParam === undefined) {
                apiVersionParam = emittedParameter;
                continue;
            }
            params.push(emittedParameter);
        }
        return params;
    } else {
        return [
            {
                optional: false,
                description: "Service host",
                clientName: "endpoint",
                clientDefaultValue: server.url,
                wireName: "$host",
                location: "path",
                type: KnownTypes.string,
                implementation: "Client",
                inOverload: false,
            },
        ];
    }
}

function emitCredentialParam(context: SdkContext, namespace: Namespace): Record<string, any> | undefined {
    const auth = getAuthentication(context.program, namespace);
    if (auth) {
        const credential_types: CredentialType[] = [];
        for (const option of auth.options) {
            for (const scheme of option.schemes) {
                const type: CredentialType = {
                    kind: "Credential",
                    scheme: scheme,
                };
                credential_types.push(type);
            }
        }
        if (credential_types.length > 0) {
            let type: EmitterType;
            if (credential_types.length === 1) {
                type = credential_types[0];
            } else {
                type = {
                    kind: "CredentialTypeUnion",
                    types: credential_types,
                };
            }
            return {
                type: getType(context, type),
                optional: false,
                description: "Credential needed for the client to connect to Azure.",
                clientName: "credential",
                location: "other",
                wireName: "credential",
                implementation: "Client",
                skipUrlEncoding: true,
                inOverload: false,
            };
        }
    }
    return undefined;
}

function emitGlobalParameters(context: SdkContext, namespace: Namespace): Record<string, any>[] {
    const clientParameters = emitServerParams(context, namespace);
    const credentialParam = emitCredentialParam(context, namespace);
    if (credentialParam) {
        clientParameters.push(credentialParam);
    }
    return clientParameters;
}

function getApiVersionParameter(context: SdkContext): Record<string, any> | void {
    const version = getDefaultApiVersion(context, getServiceNamespace(context));
    if (apiVersionParam) {
        return apiVersionParam;
    } else if (version !== undefined) {
        return {
            clientName: "api_version",
            clientDefaultValue: version.value,
            description: "Api Version",
            implementation: "Client",
            location: "query",
            wireName: "api-version",
            skipUrlEncoding: false,
            optional: false,
            inDocString: true,
            inOverload: false,
            inOverridden: false,
            type: getConstantType(version.value),
            isApiVersion: true,
        };
    }
}

function emitClients(context: SdkContext, namespace: string): Record<string, any>[] {
    const clients = listClients(context);
    const retval: Record<string, any>[] = [];
    for (const client of clients) {
        if (getNamespace(context, client.name) !== namespace) {
            continue;
        }
        const server = getServerHelper(context, client.service);
        const emittedClient = {
            name: client.name.split(".").at(-1),
            description: getDocStr(context, client.type),
            parameters: emitGlobalParameters(context, client.service),
            operationGroups: emitOperationGroups(context, client),
            url: server ? server.url : "",
            apiVersions: [],
        };
        const emittedApiVersionParam = getApiVersionParameter(context);
        if (emittedApiVersionParam) {
            emittedClient.parameters.push(emittedApiVersionParam);
        }
        retval.push(emittedClient);
    }
    return retval;
}

function getServiceNamespace(context: SdkContext): Namespace {
    return listServices(context.program)[0].type;
}

function getNamespace(context: SdkContext, clientName: string): string {
    // We get client namespaces from the client name. If there's a dot, we add that to the namespace
    const submodule = clientName.split(".").slice(0, -1).join(".").toLowerCase();
    if (!submodule) {
        return getClientNamespaceString(context)!.toLowerCase();
    }
    return submodule;
}

function getNamespaces(context: SdkContext): Set<string> {
    const namespaces = new Set<string>();
    for (const client of listClients(context)) {
        namespaces.add(getNamespace(context, client.name));
    }
    return namespaces;
}

function emitCodeModel(context: EmitContext<PythonEmitterOptions>) {
    const sdkContext = createSdkContext(context);
    const clientNamespaceString = getClientNamespaceString(sdkContext)?.toLowerCase();
    // Get types
    const codeModel: Record<string, any> = {
        namespace: clientNamespaceString,
        subnamespaceToClients: {},
    };
    for (const model of getAllModels(sdkContext)) {
        getType(sdkContext, model);
    }
    for (const namespace of getNamespaces(sdkContext)) {
        if (namespace === clientNamespaceString) {
            codeModel["clients"] = emitClients(sdkContext, namespace);
        } else {
            codeModel["subnamespaceToClients"][namespace] = emitClients(sdkContext, namespace);
        }
    }
    codeModel["types"] = [...typesMap.values(), ...Object.values(KnownTypes), ...simpleTypesMap.values()];
    return codeModel;
}

const KnownTypes = {
    string: { type: "string" },
    anyObject: { type: "any-object" },
};
