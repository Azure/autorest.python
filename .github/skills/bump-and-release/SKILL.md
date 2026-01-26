---
name: bump-and-release
description: Bump dependency "@typespec/http-client-python" and release new versions for Azure/autorest.python repo. Use when user wants to bump, update, or upgrade the @typespec/http-client-python dependency, create a release PR, or publish new versions of autorest.python and typespec-python packages.
---

# Bump and Release

Bump the "@typespec/http-client-python" dependency and create a release PR for the Azure/autorest.python repository.

## Context Variables

- **BASE_BRANCH**: The branch to base changes on (default: "main")
- **CURRENT_DATE**: Current date in YYYY-MM-DD format (e.g., "2025-01-01")

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

### Step 3: Run Version Tool

Run the change version command:
```bash
pnpm change version
```

Verify at least 4 files are changed:
- `packages/autorest.python/package.json`
- `packages/autorest.python/CHANGELOG.md`
- `packages/typespec-python/package.json`
- `packages/typespec-python/CHANGELOG.md`

### Step 4: Check for Minor Version Bump

The version tool calculates the next version but may choose patch instead of minor incorrectly.

1. Run `git diff` to inspect updated CHANGELOG.md files
2. If any CHANGELOG.md contains "### Features", upgrade to minor version instead of patch version
3. Update version numbers in all 4 files:
   - `packages/autorest.python/package.json`
   - `packages/autorest.python/CHANGELOG.md`
   - `packages/typespec-python/package.json`
   - `packages/typespec-python/CHANGELOG.md`

### Step 5: Build and Stage

```bash
pnpm install && pnpm build && git add -u
```

### Step 6: Commit and Push

```bash
git commit -m "bump version"
git push origin HEAD
```

### Step 7: Create PR

If no existing PR exists for the current branch, create a new pull request targeting the BASE_BRANCH.
