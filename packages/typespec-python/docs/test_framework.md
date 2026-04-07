# Test Framework for typespec-python

This document describes the test framework used in the `typespec-python` package
and how it relates to the upstream
[`http-client-python`](https://github.com/microsoft/typespec/tree/main/packages/http-client-python)
package in the typespec repository.

## Overview

The test framework is a **dual-flavor testing system** (Azure and Unbranded) built
on **pytest** and **tox**. Tests run against a mock API server
([tsp-spector](https://github.com/microsoft/typespec)) that serves TypeSpec-defined
HTTP endpoints on `localhost:3000`.

## Folder Structure

```
packages/typespec-python/
└── tests/
    ├── conftest.py              # Root fixtures (server lifecycle, core_library, credentials, image data)
    ├── install_packages.py      # Installs generated SDK packages before test runs
    ├── pytest.ini               # Pytest config (asyncio_mode = auto)
    ├── tox.ini                  # Test environments (test, lint, mypy, pyright, docs, ci)
    │
    ├── data/                    # Static test data (image.png, image.jpg)
    │
    ├── requirements/            # Dependency files
    │   ├── base.txt             # Common: pytest, pytest-asyncio, tox, coverage, etc.
    │   ├── azure.txt            # Azure flavor: azure-core, azure-mgmt-core, geojson
    │   ├── unbranded.txt        # Unbranded flavor: corehttp
    │   ├── lint.txt             # Linting: pylint, black
    │   ├── typecheck.txt        # Type checking: pyright, mypy
    │   └── docs.txt             # Documentation: sphinx, myst_parser
    │
    ├── generated/               # Auto-generated SDK packages from TypeSpec specs
    │   ├── azure/               # ~116 Azure-flavored packages
    │   └── unbranded/           # ~64 Unbranded packages
    │
    └── mock_api/                # Hand-written integration tests
        ├── azure/               # Azure-specific tests
        │   ├── conftest.py      # Azure fixtures (credentials, LRO polling, header validation)
        │   ├── asynctests/      # Async test variants
        │   ├── data/            # Test image data
        │   └── test_*.py        # Sync test files
        ├── shared/              # Tests that run for both flavors
        │   ├── conftest.py      # Shared fixtures
        │   ├── asynctests/      # Async test variants
        │   ├── unittests/       # Unit tests (e.g. pyproject parsing)
        │   ├── data/            # Test image data
        │   └── test_*.py        # Sync test files
        └── unbranded/           # Unbranded-specific tests
            ├── conftest.py      # Unbranded fixtures
            ├── asynctests/      # Async test variants
            ├── data/            # Test image data
            └── test_*.py        # Sync test files
```

## Test Flavors

| Flavor | Core library | Credential class | What it tests |
|--------|-------------|-----------------|---------------|
| **azure** | `azure.core` | `AzureKeyCredential` | Azure SDK conventions, ARM resources, LRO, paging |
| **unbranded** | `corehttp` | `ServiceKeyCredential` | Non-Azure SDK generation without Azure branding |

When tests run:
- **Azure**: `pytest mock_api/azure mock_api/shared` with `FLAVOR=azure`
- **Unbranded**: `pytest mock_api/unbranded mock_api/shared` with `FLAVOR=unbranded`

The `shared/` tests run for **both** flavors. Root `conftest.py` uses `core_library()`
to dynamically import the appropriate core library.

## Running Tests

```bash
cd packages/typespec-python/tests

# Run Azure flavor tests
tox -e test-azure

# Run Unbranded flavor tests
tox -e test-unbranded

# Run all CI checks for a flavor (tests + lint + type checking)
tox -e ci-azure
tox -e ci-unbranded
```

### Available tox Environments

| Environment | Description |
|------------|-------------|
| `test-azure` / `test-unbranded` | Run pytest integration tests |
| `lint-azure` / `lint-unbranded` | Run pylint |
| `mypy-azure` / `mypy-unbranded` | Run mypy type checking |
| `pyright-azure` / `pyright-unbranded` | Run pyright type checking |
| `docs-azure` / `docs-unbranded` | Build API docs with Sphinx |
| `ci-azure` / `ci-unbranded` | All checks combined |

## Key Components

### Mock API Server

Tests rely on `tsp-spector` to serve TypeSpec-defined mock endpoints. The root
`conftest.py` starts the server automatically at session start and tears it down
after all tests complete. The server runs on `localhost:3000`.

### Generated Packages

Each test spec produces a generated SDK package under `tests/generated/{flavor}/`.
Before tests run, `install_packages.py` installs all generated packages into the
test environment using `uv pip install --no-deps`.

### Async Tests

Every `test_*.py` in the sync directory has a corresponding `test_*_async.py` in
`asynctests/`. Async fixtures use `@pytest_asyncio.fixture` and `pytest.ini`
configures `asyncio_mode = auto`.

## Folder Mapping to the typespec Repository

The test files are shared with the upstream
[`http-client-python`](https://github.com/microsoft/typespec/tree/main/packages/http-client-python)
package. The **typespec repo is the source of truth** for shared test files.

### Path Mapping

| typespec repo | autorest.python repo |
|--------------|---------------------|
| `packages/http-client-python/tests/mock_api/azure/` | `packages/typespec-python/tests/mock_api/azure/` |
| `packages/http-client-python/tests/mock_api/shared/` | `packages/typespec-python/tests/mock_api/shared/` |
| `packages/http-client-python/tests/mock_api/unbranded/` | `packages/typespec-python/tests/mock_api/unbranded/` |
| `packages/http-client-python/tests/requirements/` | `packages/typespec-python/tests/requirements/` |
| `packages/http-client-python/eng/scripts/ci/regenerate-common.ts` | `packages/typespec-python/eng/scripts/regenerate-common.ts` |

### What Is Synced

The script `eng/scripts/sync_from_typespec.py` copies from typespec → autorest.python:

1. **`regenerate-common.ts`** — shared regeneration logic
2. **Requirements files** — `azure.txt` and `unbranded.txt` (marker-delimited
   common sections are synced; repo-specific deps like `geojson` are preserved)
3. **Test files** — all files under `mock_api/{shared,azure,unbranded}` except:
   - `conftest.py` (each repo has its own)
   - `tox.ini`, `requirements.txt`, `dev_requirements.txt`
   - `.pyc` files

### What Is NOT Synced

| Item | Reason |
|------|--------|
| `conftest.py` files | Different server startup and fixture logic per repo |
| `tests/mock_api/shared/unittests/` | Repo-specific unit tests |
| `tests/generated/` | Regenerated independently in each repo |
| `tests/unit/` (typespec only) | Internal to http-client-python |
| `pytest.ini`, `tox.ini` | Different CI configurations per repo |

### Requirements Marker Convention

Requirements files (`azure.txt`, `unbranded.txt`) use markers to delimit the
common section synced between repos:

```
# === common azure dependencies across repos ===
# Azure SDK dependencies
-r base.txt
azure-core>=1.37.0
azure-mgmt-core==1.6.0
# === end common azure dependencies across repos ===
geojson>=3.0.0          # <-- autorest.python-only dependency, outside markers
```

Dependencies outside the markers are preserved during sync.

### Sync Workflow

The sync is run automatically as part of [pipeline](https://dev.azure.com/azure-sdk/internal/_build?definitionId=7257), or manually:

```bash
python eng/scripts/sync_from_typespec.py <path-to-typespec-repo>
```
