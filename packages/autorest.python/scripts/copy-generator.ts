import { existsSync, removeSync, copySync } from "fs-extra";
import { join, win32, posix } from "path";

const force: boolean = process.argv[2] === "--force";

function copyAndCreateDir(sourceDir: string, destDir: string) {
    // Delete the destination directory if it exists
    if (existsSync(destDir)) {
        if (force) removeSync(destDir);
        else process.exit(0);
    }

    // Copy the source directory to the destination directory
    copySync(sourceDir, destDir, {
        filter: (src: string) => {
            return !src.replaceAll(win32.sep, posix.sep).includes("/test/");
        },
    });
}

const typespecModulePath: string = join(__dirname, "..", "node_modules", "@typespec", "http-client-python");

// Copy the generator directory
copyAndCreateDir(join(typespecModulePath, "generator"), join(__dirname, "..", "generator"));
