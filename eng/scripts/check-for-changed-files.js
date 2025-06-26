// @ts-check

const { run } = require("./helpers.js");

// Stage all current changes first (if any)

run("git", ["add", "."], {
    encoding: "utf-8",
    stdio: [null, "pipe", "pipe"],
});

// Reset the index but keep working directory
run("git", ["reset"], {
    encoding: "utf-8",
    stdio: [null, "pipe", "pipe"],
});

// Re-add everything - this forces Git to apply .gitattributes rules to ALL files
run("git", ["add", "--renormalize", "."], {
    encoding: "utf-8",
    stdio: [null, "pipe", "pipe"],
});

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
    const diffProc = run("git", ["diff", "."], {
        encoding: "utf-8",
        stdio: [null, "pipe", "pipe"],
    });
    
    if (diffProc.stdout) {
        console.error(diffProc.stdout);
    }
    process.exit(1);
}
