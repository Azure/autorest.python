/* eslint-disable no-console */
import yargs from "yargs";
import { hideBin } from "yargs/helpers";
import { runCommand } from "./utils.js";

interface Arguments {
    folderName: string;
}

// PARSE INPUT ARGUMENTS
const argv = yargs(hideBin(process.argv)).option("folderName", {
    type: "string",
    description: "Specify the flavor",
}).argv as Arguments;

runCommand(`black ${argv.folderName.split(",").join(" ")}`, "black");
