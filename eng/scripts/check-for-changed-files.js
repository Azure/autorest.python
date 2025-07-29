// @ts-check

const { run } = require("./helpers.js");

const proc = run("git", ["status", "--porcelain", "."], {
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
  console.error(
    `ERROR: There are diffs in regeneration. Please run 'inv regenerate' and re-run. You may also have to remove 'node_modules' and re-run 'npm install' to get the latest testserver.`,
  );
  process.exit(1);
}
