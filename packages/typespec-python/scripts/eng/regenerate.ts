/* eslint-disable no-console */
import { exec as execCallback } from "child_process";
import { promisify } from "util";
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import { dirname, join, relative, resolve } from "path";
import { promises, rmSync } from "fs";
import { fileURLToPath } from "url";

// Promisify the exec function
const exec = promisify(execCallback);

// Get the directory of the current file
const PLUGIN_DIR = resolve(fileURLToPath(import.meta.url), "../../../");
const AZURE_HTTP_SPECS = resolve(PLUGIN_DIR, "node_modules/@azure-tools/azure-http-specs/specs");
const HTTP_SPECS = resolve(PLUGIN_DIR, "node_modules/@typespec/http-specs/specs");
interface TspCommand {
    outputDir: string;
    command: string;
}

const EMITTER_OPTIONS: Record<string, Record<string, string> | Record<string, string>[]> = {
    "resiliency/srv-driven/old.tsp": {
        "package-name": "resiliency-srv-driven1",
        "package-mode": "azure-dataplane",
        "package-pprint-name": "ResiliencySrvDriven1",
    },
    "resiliency/srv-driven": {
        "package-name": "resiliency-srv-driven2",
        "package-mode": "azure-dataplane",
        "package-pprint-name": "ResiliencySrvDriven2",
    },
    "authentication/http/custom": {
        "package-name": "authentication-http-custom",
        "package-pprint-name": "Authentication Http Custom Service",
    },
    "authentication/union": {
        "package-name": "authentication-union",
    },
    "type/array": {
        "package-name": "typetest-array",
    },
    "type/dictionary": {
        "package-name": "typetest-dictionary",
    },
    "type/enum/extensible": {
        "package-name": "typetest-enum-extensible",
    },
    "type/enum/fixed": {
        "package-name": "typetest-enum-fixed",
    },
    "type/model/empty": {
        "package-name": "typetest-model-empty",
    },
    "type/model/inheritance/enum-discriminator": {
        "package-name": "typetest-model-enumdiscriminator",
    },
    "type/model/inheritance/nested-discriminator": {
        "package-name": "typetest-model-nesteddiscriminator",
    },
    "type/model/inheritance/not-discriminated": {
        "package-name": "typetest-model-notdiscriminated",
    },
    "type/model/inheritance/single-discriminator": {
        "package-name": "typetest-model-singlediscriminator",
    },
    "type/model/inheritance/recursive": {
        "package-name": "typetest-model-recursive",
    },
    "type/model/usage": {
        "package-name": "typetest-model-usage",
    },
    "type/model/visibility": [
        { "package-name": "typetest-model-visibility" },
        { "package-name": "headasbooleantrue", "head-as-boolean": "true" },
        { "package-name": "headasbooleanfalse", "head-as-boolean": "false" },
    ],
    "type/property/nullable": {
        "package-name": "typetest-property-nullable",
    },
    "type/property/optionality": {
        "package-name": "typetest-property-optional",
    },
    "type/property/additional-properties": {
        "package-name": "typetest-property-additionalproperties",
    },
    "type/scalar": {
        "package-name": "typetest-scalar",
    },
    "type/property/value-types": {
        "package-name": "typetest-property-valuetypes",
    },
    "type/union": {
        "package-name": "typetest-union",
    },
    "azure/core/lro/rpc": {
        "package-name": "azurecore-lro-rpc",
    },
    "client/structure/multi-client": {
        "package-name": "client-structure-multiclient",
    },
    "client/structure/renamed-operation": {
        "package-name": "client-structure-renamedoperation",
    },
    "client/structure/two-operation-group": {
        "package-name": "client-structure-twooperationgroup",
    },
    "client/namespace": {
        "enable-typespec-namespace": "true",
    },
};

function toPosix(dir: string): string {
    return dir.replace(/\\/g, "/");
}

function getEmitterOption(spec: string, flavor: string): Record<string, string>[] {
    const specDir = spec.includes("azure") ? AZURE_HTTP_SPECS : HTTP_SPECS;
    const relativeSpec = toPosix(relative(specDir, spec));
    const key = relativeSpec.includes("resiliency/srv-driven/old.tsp") ? relativeSpec : dirname(relativeSpec);
    const emitter_options = EMITTER_OPTIONS[key] || [{}];
    const result = Array.isArray(emitter_options) ? emitter_options : [emitter_options];

    function updateOptions(options: Record<string, string>): void {
        if (options["package-name"] && options["enable-typespec-namespace"] === undefined) {
            options["enable-typespec-namespace"] = "false";
        }
    }

    if (flavor !== "azure") {
        for (const options of result) {
            if (Array.isArray(options)) {
                for (const option of options) {
                    updateOptions(option);
                }
            } else {
                updateOptions(options);
            }
        }
    }

    return result;
}

// Function to execute CLI commands asynchronously
async function executeCommand(tspCommand: TspCommand): Promise<void> {
    try {
        rmSync(tspCommand.outputDir, { recursive: true, force: true });
    } catch (error) {
        console.error(`rm error: ${error}`);
    }
    try {
        console.log(`exec: ${tspCommand.command}`);
        const { stdout, stderr } = await exec(tspCommand.command);
        if (stdout) console.log(`stdout: ${stdout}`);
        if (stderr) console.error(`stderr: ${stderr}`);
    } catch (error) {
        console.error(`exec error: ${error}`);
        throw error;
    }
}

interface RegenerateFlagsInput {
    flavor?: "azure" | "unbranded";
    debug?: boolean;
    name?: string;
}

interface RegenerateFlags {
    flavor: "azure" | "unbranded";
    debug: boolean;
    name?: string;
}

const SpecialFlags: Record<string, Record<string, any>> = {
    azure: {
        "generate-test": true,
        "generate-sample": true,
    },
};

async function getSubdirectories(baseDir: string, flags: RegenerateFlags): Promise<string[]> {
    const subdirectories: string[] = [];

    async function searchDir(currentDir: string) {
        const items = await promises.readdir(currentDir, { withFileTypes: true });

        const promisesArray = items.map(async (item) => {
            const subDirPath = join(currentDir, item.name);
            if (item.isDirectory()) {
                const mainTspPath = join(subDirPath, "main.tsp");
                const clientTspPath = join(subDirPath, "client.tsp");

                const mainTspRelativePath = toPosix(relative(baseDir, mainTspPath));

                // after fix test generation for nested operation group, remove this check
                if (mainTspRelativePath.includes("client-operation-group")) return;

                // after https://github.com/Azure/autorest.python/issues/3043 fixed, remove this check
                if (mainTspRelativePath.includes("azure/client-generator-core/api-version")) return;

                const hasMainTsp = await promises
                    .access(mainTspPath)
                    .then(() => true)
                    .catch(() => false);
                const hasClientTsp = await promises
                    .access(clientTspPath)
                    .then(() => true)
                    .catch(() => false);

                if (mainTspRelativePath.toLowerCase().includes(flags.name || "")) {
                    if (mainTspRelativePath.includes("resiliency/srv-driven")) {
                        subdirectories.push(resolve(subDirPath, "old.tsp"));
                    }
                    if (hasClientTsp) {
                        subdirectories.push(resolve(subDirPath, "client.tsp"));
                    } else if (hasMainTsp) {
                        subdirectories.push(resolve(subDirPath, "main.tsp"));
                    }
                }

                // Recursively search in the subdirectory
                await searchDir(subDirPath);
            }
        });

        await Promise.all(promisesArray);
    }

    await searchDir(baseDir);
    return subdirectories;
}

function defaultPackageName(spec: string): string {
    const specDir = spec.includes("azure") ? AZURE_HTTP_SPECS : HTTP_SPECS;
    return toPosix(relative(specDir, dirname(spec)))
        .replace(/\//g, "-")
        .toLowerCase();
}

interface EmitterConfig {
    optionsStr: string;
    outputDir: string;
}

function addOptions(spec: string, generatedFolder: string, flags: RegenerateFlags): EmitterConfig[] {
    const emitterConfigs: EmitterConfig[] = [];
    for (const config of getEmitterOption(spec, flags.flavor)) {
        const options: Record<string, string> = { ...config };
        options["flavor"] = flags.flavor;
        for (const [k, v] of Object.entries(SpecialFlags[flags.flavor] ?? {})) {
            options[k] = v;
        }
        if (options["emitter-output-dir"] === undefined) {
            const packageName = options["package-name"] || defaultPackageName(spec);
            options["emitter-output-dir"] = toPosix(`${generatedFolder}/test/${flags.flavor}/generated/${packageName}`);
        }
        if (flags.debug) {
            options["debug"] = "true";
        }
        if (flags.flavor === "unbranded") {
            options["company-name"] = "Unbranded";
        }
        options["examples-dir"] = toPosix(join(dirname(spec), "examples"));
        const configs = Object.entries(options).flatMap(([k, v]) => {
            return `--option @azure-tools/typespec-python.${k}=${typeof v === "string" && v.indexOf(" ") > -1 ? `"${v}"` : v}`;
        });
        emitterConfigs.push({
            optionsStr: configs.join(" "),
            outputDir: options["emitter-output-dir"],
        });
    }
    return emitterConfigs;
}
function _getCmdList(spec: string, flags: RegenerateFlags): TspCommand[] {
    return addOptions(spec, PLUGIN_DIR, flags).map((option) => {
        return {
            outputDir: option.outputDir,
            command: `tsp compile ${spec} --emit=${toPosix(PLUGIN_DIR)} ${option.optionsStr}`,
        };
    });
}

async function runTaskPool(tasks: Array<() => Promise<void>>, poolLimit: number): Promise<void> {
    let currentIndex = 0;

    async function worker() {
        while (currentIndex < tasks.length) {
            const index = currentIndex++;
            await tasks[index]();
        }
    }

    const workers = new Array(Math.min(poolLimit, tasks.length)).fill(null).map(() => worker());
    await Promise.all(workers);
}

async function regenerate(flags: RegenerateFlagsInput): Promise<void> {
    if (flags.flavor === undefined) {
        await regenerate({ ...flags, flavor: "azure" });
        await regenerate({ ...flags, flavor: "unbranded" });
    } else {
        const flagsResolved = { debug: false, flavor: flags.flavor, ...flags };
        const subdirectoriesForAzure = await getSubdirectories(AZURE_HTTP_SPECS, flagsResolved);
        const subdirectoriesForNonAzure = await getSubdirectories(HTTP_SPECS, flagsResolved);
        const subdirectories =
            flags.flavor === "azure"
                ? [...subdirectoriesForAzure, ...subdirectoriesForNonAzure]
                : subdirectoriesForNonAzure;
        const cmdList: TspCommand[] = subdirectories.flatMap((subdirectory) =>
            _getCmdList(subdirectory, flagsResolved),
        );

        // Create tasks as functions for the pool
        const tasks: Array<() => Promise<void>> = cmdList.map((tspCommand) => {
            return () => executeCommand(tspCommand);
        });

        // Run tasks with a concurrency limit
        await runTaskPool(tasks, 30);
    }
}

// PARSE INPUT ARGUMENTS
const argv = yargs(hideBin(process.argv))
    .option("flavor", {
        type: "string",
        choices: ["azure", "unbranded"],
        description: "Specify the flavor",
    })
    .option("debug", {
        alias: "d",
        type: "boolean",
        description: "Debug mode",
    })
    .option("name", {
        alias: "n",
        type: "string",
        description: "Specify filename if you only want to generate a subset",
    }).argv;

const start = performance.now();
regenerate(argv as RegenerateFlags)
    .then(() => console.log(`Regeneration successful, time taken: ${Math.round((performance.now() - start) / 1000)} s`))
    .catch((error) => console.error(`Regeneration failed: ${error.message}`));
