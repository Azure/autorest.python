/* eslint-disable no-console */
import { execSync } from "child_process";
import { readFileSync } from "fs";
import { join } from "path";
import yargs from "yargs";
import { hideBin } from "yargs/helpers";

interface Arguments {
    validFolders: string[];
    folder?: string;
    command?: string;
}

const validFolders = ["azure", "unbranded"];

const validCommands = ["ci", "lint", "mypy", "pyright", "apiview"];

// Parse command-line arguments using yargs
const argv = yargs(hideBin(process.argv))
    .option("validFolders", {
        alias: "vf",
        describe: "Specify the valid folders",
        type: "array",
        default: validFolders,
    })
    .option("folder", {
        alias: "f",
        describe: "Specify the folder to use",
        choices: validFolders,
        type: "string",
    })
    .option("command", {
        alias: "c",
        describe: "Specify the command to run",
        choices: validCommands,
        type: "string",
    }).argv as Arguments;

const foldersToProcess = argv.folder ? [argv.folder] : argv.validFolders;

const commandToRun = argv.command || "all";

function getCommand(command: string, folder: string) {
    if (!validCommands.includes(command)) throw new Error(`Unknown command '${command}'.`);
    return `FOLDER=${folder} tox -c ./test/${folder}/tox.ini -e ${command}`;
}

function sectionExistsInToxIni(command: string, folder: string): boolean {
    const toxIniPath = join(__dirname, `../test/${folder}/tox.ini`);
    const toxIniContent = readFileSync(toxIniPath, "utf-8");
    const sectionHeader = `[testenv:${command}]`;
    return toxIniContent.includes(sectionHeader);
}

function myExecSync(command: string, folder: string): void {
    if (!sectionExistsInToxIni(command, folder)) {
        console.log(`No section for ${command} in tox.ini for folder ${folder}. Skipping...`);
        return;
    }
    execSync(getCommand(command, folder), { stdio: "inherit" });
}

foldersToProcess.forEach((folder) => {
    try {
        if (commandToRun === "all") {
            for (const key of validCommands) {
                console.log(`Running ${key} for folder ${folder}...`);
                myExecSync(key, folder);
            }
        } else if (getCommand(commandToRun, folder)) {
            console.log(`Running ${commandToRun} for folder ${folder}...`);
            myExecSync(commandToRun, folder);
        } else {
            console.error(`Error: Unknown command '${commandToRun}'.`);
            process.exit(1);
        }
    } catch (error) {
        console.error((error as Error).message);
        console.error(`Error executing command for folder ${folder}: ${(error as Error).message}`);
        process.exit(1);
    }
});
