import { copyFileSync, readdirSync } from "fs";
import { existsSync, removeSync, copySync } from "fs-extra";
import { join } from "path";

const force: boolean = process.argv[2] === "--force";

function copyAndCreateDir(sourceDir: string, destDir: string) {
    // Delete the destination directory if it exists
    if (existsSync(destDir)) {
        if (force) removeSync(destDir);
        else process.exit(0);
    }

    // Copy the source directory to the destination directory
    copySync(sourceDir, destDir);
}

const typespecModulePath: string = join(__dirname, "..", "node_modules", "@azure-tools", "typespec-python");

// Copy the generator directory
copyAndCreateDir(join(typespecModulePath, "generator"), join(__dirname, "..", "generator"));

// Copy the scripts directory
copyAndCreateDir(join(typespecModulePath, "scripts", "eng"), join(__dirname, "..", "scripts", "eng"));
