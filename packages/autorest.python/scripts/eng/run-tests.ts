/* eslint-disable no-console */
import { execSync } from "child_process";
import { readFileSync } from "fs";
import { join } from "path";
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import { fileURLToPath } from "url";

interface Arguments {
    validFolders: string[];
    flavor?: string;
    env?: string;
    name?: string;
}

// Note: apiview removed to reduce CI time - it was causing timeouts
const validEnvs = ["ci", "lint", "mypy", "pyright"];

// Parse command-line arguments using yargs
const argv = yargs(hideBin(process.argv))
    .option("validFolders", {
        alias: "vf",
        describe: "Specify the valid folders",
        type: "array",
        default: ["azure", "unbranded"],
    })
    .option("flavor", {
        alias: ["f", "folder"],
        describe: "Specify the flavor/folder to use",
        type: "string",
    })
    .option("env", {
        alias: ["e", "command"],
        describe: "Specify the environment/command to run",
        choices: validEnvs,
        type: "string",
    })
    .option("name", {
        alias: "n",
        describe: "Specify the name of the test",
        type: "string",
    }).argv as Arguments;

const foldersToProcess = argv.flavor ? [argv.flavor] : argv.validFolders;

const envToRun = argv.env || "all";

function getCommand(env: string, folder: string, name?: string): string {
    if (!validEnvs.includes(env)) throw new Error(`Unknown env '${env}'.`);

    // Check if running on Windows
    const isWindows = process.platform === "win32";
    const baseCommand = `tox -c ./test/${folder}/tox.ini -e ${env}`;

    let retval: string;
    if (isWindows) {
        // Windows command format: set FOLDER=value && command
        retval = `set FOLDER=${folder} && ${baseCommand}`;
    } else {
        // Unix/Linux/macOS format: FOLDER=value command
        retval = `FOLDER=${folder} ${baseCommand}`;
    }

    if (name) {
        return `${retval} -- -f ${name}`;
    }
    return retval;
}

function sectionExistsInToxIni(env: string, folder: string): boolean {
    const toxIniPath = join(fileURLToPath(import.meta.url), `../../../test/${folder}/tox.ini`);
    const toxIniContent = readFileSync(toxIniPath, "utf-8");
    const sectionHeader = `[testenv:${env}]`;
    return toxIniContent.includes(sectionHeader);
}

function myExecSync(env: string, folder: string, name?: string): void {
    if (!sectionExistsInToxIni(env, folder)) {
        console.log(`No section for ${env} in tox.ini for folder ${folder}. Skipping...`);
        return;
    }
    execSync(getCommand(env, folder, name), { stdio: "inherit" });
}

foldersToProcess.forEach((folder) => {
    try {
        if (envToRun === "all") {
            for (const key of validEnvs) {
                console.log(`Running ${key} for folder ${folder}...`);
                myExecSync(key, folder, argv.name);
            }
        } else if (getCommand(envToRun, folder, argv.name)) {
            console.log(`Running ${envToRun} for folder ${folder}...`);
            myExecSync(envToRun, folder, argv.name);
        } else {
            console.error(`Error: Unknown env '${envToRun}'.`);
            process.exit(1);
        }
    } catch (error) {
        console.error((error as Error).message);
        console.error(`Error executing command for folder ${folder}: ${(error as Error).message}`);
        process.exit(1);
    }
});
