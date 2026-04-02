/* eslint-disable no-console */
import { ChildProcess, spawn } from "child_process";
import { readFileSync } from "fs";
import { cpus } from "os";
import { dirname, join } from "path";
import pc from "picocolors";
import { fileURLToPath } from "url";
import { parseArgs } from "util";

const root = join(dirname(fileURLToPath(import.meta.url)), "../../../");

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
                                  Available: ci, lint, mypy, pyright, apiview
  -n, --name <pattern>            Filter tests by name pattern
  -j, --jobs <n>                  Number of parallel jobs (default: CPU cores - 2)
  -q, --quiet                     Suppress test output (only show pass/fail summary)
  -h, --help                      Show this help message

${pc.bold("Environments:")}
  ci         Run all checks (test + lint + mypy + pyright)
  lint       Run pylint on generated packages
  mypy       Run mypy type checking on generated packages
  pyright    Run pyright type checking on generated packages
  apiview    Run API view validation

${pc.bold("Examples:")}
  run-tests.ts                           # Run ci for all flavors
  run-tests.ts --flavor=azure            # Run ci for azure only
  run-tests.ts -f azure -e lint          # Run lint for azure only
  run-tests.ts -e mypy,pyright           # Run mypy and pyright for all flavors
`);
  process.exit(0);
}

interface ToxResult {
  env: string;
  success: boolean;
  duration: number;
  error?: string;
}

function sectionExistsInToxIni(command: string, folder: string): boolean {
  const toxIniPath = join(root, `test/${folder}/tox.ini`);
  try {
    const toxIniContent = readFileSync(toxIniPath, "utf-8");
    const sectionHeader = `[testenv:${command}]`;
    return toxIniContent.includes(sectionHeader);
  } catch {
    return false;
  }
}

async function runToxEnv(
  env: string,
  folder: string,
  name?: string,
): Promise<ToxResult> {
  const startTime = Date.now();
  const displayName = `${env}-${folder}`;

  if (!sectionExistsInToxIni(env, folder)) {
    console.log(`${pc.yellow("[SKIP]")} ${displayName} (no tox section)`);
    return {
      env: displayName,
      success: true,
      duration: 0,
    };
  }

  console.log(`${pc.blue("[START]")} ${displayName}`);

  const toxIniPath = join(root, `test/${folder}/tox.ini`);
  const args = ["tox", "-c", toxIniPath, "-e", env];
  if (name) {
    args.push("--", "-f", name);
  }

  // Set FOLDER environment variable for tox
  const envVars = {
    ...process.env,
    FOLDER: folder,
  };

  return new Promise((resolve) => {
    const proc: ChildProcess = spawn("python", ["-m", ...args], {
      cwd: root,
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
        console.log(`${pc.green("[PASS]")} ${displayName} (${duration.toFixed(1)}s)`);
      } else {
        console.log(`${pc.red("[FAIL]")} ${displayName} (${duration.toFixed(1)}s)`);
      }

      resolve({
        env: displayName,
        success,
        duration,
        error: success ? undefined : stderr || `Exit code: ${code}`,
      });
    });

    proc.on("error", (err) => {
      const duration = (Date.now() - startTime) / 1000;
      console.log(`${pc.red("[ERROR]")} ${displayName}: ${err.message}`);
      resolve({
        env: displayName,
        success: false,
        duration,
        error: err.message,
      });
    });
  });
}

async function runParallel(
  tasks: Array<{ env: string; folder: string }>,
  maxJobs: number,
  name?: string,
): Promise<ToxResult[]> {
  const results: ToxResult[] = [];
  const running: Map<string, Promise<ToxResult>> = new Map();

  for (const { env, folder } of tasks) {
    const key = `${env}-${folder}`;

    // Wait if we're at max capacity
    if (running.size >= maxJobs) {
      const completed = await Promise.race(running.values());
      results.push(completed);
      running.delete(completed.env);
    }

    // Start new task
    const task = runToxEnv(env, folder, name);
    running.set(key, task);
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
  console.log(
    pc.cyan("║") +
      pc.bold("              TypeSpec Python SDK Tests                   ") +
      pc.cyan("║"),
  );
  console.log(pc.cyan("╚══════════════════════════════════════════════════════════╝") + "\n");

  // Determine flavors
  const flavors = argv.values.flavor === "all" ? ["azure", "unbranded"] : [argv.values.flavor!];

  // Determine environments
  let envs: string[];
  if (argv.values.env) {
    envs = argv.values.env.split(",").map((e) => e.trim());
  } else {
    // Default: run ci
    envs = ["ci"];
  }

  // Build task list
  const tasks: Array<{ env: string; folder: string }> = [];
  for (const env of envs) {
    for (const folder of flavors) {
      tasks.push({ env, folder });
    }
  }

  // Determine parallelism
  const maxJobs = argv.values.jobs
    ? parseInt(argv.values.jobs, 10)
    : Math.max(2, cpus().length - 2);

  console.log(`  Flavors:      ${flavors.join(", ")}`);
  console.log(`  Environments: ${envs.join(", ")}`);
  console.log(`  Jobs:         ${maxJobs}`);
  if (argv.values.name) {
    console.log(`  Filter:       ${argv.values.name}`);
  }
  console.log();

  // Run tests
  const results = await runParallel(tasks, maxJobs, argv.values.name);

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
