/* eslint-disable no-console */
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import { runCommand } from "./utils.js";

interface Arguments {
    folderName: string;
    command?: "pylint" | "mypy" | "pyright";
}

const validCommands = ["pylint", "mypy", "pyright"];

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
