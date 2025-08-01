# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------


def test_azure_mgmt_test_import():
    # just need to check import so that we could make sure the generated code is valid
    from azure.mgmt.test import AutoRestSwaggerBATArrayService
    from azure.mgmt.test import models
    from azure.mgmt.test import operations


def test_azure_test_import():
    # just need to check import so that we could make sure the generated code is valid
    from azure.test._generated import AutoRestSwaggerBATArrayService
    from azure.test._generated import models
    from azure.test._generated import operations

    from azure.test import CustomizeClient


def test_package_mode_for_azure_mgmt_test():
    # check whether samples/specification/azure-mgmt-test/test/azure-mgmt-test contains setup.py/CHANGELOG.md
    import os
    from pathlib import Path

    # Get the path to the samples directory relative to this test file
    current_dir = Path(__file__).parent
    samples_dir = (
        current_dir.parent.parent / "samples" / "specification" / "azure-mgmt-test" / "test" / "azure-mgmt-test"
    )

    # Check if setup.py exists
    setup_py_path = samples_dir / "setup.py"
    assert setup_py_path.exists(), f"setup.py not found at {setup_py_path}"

    # Check if CHANGELOG.md exists
    changelog_path = samples_dir / "CHANGELOG.md"
    assert changelog_path.exists(), f"CHANGELOG.md not found at {changelog_path}"

    # setup.py shall not exist in inner folder
    inner_setup_py_path = samples_dir / "azure/mgmt/test/setup.py"
    assert not inner_setup_py_path.exists(), f"setup.py should not exist at {inner_setup_py_path}"

    # CHANGELOG.md shall not exist in inner folder
    inner_changelog_path = samples_dir / "azure/mgmt/test/CHANGELOG.md"
    assert not inner_changelog_path.exists(), f"CHANGELOG.md should not exist at {inner_changelog_path}"
