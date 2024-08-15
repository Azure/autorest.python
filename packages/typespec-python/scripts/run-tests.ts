/* eslint-disable no-console */
import { execSync } from "child_process";
import yargs from "yargs";
import { hideBin } from "yargs/helpers";

interface Arguments {
    folder: string;
    command?: string;
}
const validCommands = ["ci", "lint", "mypy", "pyright", "apiview"];

// Parse command-line arguments using yargs
const argv = yargs(hideBin(process.argv))
    .option("folder", {
        alias: "f",
        describe: "Specify the folder to use",
        choices: ["azure", "unbranded"],
        demandOption: true,
        type: "string",
    })
    .option("command", {
        alias: "c",
        describe: "Specify the command to run",
        choices: validCommands,
        type: "string",
    }).argv as Arguments;

const folder = argv.folder;
const commandToRun = argv.command || "all";

const commands: Record<string, string> = {
    ci: `FOLDER=${folder} tox -c ./test/${folder}/tox.ini -e ci`,
    lint: `FOLDER=${folder} tox -c ./test/${folder}/tox.ini -e lint`,
    mypy: `FOLDER=${folder} tox -c ./test/${folder}/tox.ini -e mypy`,
    pyright: `FOLDER=${folder} tox -c ./test/${folder}/tox.ini -e pyright`,
    apiview: `FOLDER=${folder} tox -c ./test/${folder}/tox.ini -e apiview`,
};

try {
    if (commandToRun === "all") {
        for (const key in commands) {
            console.log(`Running ${key}...`);
            execSync(commands[key], { stdio: "inherit" });
        }
    } else if (commands[commandToRun]) {
        console.log(`Running ${commandToRun}...`);
        execSync(commands[commandToRun], { stdio: "inherit" });
    } else {
        console.error(`Error: Unknown command '${commandToRun}'.`);
        process.exit(1);
    }
} catch (error) {
    console.error(`Error executing command: ${(error as Error).message}`);
    process.exit(1);
}
