import { copyFileSync, readdirSync } from "fs";
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



// Define the source and destination directories for the scripts
const scriptsSourceDir: string = join(typespecModulePath, "scripts");
const scriptsDestDir: string = join(__dirname, "..", "scripts");

// Read the contents of the source directory
const files = readdirSync(scriptsSourceDir);

const filesToCopy = [
    "run-tests.ts",
    "pylintrc",
    "mypy.ini",
    "pyrightconfig.json",
]

// Filter and copy .ts files to the destination directory
files.filter(file => filesToCopy.includes(file)).forEach(file => {
    const sourceFile = join(scriptsSourceDir, file);
    const destFile = join(scriptsDestDir, file);

    copyFileSync(sourceFile, destFile);
});
