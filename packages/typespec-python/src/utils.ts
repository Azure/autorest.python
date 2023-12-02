import { SdkHeaderParameter, SdkHttpParameter, SdkParameter, SdkQueryParameter, SdkServiceMethod, SdkServiceOperation } from "@azure-tools/typespec-client-generator-core";

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

export function isAbstract<TServiceOperation extends SdkServiceOperation>(method: SdkServiceMethod<TServiceOperation>): boolean {
    return method.operation.bodyParams[0]?.contentTypes.length > 1;
}

export function getDelimeterAndExplode(parameter: SdkQueryParameter | SdkHeaderParameter): [string | undefined, boolean] {
    let delimiter: string | undefined = undefined;
    let explode = false;
    if (parameter.collectionFormat === "csv") {
        delimiter = "comma"
    } else if (parameter.collectionFormat === "ssv") {
        delimiter = "space"
    } else if (parameter.collectionFormat === "tsv") {
        delimiter = "tab";
    } else if (parameter.collectionFormat === "pipes") {
        delimiter = "pipe"
    } else {
        explode = true;
    }
    return [delimiter, explode]
}
