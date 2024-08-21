import { existsSync, removeSync, copySync } from "fs-extra";
import { join } from "path";

const force: boolean = process.argv[2] === "--force";

const typespecModulePath: string = join(__dirname, "..", "node_modules", "@azure-tools", "typespec-python");

// Define the source and destination directories
const sourceDir: string = join(typespecModulePath, "generator");
const destDir: string = join(__dirname, "..", "generator");

// Delete the destination directory if it exists
if (existsSync(destDir)) {
    if (force) removeSync(destDir);
    else process.exit(0);
}

// Copy the source directory to the destination directory
copySync(sourceDir, destDir);
