// This script wraps logic in @azure-tools/extension to resolve
// the path to Python 3 so that a Python script file can be run
// from an npm script in package.json.  It uses the same Python 3
// path resolution algorithm as AutoRest so that the behavior
// is fully consistent (and also supports AUTOREST_PYTHON_EXE).
//
// Invoke it like so: "node run-python3.js script.py"

const cp = require("child_process");
const extension = require("@azure-tools/extension");

async function runPython3(scriptName, debug = "") {
  const command = ["python", scriptName, debug];
  await extension.updatePythonPath(command);
  cp.execSync(command.join(" "), {
    stdio: [0, 1, 2]
  });
}

runPython3(...process.argv.slice(2)).catch(err => {
  const error = err.toString();

  // Python script errors are already written out via stderr so don't
  // write them twice.  Write out all other errors to stderr.
  if (!error.startsWith("Error: Command failed")) {
    console.error(error);
  }
  process.exit(1);
});
