/* eslint-disable no-console */
import { exec } from "child_process";
import { existsSync } from "fs";
import { dirname, join } from "path";
import { fileURLToPath } from "url";
import chalk from "chalk";

// Function to run a command and log the output
export function runCommand(command: string, prettyName: string) {
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
            console.error(chalk.red(`Error executing ${command}: ${stderr || stdout}`));
            return;
        }
        if (stderr) {
            // Process stderr output
            console.log(chalk.yellow(`${command}:\n${stderr}`));
        }
        console.log(chalk.green(`${prettyName} passed`));
    });
}
