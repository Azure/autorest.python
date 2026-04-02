/* eslint-disable no-console */
import { executeCommand } from "./utils.js";

// Run ESLint on TypeScript emitter code
// Python linting for generated packages is done via tox in test/{flavor}/tox.ini
executeCommand("pnpm exec eslint . --max-warnings=0", "eslint");
