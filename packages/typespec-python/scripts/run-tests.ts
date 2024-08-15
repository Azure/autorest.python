import { execSync } from 'child_process';

const folder = process.env.folder;
if (!folder) {
    console.error('Error: folder environment variable is not set.');
    process.exit(1);
}

const command = `FOLDER=${folder} tox -c ./test/${folder}/tox.ini -e ci`;

try {
    execSync(command, { stdio: 'inherit' });
} catch (error) {
    console.error(`Error executing command: ${(error as Error).message}`);
    process.exit(1);
}
