/* eslint-disable no-console */
import { exec } from "child_process";
import { existsSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import chalk from "chalk";

interface Arguments {
    folderName: string;
    command?: "pylint" | "mypy" | "pyright";
}

const validCommands = ["pylint", "mypy", "pyright"];

// Function to run a command and log the output
function runCommand(command: string, prettyName: string) {
    let pythonPath = join(dirname(fileURLToPath(import.meta.url)), "..", "venv/");
    if (existsSync(join(pythonPath, "bin"))) {
        pythonPath = join(pythonPath, "bin", "python");
    } else if (existsSync(join(pythonPath, "Scripts"))) {
        pythonPath = join(pythonPath, "Scripts", "python");
    } else {
        throw new Error(pythonPath);
    }
    command = `${pythonPath} -m ${command}`;
    exec(command, (error, stdout, stderr) => {
        if (error) {
            console.error(chalk.red(`Error executing ${command}: ${stdout}`));
            return;
        }
        if (stderr) {
            console.error(chalk.yellow(`Error output from ${command}: ${stderr}`));
            return;
        }
        console.log(chalk.green(`${prettyName} passed`));
    });
}

// PARSE INPUT ARGUMENTS
const argv = yargs(hideBin(process.argv))
    .option("folderName", {
        type: "string",
        choices: ["generator", "autorest"],
        description: "Specify the flavor",
        default: "generator",
    })
    .option("command", {
        alias: "c",
        type: "string",
        choices: validCommands,
        description: "Specify the command to run",
    }).argv as Arguments;

export function pylint() {
    runCommand(`pylint ${argv.folderName}/ --rcfile ./scripts/pylintrc`, "pylint");
}

export function mypy() {
    runCommand(`mypy ${argv.folderName}/ --config-file ./scripts/mypy.ini`, "mypy");
}

export function pyright() {
    runCommand(`pyright ${argv.folderName}/ -p ./scripts/pyrightconfig.json`, "pyright");
}

if (argv.command === "pylint") {
    pylint();
} else if (argv.command === "mypy") {
    mypy();
} else if (argv.command === "pyright") {
    pyright();
} else {
    pylint();
    mypy();
    pyright();
}
