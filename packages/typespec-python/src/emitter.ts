import { getPagedResult, getLroMetadata } from "@azure-tools/typespec-azure-core";
import {
    EnumMember,
    Enum,
    getDoc,
    getFriendlyName,
    getMaxLength,
    getMaxValue,
    getMinLength,
    getMinValue,
    getPattern,
    getSummary,
    getVisibility,
    ignoreDiagnostics,
    isErrorModel,
    isNeverType,
    Model,
    ModelProperty,
    Namespace,
    getEffectiveModelType,
    getDiscriminator,
    Operation,
    isKey,
    Scalar,
    EmitContext,
    listServices,
    Union,
    isNullType,
    SyntaxKind,
    Type,
    getNamespaceFullName,
    IntrinsicType,
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
    HttpOperationResponseContent,
    HttpServer,
    isStatusCode,
    HttpOperation,
    isHeader,
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
    getClientFormat,
    createSdkContext,
    SdkContext,
    getPropertyNames,
    getLibraryName,
    getAllModels,
    isInternal,
    getSdkSimpleType,
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

type EmitterType = Type | CredentialType | CredentialTypeUnion;

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
            .replace(/\s+/g, "_")
            .replace(/\$/g, "")
            .replace(/-/g, "_")
            .replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`);

    return camelToSnakeCaseRe(name[0].toLowerCase() + name.slice(1));
}

const typesMap = new Map<EmitterType, Record<string, any>>();
const simpleTypesMap = new Map<string, Record<string, any>>();
const endpointPathParameters: Record<string, any>[] = [];
let apiVersionParam: Record<string, any> | undefined = undefined;

function isSimpleType(context: SdkContext, type: EmitterType | undefined): boolean {
    // these decorators can only work for simple type(int/string/float, etc)
    if (type && (type.kind === "Scalar" || type.kind === "ModelProperty")) {
        const funcs = [getMinValue, getMaxValue, getMinLength, getMaxLength, getPattern];
        for (const func of funcs) {
            if (func(context.program, type)) {
                return true;
            }
        }
    }
    return false;
}

function getDocStr(context: SdkContext, target: Type): string {
    return getDoc(context.program, target) ?? "";
}

function handleDiscriminator(context: SdkContext, type: Model, model: Record<string, any>) {
    const discriminator = getDiscriminator(context.program, type);
    if (discriminator) {
        let discriminatorProperty;
        for (const childModel of type.derivedModels) {
            const modelType = getType(context, childModel);
            for (const property of modelType.properties) {
                if (property.restApiName === discriminator.propertyName) {
                    modelType.discriminatorValue = property.type.value;
                    property.isDiscriminator = true;
                    model.discriminatedSubtypes[property.type.value] = modelType;
                    discriminatorProperty = property;
                }
            }
        }
        // it is not included in properties of cadl but needed by python codegen
        if (discriminatorProperty) {
            const discriminatorType = { ...discriminatorProperty.type };
            discriminatorType.value = null;
            const propertyCopy = {
                ...discriminatorProperty,
                isPolymorphic: true,
                type: discriminatorType,
            };
            propertyCopy.description = "";
            model.properties.push(propertyCopy);
        }
    }
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

function getEntityType(context: SdkContext, entity: ModelProperty): any {
    const result = getType(context, entity.type);
    const format = getClientFormat(context, entity);
    if (format) {
        if (format === "rfc1123") {
            result["format"] = "date-time-rfc1123";
        } else if (format === "iso8601") {
            result["format"] = "date-time";
        }
    }
    return result;
}

function getType(context: SdkContext, type: EmitterType): any {
    // don't cache simple type(string, int, etc) since decorators may change the result
    const program = context.program;
    const enableCache = !isSimpleType(context, type);
    const effectiveModel = type.kind === "Model" ? getEffectiveSchemaType(context, type) : type;
    if (enableCache) {
        const cached = typesMap.get(effectiveModel);
        if (cached) {
            return cached;
        }
    }
    let newValue = emitType(context, type);
    if (enableCache) {
        typesMap.set(effectiveModel, newValue);
        if (type.kind === "Model") {
            // need to do properties after insertion to avoid infinite recursion
            for (const property of type.properties.values()) {
                if (isStatusCode(program, property) || isNeverType(property.type) || isHeader(program, property)) {
                    continue;
                }
                newValue.properties.push(emitProperty(context, property));
            }
            // need to do discriminator outside `emitModel` to avoid infinite recursion
            handleDiscriminator(context, type, newValue);
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
    type: Type;
    restApiName: string;
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
                        bodyModel.templateArguments &&
                        bodyModel.templateArguments.some((it) => {
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
        restApiName: body.parameter?.name ?? "body",
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
    let type = getEntityType(context, parameter.param);
    let clientDefaultValue = undefined;
    if (parameter.name.toLowerCase() === "content-type" && type["type"] === "constant") {
        /// We don't want constant types for content types, so we make sure if it's
        /// a constant, we make it not constant
        clientDefaultValue = type["value"];
        type = type["valueType"];
    }
    const paramMap: Record<string, any> = {
        restApiName: parameter.type === "path" ? parameter.param.name : parameter.name,
        location: parameter.type,
        type: type,
        implementation: implementation,
        skipUrlEncoding: parameter.type === "endpointPath",
    };
    if (type.type === "list" && (parameter.type === "query" || parameter.type === "header")) {
        if (parameter.format === "csv") {
            paramMap["delimiter"] = "comma";
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
        restApiName: "Content-Type",
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
        restApiName: null,
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
        restApiName: "Accept",
        skipUrlEncoding: false,
        type: getConstantType("application/json"),
    };
}

function emitResponseHeaders(context: SdkContext, headers?: Record<string, ModelProperty>): Record<string, any>[] {
    const retval: Record<string, any>[] = [];
    if (!headers) {
        return retval;
    }
    for (const [key, value] of Object.entries(headers)) {
        retval.push({
            type: getEntityType(context, value),
            restApiName: key,
        });
    }
    return retval;
}

function isAzureCoreModel(t: Type): boolean {
    return (
        t.kind === "Model" &&
        t.namespace !== undefined &&
        ["Azure.Core", "Azure.Core.Foundations"].includes(getNamespaceFullName(t.namespace))
    );
}

function emitResponse(
    context: SdkContext,
    response: HttpOperationResponse,
    innerResponse: HttpOperationResponseContent,
): Record<string, any> {
    let type = undefined;
    if (innerResponse.body?.type) {
        let modelType = undefined;
        if (innerResponse.body.type.kind === "Model") {
            modelType = getEffectiveSchemaType(context, innerResponse.body.type);
        }
        if (modelType && !isAzureCoreModel(modelType)) {
            type = getType(context, modelType);
        } else if (modelType && ["CustomPage", "Page"].includes(modelType.name)) {
            // hacky sorry. we want a dummy type here so we get the accept parameter
            // we don't want to generate the paged models
            type = getType(context, Array.from(modelType.properties.values())[0].type);
        } else if (!modelType) {
            type = getType(context, innerResponse.body.type);
        }
    }
    const statusCodes = [];
    if (response.statusCode === "*") {
        statusCodes.push("default");
    } else {
        statusCodes.push(parseInt(response.statusCode));
    }
    return {
        headers: emitResponseHeaders(context, innerResponse.headers),
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

function addLroInformation(emittedOperation: Record<string, any>, initialOperation: Record<string, any>) {
    emittedOperation["discriminator"] = "lro";
    emittedOperation["initialOperation"] = initialOperation;
    emittedOperation["exposeStreamKeyword"] = false;
}

function addPagingInformation(context: SdkContext, operation: Operation, emittedOperation: Record<string, any>) {
    emittedOperation["discriminator"] = "paging";
    const pagedResult = getPagedResult(context.program, operation);
    if (pagedResult === undefined) {
        throw Error("Trying to add paging information, but not paging metadata for this operation");
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
    const initialOperation = emitBasicOperation(
        context,
        getLroMetadata(context.program, operation)!.operation,
        operationGroupName,
    )[0];
    initialOperation["name"] = `_${initialOperation["name"]}_initial`;
    initialOperation["isLroInitialOperation"] = true;
    initialOperation["wantTracing"] = false;
    initialOperation["exposeStreamKeyword"] = false;
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
        addLroInformation(emittedOperation, initialOperation);
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
        addLroInformation(emittedOperation, initialOperation);
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
        for (const innerResponse of response.responses) {
            const emittedResponse = emitResponse(context, response, innerResponse);
            if (
                emittedResponse["type"] &&
                parameters.filter((e) => e.restApiName.toLowerCase() === "accept").length === 0
            ) {
                parameters.push(emitAcceptParameter(isOverload, isOverriden));
            }
            if (isErrorModel(context.program, response.type)) {
                // * is valid status code in cadl but invalid for autorest.python
                if (response.statusCode === "*") {
                    exceptions.push(emittedResponse);
                }
            } else {
                responses.push(emittedResponse);
            }
        }
    }

    let bodyParameter: Record<string, any> | undefined;
    if (httpOperation.parameters.body === undefined) {
        bodyParameter = undefined;
    } else {
        bodyParameter = emitBodyParameter(context, httpOperation);
        if (parameters.filter((e) => e.restApiName.toLowerCase() === "content-type").length === 0) {
            parameters.push(emitContentTypeParameter(bodyParameter, isOverload, isOverriden));
        }
        if (bodyParameter.type.type === "model" && bodyParameter.type.base === "json") {
            bodyParameter["propertyToParameterName"] = {};
            if (!isOverload) {
                bodyParameter.defaultToUnsetSentinel = true;
            }
            for (const property of bodyParameter.type.properties) {
                bodyParameter["propertyToParameterName"][property["restApiName"]] = property["clientName"];
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

function isReadOnly(context: SdkContext, type: ModelProperty): boolean {
    // https://microsoft.github.io/cadl/standard-library/rest/operations#automatic-visibility
    // Only "read" should be readOnly
    const visibility = getVisibility(context.program, type);
    if (visibility) {
        return visibility.includes("read");
    } else {
        return false;
    }
}

function emitProperty(context: SdkContext, property: ModelProperty): Record<string, any> {
    let clientDefaultValue = undefined;
    const propertyDefaultKind = property.default?.kind;
    if (
        property.default &&
        (propertyDefaultKind === "Number" || propertyDefaultKind === "String" || propertyDefaultKind === "Boolean")
    ) {
        clientDefaultValue = property.default.value;
    }
    const [clientName, jsonName] = getPropertyNames(context, property);
    return {
        clientName: camelToSnakeCase(clientName),
        restApiName: jsonName,
        type: getEntityType(context, property),
        optional: property.optional,
        description: getDocStr(context, property),
        addedOn: getAddedOnVersion(context, property),
        readonly: isReadOnly(context, property) || isKey(context.program, property),
        clientDefaultValue: clientDefaultValue,
    };
}

function getName(context: SdkContext, type: Model): string {
    const friendlyName = getFriendlyName(context.program, type);
    if (friendlyName) {
        return friendlyName;
    } else {
        const modelName = getLibraryName(context, type);
        if (type.templateArguments && type.templateArguments.length > 0) {
            return modelName + type.templateArguments.map((it) => (it.kind === "Model" ? it.name : "")).join("");
        } else {
            return modelName;
        }
    }
}

function emitModel(context: SdkContext, type: Model): Record<string, any> {
    // Now we know it's a defined model
    const properties: Record<string, any>[] = [];
    let baseModel = undefined;
    if (type.baseModel) {
        baseModel = getType(context, type.baseModel);
    }
    const modelName = getName(context, type) || getEffectiveSchemaType(context, type).name;
    return {
        type: "model",
        name: modelName,
        description: getDocStr(context, type),
        parents: baseModel ? [baseModel] : [],
        discriminatedSubtypes: {},
        properties: properties,
        addedOn: getAddedOnVersion(context, type),
        snakeCaseName: modelName ? camelToSnakeCase(modelName) : modelName,
        base: modelName === "" ? "json" : "dpg",
        internal: isInternal(context, type),
    };
}

function intOrFloat(value: number): string {
    return value.toString().indexOf(".") === -1 ? "integer" : "float";
}

function enumName(name: string): string {
    if (name.toUpperCase() === name) {
        return name;
    }
    return camelToSnakeCase(name).toUpperCase();
}

function emitEnum(context: SdkContext, type: Enum): Record<string, any> {
    const enumValues = [];
    for (const m of type.members.values()) {
        enumValues.push({
            name: enumName(m.name),
            value: m.value ?? m.name,
            description: getDocStr(context, m),
        });
    }

    return {
        type: "enum",
        name: type.name,
        description: getDocStr(context, type),
        valueType: { type: enumMemberType(type.members.values().next().value) },
        values: enumValues,
    };
    function enumMemberType(member: EnumMember) {
        if (typeof member.value === "number") {
            return intOrFloat(member.value);
        }
        return "string";
    }
}

function constantType(value: any, valueType: string): Record<string, any> {
    return { type: "constant", value: value, valueType: { type: valueType } };
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

function emitSimpleType(context: SdkContext, type: Scalar | IntrinsicType): Record<string, any> {
    const sdkType = getSdkSimpleType(context, type);
    const extraInformation: Record<string, any> = {};
    if (sdkType.kind === "string") {
        extraInformation["pattern"] = sdkType.pattern;
        extraInformation["minLength"] = sdkType.minLength;
        extraInformation["maxLength"] = sdkType.maxLength;
    } else if (
        sdkType.kind === "int32" ||
        sdkType.kind === "int64" ||
        sdkType.kind === "float32" ||
        sdkType.kind === "float64"
    ) {
        extraInformation["minValue"] = sdkType.minValue;
        extraInformation["maxValue"] = sdkType.maxValue;
    }
    return {
        type: sdkScalarKindToPythonKind[sdkType.kind] || sdkType.kind, // TODO: switch to kind
        doc: sdkType.doc,
        apiVersions: sdkType.apiVersions,
        sdkDefaultValue: sdkType.sdkDefaultValue,
        format: sdkType.format,
        ...extraInformation,
    };
}

function emitListOrDict(context: SdkContext, type: Model): Record<string, any> | undefined {
    if (type.indexer !== undefined) {
        if (isNeverType(type.indexer.key)) {
        } else {
            const name = type.indexer.key.name;
            const elementType = type.indexer.value!;
            if (name === "string") {
                if (elementType.kind === "Intrinsic") {
                }
                return { type: "dict", elementType: getType(context, type.indexer.value!) };
            } else if (name === "integer") {
                return { type: "list", elementType: getType(context, type.indexer.value!) };
            }
        }
    }
    return undefined;
}

function mapCadlType(context: SdkContext, type: Type): any {
    switch (type.kind) {
        case "Number":
            return constantType(type.value, intOrFloat(type.value));
        case "String":
            return constantType(type.value, "string");
        case "Boolean":
            return constantType(type.value, "boolean");
        case "Model":
            return emitListOrDict(context, type);
    }
}

function capitalize(name: string): string {
    return name[0].toUpperCase() + name.slice(1);
}

function emitUnion(context: SdkContext, type: Union): Record<string, any> {
    const nonNullOptions = [...type.variants.values()].map((x) => x.type).filter((t) => !isNullType(t));

    const notLiteral = (t: Type): boolean => ["Boolean", "Number", "String"].indexOf(t.kind) < 0;
    if (nonNullOptions.every(notLiteral)) {
        if (nonNullOptions.length === 1) {
            // Generate as internal type if there is only one internal type in this Union.
            return emitType(context, nonNullOptions[0]);
        }
        // Generate as CombinedType if non of the options is Literal.
        const unionName = type.name;
        return {
            name: unionName,
            snakeCaseName: camelToSnakeCase(unionName || ""),
            description: `Type of ${unionName}`,
            internal: true,
            type: "combined",
            types: nonNullOptions.map((x) => getType(context, x)),
            xmlMetadata: {},
        };
    } else if (nonNullOptions.some(notLiteral)) {
        // Can't generate if this union is a mixed up of literals and sub-types
        throw Error(`Can't do union for ${JSON.stringify(nonNullOptions)}`);
    }

    // Geneate Union of Literals as Python Enum
    const values: Record<string, any>[] = [];
    for (const option of nonNullOptions) {
        const value = emitType(context, option)["value"];
        values.push({
            description: "",
            name: camelToSnakeCase(value).toUpperCase(),
            value: value,
        });
    }
    let enumName = "MyEnum";
    if (
        type.node &&
        type.node.parent &&
        [SyntaxKind.ModelStatement, SyntaxKind.ModelProperty].includes(type.node.parent.kind)
    ) {
        if (type.node.parent.kind === SyntaxKind.ModelStatement) {
            enumName = capitalize(type.node.parent.id.sv);
        } else if (type.node.parent.kind === SyntaxKind.ModelProperty) {
            const parent = type.node.parent as any;
            if (parent.id.sv) {
                enumName = capitalize(parent.id.sv) + "Type";
            }
        }
    }
    return {
        name: enumName,
        snakeCaseName: camelToSnakeCase(enumName),
        description: `Type of ${enumName}`,
        internal: true,
        type: "enum",
        valueType: emitType(context, nonNullOptions[0])["valueType"],
        values: values,
        xmlMetadata: {},
    };
}

function emitType(context: SdkContext, type: EmitterType): Record<string, any> {
    if (type.kind === "Credential") {
        return emitCredential(type.scheme);
    }
    if (type.kind === "CredentialTypeUnion") {
        return emitCredentialUnion(type);
    }
    const builtinType = mapCadlType(context, type);
    if (builtinType !== undefined) {
        // add in description elements for types derived from primitive types (SecureString, etc.)
        const doc = getDoc(context.program, type);
        if (doc) {
            builtinType.description = doc;
        }
        return builtinType;
    }

    switch (type.kind) {
        case "Intrinsic":
            return { type: "any" };
        case "Model":
            return emitModel(context, type);
        case "Scalar":
            return emitSimpleType(context, type);
        case "Union":
            return emitUnion(context, type);
        case "UnionVariant":
            return {};
        case "Enum":
            return emitEnum(context, type);
        default:
            throw Error(`Not supported ${type.kind}`);
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
                restApiName: "$host",
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
                restApiName: "$host",
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
                restApiName: "credential",
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
            restApiName: "api-version",
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
};
