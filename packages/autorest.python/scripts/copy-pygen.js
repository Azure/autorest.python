const fs = require('fs-extra');
const path = require('path');
const url = require('url');

// Define the source and destination directories
const sourceDir = path.join(__dirname, "..", "..", 'pygen');
const destDir = path.join(__dirname, "..", "node_modules", "pygen");

// Define the filter function. Don't want to copy node_modules
const filterFunc = (src) => {
    return src.indexOf('node_modules') === -1;
  };

// Copy the source directory to the destination directory
fs.copySync(sourceDir, destDir, { filter: filterFunc });
