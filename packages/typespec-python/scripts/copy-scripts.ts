import fsExtra from "fs-extra";
import { dirname, join, posix, win32 } from "path";
import { fileURLToPath } from "url";

const force: boolean = process.argv[2] === "--force";
const __dirname = dirname(fileURLToPath(import.meta.url));

function copyAndCreateDir(sourceDir: string, destDir: string) {
    // Delete the destination directory if it exists
    if (fsExtra.existsSync(destDir)) {
        if (force) fsExtra.removeSync(destDir);
        else process.exit(0);
    }

    // Copy the source directory to the destination directory
    fsExtra.copySync(sourceDir, destDir, {
        filter: (src: string) => {
            return !src.replaceAll(win32.sep, posix.sep).includes("/test/");
        },
    });
}

const typespecModulePath: string = join(__dirname, "..", "node_modules", "@typespec", "http-client-python");

// Copy the generator directory
copyAndCreateDir(join(typespecModulePath, "generator"), join(__dirname, "..", "generator"));
