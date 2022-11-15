import { getPagedResult } from "@azure-tools/cadl-azure-core";
import {
    EnumMember,
    Enum,
    getDoc,
    getFriendlyName,
    getIntrinsicModelName,
    getMaxLength,
    getMaxValue,
    getMinLength,
    getMinValue,
    getPattern,
    getServiceNamespace,
    getServiceNamespaceString,
    getSummary,
    getVisibility,
    ignoreDiagnostics,
    isErrorModel,
    isNeverType,
    Model,
    ModelProperty,
    Namespace,
    Program,
    resolvePath,
    Type,
    getEffectiveModelType,
    JSONSchemaType,
    createCadlLibrary,
    getDiscriminator,
    Operation,
    isKey,
} from "@cadl-lang/compiler";
import {
    getAuthentication,
    getContentTypes,
    getHeaderFieldName,
    getHttpOperation,
    getPathParamName,
    getQueryParamName,
    getServers,
    HttpAuth,
    HttpOperationParameter,
    HttpOperationParameters,
    HttpOperationResponse,
    HttpOperationResponseContent,
    HttpServer,
    isStatusCode,
} from "@cadl-lang/rest/http";
import { getAddedOn, getVersions } from "@cadl-lang/versioning";
import { execFileSync } from "child_process";
import { dump } from "js-yaml";
import {
    Client,
    listClients,
    listOperationGroups,
    listOperationsInOperationGroup,
    isApiVersion,
    getDefaultApiVersion,
} from "@azure-tools/cadl-dpg";
import { getResourceOperation } from "@cadl-lang/rest";

interface HttpServerParameter {
    type: "endpointPath";
    name: string;
    param: ModelProperty;
}

interface CredentialType {
    kind: "Credential";
    scheme: HttpAuth;
}

export interface EmitterOptions {
    "basic-setup-py": boolean;
    "package-version": string;
    "package-name": string;
    "output-path": string;
}

const EmitterOptionsSchema: JSONSchemaType<EmitterOptions> = {
    type: "object",
    additionalProperties: false,
    properties: {
        "basic-setup-py": { type: "boolean", nullable: true },
        "package-version": { type: "string", nullable: true },
        "package-name": { type: "string", nullable: true },
        "output-path": { type: "string", nullable: true },
    },
    required: [],
};

const defaultOptions = {
    "basic-setup-py": true,
    "package-version": "1.0.0b1",
};

export const $lib = createCadlLibrary({
    name: "MyEmitter",
    diagnostics: {},
    emitter: {
        options: EmitterOptionsSchema,
    },
});

export async function $onEmit(program: Program, options: EmitterOptions) {
    const resolvedOptions = { ...defaultOptions, ...options };
    const yamlMap = createYamlEmitter(program);
    const root = process.cwd();
    const outputFolder = resolvedOptions["output-path"] ?? program.compilerOptions.outputPath!;
    const yamlPath = resolvePath(outputFolder, "output.yaml");
    const commandArgs = [
        `${root}/node_modules/@autorest/python/run-python3.js`,
        `${root}/node_modules/@autorest/python/run_cadl.py`,
        `--output-folder=${outputFolder}`,
        `--cadl-file=${yamlPath}`,
    ];
    for (const [key, value] of Object.entries(resolvedOptions)) {
        commandArgs.push(`--${key}=${value}`);
    }
    if (
        program.compilerOptions.trace?.includes("*") ||
        program.compilerOptions.trace?.includes("@azure-tools/cadl-python") ||
        program.compilerOptions.trace?.includes("@azure-tools/cadl-python.*")
    ) {
        commandArgs.push("--debug");
    }
    if (!program.compilerOptions.noEmit && !program.hasError()) {
        // TODO: change behavior based off of https://github.com/microsoft/cadl/issues/401
        await program.host.writeFile(yamlPath, dump(yamlMap));
        execFileSync(process.execPath, commandArgs);
    }
}

function camelToSnakeCase(name: string): string {
    const camelToSnakeCaseRe = (str: string) =>
        str
            .replace(/\s+/g, "_")
            .replace(/\$/g, "")
            .replace(/-/g, "_")
            .replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`);

    return camelToSnakeCaseRe(name[0].toLowerCase() + name.slice(1));
}

const typesMap = new Map<Type | CredentialType, Record<string, any>>();
const simpleTypesMap = new Map<string, Record<string, any>>();
const endpointPathParameters: Record<string, any>[] = [];
let apiVersionParam: Record<string, any> | undefined = undefined;

function isSimpleType(program: Program, modelTypeProperty: ModelProperty | undefined): boolean {
    // these decorators can only work for simple type(int/string/float, etc)
    if (modelTypeProperty) {
        const funcs = [getMinValue, getMaxValue, getMinLength, getMaxLength, getPattern];
        for (const func of funcs) {
            if (func(program, modelTypeProperty)) {
                return true;
            }
        }
    }
    return false;
}

function getDocStr(program: Program, target: Type): string {
    return getDoc(program, target) ?? "";
}

function isLro(program: Program, operation: Operation): boolean {
    for (const decorator of operation.decorators) {
        if (decorator.decorator.name === "$pollingOperation") {
            return true;
        }
    }
    return false;
}

function handleDiscriminator(program: Program, type: Model, model: Record<string, any>) {
    const discriminator = getDiscriminator(program, type);
    if (discriminator) {
        let discriminatorProperty;
        for (const childModel of type.derivedModels) {
            const modelType = getType(program, childModel);
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

function getEffectiveSchemaType(program: Program, type: Model): Model {
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

function getType(
    program: Program,
    type: Type | CredentialType,
    modelTypeProperty: ModelProperty | undefined = undefined,
): any {
    // don't cache simple type(string, int, etc) since decorators may change the result
    const enableCache = !isSimpleType(program, modelTypeProperty);
    if (enableCache) {
        const cached = typesMap.get(type);
        if (cached) {
            return cached;
        }
        if (type.kind === "Model") {
            const modelName = getName(program, type);
            for (const key of typesMap.keys()) {
                if (key.kind === "Model" && getName(program, key) === modelName) {
                    return typesMap.get(key);
                }
            }
        }
    }
    let newValue = emitType(program, type, modelTypeProperty);
    if (enableCache) {
        typesMap.set(type, newValue);
        if (type.kind === "Model") {
            // need to do properties after insertion to avoid infinite recursion
            for (const property of type.properties.values()) {
                if (isStatusCode(program, property)) {
                    continue;
                }
                newValue.properties.push(emitProperty(program, property));
            }
            // need to do discriminator outside `emitModel` to avoid infinite recursion
            handleDiscriminator(program, type, newValue);
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
function getAddedOnVersion(p: Program, t: Type): string | undefined {
    return getAddedOn(p as any, t as any)?.value;
}

function emitParamBase(program: Program, parameter: ModelProperty | Type): Record<string, any> {
    let optional: boolean;
    let name: string;
    let description: string = "";
    let addedOn: string | undefined;

    if (parameter.kind === "ModelProperty") {
        optional = parameter.optional;
        name = parameter.name;
        description = getDocStr(program, parameter);
        addedOn = getAddedOnVersion(program, parameter);
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

function emitBodyParameter(
    program: Program,
    bodyType: Type,
    params: HttpOperationParameters,
    operation: Operation,
): Record<string, any> {
    const base = emitParamBase(program, params.bodyParameter ?? bodyType);
    const contentTypeParam = params.parameters.find((p) => p.type === "header" && p.name === "content-type");
    const contentTypes = contentTypeParam
        ? ignoreDiagnostics(getContentTypes(contentTypeParam.param))
        : ["application/json"];
    if (contentTypes.length !== 1) {
        throw Error("Currently only one kind of content-type!");
    }
    let type;
    const resourceOperation = getResourceOperation(program, operation);
    if (resourceOperation) {
        type = getType(program, resourceOperation.resourceType);
    } else if (params.bodyParameter) {
        type = getType(program, params.bodyParameter.type, params.bodyParameter);
    } else {
        type = getType(program, bodyType);
    }

    return {
        contentTypes,
        type,
        restApiName: params.bodyParameter?.name ?? "body",
        location: "body",
        ...base,
        defaultContentType: contentTypes.includes("application/json") ? "application/json" : contentTypes[0],
    };
}

function emitParameter(
    program: Program,
    parameter: HttpOperationParameter | HttpServerParameter,
    implementation: string,
): Record<string, any> {
    const base = emitParamBase(program, parameter.param);
    let type = getType(program, parameter.param.type, parameter.param);
    let clientDefaultValue = undefined;
    if (parameter.name.toLowerCase() === "content-type" && type["type"] === "constant") {
        /// We don't want constant types for content types, so we make sure if it's
        /// a constant, we make it not constant
        clientDefaultValue = type["value"];
        type = type["valueType"];
    }
    const paramMap: Record<string, any> = {
        restApiName: parameter.name,
        location: parameter.type,
        type: type,
        implementation: implementation,
    };

    if (paramMap.type.type === "constant") {
        clientDefaultValue = paramMap.type.value;
    }

    if (isApiVersion(program, parameter as HttpOperationParameter)) {
        const defaultApiVersion = getDefaultApiVersion(program, getServiceNamespace(program));
        paramMap.type = defaultApiVersion ? getConstantType(defaultApiVersion.value) : KnownTypes.string;
        paramMap.implementation = "Client";
        paramMap.in_docstring = false;
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

function emitAcceptParameter(program: Program, inOverload: boolean, inOverriden: boolean): Record<string, any> {
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

function emitResponseHeaders(program: Program, headers?: Record<string, ModelProperty>): Record<string, any>[] {
    const retval: Record<string, any>[] = [];
    if (!headers) {
        return retval;
    }
    for (const [key, value] of Object.entries(headers)) {
        retval.push({
            type: getType(program, value.type),
            restApiName: key,
        });
    }
    return retval;
}

function isAzureCoreErrorType(t?: Type): boolean {
    if (t?.kind !== "Model" || !["Error", "ErrorResponse", "InnerError"].includes(t.name)) return false;
    const namespaces = ".Azure.Core.Foundations".split(".");
    while (
        namespaces.length > 0 &&
        (t?.kind === "Model" || t?.kind === "Namespace") &&
        t.namespace?.name === namespaces.pop()
    ) {
        t = t.namespace;
    }
    return namespaces.length == 0;
}

function emitResponse(
    program: Program,
    response: HttpOperationResponse,
    innerResponse: HttpOperationResponseContent,
): Record<string, any> {
    let type = undefined;
    if (innerResponse.body?.type && !isAzureCoreErrorType(innerResponse.body?.type)) {
        // temporary logic. It can be removed after compiler optimize the response
        const candidate = ["ResourceOkResponse", "ResourceCreatedResponse", "AcceptedResponse"];
        const originType = innerResponse.body.type as Model;
        if (innerResponse.body.type.kind == "Model" && candidate.find((e) => e === originType.name)) {
            const modelType = getEffectiveSchemaType(program, originType);
            type = getType(program, modelType);
        } else {
            type = getType(program, innerResponse.body.type);
        }
    }
    const statusCodes = [];
    if (response.statusCode === "*") {
        statusCodes.push("default");
    } else {
        statusCodes.push(parseInt(response.statusCode));
    }
    return {
        headers: emitResponseHeaders(program, innerResponse.headers),
        statusCodes: statusCodes,
        addedOn: getAddedOnVersion(program, response.type),
        discriminator: "basic",
        type: type,
    };
}

function emitOperation(program: Program, operation: Operation, operationGroupName: string): Record<string, any> {
    const lro = isLro(program, operation);
    const paging = getPagedResult(program, operation);
    if (lro && paging) {
        return emitLroPagingOperation(program, operation, operationGroupName);
    } else if (paging) {
        return emitPagingOperation(program, operation, operationGroupName);
    } else if (lro) {
        return emitLroOperation(program, operation, operationGroupName);
    }
    return emitBasicOperation(program, operation, operationGroupName);
}

function addLroInformation(emittedOperation: Record<string, any>) {
    emittedOperation["discriminator"] = "lro";
}

function addPagingInformation(program: Program, operation: Operation, emittedOperation: Record<string, any>) {
    emittedOperation["discriminator"] = "paging";
    const pagedResult = getPagedResult(program, operation);
    if (pagedResult === undefined) {
        throw Error("Trying to add paging information, but not paging metadata for this operation");
    }
    emittedOperation["itemName"] = pagedResult.itemsPath;
    emittedOperation["continuationTokenName"] = pagedResult.nextLinkPath;
}

function emitLroPagingOperation(
    program: Program,
    operation: Operation,
    operationGroupName: string,
): Record<string, any> {
    const emittedOperation = emitBasicOperation(program, operation, operationGroupName);
    addLroInformation(emittedOperation);
    addPagingInformation(program, operation, emittedOperation);
    emittedOperation["discriminator"] = "lropaging";
    return emittedOperation;
}

function emitLroOperation(program: Program, operation: Operation, operationGroupName: string): Record<string, any> {
    const emittedOperation = emitBasicOperation(program, operation, operationGroupName);
    addLroInformation(emittedOperation);
    return emittedOperation;
}

function emitPagingOperation(program: Program, operation: Operation, operationGroupName: string): Record<string, any> {
    const emittedOperation = emitBasicOperation(program, operation, operationGroupName);
    addPagingInformation(program, operation, emittedOperation);
    return emittedOperation;
}

function emitBasicOperation(program: Program, operation: Operation, operationGroupName: string): Record<string, any> {
    // Set up parameters for operation
    const parameters: Record<string, any>[] = [];
    if (endpointPathParameters) {
        for (const param of endpointPathParameters) {
            parameters.push(param);
        }
    }
    const httpOperation = ignoreDiagnostics(getHttpOperation(program, operation));
    for (const param of httpOperation.parameters.parameters) {
        const emittedParam = emitParameter(program, param, "Method");
        if (isApiVersion(program, param) && apiVersionParam === undefined) {
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
            const emittedResponse = emitResponse(program, response, innerResponse);
            if (
                emittedResponse["type"] &&
                parameters.filter((e) => e.restApiName.toLowerCase() === "accept").length === 0
            ) {
                parameters.push(emitAcceptParameter(program, isOverload, isOverriden));
            }
            if (isErrorModel(program, response.type)) {
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
    if (httpOperation.parameters.bodyType === undefined) {
        bodyParameter = undefined;
    } else {
        bodyParameter = emitBodyParameter(
            program,
            httpOperation.parameters.bodyType,
            httpOperation.parameters,
            operation,
        );
        if (parameters.filter((e) => e.restApiName.toLowerCase() === "content-type").length === 0) {
            parameters.push(emitContentTypeParameter(bodyParameter, isOverload, isOverriden));
        }
    }
    const name = camelToSnakeCase(operation.name);
    return {
        name: name,
        description: getDocStr(program, operation),
        summary: getSummary(program, operation),
        url: httpOperation.path,
        method: httpOperation.verb.toUpperCase(),
        parameters: parameters,
        bodyParameter: bodyParameter,
        responses: responses,
        exceptions: exceptions,
        groupName: operationGroupName,
        addedOn: getAddedOnVersion(program, operation),
        discriminator: "basic",
        isOverload: false,
        overloads: [],
        apiVersions: [getAddedOnVersion(program, operation)],
    };
}

function emitString(program: Program, modelTypeProperty: ModelProperty | undefined): Record<string, any> {
    let maxLength = undefined;
    let minLength = undefined;
    let pattern = undefined;
    if (modelTypeProperty) {
        maxLength = getMaxLength(program, modelTypeProperty);
        minLength = getMinLength(program, modelTypeProperty);
        pattern = getPattern(program, modelTypeProperty);
    }
    if (!(maxLength || minLength || pattern)) {
        return KnownTypes.string;
    }
    return { minLength, maxLength, pattern, type: "string" };
}

function emitNumber(type: string, program: Program, modelTypeProperty: ModelProperty | undefined): Record<string, any> {
    let minimum = undefined;
    let maximum = undefined;
    if (modelTypeProperty) {
        minimum = getMinValue(program, modelTypeProperty);
        maximum = getMaxValue(program, modelTypeProperty);
    }

    if (!(maximum || minimum)) {
        return { type };
    }
    return { minimum, maximum, type };
}

function isReadOnly(program: Program, type: ModelProperty): boolean {
    const visibility = getVisibility(program, type);
    if (visibility) {
        return !visibility.includes("write");
    } else {
        return false;
    }
}

function emitProperty(program: Program, property: ModelProperty): Record<string, any> {
    let clientDefaultValue = undefined;
    const propertyDefaultKind = property.default?.kind;
    if (
        property.default &&
        (propertyDefaultKind === "Number" || propertyDefaultKind === "String" || propertyDefaultKind == "Boolean")
    ) {
        clientDefaultValue = property.default.value;
    }
    return {
        clientName: camelToSnakeCase(property.name),
        restApiName: property.name,
        type: getType(program, property.type, property),
        optional: property.optional,
        description: getDocStr(program, property),
        addedOn: getAddedOnVersion(program, property),
        readonly: isReadOnly(program, property) || isKey(program, property),
        clientDefaultValue: clientDefaultValue,
    };
}

function getName(program: Program, type: Model): string {
    const friendlyName = getFriendlyName(program, type);
    if (friendlyName) {
        return friendlyName;
    } else {
        if (type.templateArguments && type.templateArguments.length > 0) {
            return type.name + type.templateArguments.map((it) => (it.kind === "Model" ? it.name : "")).join("");
        } else {
            return type.name;
        }
    }
}

function emitModel(program: Program, type: Model, modelTypeProperty: ModelProperty | undefined): Record<string, any> {
    if (type.indexer) {
        if (isNeverType(type.indexer.key)) {
        } else {
            const name = getIntrinsicModelName(program, type.indexer.key);
            const elementType = type.indexer.value!;
            if (name === "string") {
                if (elementType.kind === "Intrinsic") {
                }
                return { type: "dict", elementType: getType(program, type.indexer.value!) };
            } else if (name === "integer") {
                return { type: "list", elementType: getType(program, type.indexer.value!) };
            }
        }
    }

    for (const decorator of type.decorators) {
        if (decorator.decorator.name === "$knownValues") {
            for (const arg of decorator.args) {
                if (typeof arg.value === "object" && arg.value.kind === "Enum") {
                    const enumResult = emitEnum(program, arg.value);
                    enumResult["name"] = type.name;
                    return enumResult;
                }
            }
        }
    }
    const name = getIntrinsicModelName(program, type);
    switch (name) {
        case "bytes":
            return { type: "byte-array", format: "byte" };
        case "int8":
        case "int16":
        case "int32":
        case "int64":
        case "safeint":
        case "uint8":
        case "uint16":
        case "uint32":
        case "uint64":
            return emitNumber("integer", program, modelTypeProperty);
        case "float32":
        case "float64":
            return emitNumber("float", program, modelTypeProperty);
        case "string":
            return emitString(program, modelTypeProperty);
        case "boolean":
            return { type: "boolean" };
        case "plainDate":
            return { type: "date" };
        case "zonedDateTime":
            return { type: "datetime", format: "date-time" };
        case "plainTime":
            return { type: "time" };
        case "duration":
            return { type: "duration" };
        default:
            // Now we know it's a defined model
            const properties: Record<string, any>[] = [];
            let baseModel = undefined;
            if (type.baseModel) {
                baseModel = getType(program, type.baseModel);
            }
            const modelName = getName(program, type);
            return {
                type: "model",
                name: modelName,
                description: getDocStr(program, type),
                parents: baseModel ? [baseModel] : [],
                discriminatedSubtypes: {},
                properties: properties,
                addedOn: getAddedOnVersion(program, type),
                snakeCaseName: modelName ? camelToSnakeCase(modelName) : modelName,
            };
    }
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

function emitEnum(program: Program, type: Enum): Record<string, any> {
    const enumValues = [];
    for (const m of type.members.values()) {
        enumValues.push({
            name: enumName(m.name),
            value: m.value ?? m.name,
            description: getDocStr(program, m),
        });
    }

    return {
        type: "enum",
        name: type.name,
        description: getDocStr(program, type),
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

function emitType(
    program: Program,
    type: Type | CredentialType,
    modelTypeProperty: ModelProperty | undefined = undefined,
): Record<string, any> {
    switch (type.kind) {
        case "Number":
            return constantType(type.value, intOrFloat(type.value));
        case "String":
            return constantType(type.value, "string");
        case "Boolean":
            return constantType(type.value, "boolean");
        case "Model":
            return emitModel(program, type, modelTypeProperty);
        case "Enum":
            return emitEnum(program, type);
        case "Credential":
            return emitCredential(type.scheme);
        case "Intrinsic":
            return { type: "any" };
        case "Union":
            const values: Record<string, any>[] = [];
            for (const option of type.options) {
                const value = emitType(program, option)["value"];
                values.push({
                    description: "",
                    name: camelToSnakeCase(value).toUpperCase(),
                    value: value,
                });
            }
            const enumName = modelTypeProperty ? capitalize(modelTypeProperty.name) + "Type" : "MyEnum";
            return {
                name: enumName,
                snakeCaseName: camelToSnakeCase(enumName),
                description: modelTypeProperty ? `Type of ${modelTypeProperty.name}.` : "n/a",
                isPublic: false,
                type: "enum",
                valueType: emitType(program, type.options[0])["valueType"],
                values: values,
                xmlMetadata: {},
            };
        default:
            throw Error(`Not supported ${type.kind}`);
    }
}

function capitalize(name: string): string {
    return name[0].toUpperCase() + name.slice(1);
}

function emitOperationGroups(program: Program, client: Client): Record<string, any>[] {
    const operationGroups: Record<string, any>[] = [];
    for (const operationGroup of listOperationGroups(program, client)) {
        const operations: Record<string, any>[] = [];
        const name = operationGroup.type.name;
        for (const operation of listOperationsInOperationGroup(program, operationGroup)) {
            operations.push(emitOperation(program, operation, name));
        }
        operationGroups.push({
            className: name,
            propertyName: name,
            operations: operations,
        });
    }
    const clientOperations: Record<string, any>[] = [];
    for (const operation of listOperationsInOperationGroup(program, client)) {
        clientOperations.push(emitOperation(program, operation, ""));
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

function getServerHelper(program: Program, namespace: Namespace): HttpServer | undefined {
    const servers = getServers(program, namespace);
    if (servers === undefined) {
        return undefined;
    }
    return servers[0];
}

function emitServerParams(program: Program, namespace: Namespace): Record<string, any>[] {
    const server = getServerHelper(program, namespace);
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
            const emittedParameter = emitParameter(program, serverParameter, "Client");
            endpointPathParameters.push(emittedParameter);
            if (isApiVersion(program, serverParameter as any) && apiVersionParam == undefined) {
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

function emitCredentialParam(program: Program, namespace: Namespace): Record<string, any> | undefined {
    const auth = getAuthentication(program, namespace);
    if (auth) {
        for (const option of auth.options) {
            for (const scheme of option.schemes) {
                const type: CredentialType = {
                    kind: "Credential",
                    scheme: scheme,
                };
                const credential_type = getType(program, type);
                if (credential_type) {
                    return {
                        type: credential_type,
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
        }
    }
    return undefined;
}

function emitGlobalParameters(program: Program, namespace: Namespace): Record<string, any>[] {
    const clientParameters = emitServerParams(program, namespace);
    const credentialParam = emitCredentialParam(program, namespace);
    if (credentialParam) {
        clientParameters.push(credentialParam);
    }
    const version = getDefaultApiVersion(program, getServiceNamespace(program));
    if (apiVersionParam) {
        clientParameters.push(apiVersionParam);
    } else if (version !== undefined) {
        clientParameters.push({
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
        });
    }
    return clientParameters;
}

function emitClients(program: Program, namespace: string): Record<string, any>[] {
    const clients = listClients(program);
    const retval: Record<string, any>[] = [];
    for (const client of clients) {
        if (getNamespace(program, client.name) !== namespace) {
            continue;
        }
        const server = getServerHelper(program, client.service);
        retval.push({
            name: client.name.split(".").at(-1),
            description: getDocStr(program, client.type),
            operationGroups: emitOperationGroups(program, client),
            parameters: emitGlobalParameters(program, client.service),
            url: server ? server.url : "",
            apiVersions: [],
        });
    }
    return retval;
}

function getNamespace(program: Program, clientName: string): string {
    // We get client namespaces from the client name. If there's a dot, we add that to the namespace
    const submodule = clientName.split(".").slice(0, -1).join(".").toLowerCase();
    if (!submodule) {
        return getServiceNamespaceString(program)!.toLowerCase();
    }
    return submodule;
}

function getNamespaces(program: Program): Set<string> {
    const namespaces = new Set<string>();
    for (const client of listClients(program)) {
        namespaces.add(getNamespace(program, client.name));
    }
    return namespaces;
}

function createYamlEmitter(program: Program) {
    const serviceNamespace = getServiceNamespace(program);
    if (serviceNamespace === undefined) {
        throw Error("Can not emit yaml for a namespace that doesn't exist.");
    }

    const serviceNamespaceString = getServiceNamespaceString(program)!.toLowerCase();
    // Get types
    const codeModel: Record<string, any> = {
        namespace: serviceNamespaceString,
        subnamespaceToClients: {},
    };
    for (const namespace of getNamespaces(program)) {
        if (namespace === serviceNamespaceString) {
            codeModel["clients"] = emitClients(program, namespace);
        } else {
            codeModel["subnamespaceToClients"][namespace] = emitClients(program, namespace);
        }
    }
    codeModel["types"] = [...typesMap.values(), ...Object.values(KnownTypes), ...simpleTypesMap.values()];
    return codeModel;
}

const KnownTypes = {
    string: { type: "string" },
};
