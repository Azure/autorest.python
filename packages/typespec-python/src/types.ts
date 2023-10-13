import { Type } from "@typespec/compiler";
import { HttpAuth, Visibility } from "@typespec/http";
import {
    SdkContext,
    SdkEnumValueType,
    SdkType,
    SdkModelType,
    SdkBodyModelPropertyType,
    SdkUnionType,
    SdkEnumType,
    SdkBuiltInType,
    SdkArrayType,
    SdkDictionaryType,
    SdkConstantType,
    SdkDatetimeType,
    SdkDurationType,
    getClientType,
} from "@azure-tools/typespec-client-generator-core";
import { dump } from "js-yaml";
import { camelToSnakeCase } from "./utils.js";
import { getModelsMode } from "./emitter.js";

export const typesMap = new Map<SdkType, Record<string, any>>();
export const simpleTypesMap = new Map<string | null, Record<string, any>>();

export interface CredentialType {
    kind: "Credential";
    scheme: HttpAuth;
}

export interface CredentialTypeUnion {
    kind: "CredentialTypeUnion";
    types: CredentialType[];
}

function isEmptyModel(type: SdkType): boolean {
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

function getSimpleTypeResult(result: Record<string, any>): Record<string, any> {
    const key = dump(result, { sortKeys: true });
    const value = simpleTypesMap.get(key);
    if (value) {
        result = value;
    } else {
        simpleTypesMap.set(key, result);
    }
    return result;
}

export function getType(
    context: SdkContext,
    type: CredentialType | CredentialTypeUnion | Type | SdkType,
): Record<string, any> {
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
            return emitEnum(type);
        case "enumvalue":
            return emitEnumValueType(context, type);
        case "constant":
            return emitConstant(type)!;
        case "array":
        case "dict":
            return emitArrayOrDict(context, type)!;
        case "datetime":
        case "duration":
            return emitDurationOrDateType(type);
        case "bytes":
        case "boolean":
        case "date":
        case "time":
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
            return emitBuiltInType(type);
        case "any":
            return { type: "any" };
        case "String":
        case "Number":
        case "Boolean":
        case "Model":
        case "Intrinsic":
        case "Scalar":
        case "Enum":
        case "Union":
        case "ModelProperty":
        case "UnionVariant":
            return getType(context, getClientType(context, type));
        default:
            throw Error(`Not supported ${type.kind}`);
    }
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
    return getSimpleTypeResult(credential_type);
}

function emitCredentialUnion(cred_types: CredentialTypeUnion): Record<string, any> {
    const result: Record<string, any> = {};
    // Export as CombinedType, which is already a Union Type in autorest codegen
    result.type = "combined";
    result.types = [];
    for (const cred_type of cred_types.types) {
        result.types.push(emitCredential(cred_type.scheme));
    }

    return getSimpleTypeResult(result);
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
        description: type.description,
        addedOn: type.apiVersions[0],
        visibility: visibilityMapping(type.visibility),
        isDiscriminator: type.discriminator,
    };
}

function emitModel(context: SdkContext, type: SdkModelType): Record<string, any> {
    if (isEmptyModel(type)) {
        return {
            type: "any",
            description: type.description,
        };
    }
    if (typesMap.has(type)) {
        return typesMap.get(type)!;
    }
    const newValue = {
        type: type.kind,
        name: type.name,
        description: type.description,
        parents: type.baseModel ? [getType(context, type.baseModel)] : [],
        discriminatorValue: type.discriminatorValue,
        discriminatedSubtypes: {} as Record<string, Record<string, any>>,
        properties: new Array<Record<string, any>>(),
        snakeCaseName: type.name ? camelToSnakeCase(type.name) : type.name,
        base: type.name === "" ? "json" : getModelsMode(context) === "msrest" ? "msrest" : "dpg",
        internal: type.access === "internal",
    };

    typesMap.set(type, newValue);
    for (const property of type.properties.values()) {
        if (property.kind === "property") {
            newValue.properties.push(emitProperty(context, property));
            // type for base discriminator returned by TCGC changes from constant to string while
            // autorest treat all discriminator as constant type, so we need to change to constant type here
            if (type.discriminatedSubtypes && property.discriminator && property.type.kind === "string") {
                newValue.properties[newValue.properties.length - 1].isPolymorphic = true;
                newValue.properties[newValue.properties.length - 1].type = getConstantType(null);
            }
        }
    }
    if (type.discriminatedSubtypes) {
        for (const key in type.discriminatedSubtypes) {
            newValue.discriminatedSubtypes[key] = getType(context, type.discriminatedSubtypes[key]);
        }
    }
    return newValue;
}

function emitEnum(type: SdkEnumType): Record<string, any> {
    if (typesMap.has(type)) {
        return typesMap.get(type)!;
    }
    const newValue = {
        name: type.name,
        snakeCaseName: camelToSnakeCase(type.name),
        description: type.description || `Type of ${type.name}`,
        internal: type.access === "internal",
        type: type.kind,
        valueType: emitBuiltInType(type.valueType),
        values: type.values.map((x) => emitEnumMember(x)),
        xmlMetadata: {},
    };
    typesMap.set(type, newValue);
    return newValue;
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
        description: type.description,
    };
}

function emitDurationOrDateType(type: SdkDurationType | SdkDatetimeType): Record<string, any> {
    return getSimpleTypeResult({
        ...emitBuiltInType(type),
        wireType: emitBuiltInType(type.wireType),
    });
}

function emitArrayOrDict(context: SdkContext, type: SdkArrayType | SdkDictionaryType): Record<string, any> {
    const kind = type.kind === "array" ? "list" : type.kind;
    return getSimpleTypeResult({
        type: kind,
        elementType: getType(context, type.valueType),
    });
}

function emitConstant(type: SdkConstantType) {
    return getSimpleTypeResult({
        type: type.kind,
        value: type.value,
        valueType: emitBuiltInType(type.valueType),
    });
}

function emitEnumValueType(context: SdkContext, type: SdkEnumValueType): Record<string, any> {
    let valueType = undefined;
    let emittedEnumName = undefined;
    if (type.__raw && 'enum' in type.__raw) {
        const emittedEnum = getType(context, getClientType(context, type.__raw.enum));
        valueType = emittedEnum.valueType;
        emittedEnumName = emittedEnum.name;
    }
    return getSimpleTypeResult({
        name: enumName(type.name),
        type: type.kind,
        value: type.value,
        valueType: valueType,
        enumName: emittedEnumName,
    });
}

const sdkScalarKindToPythonKind: Record<string, string> = {
    int32: "integer",
    int64: "integer",
    float32: "float",
    float64: "float",
};

function emitBuiltInType(type: SdkBuiltInType | SdkDurationType | SdkDatetimeType): Record<string, any> {
    if (type.kind === "duration" && type.encode === "seconds") {
        return getSimpleTypeResult({
            type: sdkScalarKindToPythonKind[type.wireType.kind],
            encode: type.encode,
        });
    }
    if (type.encode === "unixTimestamp") {
        return getSimpleTypeResult({
            type: "unixtime",
            encode: type.encode,
        });
    }
    return getSimpleTypeResult({
        type: sdkScalarKindToPythonKind[type.kind] || type.kind, // TODO: switch to kind
        encode: type.encode,
    });
}

function emitUnion(context: SdkContext, type: SdkUnionType): Record<string, any> {
    return getSimpleTypeResult({
        name: type.name,
        snakeCaseName: camelToSnakeCase(type.name || ""),
        description: `Type of ${type.name}`,
        internal: true,
        type: "combined",
        types: type.values.map((x) => getType(context, x)),
        xmlMetadata: {},
    });
}

export function getConstantType(key: string | null): Record<string, any> {
    const cache = simpleTypesMap.get(key);
    if (cache) {
        return cache;
    }
    const type = {
        apiVersions: [],
        type: "constant",
        value: key,
        valueType: KnownTypes.string,
        xmlMetadata: {},
    };
    simpleTypesMap.set(key, type);
    return type;
}

export const KnownTypes = {
    string: { type: "string" },
    anyObject: { type: "any-object" },
};
