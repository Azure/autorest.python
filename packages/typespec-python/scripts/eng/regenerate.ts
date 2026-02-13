/* eslint-disable no-console */
import { exec as execCallback } from "child_process";
import { promisify } from "util";
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import { join, resolve } from "path";
import { promises, rmSync } from "fs";
import { fileURLToPath } from "url";
import {
    BASE_AZURE_EMITTER_OPTIONS,
    BASE_EMITTER_OPTIONS,
    buildOptions,
    regenerate,
    toPosix,
    type RegenerateConfig,
    type RegenerateFlags,
    type RegenerateFlagsInput,
    type TspCommand,
} from "./regenerate-common.js";

// Promisify the exec function
const exec = promisify(execCallback);

// Get the directory of the current file
const PLUGIN_DIR = resolve(fileURLToPath(import.meta.url), "../../../");
const AZURE_HTTP_SPECS = resolve(PLUGIN_DIR, "node_modules/@azure-tools/azure-http-specs/specs");
const HTTP_SPECS = resolve(PLUGIN_DIR, "node_modules/@typespec/http-specs/specs");
const EMITTER_NAME = "@azure-tools/typespec-python";

const AZURE_EMITTER_OPTIONS: Record<string, Record<string, string> | Record<string, string>[]> = {
    ...BASE_AZURE_EMITTER_OPTIONS,
};

const EMITTER_OPTIONS: Record<string, Record<string, string> | Record<string, string>[]> = {
    ...BASE_EMITTER_OPTIONS,
    "type/model/inheritance/recursive": [
        {
            "package-name": "typetest-model-recursive",
            "namespace": "typetest.model.recursive",
        },
        {
            "package-name": "generation-subdir",
            "namespace": "generation.subdir",
            "generation-subdir": "_generated",
            "clear-output-folder": "true",
        },
    ],
    "client/structure/client-operation-group": {
        "package-name": "client-structure-clientoperationgroup",
        "namespace": "client.structure.clientoperationgroup",
    },
    "client/structure/multi-client": {
        "package-name": "client-structure-multiclient",
        "namespace": "client.structure.multiclient",
    },
    "client/structure/renamed-operation": {
        "package-name": "client-structure-renamedoperation",
        "namespace": "client.structure.renamedoperation",
    },
    "client/structure/two-operation-group": {
        "package-name": "client-structure-twooperationgroup",
        "namespace": "client.structure.twooperationgroup",
    },
};

// Function to execute CLI commands asynchronously
async function executeCommand(tspCommand: TspCommand): Promise<void> {
    try {
        const cmd = tspCommand.command as string;
        console.log(`exec: ${cmd}`);
        const { stdout, stderr } = await exec(cmd);
        if (stdout) console.log(`stdout: ${stdout}`);
        if (stderr) console.error(`stderr: ${stderr}`);
    } catch (error) {
        console.error(`exec error: ${error}`);
        rmSync(tspCommand.outputDir, { recursive: true, force: true });
        throw error;
    }
}

// create some files before regeneration. After regeneration, these files should be deleted and we will test it
// in test case
async function preprocess(flags: RegenerateFlagsInput): Promise<void> {
    if (flags.flavor === "azure") {
        const generalParts = [PLUGIN_DIR, "test", "azure", "generated"];
        await promises.writeFile(
            join(
                ...generalParts,
                "authentication-api-key",
                "authentication",
                "apikey",
                "_operations",
                "to_be_deleted.py",
            ),
            "# This file is to be deleted after regeneration",
        );

        const folderParts = [...generalParts, "generation-subdir"];
        await promises.writeFile(
            join(...folderParts, "generation", "subdir", "_generated", "to_be_deleted.py"),
            "# This file is to be deleted after regeneration",
        );
        await promises.writeFile(
            join(...folderParts, "generated_tests", "to_be_deleted.py"),
            "# This file is to be kept after regeneration",
        );
        await promises.writeFile(
            join(...folderParts, "generation", "subdir", "to_be_kept.py"),
            "# This file is to be kept after regeneration",
        );
    }
}

function _getCmdList(spec: string, flags: RegenerateFlags): TspCommand[] {
    return buildOptions(spec, PLUGIN_DIR, flags, config).map((po) => {
        const optionsStr = Object.entries(po.options).flatMap(([k, v]) => {
            return `--option ${EMITTER_NAME}.${k}=${typeof v === "string" && v.indexOf(" ") > -1 ? `"${v}"` : v}`;
        }).join(" ");
        return {
            outputDir: po.outputDir,
            command: `tsp compile ${spec} --emit=${toPosix(PLUGIN_DIR)} ${optionsStr}`,
        };
    });
}

const config: RegenerateConfig = {
    azureHttpSpecs: AZURE_HTTP_SPECS,
    httpSpecs: HTTP_SPECS,
    emitterOptions: EMITTER_OPTIONS,
    azureEmitterOptions: AZURE_EMITTER_OPTIONS,
    preprocess,
    getCmdList: _getCmdList,
    executeCommand,
};

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
regenerate(argv as RegenerateFlags, config)
    .then(() => console.log(`Regeneration successful, time taken: ${Math.round((performance.now() - start) / 1000)} s`))
    .catch((error) => console.error(`Regeneration failed: ${error.message}`));
