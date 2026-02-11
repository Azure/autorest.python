---
name: bump-and-release
description: Bump dependency "@typespec/http-client-python" and release new versions for Azure/autorest.python repo. Use when user wants to bump, update, or upgrade the @typespec/http-client-python dependency, create a release PR, or publish new versions of autorest.python and typespec-python packages.
---

# Bump and Release

Bump the "@typespec/http-client-python" dependency and create a release PR for the Azure/autorest.python repository.

## Context Variables

- **BASE_BRANCH**: The branch to base changes on (default: "main")
- **CURRENT_DATE**: Current date in YYYY-MM-DD format (e.g., "2025-01-01")

## Prerequisites

Before starting, verify that `npm-check-updates` is available:
```bash
npx npm-check-updates --version
```

If the command fails or prompts for installation, install it globally:
```bash
npm install -g npm-check-updates
```

## Workflow

### Step 1: Prepare Branch

Navigate to the root folder of "Azure/autorest.python" repo.

**If BASE_BRANCH is "main":**
```bash
git reset HEAD && git checkout . && git checkout origin/main && git pull origin main && git checkout -b publish/release-{{CURRENT_DATE}}
```

**If BASE_BRANCH is not "main":**
```bash
git reset HEAD && git checkout . && git fetch origin {{BASE_BRANCH}} && git checkout {{BASE_BRANCH}}
```

### Step 2: Get Latest Version and Update Dependencies

1. Get the latest VERSION of "@typespec/http-client-python" from npm:
   ```bash
   npm view @typespec/http-client-python version
   ```

2. Update the version of "@typespec/http-client-python" to `~{{VERSION}}` in both files:
   - `packages/autorest.python/package.json`
   - `packages/typespec-python/package.json`

### Steps 3–5: Update Dependencies (only if BASE_BRANCH is "main")

> **Skip Steps 3, 4, and 5 if BASE_BRANCH is not "main".**

### Step 3: Update Dependencies

Run npm-check-updates for `packages/typespec-python/package.json`:
```bash
npx npm-check-updates -u --filter @typespec/*,@azure-tools/* --packageFile packages/typespec-python/package.json
```

### Step 4: Update peerDependencies

Update `peerDependencies` in `packages/typespec-python/package.json`:
- If format is `">=0.a.b <1.0.0"`: Update only the `0.a.b` portion, keep the range format unchanged
- If format is `"^1.a.b"`: Update to the latest version

### Step 5: Verify devDependencies Versions for Specs

Verify `devDependencies` versions for specs in `packages/typespec-python/package.json`:
- Check `@typespec/http-specs` and `@azure-tools/azure-http-specs`
- If the original version in `package.json` is newer than the updated value, keep the original version
- Dev versions are typically in the form `x.y.z-alpha.N-dev.M` (e.g., `0.1.0-alpha.37-dev.3`).

Example:
- Original: `@typespec/http-specs: 0.1.0-alpha.12-dev.5`, updated by step 3 to `0.1.0-alpha.11` → keep `0.1.0-alpha.12-dev.5`.
- Original: `@typespec/http-specs: 0.1.0-alpha.12-dev.5`, updated by step 3 to `0.1.0-alpha.12` → keep `0.1.0-alpha.12` (step 3 works as expected).
- Original: `@azure-tools/azure-http-specs: 0.1.0-alpha.12-dev.2`, updated to `0.1.0-alpha.11` → keep `0.1.0-alpha.12-dev.2`.
- Original: `@azure-tools/azure-http-specs: 0.1.0-alpha.12-dev.2`, updated to `0.1.0-alpha.12` → keep `0.1.0-alpha.12` (step 3 works as expected).

### Step 6: Run Version Tool

Run the change version command:
```bash
pnpm change version
```

Verify at least 4 files are changed:
- `packages/autorest.python/package.json`
- `packages/autorest.python/CHANGELOG.md`
- `packages/typespec-python/package.json`
- `packages/typespec-python/CHANGELOG.md`

### Step 7: Check for Minor Version Bump

The version tool calculates the next version but may choose patch instead of minor incorrectly.

1. Run `git diff` to inspect updated CHANGELOG.md files
2. If any CHANGELOG.md contains "### Features", upgrade to minor version instead of patch version
3. Update version numbers in all 4 files:
   - `packages/autorest.python/package.json`
   - `packages/autorest.python/CHANGELOG.md`
   - `packages/typespec-python/package.json`
   - `packages/typespec-python/CHANGELOG.md`

### Step 8: Build and Stage

```bash
pnpm install && pnpm build && git add -u
```

### Step 9: Commit and Push

```bash
git commit -m "bump version"
git push origin HEAD
```

### Step 10: Create PR

If no existing PR exists for the current branch, create a new pull request targeting the BASE_BRANCH.
