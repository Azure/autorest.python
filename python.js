"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.patchPythonPath = exports.updatePythonPath = exports.resolvePythonRequirement = exports.PythonRequirement = void 0;
const exec_cmd_1 = require("../exec-cmd");
const common_1 = require("./common");
const version_1 = require("./version");
exports.PythonRequirement = "python";
/**
 * Small python script that will print the python version.
 */
const PRINT_PYTHON_VERSION_SCRIPT = "import sys; print('.'.join(map(str, sys.version_info[:3])))";
const resolvePythonRequirement = async (requirement) => {
    var _a;
    // Hardcoding AUTOREST_PYTHON_EXE is for backward compatibility
    const path = (_a = (0, common_1.getExecutablePath)(requirement)) !== null && _a !== void 0 ? _a : process.env["AUTOREST_PYTHON_EXE"];
    if (path) {
        return await tryPython(requirement, path);
    }
    const errors = [];
    // On windows try `py` executable with `-3` flag.
    if (process.platform === "win32") {
        const pyResult = await tryPython(requirement, "py", ["-3"]);
        if ("error" in pyResult) {
            errors.push(pyResult);
        }
        else {
            return pyResult;
        }
    }
    const python3Result = await tryPython(requirement, "python3");
    if ("error" in python3Result) {
        errors.push(python3Result);
    }
    else {
        return python3Result;
    }
    const pythonResult = await tryPython(requirement, "python");
    if ("error" in pythonResult) {
        errors.push(pythonResult);
    }
    else {
        return pythonResult;
    }
    return createPythonErrorMessage(requirement, errors);
};
exports.resolvePythonRequirement = resolvePythonRequirement;
/**
 * This method is kept for backward compatibility and will be removed in a future release.
 * @deprecated Please use patchPythonPath(command, requirement) instead.
 */
const updatePythonPath = async (command) => {
    const newCommand = await (0, exports.patchPythonPath)(command, { version: ">=3.6", environmentVariable: "AUTOREST_PYTHON_EXE" });
    command[0] = newCommand[0];
    return newCommand;
};
exports.updatePythonPath = updatePythonPath;
/**
 * @param command list of the command and arguments. First item in array must be a python exe @see KnownPythonExe. (e.g. ["python", "mypythonfile.py"]
 * @param requirement
 */
const patchPythonPath = async (command, requirement) => {
    var _a;
    const [_, ...args] = command;
    const resolution = await (0, exports.resolvePythonRequirement)(requirement);
    if ("error" in resolution) {
        throw new Error(`Failed to find compatible python version. ${resolution.message}`);
    }
    return [resolution.command, ...((_a = resolution.additionalArgs) !== null && _a !== void 0 ? _a : []), ...args];
};
exports.patchPythonPath = patchPythonPath;
const tryPython = async (requirement, command, additionalArgs = []) => {
    const resolution = {
        name: exports.PythonRequirement,
        command,
        additionalArgs: additionalArgs.length > 0 ? additionalArgs : undefined,
    };
    try {
        const result = await (0, exec_cmd_1.execute)(command, [...additionalArgs, "-c", PRINT_PYTHON_VERSION_SCRIPT]);
        return (0, version_1.validateVersionRequirement)(resolution, result.stdout.trim(), requirement);
    }
    catch (e) {
        return {
            error: true,
            ...resolution,
            message: `'${command}' command line is not found in the path. Make sure to have it installed.`,
        };
    }
};
const createPythonErrorMessage = (requirement, errors) => {
    var _a;
    const versionReq = (_a = requirement.version) !== null && _a !== void 0 ? _a : "*";
    const lines = [
        `Couldn't find a valid python interpreter satisfying the requirement (version: ${versionReq}). Tried:`,
        ...errors.map((x) => ` - ${x.command} (${x.message})`),
    ];
    return {
        error: true,
        name: "python",
        command: "python",
        message: lines.join("\n"),
    };
};
//# sourceMappingURL=python.js.map