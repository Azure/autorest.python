import {
  SdkContext,
  SdkHeaderParameter,
  SdkHttpParameter,
  SdkParameter,
  SdkQueryParameter,
  SdkServiceMethod,
  SdkServiceOperation,
} from "@azure-tools/typespec-client-generator-core";
import { getType } from "./types.js";
import { getNamespaceFullName, Type } from "@typespec/compiler";

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

export function getImplementation(parameter: SdkParameter | SdkHttpParameter): "client" | "method" {
  if (parameter.onClient) return "client";
  return "method";
}

export function isAbstract<TServiceOperation extends SdkServiceOperation>(
  method: SdkServiceMethod<TServiceOperation>,
): boolean {
  return method.operation.bodyParams[0]?.contentTypes.length > 1;
}

export function getDelimeterAndExplode(
  parameter: SdkQueryParameter | SdkHeaderParameter,
): [string | undefined, boolean] {
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

export function emitParamBase<TServiceOperation extends SdkServiceOperation>(
  context: SdkContext<TServiceOperation>,
  parameter: SdkParameter | SdkHttpParameter,
): ParamBase {
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

export function isAzureCoreModel(t: Type | undefined): boolean {
  if (!t) return false;
  return (
    t.kind === "Model" &&
    t.namespace !== undefined &&
    ["Azure.Core", "Azure.Core.Foundations"].includes(getNamespaceFullName(t.namespace))
  );
}
