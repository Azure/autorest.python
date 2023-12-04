import { EmitContext } from "@typespec/compiler";
import { createSdkContext, SdkContext, SdkHttpOperation } from "@azure-tools/typespec-client-generator-core";
import { resolveModuleRoot, saveCodeModelAsYaml } from "./external-process.js";
import { dirname } from "path";
import { fileURLToPath } from "url";
import { execFileSync } from "child_process";
import { PythonEmitterOptions } from "./lib.js";
import { emitCodeModel } from "./code-model.js";

const defaultOptions = {
  "package-version": "1.0.0b1",
  "generate-packaging-files": true,
  "unbranded": false,
};

export function getModelsMode(context: SdkContext): "msrest" | "dpg" | "none" {
  const specifiedModelsMode = context.emitContext.options["models-mode"];
  if (specifiedModelsMode) {
    const modelModes = ["msrest", "dpg", "none"];
    if (modelModes.includes(specifiedModelsMode)) {
      return specifiedModelsMode;
    }
    throw new Error(`Need to specify models mode with the following values: ${modelModes.join(", ")}`);
  }
  if (context.arm) return "msrest";
  return "dpg";
}

function addDefaultCalculatedOptions(
  sdkContext: SdkContext,
  options: PythonEmitterOptions & InternalPythonEmitterOptions,
  yamlMap: Record<string, any>,
) {
  options["models-mode"] = getModelsMode(sdkContext);
  if (options["generate-packaging-files"]) {
    options["package-mode"] = sdkContext.arm ? "azure-mgmt" : "azure-dataplane";
  }
  if (!options["package-name"]) {
    options["package-name"] = yamlMap["namespace"].replace(/\./g, "-");
  }
}

interface InternalPythonEmitterOptions {
  "package-mode"?: string;
}

export async function $onEmit(context: EmitContext<PythonEmitterOptions>) {
  const program = context.program;
  const resolvedOptions: PythonEmitterOptions & InternalPythonEmitterOptions = {
    ...defaultOptions,
    ...context.options,
  };

  const sdkContext = createSdkContext<SdkHttpOperation>(context, "@azure-tools/typespec-python");
  const root = await resolveModuleRoot(program, "@autorest/python", dirname(fileURLToPath(import.meta.url)));
  const outputDir = context.emitterOutputDir;
  const yamlMap = emitCodeModel(sdkContext);
  const yamlPath = await saveCodeModelAsYaml("typespec-python-yaml-map", yamlMap);
  addDefaultCalculatedOptions(sdkContext, resolvedOptions, yamlMap);
  const commandArgs = [
    `${root}/run-python3.js`,
    `${root}/run_cadl.py`,
    `--output-folder=${outputDir}`,
    `--cadl-file=${yamlPath}`,
  ];
  if (resolvedOptions["packaging-files-config"]) {
    const keyValuePairs = Object.entries(resolvedOptions["packaging-files-config"]).map(([key, value]) => {
      return `${key}:${value}`;
    });
    commandArgs.push(`--packaging-files-config='${keyValuePairs.join("|")}'`);
    resolvedOptions["packaging-files-config"] = undefined;
  }

  for (const [key, value] of Object.entries(resolvedOptions)) {
    if (value !== undefined) {
      commandArgs.push(`--${key}=${value}`);
    }
  }
  if (resolvedOptions.debug) {
    commandArgs.push("--debug");
  }
  if (sdkContext.arm === true) {
    commandArgs.push("--azure-arm=true");
  }
  commandArgs.push("--from-typespec=true");
  if (!program.compilerOptions.noEmit && !program.hasError()) {
    execFileSync(process.execPath, commandArgs);
  }
}
