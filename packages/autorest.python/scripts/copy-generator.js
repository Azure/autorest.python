const { realpath, stat, readFile } = require("fs/promises");
const fs = require("fs-extra");
const path = require("path");

async function resolveAndCopy() {
    let resolved;

    // Resolve @azure-tools/typespec-python module path
    try {
        const module = await import("@azure-tools/typespec-python");

        const host = {
            realpath,
            readFile: async (path) => await readFile(path, "utf-8"),
            stat,
        };

        resolved = await module.resolveModule(host, "@azure-tools/typespec-python", {
            baseDir: process.cwd(),
        });
        if (resolved.type !== "module") {
            throw new Error(
                `Error resolving "@azure-tools/typespec-python", expected to find a node module but found a file: "${resolved.path}".`
            );
        }
    } catch (err) {
        throw new Error(
            `Error resolving "@azure-tools/typespec-python", could not find the module: "${err}".`
        );
    }

    // Define the source and destination directories
    const sourceDir = path.join(resolved.path, "generator");
    const destDir = path.join(__dirname, "..", "generator");

    // Delete the destination directory if it exists
    if (fs.existsSync(destDir)) {
        fs.removeSync(destDir);
    }

    // Copy the source directory to the destination directory
    fs.copySync(sourceDir, destDir);
}


resolveAndCopy().catch(console.error);
