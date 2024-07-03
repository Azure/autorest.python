const fs = require("fs-extra");
const path = require("path");

const force = process.argv[2] === "--force" ? true : false;

const typespecModulePath = path.join(__dirname, "..", "node_modules", "@azure-tools", "typespec-python");

// Define the source and destination directories
const sourceDir = path.join(typespecModulePath, "generator");
const destDir = path.join(__dirname, "..", "generator");

// Delete the destination directory if it exists
if (fs.existsSync(destDir)) {
    if (force) fs.removeSync(destDir);
    else process.exit(0);
}

// Copy the source directory to the destination directory
fs.copySync(sourceDir, destDir);
