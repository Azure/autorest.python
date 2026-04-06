/* eslint-disable no-console */
import { ChildProcess, spawn } from "child_process";
import fs from "fs";
import { cpus } from "os";
import { dirname, join } from "path";
import pc from "picocolors";
import { fileURLToPath } from "url";
import { parseArgs } from "util";

const root = join(dirname(fileURLToPath(import.meta.url)), "../../../");
const testsDir = join(root, "tests");

const argv = parseArgs({
    args: process.argv.slice(2),
    options: {
        flavor: { type: "string", short: "f", default: "all" },
        env: { type: "string", short: "e" },
        name: { type: "string", short: "n" },
        jobs: { type: "string", short: "j" },
        quiet: { type: "boolean", short: "q", default: false },
        help: { type: "boolean", short: "h", default: false },
    },
});

if (argv.values.help) {
    console.log(`
${pc.bold("Usage:")} run-tests.ts [options]

${pc.bold("Options:")}
  -f, --flavor <azure|unbranded>  SDK flavor to test
                                  If not specified, tests both flavors
  -e, --env <env1,env2,...>       Specific tox environments to run
                                  Available: test, lint, mypy, pyright, docs, ci
  -n, --name <pattern>            Filter tests by name pattern
  -j, --jobs <n>                  Number of parallel jobs (default: CPU cores - 2)
  -q, --quiet                     Suppress test output (only show pass/fail summary)
  -h, --help                      Show this help message

${pc.bold("Environments:")}
  test       Run pytest tests for generated packages
  lint       Run pylint on generated packages
  mypy       Run mypy type checking on generated packages
  pyright    Run pyright type checking on generated packages
  docs       Run documentation validation (apiview, sphinx)
  ci         Run all checks (test + lint + mypy + pyright)

${pc.bold("Examples:")}
  run-tests.ts                           # Run test for all flavors
  run-tests.ts --flavor=azure            # Run test for azure only
  run-tests.ts -f azure -e lint          # Run lint for azure only
  run-tests.ts -e mypy,pyright           # Run mypy and pyright for all flavors
  run-tests.ts -e docs -f azure          # Run docs validation for azure
`);
    process.exit(0);
}

// Get Python venv path
function getVenvPython(): string {
    const venvPath = join(root, "venv");
    if (fs.existsSync(join(venvPath, "bin"))) {
        return join(venvPath, "bin", "python");
    } else if (fs.existsSync(join(venvPath, "Scripts"))) {
        return join(venvPath, "Scripts", "python.exe");
    }
    throw new Error("Virtual environment not found. Run 'npm run install' first.");
}

interface ToxResult {
    env: string;
    success: boolean;
    duration: number;
    error?: string;
}

async function runToxEnv(env: string, pythonPath: string, name?: string): Promise<ToxResult> {
    const startTime = Date.now();

    console.log(`${pc.blue("[START]")} ${env}`);

    const toxIniPath = join(testsDir, "tox.ini");
    const args = ["-m", "tox", "-c", toxIniPath, "-e", env];
    if (name) {
        args.push("--", "-k", name);
    }

    // Set FLAVOR environment variable
    const flavor = env.split("-")[1] || "azure";
    const envVars = {
        ...process.env,
        FLAVOR: flavor,
    };

    return new Promise((resolve) => {
        const proc: ChildProcess = spawn(pythonPath, args, {
            cwd: testsDir,
            stdio: !argv.values.quiet ? "inherit" : "pipe",
            env: envVars,
        });

        let stderr = "";
        if (argv.values.quiet && proc.stderr) {
            proc.stderr.on("data", (data) => {
                stderr += data.toString();
            });
        }

        proc.on("close", (code) => {
            const duration = (Date.now() - startTime) / 1000;
            const success = code === 0;

            if (success) {
                console.log(`${pc.green("[PASS]")} ${env} (${duration.toFixed(1)}s)`);
            } else {
                console.log(`${pc.red("[FAIL]")} ${env} (${duration.toFixed(1)}s)`);
            }

            resolve({
                env,
                success,
                duration,
                error: success ? undefined : stderr || `Exit code: ${code}`,
            });
        });

        proc.on("error", (err) => {
            const duration = (Date.now() - startTime) / 1000;
            console.log(`${pc.red("[ERROR]")} ${env}: ${err.message}`);
            resolve({
                env,
                success: false,
                duration,
                error: err.message,
            });
        });
    });
}

async function runParallel(envs: string[], pythonPath: string, maxJobs: number, name?: string): Promise<ToxResult[]> {
    const results: ToxResult[] = [];
    const running: Map<string, Promise<ToxResult>> = new Map();

    for (const env of envs) {
        // Wait if we're at max capacity
        if (running.size >= maxJobs) {
            const completed = await Promise.race(running.values());
            results.push(completed);
            running.delete(completed.env);
        }

        // Start new task
        const task = runToxEnv(env, pythonPath, name);
        running.set(env, task);
    }

    // Wait for remaining tasks
    const remaining = await Promise.all(running.values());
    results.push(...remaining);

    return results;
}

function printSummary(results: ToxResult[]): void {
    console.log("\n" + pc.bold("═".repeat(60)));
    console.log(pc.bold(" Test Results Summary"));
    console.log(pc.bold("═".repeat(60)) + "\n");

    const passed = results.filter((r) => r.success);
    const failed = results.filter((r) => !r.success);
    const totalDuration = results.reduce((sum, r) => sum + r.duration, 0);

    for (const result of results) {
        const status = result.success ? pc.green("PASS") : pc.red("FAIL");
        console.log(`  ${status}  ${result.env} (${result.duration.toFixed(1)}s)`);
    }

    console.log("\n" + "─".repeat(60));
    console.log(
        `  ${pc.green(`Passed: ${passed.length}`)}  ` +
            `${pc.red(`Failed: ${failed.length}`)}  ` +
            `Total: ${results.length}  ` +
            `Duration: ${totalDuration.toFixed(1)}s`,
    );
    console.log("─".repeat(60) + "\n");

    if (failed.length > 0) {
        console.log(pc.red("Failed environments:"));
        for (const result of failed) {
            console.log(`  - ${result.env}`);
        }
        console.log();
    }
}

async function main(): Promise<void> {
    const startTime = Date.now();

    // Header
    console.log(pc.cyan("\n╔══════════════════════════════════════════════════════════╗"));
    console.log(pc.cyan("║") + pc.bold("              TypeSpec Python SDK Tests                   ") + pc.cyan("║"));
    console.log(pc.cyan("╚══════════════════════════════════════════════════════════╝") + "\n");

    // Get Python path
    let pythonPath: string;
    try {
        pythonPath = getVenvPython();
    } catch (error) {
        console.error(pc.red((error as Error).message));
        process.exit(1);
    }

    // Determine flavors
    const flavors = argv.values.flavor === "all" ? ["azure", "unbranded"] : [argv.values.flavor!];

    // Determine environments
    let baseEnvs: string[];
    if (argv.values.env) {
        baseEnvs = argv.values.env.split(",").map((e) => e.trim());
    } else {
        // Default: run test environments
        baseEnvs = ["test"];
    }

    // Build full environment list (env-flavor format)
    const envs: string[] = [];
    for (const env of baseEnvs) {
        for (const flavor of flavors) {
            envs.push(`${env}-${flavor}`);
        }
    }

    // Determine parallelism
    // Test environments must run sequentially because they each start a mock server on port 3000
    const hasTestEnvs = envs.some((e) => e.startsWith("test-"));
    const maxJobs = argv.values.jobs
        ? parseInt(argv.values.jobs, 10)
        : hasTestEnvs
          ? 1
          : Math.max(2, cpus().length - 2);

    console.log(`  Flavors:      ${flavors.join(", ")}`);
    console.log(`  Environments: ${envs.join(", ")}`);
    console.log(`  Jobs:         ${maxJobs}${hasTestEnvs && !argv.values.jobs ? " (sequential for test envs)" : ""}`);
    if (argv.values.name) {
        console.log(`  Filter:       ${argv.values.name}`);
    }
    console.log();

    // Run tests
    const results = await runParallel(envs, pythonPath, maxJobs, argv.values.name);

    // Print summary
    printSummary(results);

    const totalDuration = (Date.now() - startTime) / 1000;
    console.log(`Total execution time: ${totalDuration.toFixed(1)}s\n`);

    // Exit with appropriate code
    const failed = results.filter((r) => !r.success);
    if (failed.length > 0) {
        process.exit(1);
    }
}

main().catch((error) => {
    console.error(`${pc.red("Unexpected error:")}`, error);
    process.exit(1);
});
