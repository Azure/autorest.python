# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import os
from pathlib import Path


def test_azure_mgmt_test_import():
    # just need to check import so that we could make sure the generated code is valid
    from azure.mgmt.test import AutoRestHeadTestService
    from azure.mgmt.test import operations


def test_azure_test_import():
    # just need to check import so that we could make sure the generated code is valid
    from azure.test._generated import AutoRestSwaggerBATArrayService
    from azure.test._generated import models
    from azure.test._generated import operations

    from azure.test import CustomizeClient


def test_package_mode_for_azure_mgmt_test():
    # check whether packaging files are in the right place

    # Get the path to the samples directory relative to this test file
    current_dir = Path(__file__).parent
    samples_dir = (
        current_dir.parent.parent / "samples" / "specification" / "azure-mgmt-test" / "test" / "azure-mgmt-test"
    )

    # generated_samples/generated_tests/apiview-properties.json/README.md/LICENSE/dev_requirements.txt/MANIFEST.in
    # CHANGELOG.md/setup.py
    # shall exist in root folder instead of inner folder
    for folder_or_file in [
        "generated_samples",
        "generated_tests",
        "apiview-properties.json",
        "README.md",
        "LICENSE",
        "dev_requirements.txt",
        "MANIFEST.in",
        "CHANGELOG.md",
        "setup.py",
    ]:
        assert (samples_dir / folder_or_file).exists(), f"{folder_or_file} not found in {samples_dir}"
        assert not (
            samples_dir / "azure/mgmt/test" / folder_or_file
        ).exists(), f"{folder_or_file} should not exist in inner folder azure/mgmt/test"

    # py.typed shall exist in inner folder instead of root folder
    assert (samples_dir / "azure/mgmt/test/py.typed").exists(), "py.typed should exist in inner folder azure/mgmt/test"
    assert not (samples_dir / "py.typed").exists(), "py.typed should not exist in root folder"

    # generated samples/tests file shall be put directly under generated_samples/generated_tests instead of inner folder,
    # so there shall be no subfolder
    for folder in ["generated_samples", "generated_tests"]:
        subdir = [s for s in (samples_dir / folder).iterdir() if s.is_dir()]
        assert not subdir, f"Subfolder should not exist in {folder} folder"
