// @ts-check

const { run } = require("./helpers.js");

const proc = run("git", ["status", "--porcelain"], {
  encoding: "utf-8",
  stdio: [null, "pipe", "pipe"],
});

if (proc.stdout) {
  console.log(proc.stdout);
}

if (proc.stderr) {
  console.error(proc.stderr);
}

if (proc.stdout || proc.stderr) {
  if (process.argv[2] !== "publish") {
    console.error(
      `ERROR: There are diffs in regeneration. Please run 'inv regenerate' and re-run.`,
    );
  } else {
    console.error(
        `ERROR: There are diffs in regeneration. Please run 'inv regenerate' and re-run.`,
    );
  }
  process.exit(1);
}