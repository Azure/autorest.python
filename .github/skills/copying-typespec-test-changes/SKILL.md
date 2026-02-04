---
name: copying-typespec-test-changes
description: Copies test file changes from Microsoft/typespec repo PRs to Azure/autorest.python repo. Use when user provides a Microsoft/typespec PR link and asks to sync test changes from http-client-python/generator/test to packages/typespec-python/test folder.
---

# Copying TypeSpec Test Changes to autorest.python

## Overview

The `packages/typespec-python/test` folder in Azure/autorest.python mirrors the `packages/http-client-python/generator/test` folder in Microsoft/typespec. When test changes are made in typespec, they need to be copied to autorest.python.

## Workflow

Copy this checklist and track your progress:

```
Task Progress:
- [ ] Step 1: Extract changed files from typespec PR
- [ ] Step 2: Identify test file changes in http-client-python/generator/test
- [ ] Step 3: Copy changes to packages/typespec-python/test
- [ ] Step 4: Format files with black
- [ ] Step 5: Verify changes
```

### Step 1: Extract changed files from typespec PR

Use the GitHub tool to fetch the PR details from Microsoft/typespec

### Step 2: Identify test file changes

Filter the changed files list to only include files under:
- `packages/http-client-python/generator/test/`

Ignore changes outside this path.

### Step 3: Copy changes to autorest.python

For each changed test file:

1. **Map the path**: Replace `packages/http-client-python/generator/test/` with `packages/typespec-python/test/`

   Example:
   - Source: `packages/http-client-python/generator/test/azure/sample_test.py`
   - Target: `packages/typespec-python/test/azure/sample_test.py`

2. **Fetch the new content**: Get the file content from the typespec PR branch

3. **Apply the change**:
   - For new files: Create the file in autorest.python
   - For modified files: Update the existing file to match
   - For deleted files: Delete the corresponding file

### Step 4: Format with black

**MUST run after all file changes:**

```bash
python -m black <changed_file_path> -l 120
```

Run this command for each Python file that was created or modified.

### Step 5: Verify changes

1. Check that all target files exist and match source content
2. Confirm black formatting was applied (no formatting errors)
3. List all changes made for user review

## Path mapping reference

| TypeSpec repo path | autorest.python path |
|---|---|
| `packages/http-client-python/generator/test/` | `packages/typespec-python/test/` |

## Important notes

- **Consistency**: Copy content exactly to maintain consistency between repos
- **Formatting**: Always run `python -m black <file> -l 120` on changed Python files
- **Scope**: Only copy files from the `generator/test` folder, ignore other changes
- **Verify**: After copying, the test files should be identical between repos (after formatting)
- **requirements.txt**: When updating `requirements.txt` files, only update dependencies with the `-e XXX` pattern (editable installs). Do NOT modify other dependencies in the file.

## Example usage

### Basic usage (local changes only)

User prompt: "Copy test changes from https://github.com/microsoft/typespec/pull/1234 to this repo"

1. Extract PR number: 1234
2. Fetch PR #1234 from microsoft/typespec
3. Find files changed under `packages/http-client-python/generator/test/`
4. For each file, copy to corresponding path under `packages/typespec-python/test/`
5. Run black formatter on each changed Python file
6. Report summary of changes

### Classic scenario (commit to autorest.python PR)

In most cases, users will provide both:
- A **typespec PR link** (source of changes)
- An **autorest.python PR link** (destination to commit changes)

User prompt: "Copy test changes from https://github.com/microsoft/typespec/pull/1234 to https://github.com/Azure/autorest.python/pull/5678"

**Workflow:**

1. Extract both PR numbers: typespec PR #1234, autorest.python PR #5678
2. Fetch the autorest.python PR #5678 to get the target branch name
3. Checkout the target branch locally:
   ```bash
   git fetch origin
   git checkout <pr-branch-name>
   ```
4. Fetch typespec PR #1234 from microsoft/typespec
5. Find files changed under `packages/http-client-python/generator/test/`
6. For each file, copy to corresponding path under `packages/typespec-python/test/`
7. Run black formatter on each changed Python file
8. Stage, commit, and push changes to the PR branch:
   ```bash
   git add packages/typespec-python/test/
   git commit -m "Sync test changes from microsoft/typespec#1234"
   git push origin <pr-branch-name>
   ```
9. Report summary of changes committed to the PR

**Important for PR commits:**
- Always fetch and checkout the PR branch before making changes
- Use a descriptive commit message referencing the source typespec PR
- Push to the same branch to update the existing autorest.python PR
