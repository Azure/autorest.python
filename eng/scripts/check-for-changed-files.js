// @ts-check

const { run } = require("./helpers.js");

// First, reset any staged changes and clean the working directory
run("git", ["reset", "HEAD", "."], {
    encoding: "utf-8",
    stdio: [null, "pipe", "pipe"],
});

// Re-add everything - this forces Git to apply .gitattributes rules to ALL files
run("git", ["add", "--renormalize", "."], {
    encoding: "utf-8",
    stdio: [null, "pipe", "pipe"],
});

// Check for differences ignoring whitespace and line endings
const proc = run("git", ["diff", "--ignore-space-at-eol", "--ignore-blank-lines", "--cached"], {
    encoding: "utf-8",
    stdio: [null, "pipe", "pipe"],
});

if (proc.stdout && proc.stdout.toString().trim()) {
    console.log("Detected actual content changes (ignoring line endings):");
    console.log(proc.stdout.toString());
    
    // Also show the status for context
    const statusProc = run("git", ["status", "--porcelain", "."], {
        encoding: "utf-8",
        stdio: [null, "pipe", "pipe"],
    });
    
    if (statusProc.stdout) {
        console.log("Git status:");
        console.log(statusProc.stdout);
    }
    
    console.error(
        `ERROR: There are actual content diffs in regeneration (excluding line ending changes). Please run 'inv regenerate' and re-run. You may also have to remove 'node_modules' and re-run 'npm install' to get the latest testserver.`,
    );
    process.exit(1);
}
