import { runCommand } from "./utils.js";
import yargs from "yargs";
import { hideBin } from "yargs/helpers";

// PARSE INPUT ARGUMENTS
const argv = yargs(hideBin(process.argv))
    .option("folderName", {
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

// Define the commands to run pylint and mypy
const pylintCommand = "pylint generator/";
const mypyCommand = "mypy generator/";



// Run pylint and mypy
runCommand(pylintCommand);
runCommand(mypyCommand);
