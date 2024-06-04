const fs = require('fs-extra');
const path = require('path');
const url = require('url');

// Define the source and destination directories
const sourceDir = path.join(__dirname, "..", "node_modules", "@azure-tools", "typespec-python", "pygen");
const destDir = path.join(__dirname, "..", "pygen");

// Copy the source directory to the destination directory
fs.copySync(sourceDir, destDir);
