/* eslint-disable no-console */
import { spawn } from "child_process";
import { dirname, join } from "path";
import pc from "picocolors";
import { fileURLToPath } from "url";
import { parseArgs } from "util";

const root = join(dirname(fileURLToPath(import.meta.url)), "../../../");

const argv = parseArgs({
    args: process.argv.slice(2),
    options: {
        help: { type: "boolean", short: "h" },
        command: { type: "string" },
        skipWarning: { type: "string" },
    },
});

if (argv.values.help) {
    console.log(`
${pc.bold("Usage:")} tsx lint.ts [options]

${pc.bold("Description:")}
  Run linting checks on the codebase.

${pc.bold("Options:")}
  ${pc.cyan("-h, --help")}
      Show this help message.
  ${pc.cyan("--command <eslint|pylint>")}
      Specify which linter to run (default: eslint).
  ${pc.cyan("--skipWarning <true|false>")}
      Skip warnings in output (default: false).

${pc.bold("Examples:")}
  ${pc.dim("# Lint TypeScript code")}
  tsx lint.ts

  ${pc.dim("# Run eslint only")}
  tsx lint.ts --command eslint
`);
    process.exit(0);
}

function runCommand(command: string, args: string[], displayName?: string): Promise<boolean> {
    const name = displayName || `${command} ${args.join(" ")}`;

    // Add node_modules/.bin to PATH so eslint can be found
    const pathSep = process.platform === "win32" ? ";" : ":";
    const binPath = join(root, "node_modules", ".bin");
    const env = {
        ...process.env,
        PATH: `${binPath}${pathSep}${process.env.PATH}`,
    };

    return new Promise((resolve) => {
        console.log(`${pc.cyan("[RUN]")} ${name}`);
        const proc = spawn(command, args, {
            cwd: root,
            stdio: "inherit",
            shell: true,
            env,
        });

        proc.on("close", (code) => {
            if (code === 0) {
                console.log(`${pc.green("[PASS]")} ${name} completed successfully`);
                resolve(true);
            } else {
                console.log(`${pc.red("[FAIL]")} ${name} failed with code ${code}`);
                resolve(false);
            }
        });

        proc.on("error", (err) => {
            console.log(`${pc.red("[ERROR]")} ${name}: ${err.message}`);
            resolve(false);
        });
    });
}

async function main(): Promise<void> {
    const command = argv.values.command || "eslint";
    const skipWarning = argv.values.skipWarning === "true";

    // Only run eslint for now (pylint is handled by tox)
    if (command !== "eslint") {
        console.log(`${pc.yellow("[SKIP]")} ${command} is handled by tox, skipping...`);
        process.exit(0);
    }

    console.log(`\n${pc.bold("=== Linting TypeScript ===")}\n`);

    const eslintArgs = [".", "--config", "eng/scripts/ci/config/eslint-ci.config.mjs"];
    if (!skipWarning) {
        eslintArgs.push("--max-warnings=0");
    }

    const success = await runCommand("eslint", eslintArgs, `eslint .${skipWarning ? "" : " --max-warnings=0"}`);

    if (!success) {
        process.exit(1);
    }

    console.log(`\n${pc.green(pc.bold("All linting checks passed!"))}\n`);
}

main().catch((error) => {
    console.error(`${pc.red("Unexpected error:")}`, error);
    process.exit(1);
});
