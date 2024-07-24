import { exec as execCallback } from 'child_process';
import { promisify } from 'util';
import yargs from 'yargs';
import { hideBin } from "yargs/helpers";
import { join, resolve } from 'path';
import { lstatSync, readdirSync, promises, access } from "fs";
import { sync } from "glob";
import { fileURLToPath } from 'url';

// Promisify the exec function
const exec = promisify(execCallback);

// Get the directory of the current file
const PLUGIN_DIR = fileURLToPath(import.meta.url);

// Function to execute CLI commands asynchronously
async function executeCommand(command: string): Promise<string> {
  try {
    const { stdout, stderr } = await exec(command, { cwd: PLUGIN_DIR });
    if (stderr) {
      console.error(`stderr: ${stderr}`);
      throw new Error(stderr);
    }
    return stdout;
  } catch (error) {
    console.error(`Error`);
    throw error;
  }
}

interface RegenerateFlags {
    flavor?: "azure" | "unbranded";
    debug?: boolean;
    name?: string;
}

// function pathExists(path: string): boolean {
//     try {
//       access(path);
//       return true;
//     } catch {
//       return false;
//     }
//   }

  async function getSubdirectories(directory: string): Promise<string[]> {
    const subdirectories: string[] = [];
    const items = await promises.readdir(directory);
  
    for (const item of items) {
      const itemPath = join(directory, item);
      const stats = await promises.lstat(itemPath);
  
      if (stats.isDirectory()) {
        subdirectories.push(itemPath);
        console.log(itemPath)
      }
    }
  
    return subdirectories;
  }

async function someAsyncOperation(subdirectory: string): Promise<void> {
    // Perform some asynchronous operation here
    console.log(subdirectory);
}

async function regenerate(flags: RegenerateFlags): Promise<boolean> {
    if (flags.flavor === undefined) {
        const azureGeneration = await regenerate({...flags, flavor: "azure"});
        const unbrandedGeneration = await regenerate({...flags, flavor: "unbranded"});
        return azureGeneration && unbrandedGeneration;
    } else {
        const CADL_RANCH_DIR = resolve(PLUGIN_DIR, '../../../', 'node_modules/@azure-tools/cadl-ranch-specs/http');
        const subdirectories = await getSubdirectories(CADL_RANCH_DIR);
            const promises = subdirectories.map(async (subdirectory) => {
                // Perform additional asynchronous operations on each subdirectory here
                await someAsyncOperation(subdirectory);
        });
        await Promise.all(promises);
        console.log("done");
        return true;
    }
};

//   try {
//     const output = await executeCommand('tsp compile');
//     console.log(`Command output: ${output}`);
//   } catch (error) {
//     console.error(`Command failed: ${error}`);
//   }

// PARSE INPUT ARGUMENTS
const argv = yargs(hideBin(process.argv))
  .option('flavor', {
    type: 'string',
    choices: ['azure', 'unbranded'],
    description: 'Specify the flavor',
  })
  .option('debug', {
    alias: 'd',
    type: 'boolean',
    description: 'Debug mode',
  })
  .option('name', {
    alias: 'n',
    type: 'string',
    description: 'Specify filename if you only want to generate a subset',
  })
  .argv;

  regenerate(argv as RegenerateFlags)
    .then(() => console.log('Regeneration successful'))
    .catch(error => console.error(`Regeneration failed: ${error.message}`));

