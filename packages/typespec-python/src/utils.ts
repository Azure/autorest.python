import {
  SdkHeaderParameter,
  SdkHttpParameter,
  SdkMethod,
  SdkModelPropertyType,
  SdkParameter,
  SdkQueryParameter,
  SdkServiceMethod,
  SdkServiceOperation,
  SdkType,
} from "@azure-tools/typespec-client-generator-core";
import { getSimpleTypeResult, getType } from "./types.js";
import { getNamespaceFullName } from "@typespec/compiler";
import { PythonSdkContext } from "./lib.js";

export function camelToSnakeCase(name: string): string {
  if (!name) return name;
  const camelToSnakeCaseRe = (str: string) =>
    str
      .replace(/[^a-zA-Z0-9]/g, "_")
      .replace(/[A-Z]/g, (letter) => `_${letter.toLowerCase()}`)
      .replace(/_+/g, "_");

  return camelToSnakeCaseRe(name[0].toLowerCase() + name.slice(1));
}

export function removeUnderscoresFromNamespace(name?: string): string {
  // needed because of the _specs_ tests
  return (name || "").replace(/_/g, "");
}

export function getImplementation(parameter: SdkParameter | SdkHttpParameter): "Client" | "Method" {
  if (parameter.onClient) return "Client";
  return "Method";
}

export function isAbstract<TServiceOperation extends SdkServiceOperation>(
  method: SdkServiceMethod<TServiceOperation>,
): boolean {
  return method.operation.bodyParams[0]?.contentTypes.length > 1;
}

export function getDelimeterAndExplode(
  parameter: SdkQueryParameter | SdkHeaderParameter,
): [string | undefined, boolean] {
  if (parameter.type.kind !== "array") return [undefined, false];
  let delimiter: string | undefined = undefined;
  let explode = false;
  if (parameter.collectionFormat === "csv") {
    delimiter = "comma";
  } else if (parameter.collectionFormat === "ssv") {
    delimiter = "space";
  } else if (parameter.collectionFormat === "tsv") {
    delimiter = "tab";
  } else if (parameter.collectionFormat === "pipes") {
    delimiter = "pipe";
  } else {
    explode = true;
  }
  return [delimiter, explode];
}

type ParamBase = {
  optional: boolean;
  description: string;
  addedOn: string | undefined;
  clientName: string;
  inOverload: boolean;
  isApiVersion: boolean;
  type: Record<string, any>;
};

export function getAddedOn<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  parameter: SdkModelPropertyType,
): string | undefined {
  // We only want added on if it's not the same as the client's added on
  if (parameter.apiVersions[0] === context.experimental_sdkPackage.clients[0].apiVersions[0]) return undefined;
  return parameter.apiVersions[0];
}

export function emitParamBase<TServiceOperation extends SdkServiceOperation>(
  context: PythonSdkContext<TServiceOperation>,
  parameter: SdkParameter | SdkHttpParameter,
  fromBody: boolean = false,
): ParamBase {
  let type = getType(context, parameter.type, fromBody);
  if (parameter.isApiVersionParam) {
    if (parameter.clientDefaultValue) {
       type = getSimpleTypeResult({ type: "constant", value: parameter.clientDefaultValue, valueType: type });
    }
  }
  return {
    optional: parameter.optional,
    description: parameter.description || "",
    addedOn: getAddedOn(context, parameter),
    clientName: camelToSnakeCase(parameter.nameInClient),
    inOverload: false,
    isApiVersion: parameter.isApiVersionParam,
    type,
  };
}

export function isAzureCoreModel(t: SdkType | undefined): boolean {
  if (!t) return false;
  const tspType = t.__raw;
  if (!tspType) return false;
  return (
    tspType.kind === "Model" &&
    tspType.namespace !== undefined &&
    ["Azure.Core", "Azure.Core.Foundations"].includes(getNamespaceFullName(tspType.namespace))
  );
}

export function getDescriptionAndSummary<TServiceOperation extends SdkServiceOperation>(
  method: SdkMethod<TServiceOperation>,
): { description?: string; summary?: string } {
  if (method.details) {
    return {
      description: method.details,
      summary: method.description,
    };
  }
  return {
    description: method.description ?? "",
  };
}

export function capitalize(name: string): string {
  return name[0].toUpperCase() + name.slice(1);
}
