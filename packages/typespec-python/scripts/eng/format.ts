/* eslint-disable no-console */
import { runCommand } from "./utils.js";

// Format Python scripts with Black
// TypeScript formatting is handled by Prettier via the format npm script
runCommand("black scripts/", "black");
