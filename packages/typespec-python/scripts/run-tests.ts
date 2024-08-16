/* eslint-disable no-console */
import { execSync } from "child_process";
import yargs from "yargs";
import { hideBin } from "yargs/helpers";

interface Arguments {
    folder?: string;
    command?: string;
}

const validFolders = ["azure", "unbranded"];

const validCommands = ["ci", "lint", "mypy", "pyright", "apiview"];

// Parse command-line arguments using yargs
const argv = yargs(hideBin(process.argv))
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

const foldersToProcess = argv.folder ? [argv.folder] : validFolders;

const commandToRun = argv.command || "all";

function getCommand(command: string, folder: string) {
    if (!validCommands.includes(command)) throw new Error(`Unknown command '${command}'.`);
    return `FOLDER=${folder} tox -c ./test/${folder}/tox.ini -e ${command}`;
}

foldersToProcess.forEach((folder) => {
    try {
        if (commandToRun === "all") {
            for (const key of validCommands) {
                console.log(`Running ${key} for folder ${folder}...`);
                execSync(getCommand(key, folder), { stdio: "inherit" });
            }
        } else if (getCommand(commandToRun, folder)) {
            console.log(`Running ${commandToRun} for folder ${folder}...`);
            execSync(getCommand(commandToRun, folder), { stdio: "inherit" });
        } else {
            console.error(`Error: Unknown command '${commandToRun}'.`);
            process.exit(1);
        }
    } catch (error) {
        console.error(`Error executing command for folder ${folder}: ${(error as Error).message}`);
        process.exit(1);
    }
});
