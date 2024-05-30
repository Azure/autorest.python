import { EmitContext } from "@typespec/compiler";
import {
    createSdkContext,
    SdkContext,
    SdkHttpOperation,
    SdkServiceOperation,
} from "@azure-tools/typespec-client-generator-core";
import { saveCodeModelAsYaml } from "./external-process.js";
import { dirname } from "path";
import { fileURLToPath } from "url";
import { execFileSync } from "child_process";
import { PythonEmitterOptions, PythonSdkContext } from "./lib.js";
import { emitCodeModel } from "./code-model.js";
import { removeUnderscoresFromNamespace } from "./utils.js";
import path from "path";

export function getModelsMode(context: SdkContext): "dpg" | "none" {
    const specifiedModelsMode = context.emitContext.options["models-mode"];
    if (specifiedModelsMode) {
        const modelModes = ["dpg", "none"];
        if (modelModes.includes(specifiedModelsMode)) {
            return specifiedModelsMode;
        }
        throw new Error(`Need to specify models mode with the following values: ${modelModes.join(", ")}`);
    }
    return "dpg";
}

function addDefaultOptions(sdkContext: SdkContext) {
    const defaultOptions = {
        "package-version": "1.0.0b1",
        "generate-packaging-files": true,
        "flavor": undefined,
    };
    sdkContext.emitContext.options = {
        ...defaultOptions,
        ...sdkContext.emitContext.options,
    };
    const options = sdkContext.emitContext.options;
    options["models-mode"] = getModelsMode(sdkContext);
    if (options["generate-packaging-files"]) {
        options["package-mode"] = sdkContext.arm ? "azure-mgmt" : "azure-dataplane";
    }
    if (!options["package-name"]) {
        options["package-name"] = removeUnderscoresFromNamespace(
            sdkContext.experimental_sdkPackage.rootNamespace.toLowerCase(),
        ).replace(/\./g, "-");
    }
    if (options.flavor !== "azure") {
        // if they pass in a flavor other than azure, we want to ignore the value
        options.flavor = undefined;
    }
    if (!options.flavor && sdkContext.emitContext.emitterOutputDir.includes("azure")) {
        options.flavor = "azure";
    }
}

function createPythonSdkContext<TServiceOperation extends SdkServiceOperation>(
    context: EmitContext<PythonEmitterOptions>,
): PythonSdkContext<TServiceOperation> {
    return {
        ...createSdkContext<PythonEmitterOptions, TServiceOperation>(context, "@azure-tools/typespec-python"),
        __endpointPathParameters: [],
    };
}

export async function $onEmit(context: EmitContext<PythonEmitterOptions>) {
    const program = context.program;
    const sdkContext = createPythonSdkContext<SdkHttpOperation>(context);
    const root = path.join(dirname(fileURLToPath(import.meta.url)), "..", "..", "pygen");
    const outputDir = context.emitterOutputDir;
    const yamlMap = emitCodeModel(sdkContext);
    addDefaultOptions(sdkContext);
    const yamlPath = await saveCodeModelAsYaml("typespec-python-yaml-map", yamlMap);
    const commandArgs = [
        `${root}/scripts/run-python3.cjs`,
        `${root}/scripts/run_tsp.py`,
        `--output-folder=${outputDir}`,
        `--cadl-file=${yamlPath}`,
    ];
    const resolvedOptions = sdkContext.emitContext.options;
    if (resolvedOptions["packaging-files-config"]) {
        const keyValuePairs = Object.entries(resolvedOptions["packaging-files-config"]).map(([key, value]) => {
            return `${key}:${value}`;
        });
        commandArgs.push(`--packaging-files-config='${keyValuePairs.join("|")}'`);
        resolvedOptions["packaging-files-config"] = undefined;
    }
    if (
        resolvedOptions["package-pprint-name"] !== undefined &&
        !resolvedOptions["package-pprint-name"].startsWith('"')
    ) {
        resolvedOptions["package-pprint-name"] = `"${resolvedOptions["package-pprint-name"]}"`;
    }

    for (const [key, value] of Object.entries(resolvedOptions)) {
        commandArgs.push(`--${key}=${value}`);
    }
    if (sdkContext.arm === true) {
        commandArgs.push("--azure-arm=true");
    }
    if (resolvedOptions.flavor === "azure") {
        commandArgs.push("--emit-cross-language-definition-file=true");
    }
    commandArgs.push("--from-typespec=true");
    if (!program.compilerOptions.noEmit && !program.hasError()) {
        execFileSync(process.execPath, commandArgs);
    }
}
