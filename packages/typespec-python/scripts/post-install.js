import fs from 'fs-extra';
import {join, dirname} from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url))
console.warn(__dirname);

// Define the source and destination directories
const sourceDir = join(__dirname, "..", "..", 'pygen');
const destDir = join(__dirname, "..", 'dist', "pygen");

// Define the filter function. Don't want to copy node_modules
const filterFunc = (src) => {
    return src.indexOf('node_modules') === -1;
  };

// Copy the source directory to the destination directory
fs.copySync(sourceDir, destDir, { filter: filterFunc });
